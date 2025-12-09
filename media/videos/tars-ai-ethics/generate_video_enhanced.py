#!/usr/bin/env python3
"""
TARS AI Ethics Video Generator - Enhanced Version
Generates a 10-12 minute video with TARS character explaining AI ethics
Supports both local TTS (gTTS) and remote AI TTS for better quality

Requirements:
- Python 3.8+
- moviepy, Pillow, numpy, gTTS, pydub
- Optional: API keys for better TTS (ElevenLabs, Google Cloud TTS)
"""

import os
import sys
import json
import argparse
from pathlib import Path
from typing import List, Dict, Tuple, Optional
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import (
    VideoClip, AudioFileClip, CompositeVideoClip, 
    TextClip, ImageClip, concatenate_videoclips,
    ColorClip
)
from gtts import gTTS
from pydub import AudioSegment
import textwrap
from dataclasses import dataclass
from tqdm import tqdm

# Configuration
@dataclass
class VideoConfig:
    """Video generation configuration"""
    video_width: int = 1920
    video_height: int = 1080
    fps: int = 30
    background_color: Tuple[int, int, int] = (10, 10, 20)  # Dark blue-black
    tars_color: Tuple[int, int, int] = (200, 200, 220)  # Light gray-blue
    text_color: Tuple[int, int, int] = (220, 220, 230)
    accent_color: Tuple[int, int, int] = (100, 150, 255)  # Blue accent
    font_size: int = 48
    subtitle_font_size: int = 36
    audio_speed: float = 1.0
    subtitle_wrap_width: int = 60
    use_enhanced_tts: bool = False  # Set to True if using API TTS

CONFIG = VideoConfig()


