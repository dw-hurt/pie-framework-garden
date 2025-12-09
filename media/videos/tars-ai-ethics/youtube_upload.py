#!/usr/bin/env python3
"""
YouTube Video Uploader
Uploads the generated TARS video to YouTube with metadata

Setup:
1. Create a project at https://console.cloud.google.com/
2. Enable YouTube Data API v3
3. Create OAuth 2.0 credentials (Desktop app)
4. Download client_secrets.json
5. Run this script - it will open browser for authentication
"""

import os
import sys
import argparse
import json
from pathlib import Path
import http.client
import httplib2
import random
import time

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# Scopes required for upload
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

# YouTube API settings
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

# Retry configuration
RETRIABLE_EXCEPTIONS = (httplib2.HttpLib2Error, IOError, http.client.NotConnected,
                       http.client.IncompleteRead, http.client.ImproperConnectionState,
                       http.client.CannotSendRequest, http.client.CannotSendHeader,
                       http.client.ResponseNotReady, http.client.BadStatusLine)
RETRIABLE_STATUS_CODES = [500, 502, 503, 504]
MAX_RETRIES = 10


class YouTubeUploader:
    """Handle YouTube video uploads"""
    
    def __init__(self, client_secrets_file: str = 'client_secrets.json',
                 credentials_file: str = 'youtube_credentials.json'):
        self.client_secrets_file = client_secrets_file
        self.credentials_file = credentials_file
        self.youtube = None
        
    def get_authenticated_service(self):
        """Authenticate and build YouTube service"""
        creds = None
        
        # Load existing credentials
        if os.path.exists(self.credentials_file):
            creds = Credentials.from_authorized_user_file(self.credentials_file, SCOPES)
        
        # If no valid credentials, authenticate
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                if not os.path.exists(self.client_secrets_file):
                    print(f"\n❌ Error: {self.client_secrets_file} not found!")
                    print("\nSetup instructions:")
                    print("1. Go to https://console.cloud.google.com/")
                    print("2. Create a new project (or select existing)")
                    print("3. Enable 'YouTube Data API v3'")
                    print("4. Go to 'Credentials' → 'Create Credentials' → 'OAuth client ID'")
                    print("5. Choose 'Desktop app' as application type")
                    print("6. Download the JSON file and save as 'client_secrets.json'")
                    print("7. Run this script again\n")
                    sys.exit(1)
                
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.client_secrets_file, SCOPES)
                creds = flow.run_local_server(port=0)
            
            # Save credentials for next run
            with open(self.credentials_file, 'w') as token:
                token.write(creds.to_json())
        
        self.youtube = build(API_SERVICE_NAME, API_VERSION, credentials=creds)
        return self.youtube
    
    def upload_video(self, video_file: str, title: str, description: str,
                    category: str = "28",  # Science & Technology
                    keywords: list = None,
                    privacy_status: str = "public") -> str:
        """
        Upload video to YouTube
        
        Args:
            video_file: Path to video file
            title: Video title
            description: Video description
            category: YouTube category ID (28 = Science & Technology)
            keywords: List of keywords/tags
            privacy_status: 'public', 'private', or 'unlisted'
        
        Returns:
            Video ID if successful
        """
        if not os.path.exists(video_file):
            print(f"❌ Error: Video file not found: {video_file}")
            return None
        
        if keywords is None:
            keywords = []
        
        # Build video metadata
        body = {
            'snippet': {
                'title': title,
                'description': description,
                'tags': keywords,
                'categoryId': category
            },
            'status': {
                'privacyStatus': privacy_status,
                'selfDeclaredMadeForKids': False
            }
        }
        
        # Create media upload object
        media = MediaFileUpload(
            video_file,
            chunksize=-1,  # Upload in single request
            resumable=True,
            mimetype='video/*'
        )
        
        print(f"\n📤 Uploading video: {video_file}")
        print(f"   Title: {title}")
        print(f"   Privacy: {privacy_status}")
        print(f"   Category: {category}")
        
        # Insert video
        request = self.youtube.videos().insert(
            part=','.join(body.keys()),
            body=body,
            media_body=media
        )
        
        # Execute upload with retries
        response = self._resumable_upload(request)
        
        if response:
            video_id = response['id']
            print(f"\n✅ Upload successful!")
            print(f"   Video ID: {video_id}")
            print(f"   Watch at: https://www.youtube.com/watch?v={video_id}")
            return video_id
        else:
            print("\n❌ Upload failed")
            return None
    
    def _resumable_upload(self, request):
        """Execute resumable upload with retry logic"""
        response = None
        error = None
        retry = 0
        
        while response is None:
            try:
                print(f"   Uploading... (attempt {retry + 1}/{MAX_RETRIES + 1})")
                status, response = request.next_chunk()
                
                if response is not None:
                    if 'id' in response:
                        return response
                    else:
                        print(f"❌ Upload failed with unexpected response: {response}")
                        return None
                        
                if status:
                    print(f"   Progress: {int(status.progress() * 100)}%")
                    
            except HttpError as e:
                if e.resp.status in RETRIABLE_STATUS_CODES:
                    error = f"HTTP error {e.resp.status}: {e.content}"
                else:
                    raise
                    
            except RETRIABLE_EXCEPTIONS as e:
                error = f"Retriable error: {e}"
            
            if error is not None:
                print(f"   ⚠️ {error}")
                retry += 1
                
                if retry > MAX_RETRIES:
                    print(f"❌ Maximum retries exceeded")
                    return None
                
                # Exponential backoff
                sleep_time = random.random() * (2 ** retry)
                print(f"   Retrying in {sleep_time:.1f} seconds...")
                time.sleep(sleep_time)


