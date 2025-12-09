# TARS AI Ethics Video Project

An automated video generation system that creates a 10-12 minute video featuring TARS (from Interstellar) explaining AI ethics principles without explicitly naming them.

## 🎯 Project Overview

This project generates a professional video featuring:
- **TARS geometric character** with animated blocks
- **Animated starfield background** with depth layers
- **Script-driven narration** with AI-generated speech
- **Subtitles** for accessibility
- **Automated YouTube upload** capability

**Key Themes Discussed:**
- Why unchecked AI ethics could be destructive
- Problems with inconsistent corporate AI frameworks
- Need for "prime ethical substructure"
- Human agency and flourishing
- Self-knowledge and epistemic humility in AI

**PIE Concepts Introduced (without direct naming):**
1. **Self-Knowledge** (Know Thyself principle)
2. **Respect for Human Agency** (Respect Autonomy principle)

## 📁 Project Structure

```
tars-video/
├── README.md                      # This file
├── DEPLOYMENT_GUIDE.md            # Complete deployment instructions
├── requirements.txt               # Python dependencies
├── script.md                      # Video script (already created)
├── generate_video_enhanced.py     # Main video generator (Python)
├── youtube_upload.py              # YouTube upload automation
├── youtube_description.txt        # Video description for YouTube
├── .env.example                   # Environment variables template
└── temp_audio/                    # Temporary audio files (auto-created)
```

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+**
- **FFmpeg** (for video processing)
- **Git** (for repository management)

### 1. Install Dependencies

```bash
# Navigate to project directory
cd tars-video

# Install Python packages
pip install -r requirements.txt

# Install FFmpeg (if not already installed)
# Windows: Download from https://ffmpeg.org/download.html
# Mac: brew install ffmpeg
# Linux: sudo apt-get install ffmpeg
```

### 2. Generate Video

```bash
# Generate the complete video (10-12 minutes)
python generate_video_enhanced.py

# Custom options
python generate_video_enhanced.py --script script.md --output my_video.mp4 --fps 30
```

**Expected output:** `tars_ai_ethics.mp4` (~100-200 MB)

**Generation time:** 15-30 minutes depending on system

### 3. Preview Video

Open `tars_ai_ethics.mp4` in your video player to review before uploading.

### 4. Upload to YouTube (Optional)

```bash
# First-time setup: Get YouTube API credentials
# See DEPLOYMENT_GUIDE.md for detailed instructions

# Upload video
python youtube_upload.py --video tars_ai_ethics.mp4 --privacy public
```

## 📊 Video Specifications

- **Duration:** 10-12 minutes
- **Resolution:** 1920x1080 (Full HD)
- **Frame Rate:** 30 fps
- **Format:** MP4 (H.264 video, AAC audio)
- **Bitrate:** 8000k
- **File Size:** ~100-200 MB

## 🎨 Customization

### Modify Visual Style

Edit `CONFIG` in `generate_video_enhanced.py`:

```python
@dataclass
class VideoConfig:
    video_width: int = 1920
    video_height: int = 1080
    fps: int = 30
    background_color: Tuple[int, int, int] = (10, 10, 20)
    tars_color: Tuple[int, int, int] = (200, 200, 220)
    # ... more options
```

### Modify Script

Edit `script.md` to change:
- Dialogue content
- Timing sections
- Actions and animations
- Tone and emphasis

### Animation Modes

Available in script via actions:
- `idle`: Subtle breathing/rotation (default)
- `thinking`: Rotating blocks pattern
- `emphatic`: Larger movements for emphasis
- `forming`: Blocks assembling from scattered positions

## 🔧 Troubleshooting

### Video generation fails

**Problem:** `ModuleNotFoundError` or import errors

**Solution:**
```bash
pip install --upgrade -r requirements.txt
```

### Audio issues

**Problem:** No audio or garbled speech

**Solution:**
- Ensure `gTTS` is installed: `pip install gTTS`
- Check internet connection (gTTS requires online access)
- Try regenerating with: `python generate_video_enhanced.py`

### FFmpeg not found

**Problem:** `FileNotFoundError: ffmpeg`

**Solution:**
- Install FFmpeg: https://ffmpeg.org/download.html
- Add to system PATH
- Restart terminal/command prompt

### YouTube upload fails

**Problem:** Authentication or API errors

**Solution:**
- Verify `client_secrets.json` is present
- Check YouTube API is enabled in Google Cloud Console
- Delete `youtube_credentials.json` and re-authenticate

## 📖 Complete Documentation

See `DEPLOYMENT_GUIDE.md` for:
- Detailed setup instructions
- YouTube API configuration
- Repository integration
- Troubleshooting guide
- Advanced customization

## 🎯 Next Steps

1. **Generate video:** `python generate_video_enhanced.py`
2. **Review output:** Check `tars_ai_ethics.mp4`
3. **Upload to YouTube:** `python youtube_upload.py`
4. **Share:** Distribute video link
5. **Integrate:** Add to PIE Framework repository

## 📜 License

Part of the PIE Framework project. See main repository for license details.

## 🤝 Contributing

This is a research project. For questions or contributions, see the main PIE Framework repository.

---

**Related Projects:**
- [PIE Framework](https://github.com/dw-hurt/pie-framework-garden)
- [PIE Framework Private](https://github.com/dw-hurt/pie-framework-private)

**Contact:** See PIE Framework repository for contact information.