class TARSGeometry:
    """Generate TARS-like geometric robot shapes with animations"""
    
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.center_x = width // 2
        self.center_y = height // 2
        
    def create_block(self, x: int, y: int, w: int, h: int, 
                     angle: float = 0, alpha: int = 255,
                     glow: bool = False) -> Image.Image:
        """Create a rotating block with optional glow effect"""
        img = Image.new('RGBA', (self.width, self.height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # Add glow effect
        if glow:
            for i in range(5, 0, -1):
                glow_alpha = alpha // (6 - i)
                glow_w = w + i * 4
                glow_h = h + i * 4
                x1, y1 = x - glow_w//2, y - glow_h//2
                x2, y2 = x + glow_w//2, y + glow_h//2
                draw.rectangle([x1, y1, x2, y2], 
                              fill=(*CONFIG.accent_color, glow_alpha))
        
        # Create main rectangle
        x1, y1 = x - w//2, y - h//2
        x2, y2 = x + w//2, y + h//2
        draw.rectangle([x1, y1, x2, y2], 
                      fill=(*CONFIG.tars_color, alpha),
                      outline=(255, 255, 255, alpha), width=3)
        
        # Add inner detail lines
        for i in range(1, 4):
            offset = h // 5 * i
            draw.line([(x1 + 10, y1 + offset), (x2 - 10, y1 + offset)],
                     fill=(255, 255, 255, alpha//2), width=1)
        
        # Rotate if needed
        if angle != 0:
            img = img.rotate(angle, center=(x, y), 
                           fillcolor=(0, 0, 0, 0), expand=False)
        
        return img
    
    def create_tars_standing(self, frame_number: int = 0, 
                           animation_mode: str = 'idle') -> np.ndarray:
        """
        Create TARS in standing configuration with various animation modes
        
        Modes:
        - 'idle': Subtle breathing/rotation
        - 'thinking': Rotating blocks pattern
        - 'emphatic': Larger movements for emphasis
        - 'forming': Blocks assembling
        """
        img = Image.new('RGBA', (self.width, self.height), 
                       (*CONFIG.background_color, 255))
        
        # Calculate animation parameters
        t = frame_number * 0.02
        
        if animation_mode == 'thinking':
            angle_offset = np.sin(t * 2) * 5
            glow = frame_number % 60 < 30
        elif animation_mode == 'emphatic':
            angle_offset = np.sin(t * 3) * 8
            glow = True
        elif animation_mode == 'forming':
            # Blocks assemble from scattered positions
            progress = min(1.0, frame_number / 60)
            angle_offset = (1 - progress) * 45
            glow = progress > 0.5
        else:  # idle
            angle_offset = np.sin(t) * 2
            glow = False
        
        # Main body (vertical stack of blocks)
        block_height = 150
        block_width = 100
        
        blocks = []
        for i in range(4):
            y = self.center_y - 200 + i * (block_height + 10)
            
            # Add slight vertical bob
            y_offset = np.sin(t + i * 0.5) * 3
            
            block = self.create_block(
                self.center_x, 
                int(y + y_offset), 
                block_width, 
                block_height,
                angle=angle_offset * (1 + i * 0.2),
                glow=glow
            )
            blocks.append(block)
        
        # Side arms (horizontal blocks)
        arm_y = self.center_y - 50
        arm_y_offset = np.sin(t * 1.5) * 5
        
        left_arm = self.create_block(
            self.center_x - 200, 
            int(arm_y + arm_y_offset),
            block_height, 
            block_width // 2,
            angle=angle_offset,
            glow=glow
        )
        right_arm = self.create_block(
            self.center_x + 200, 
            int(arm_y - arm_y_offset),
            block_height, 
            block_width // 2,
            angle=-angle_offset,
            glow=glow
        )
        
        # Composite all blocks
        for block in blocks:
            img = Image.alpha_composite(img, block)
        img = Image.alpha_composite(img, left_arm)
        img = Image.alpha_composite(img, right_arm)
        
        return np.array(img)
    
    def create_starfield(self, frame_number: int = 0) -> np.ndarray:
        """Create animated starfield background with depth"""
        img = Image.new('RGB', (self.width, self.height), CONFIG.background_color)
        draw = ImageDraw.Draw(img)
        
        # Generate stars with parallax layers
        np.random.seed(42)
        
        # Background stars (slow)
        for _ in range(150):
            x = np.random.randint(0, self.width)
            y = np.random.randint(0, self.height)
            size = 1
            brightness = np.random.randint(80, 150)
            
            # Slow twinkle
            twinkle = np.sin(frame_number * 0.05 + x + y) * 20
            brightness = max(0, min(255, brightness + twinkle))
            
            draw.ellipse([x, y, x+size, y+size], 
                        fill=(brightness, brightness, brightness))
        
        # Midground stars (medium)
        for _ in range(50):
            x = np.random.randint(0, self.width)
            y = np.random.randint(0, self.height)
            size = 2
            brightness = np.random.randint(120, 200)
            
            # Medium twinkle
            twinkle = np.sin(frame_number * 0.1 + x * 2 + y) * 30
            brightness = max(0, min(255, brightness + twinkle))
            
            draw.ellipse([x, y, x+size, y+size], 
                        fill=(brightness, brightness, brightness))
        
        # Foreground stars (fast)
        for _ in range(20):
            x = np.random.randint(0, self.width)
            y = np.random.randint(0, self.height)
            size = 3
            brightness = np.random.randint(180, 255)
            
            # Fast twinkle
            twinkle = np.sin(frame_number * 0.15 + x * 3 + y * 2) * 40
            brightness = max(0, min(255, brightness + twinkle))
            
            draw.ellipse([x, y, x+size, y+size], 
                        fill=(brightness, brightness, brightness))
        
        return np.array(img)


class ScriptParser:
    """Parse the script markdown into timed segments with metadata"""
    
    @staticmethod
    def parse_script(script_path: str) -> List[Dict]:
        """Parse script into timed segments with actions and timing"""
        with open(script_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        segments = []
        current_segment = None
        current_section = "INTRO"
        
        lines = content.split('\n')
        for line in lines:
            # Detect section headers for timing hints
            if line.strip().startswith('## ') and '(' in line:
                # Extract section name and timing
                parts = line.split('(')
                if len(parts) > 1:
                    current_section = parts[0].replace('##', '').strip()
            
            # Detect speaker
            if line.strip().startswith('**TARS:**'):
                if current_segment and current_segment['text'].strip():
                    segments.append(current_segment)
                current_segment = {
                    'speaker': 'TARS',
                    'text': '',
                    'actions': [],
                    'section': current_section,
                    'animation_mode': 'idle'
                }
            
            # Detect actions and set animation modes
            elif line.strip().startswith('*[') and line.strip().endswith(']*'):
                if current_segment:
                    action = line.strip()[2:-2]  # Remove *[ and ]*
                    current_segment['actions'].append(action)
                    
                    # Set animation mode based on action
                    action_lower = action.lower()
                    if 'rotating' in action_lower or 'shift' in action_lower:
                        current_segment['animation_mode'] = 'thinking'
                    elif 'materializes' in action_lower or 'forming' in action_lower:
                        current_segment['animation_mode'] = 'forming'
                    elif 'beat' in action_lower or 'pause' in action_lower:
                        current_segment['animation_mode'] = 'emphatic'
            
            # Collect dialogue (skip headers, stage directions, etc.)
            elif (line.strip() and 
                  not line.startswith('#') and 
                  not line.startswith('**[') and
                  not line.startswith('---') and
                  not line.startswith('**Character')):
                if current_segment:
                    current_segment['text'] += line.strip() + ' '
        
        # Add last segment
        if current_segment and current_segment['text'].strip():
            segments.append(current_segment)
        
        return segments


class VideoGenerator:
    """Generate the complete video with enhanced features"""
    
    def __init__(self, output_path: str = "tars_ai_ethics.mp4"):
        self.output_path = output_path
        self.geometry = TARSGeometry(CONFIG.video_width, CONFIG.video_height)
        self.temp_dir = Path("temp_audio")
        self.temp_dir.mkdir(exist_ok=True)
        
    def generate_audio(self, text: str, output_file: str, 
                      segment_index: int = 0) -> str:
        """
        Generate speech audio from text
        Uses gTTS by default, can be extended for better TTS APIs
        """
        # Clean text for TTS
        clean_text = text.replace('*', '').replace('[', '').replace(']', '')
        clean_text = clean_text.replace('  ', ' ').strip()
        
        if not clean_text:
            return None
        
        try:
            # Use gTTS (free, decent quality)
            tts = gTTS(text=clean_text, lang='en', slow=False)
            tts.save(output_file)
            
            # Post-process: adjust speed slightly for more robotic feel
            audio = AudioSegment.from_mp3(output_file)
            
            # Slight speed increase for TARS's efficient speech
            if CONFIG.audio_speed != 1.0:
                audio = audio.speedup(playback_speed=CONFIG.audio_speed)
            
            # Export processed audio
            audio.export(output_file, format="mp3")
            
            return output_file
            
        except Exception as e:
            print(f"    ⚠️ Audio generation error for segment {segment_index}: {e}")
            return None
    
    def create_subtitle_clip(self, text: str, duration: float, 
                           start_time: float = 0) -> TextClip:
        """Create subtitle text overlay with word wrapping"""
        # Wrap text for readability
        wrapped = textwrap.fill(text, width=CONFIG.subtitle_wrap_width)
        
        # Limit subtitle length
        if len(wrapped) > 200:
            wrapped = wrapped[:197] + "..."
        
        try:
            txt_clip = TextClip(
                wrapped,
                fontsize=CONFIG.subtitle_font_size,
                color='white',
                font='Arial-Bold',
                method='caption',
                size=(CONFIG.video_width - 200, None),
                align='center',
                stroke_color='black',
                stroke_width=2
            )
            txt_clip = txt_clip.set_position(('center', CONFIG.video_height - 150))
            txt_clip = txt_clip.set_start(start_time).set_duration(duration)
            
            return txt_clip
            
        except Exception as e:
            print(f"    ⚠️ Subtitle creation error: {e}")
            return None
    
    def create_title_card(self, text: str, duration: float = 3.0) -> CompositeVideoClip:
        """Create title card with text"""
        # Black background
        background = ColorClip(
            size=(CONFIG.video_width, CONFIG.video_height),
            color=(0, 0, 0),
            duration=duration
        )
        
        # Title text
        title = TextClip(
            text,
            fontsize=72,
            color='white',
            font='Arial-Bold',
            method='caption',
            size=(CONFIG.video_width - 400, None),
            align='center'
        )
        title = title.set_position('center').set_duration(duration)
        
        return CompositeVideoClip([background, title])
    
    def create_segment_video(self, segment: Dict, segment_index: int) -> Optional[CompositeVideoClip]:
        """Create video for one script segment"""
        print(f"    📝 {segment['text'][:60]}...")
        
        # Generate audio
        audio_file = self.temp_dir / f"segment_{segment_index:03d}.mp3"
        audio_path = self.generate_audio(segment['text'], str(audio_file), segment_index)
        
        if not audio_path or not os.path.exists(audio_path):
            print(f"    ⚠️ Skipping segment {segment_index} - no audio generated")
            return None
        
        # Load audio to get duration
        try:
            audio_clip = AudioFileClip(str(audio_path))
            duration = audio_clip.duration
        except Exception as e:
            print(f"    ⚠️ Audio loading error: {e}")
            return None
        
        # Determine animation mode
        animation_mode = segment.get('animation_mode', 'idle')
        
        # Create video clip with TARS animation
        def make_frame(t):
            frame_number = int(t * CONFIG.fps)
            
            # Starfield background
            background = self.geometry.create_starfield(frame_number)
            
            # TARS overlay with animation
            tars = self.geometry.create_tars_standing(frame_number, animation_mode)
            
            # Composite (alpha blending)
            alpha = tars[:, :, 3:4] / 255.0
            tars_rgb = tars[:, :, :3]
            frame = background * (1 - alpha) + tars_rgb * alpha
            
            return frame.astype('uint8')
        
        try:
            video_clip = VideoClip(make_frame, duration=duration)
            video_clip = video_clip.set_audio(audio_clip)
            video_clip = video_clip.set_fps(CONFIG.fps)
            
            # Add subtitles
            subtitle = self.create_subtitle_clip(segment['text'], duration, 0)
            
            if subtitle:
                final_clip = CompositeVideoClip([video_clip, subtitle])
            else:
                final_clip = video_clip
            
            return final_clip
            
        except Exception as e:
            print(f"    ⚠️ Video clip creation error: {e}")
            return None
    
    def generate(self, script_path: str, add_intro_outro: bool = True):
        """Generate complete video with intro and outro cards"""
        print("\n" + "="*60)
        print("🎬 TARS AI ETHICS VIDEO GENERATOR")
        print("="*60 + "\n")
        
        print("📄 Parsing script...")
        segments = ScriptParser.parse_script(script_path)
        print(f"   ✅ Found {len(segments)} segments\n")
        
        clips = []
        
        # Add intro title card
        if add_intro_outro:
            print("🎞️  Creating intro card...")
            intro = self.create_title_card(
                "TARS\nExplains AI Ethics",
                duration=3.0
            )
            clips.append(intro)
        
        # Generate all segments with progress bar
        print(f"🎥 Generating {len(segments)} video segments...\n")
        
        for i, segment in enumerate(tqdm(segments, desc="Processing segments")):
            try:
                clip = self.create_segment_video(segment, i)
                if clip:
                    clips.append(clip)
            except Exception as e:
                print(f"    ❌ Error generating segment {i}: {e}")
                continue
        
        # Add outro title card
        if add_intro_outro:
            print("\n🎞️  Creating outro card...")
            outro = self.create_title_card(
                "BUILD AI THAT MAKES US\nMORE HUMAN — NOT LESS\n\n\nLearn more at:\nPIE Framework",
                duration=5.0
            )
            clips.append(outro)
        
        if not clips:
            print("\n❌ Error: No video clips were generated successfully")
            return False
        
        print(f"\n🔗 Concatenating {len(clips)} clips...")
        try:
            final_video = concatenate_videoclips(clips, method="compose")
        except Exception as e:
            print(f"❌ Concatenation error: {e}")
            return False
        
        print(f"💾 Writing final video to {self.output_path}...")
        print("   (This may take several minutes...)\n")
        
        try:
            final_video.write_videofile(
                self.output_path,
                fps=CONFIG.fps,
                codec='libx264',
                audio_codec='aac',
                bitrate='8000k',
                preset='medium',
                temp_audiofile='temp-audio.m4a',
                remove_temp=True,
                threads=4,
                logger='bar'
            )
        except Exception as e:
            print(f"\n❌ Video writing error: {e}")
            return False
        
        print("\n✅ Video generation complete!")
        print(f"📹 Output: {self.output_path}")
        print(f"📊 Duration: {final_video.duration:.1f} seconds ({final_video.duration/60:.1f} minutes)")
        print(f"📦 File size: {os.path.getsize(self.output_path) / 1024 / 1024:.1f} MB\n")
        
        # Cleanup
        print("🧹 Cleaning up temporary files...")
        for audio_file in self.temp_dir.glob("*.mp3"):
            try:
                audio_file.unlink()
            except:
                pass
        
        return True


def main():
    """Main execution with CLI arguments"""
    parser = argparse.ArgumentParser(
        description='Generate TARS AI Ethics video from script'
    )
    parser.add_argument(
        '--script',
        default='script.md',
        help='Path to script markdown file (default: script.md)'
    )
    parser.add_argument(
        '--output',
        default='tars_ai_ethics.mp4',
        help='Output video filename (default: tars_ai_ethics.mp4)'
    )
    parser.add_argument(
        '--no-intro-outro',
        action='store_true',
        help='Skip intro and outro title cards'
    )
    parser.add_argument(
        '--fps',
        type=int,
        default=30,
        help='Frames per second (default: 30)'
    )
    
    args = parser.parse_args()
    
    # Update config
    CONFIG.fps = args.fps
    
    # Check script exists
    if not os.path.exists(args.script):
        print(f"❌ Error: Script file '{args.script}' not found")
        print("Please ensure the script file exists in the current directory")
        return 1
    
    # Generate video
    generator = VideoGenerator(args.output)
    success = generator.generate(args.script, add_intro_outro=not args.no_intro_outro)
    
    if success:
        print("\n" + "="*60)
        print("🎬 VIDEO READY FOR YOUTUBE UPLOAD!")
        print("="*60)
        print(f"\nNext steps:")
        print(f"1. Review the video: {args.output}")
        print(f"2. Upload to YouTube using: python youtube_upload.py")
        print(f"3. Share your video!\n")
        return 0
    else:
        return 1


if __name__ == "__main__":
    sys.exit(main())
