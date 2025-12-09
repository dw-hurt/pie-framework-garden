# TARS Video - Quick Start Guide

**Goal:** Generate a 10-12 minute video of TARS explaining AI ethics, then upload to YouTube.

## 🚀 3-Step Quick Start

### Step 1: Setup (5 minutes)

```bash
# 1. Download all project files to your computer
#    Save to: C:\Users\YourName\Documents\tars-video

# 2. Install Python dependencies
cd C:\Users\YourName\Documents\tars-video
pip install -r requirements.txt

# 3. Install FFmpeg
#    Windows: Download from https://ffmpeg.org/download.html
#    Add to PATH environment variable
```

### Step 2: Generate Video (20-30 minutes)

```bash
# Run the generator
python generate_video_enhanced.py

# Wait for completion...
# Output: tars_ai_ethics.mp4 (~150 MB)
```

### Step 3: Upload to YouTube (10 minutes)

```bash
# Setup YouTube API (first time only)
# 1. Go to https://console.cloud.google.com/
# 2. Create project → Enable "YouTube Data API v3"
# 3. Create OAuth credentials (Desktop app)
# 4. Download as client_secrets.json

# Upload video
python youtube_upload.py --privacy public
```

## 📋 Checklist

**Before generating:**
- [ ] Python 3.8+ installed
- [ ] FFmpeg installed and in PATH
- [ ] All project files downloaded
- [ ] Dependencies installed (`pip install -r requirements.txt`)

**After generating:**
- [ ] Video file created: `tars_ai_ethics.mp4`
- [ ] Duration is 10-12 minutes
- [ ] Preview video - check audio sync
- [ ] Subtitles are readable

**Before uploading:**
- [ ] Google Cloud project created
- [ ] YouTube Data API v3 enabled
- [ ] OAuth credentials downloaded as `client_secrets.json`
- [ ] Video reviewed and approved

**After uploading:**
- [ ] Video uploaded successfully
- [ ] YouTube link works
- [ ] Add custom thumbnail (optional)
- [ ] Add to PIE Framework repository
- [ ] Update GitBook with video link

## 🎯 Expected Results

**Video Specifications:**
- **Duration:** 10-12 minutes
- **Resolution:** 1920x1080 (Full HD)
- **File Size:** ~100-200 MB
- **Format:** MP4 (H.264 video, AAC audio)

**Content:**
- TARS character (animated geometric blocks)
- Starfield background
- AI-generated narration
- Subtitles throughout
- Intro and outro cards

## 🔗 Key Links

- **Full Documentation:** See `DEPLOYMENT_GUIDE.md`
- **Troubleshooting:** See `DEPLOYMENT_GUIDE.md` → Troubleshooting section
- **FFmpeg Download:** https://ffmpeg.org/download.html
- **Google Cloud Console:** https://console.cloud.google.com/
- **YouTube Studio:** https://studio.youtube.com/

## ⏱️ Time Estimates

| Task | Time |
|------|------|
| Initial setup | 5-10 minutes |
| Video generation | 20-30 minutes |
| Video review | 5 minutes |
| YouTube setup (first time) | 10-15 minutes |
| Video upload | 5-10 minutes |
| **Total (first time)** | **45-70 minutes** |
| **Total (subsequent)** | **25-35 minutes** |

## 🆘 Common Issues

**"ffmpeg not found"**
→ Install FFmpeg and add to PATH. Restart terminal.

**"ModuleNotFoundError"**
→ Run: `pip install -r requirements.txt`

**Audio generation fails**
→ Check internet connection (gTTS requires online access)

**YouTube upload fails**
→ Verify API enabled and client_secrets.json present

**Video too large**
→ Normal! 100-200 MB for 10-12 minute HD video

## 📖 Full Documentation

For detailed instructions, troubleshooting, and advanced options:
- Read `README.md` for overview
- Read `DEPLOYMENT_GUIDE.md` for complete walkthrough

---

**Ready to start?** Run: `python generate_video_enhanced.py`
