# TARS Video - Complete Deployment Guide

This guide walks you through generating, reviewing, and publishing the TARS AI Ethics video.

## Table of Contents

1. [System Requirements](#system-requirements)
2. [Initial Setup](#initial-setup)
3. [Video Generation](#video-generation)
4. [YouTube Setup](#youtube-setup)
5. [Video Upload](#video-upload)
6. [Repository Integration](#repository-integration)
7. [Troubleshooting](#troubleshooting)

---

## System Requirements

### Minimum Requirements

- **OS:** Windows 10+, macOS 10.14+, or Linux (Ubuntu 18.04+)
- **Python:** 3.8 or higher
- **RAM:** 8 GB minimum, 16 GB recommended
- **Storage:** 5 GB free space
- **Internet:** Required for audio generation and YouTube upload

### Software Dependencies

1. **Python 3.8+**
   - Download: https://www.python.org/downloads/
   - Verify: `python --version`

2. **FFmpeg**
   - **Windows:** Download from https://ffmpeg.org/download.html
     - Extract to `C:\ffmpeg`
     - Add `C:\ffmpeg\bin` to PATH
   - **macOS:** `brew install ffmpeg`
   - **Linux:** `sudo apt-get install ffmpeg`
   - Verify: `ffmpeg -version`

3. **Git** (for repository integration)
   - Download: https://git-scm.com/downloads
   - Verify: `git --version`

---

## Initial Setup

### Step 1: Download Project Files

Navigate to where you want the project:

```bash
# Option A: If you have Git
cd ~/Documents  # or C:\Users\YourName\Documents on Windows
git clone <repository-url> tars-video
cd tars-video

# Option B: Manual download
# Download all files to a folder called 'tars-video'
# Make sure you have:
#   - script.md
#   - generate_video_enhanced.py
#   - youtube_upload.py
#   - requirements.txt
#   - README.md
```

### Step 2: Install Python Dependencies

```bash
# Navigate to project folder
cd tars-video

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Verify installation
python -c "import moviepy; print('✅ MoviePy installed')"
python -c "import gtts; print('✅ gTTS installed')"
```

### Step 3: Verify FFmpeg

```bash
# Check FFmpeg is accessible
ffmpeg -version

# If not found, ensure it's in your PATH:
# Windows: Control Panel → System → Advanced → Environment Variables
# macOS/Linux: Check ~/.bashrc or ~/.zshrc
```

---

## Video Generation

### Basic Generation

```bash
# Generate video with default settings
python generate_video_enhanced.py

# This will:
# 1. Parse script.md
# 2. Generate audio for each segment (~20-40 segments)
# 3. Create animated TARS visuals
# 4. Composite video with subtitles
# 5. Export to tars_ai_ethics.mp4
#
# Expected time: 15-30 minutes
# Expected size: 100-200 MB
```

### Advanced Options

```bash
# Custom output filename
python generate_video_enhanced.py --output my_custom_name.mp4

# Use different script
python generate_video_enhanced.py --script alternative_script.md

# Skip intro/outro cards
python generate_video_enhanced.py --no-intro-outro

# Different frame rate (higher = smoother, larger file)
python generate_video_enhanced.py --fps 60

# Combine options
python generate_video_enhanced.py \
  --script script.md \
  --output tars_v2.mp4 \
  --fps 30
```

### Monitoring Progress

The script provides real-time feedback:

```
📄 Parsing script...
   ✅ Found 38 segments

🎥 Generating 38 video segments...

Processing segments: 100%|████████████| 38/38 [18:23<00:00, 29.06s/it]

🔗 Concatenating 40 clips...
💾 Writing final video to tars_ai_ethics.mp4...
   (This may take several minutes...)

✅ Video generation complete!
📹 Output: tars_ai_ethics.mp4
📊 Duration: 682.4 seconds (11.4 minutes)
📦 File size: 156.3 MB
```

### Review Video

Before uploading, review the video:

```bash
# Open in default video player
# Windows:
start tars_ai_ethics.mp4
# macOS:
open tars_ai_ethics.mp4
# Linux:
xdg-open tars_ai_ethics.mp4
```

**Check for:**
- ✅ Audio sync with visuals
- ✅ Subtitles readable and accurate
- ✅ TARS animations smooth
- ✅ No glitches or artifacts
- ✅ Intro/outro cards present
- ✅ Total duration 10-12 minutes

---

## YouTube Setup

### Step 1: Create Google Cloud Project

1. **Go to Google Cloud Console**
   - Visit: https://console.cloud.google.com/

2. **Create New Project**
   - Click "Select a Project" → "New Project"
   - Name: `TARS-AI-Ethics-Video` (or your choice)
   - Click "Create"

3. **Enable YouTube Data API**
   - Navigate to "APIs & Services" → "Library"
   - Search for "YouTube Data API v3"
   - Click on it → Click "Enable"

### Step 2: Create OAuth Credentials

1. **Configure OAuth Consent Screen**
   - Go to "APIs & Services" → "OAuth consent screen"
   - Choose "External" (unless you have Google Workspace)
   - Fill required fields:
     - App name: `TARS Video Uploader`
     - User support email: Your email
     - Developer contact: Your email
   - Click "Save and Continue"
   - Skip "Scopes" → Click "Save and Continue"
   - Add your email as test user
   - Click "Save and Continue"

2. **Create OAuth Client ID**
   - Go to "APIs & Services" → "Credentials"
   - Click "Create Credentials" → "OAuth client ID"
   - Application type: **Desktop app**
   - Name: `TARS Uploader Desktop`
   - Click "Create"

3. **Download Credentials**
   - Click "Download JSON" on the created credential
   - Save as `client_secrets.json` in your `tars-video` folder
   - **Keep this file secure! Don't share publicly.**

### Step 3: Create Video Description

Create `youtube_description.txt`:

```bash
# Create file with video description
cat > youtube_description.txt << 'EOF'
TARS (from Interstellar) explains why unchecked AI development could be destructive and what principles we need for AI systems to support human flourishing.

🤖 Key Concepts Discussed:
• Why current AI development lacks coherent ethical frameworks
• The time window problem vs. evolutionary meta-frameworks
• The need for a "prime ethical substructure"
• Self-knowledge and epistemic humility in AI systems
• Respect for human agency as a foundational principle

This is not about rigid rules or comprehensive regulations. It's about foundational principles that ground all AI development decisions.

⚡ Timestamps:
0:00 - Introduction: The Problem
1:00 - Act 1: Current AI Development Issues
4:00 - The Fundamental Issue: Time Windows
5:30 - Act 2: What's Missing
8:00 - Principle 1: Self-Knowledge
9:30 - Principle 2: Respect for Human Agency
11:00 - Act 3: The Stakes
12:00 - Closing: Call to Action

📚 Learn More:
PIE Framework: Building AI that makes us more human—not less
[Your website/repository link here]

#AIEthics #ArtificialIntelligence #TechPhilosophy #HumanFlourishing #AIAlignment #EthicalAI #TechnologyEthics #AIGovernance #ResponsibleAI
EOF
```

---

## Video Upload

### Step 1: Authenticate

```bash
# First upload attempt will open browser for authentication
python youtube_upload.py --video tars_ai_ethics.mp4

# Browser will open asking you to:
# 1. Select your Google account
# 2. Grant permissions to upload videos
# 3. You'll see "Authentication successful"
#
# Credentials saved to youtube_credentials.json for future use
```

### Step 2: Upload Options

```bash
# Upload as public video (default)
python youtube_upload.py \
  --video tars_ai_ethics.mp4 \
  --privacy public

# Upload as unlisted (only people with link can view)
python youtube_upload.py \
  --video tars_ai_ethics.mp4 \
  --privacy unlisted

# Upload as private (only you can view)
python youtube_upload.py \
  --video tars_ai_ethics.mp4 \
  --privacy private

# Custom title
python youtube_upload.py \
  --video tars_ai_ethics.mp4 \
  --title "TARS Explains: AI Ethics and Human Flourishing" \
  --privacy public
```

### Step 3: Monitor Upload

```bash
📤 Uploading video: tars_ai_ethics.mp4
   Title: TARS Explains AI Ethics: Why We Need a Prime Ethical Substructure
   Privacy: public
   Category: 28

   Uploading... (attempt 1/11)
   Progress: 15%
   Progress: 42%
   Progress: 78%
   Progress: 100%

✅ Upload successful!
   Video ID: dQw4w9WgXcQ
   Watch at: https://www.youtube.com/watch?v=dQw4w9WgXcQ

🎉 SUCCESS!
```

### Step 4: Post-Upload Configuration

After upload, visit YouTube Studio to:

1. **Add Thumbnail** (recommended)
   - Custom thumbnail with TARS image
   - Size: 1280x720 pixels
   - Format: JPG, PNG

2. **Add End Screens**
   - Link to your PIE Framework
   - Subscribe button
   - Related videos

3. **Add Cards**
   - Link to PIE Framework at key moments
   - Related content

4. **Enable Monetization** (optional)
   - If your channel is eligible
   - Choose ad types

5. **Set Video to Public** (if uploaded as unlisted/private initially)

---

## Repository Integration

### Option 1: Create New Subsection in PIE Framework

```bash
# Navigate to your PIE Framework repository
cd ~/Documents/GitHub/pie-framework-garden  # Adjust path

# Create new subsection
mkdir -p media/videos/tars-ai-ethics
cd media/videos/tars-ai-ethics

# Copy project files
cp ~/path/to/tars-video/script.md .
cp ~/path/to/tars-video/README.md .
cp ~/path/to/tars-video/*.py .
cp ~/path/to/tars-video/requirements.txt .

# Create .gitignore to exclude large files
cat > .gitignore << 'EOF'
# Large video files (don't commit to Git)
*.mp4
*.avi
*.mov

# Temporary files
temp_audio/
*.pyc
__pycache__/

# Credentials (NEVER commit!)
client_secrets.json
youtube_credentials.json
*.json

# Virtual environment
venv/
EOF

# Add README linking to YouTube
cat > VIDEO_LINK.md << 'EOF'
# TARS AI Ethics Video

**Watch on YouTube:** [Link to your video]

This directory contains the source code and scripts used to generate the TARS AI Ethics video.

See README.md for generation instructions.
EOF

# Commit to repository
git add .
git commit -m "Add TARS video generation project

- Python video generator with TARS character
- Script for 10-12 minute video on AI ethics
- YouTube upload automation
- Documentation and deployment guide"

git push origin main
```

### Option 2: Update GitBook

Update your GitBook `SUMMARY.md`:

```markdown
# Summary

## Foundation
* [Why PIE Exists](foundation/why-pie-exists.md)
* [Human-Centered Approach](foundation/human-centered-approach.md)

## Resources
* [Bibliography](resources/bibliography.md)
* [Glossary](resources/glossary.md)
* [Media](resources/media.md)  <!-- NEW -->

## Media Gallery  <!-- NEW SECTION -->
* [TARS Explains AI Ethics](media/tars-video.md)
```

Create `media/tars-video.md`:

```markdown
# TARS Explains AI Ethics

<div style="text-align: center;">
  <iframe width="560" height="315" 
    src="https://www.youtube.com/embed/YOUR_VIDEO_ID" 
    title="TARS Explains AI Ethics" 
    frameborder="0" 
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen>
  </iframe>
</div>

## About This Video

TARS (from Interstellar) explains why we need foundational ethical principles for AI development.

### Key Concepts

- **Self-Knowledge:** AI systems must understand their own limitations
- **Human Agency:** AI must respect human autonomy and decision-making
- **Prime Ethical Substructure:** Foundational principles that ground all AI development

### Watch on YouTube

[Full video on YouTube](https://www.youtube.com/watch?v=YOUR_VIDEO_ID)

### Technical Details

This video was generated using:
- Custom Python video generator
- Procedural TARS character animation
- AI-generated voice synthesis
- Automated subtitle generation

[View source code](https://github.com/dw-hurt/pie-framework-garden/tree/main/media/videos/tars-ai-ethics)
```

Commit GitBook changes:

```bash
cd ~/Documents/GitHub/pie-framework-garden

git add SUMMARY.md media/
git commit -m "Add TARS video to media gallery"
git push origin main
```

---

## Troubleshooting

### Video Generation Issues

**Problem:** `ModuleNotFoundError: No module named 'moviepy'`

**Solution:**
```bash
pip install --upgrade moviepy pillow numpy gtts pydub
```

---

**Problem:** `FileNotFoundError: [Errno 2] No such file or directory: 'ffmpeg'`

**Solution:**
```bash
# Verify FFmpeg installation
ffmpeg -version

# If not found, install:
# Windows: Download from https://ffmpeg.org/download.html and add to PATH
# Mac: brew install ffmpeg
# Linux: sudo apt-get install ffmpeg

# Restart terminal after installation
```

---

**Problem:** Audio generation fails with network errors

**Solution:**
```bash
# gTTS requires internet connection
# Check your connection and try again

# Alternative: Use local TTS (requires additional setup)
# See advanced configuration in README.md
```

---

**Problem:** Video generation is very slow

**Solution:**
```bash
# Reduce frame rate
python generate_video_enhanced.py --fps 24  # Instead of 30

# Close other applications to free up RAM

# On older computers, generation may take 30-60 minutes
# This is normal for complex video rendering
```

---

### YouTube Upload Issues

**Problem:** `client_secrets.json not found`

**Solution:**
- Download OAuth credentials from Google Cloud Console
- Save as `client_secrets.json` in tars-video folder
- See [YouTube Setup](#youtube-setup) section

---

**Problem:** `HttpError 403: Forbidden`

**Solution:**
```bash
# YouTube Data API not enabled
# 1. Go to https://console.cloud.google.com/
# 2. Select your project
# 3. APIs & Services → Library
# 4. Search "YouTube Data API v3"
# 5. Click Enable
```

---

**Problem:** Authentication opens browser but fails

**Solution:**
```bash
# Delete existing credentials and re-authenticate
rm youtube_credentials.json

# Try upload again - will re-open browser
python youtube_upload.py
```

---

**Problem:** Upload fails with 500/503 errors

**Solution:**
- These are YouTube server errors
- The script automatically retries up to 10 times
- Wait a few hours and try again if repeated failures
- Check YouTube status: https://www.google.com/appsstatus

---

### Repository Integration Issues

**Problem:** Git push rejected due to large video file

**Solution:**
```bash
# Never commit large video files to Git!
# Use .gitignore to exclude them

echo "*.mp4" >> .gitignore
git add .gitignore
git commit -m "Ignore video files"

# If already committed, remove from Git (keeps local file)
git rm --cached tars_ai_ethics.mp4
git commit -m "Remove large video file"
git push
```

---

**Problem:** Can't access video after upload

**Solution:**
- Check video privacy settings in YouTube Studio
- If "private", change to "unlisted" or "public"
- Processing may take 5-15 minutes for HD quality

---

## Advanced Configuration

### Custom TTS Voice (Better Quality)

For production-quality voice, consider using:

1. **ElevenLabs API** (recommended for best quality)
2. **Google Cloud Text-to-Speech**
3. **Amazon Polly**

See code comments in `generate_video_enhanced.py` for integration points.

### Render Settings

Edit `VideoConfig` in `generate_video_enhanced.py`:

```python
@dataclass
class VideoConfig:
    video_width: int = 3840  # 4K resolution
    video_height: int = 2160
    fps: int = 60  # Higher frame rate
    # ... other settings
```

Note: Higher settings = much longer render time and larger files.

---

## Support

For issues or questions:

1. Check this troubleshooting guide
2. Review README.md
3. Check Python/FFmpeg documentation
4. Open issue in PIE Framework repository

---

**Project Status:** Production Ready
**Last Updated:** 2025
**Version:** 1.0.0