def main():
    """Main CLI"""
    parser = argparse.ArgumentParser(
        description='Upload video to YouTube'
    )
    parser.add_argument(
        '--video',
        default='tars_ai_ethics.mp4',
        help='Video file to upload (default: tars_ai_ethics.mp4)'
    )
    parser.add_argument(
        '--title',
        default='TARS Explains AI Ethics: Why We Need a Prime Ethical Substructure',
        help='Video title'
    )
    parser.add_argument(
        '--description-file',
        default='youtube_description.txt',
        help='File containing video description'
    )
    parser.add_argument(
        '--privacy',
        choices=['public', 'private', 'unlisted'],
        default='public',
        help='Privacy status (default: public)'
    )
    parser.add_argument(
        '--category',
        default='28',
        help='YouTube category ID (28=Science & Technology)'
    )
    
    args = parser.parse_args()
    
    # Load description from file if it exists
    if os.path.exists(args.description_file):
        with open(args.description_file, 'r', encoding='utf-8') as f:
            description = f.read()
    else:
        description = """TARS (from Interstellar) explains why unchecked AI development could be destructive and what principles we need for AI systems to support human flourishing.

Key concepts discussed:
• Why current AI development lacks coherence
• The time window problem vs. evolutionary meta-frameworks
• The need for a prime ethical substructure
• Self-knowledge and epistemic humility in AI
• Respect for human agency

This is not about rigid rules or comprehensive regulations. It's about foundational principles that ground all AI development decisions.

Learn more: PIE Framework
#AIethics #ArtificialIntelligence #TechPhilosophy #HumanFlourishing"""
    
    # Keywords
    keywords = [
        'AI ethics',
        'artificial intelligence',
        'technology philosophy',
        'human flourishing',
        'AI safety',
        'tech ethics',
        'TARS',
        'Interstellar',
        'human agency',
        'AI alignment',
        'ethical AI'
    ]
    
    print("\n" + "="*60)
    print("📺 YOUTUBE VIDEO UPLOADER")
    print("="*60)
    
    # Check video exists
    if not os.path.exists(args.video):
        print(f"\n❌ Error: Video file not found: {args.video}")
        print("Generate the video first: python generate_video_enhanced.py\n")
        return 1
    
    # Authenticate and upload
    uploader = YouTubeUploader()
    
    try:
        uploader.get_authenticated_service()
        video_id = uploader.upload_video(
            video_file=args.video,
            title=args.title,
            description=description,
            keywords=keywords,
            category=args.category,
            privacy_status=args.privacy
        )
        
        if video_id:
            print("\n" + "="*60)
            print("🎉 SUCCESS!")
            print("="*60)
            return 0
        else:
            return 1
            
    except HttpError as e:
        print(f"\n❌ HTTP Error: {e.resp.status} - {e.content}")
        return 1
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
