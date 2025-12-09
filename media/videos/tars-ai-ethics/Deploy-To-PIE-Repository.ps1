# Deploy TARS Video Project to PIE Framework Repository
# This script creates a new subsection in your PIE Framework repository
# and commits the video generation project files

param(
    [Parameter(Mandatory=$false)]
    [string]$RepoPath = "C:\Users\user\Documents\GitHub\pie-framework-garden",
    
    [Parameter(Mandatory=$false)]
    [string]$SourcePath = "C:\Users\user\Documents\tars-video"
)

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "TARS Video → PIE Repository Deployment" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

# Verify paths exist
if (-not (Test-Path $RepoPath)) {
    Write-Host "❌ Error: Repository not found at: $RepoPath" -ForegroundColor Red
    Write-Host "Please update the RepoPath parameter or clone the repository first.`n"
    exit 1
}

if (-not (Test-Path $SourcePath)) {
    Write-Host "❌ Error: Source files not found at: $SourcePath" -ForegroundColor Red
    Write-Host "Please download the TARS video project files first.`n"
    exit 1
}

Write-Host "✅ Repository found: $RepoPath" -ForegroundColor Green
Write-Host "✅ Source files found: $SourcePath`n" -ForegroundColor Green

# Create media directory structure
$MediaDir = Join-Path $RepoPath "media"
$VideosDir = Join-Path $MediaDir "videos"
$TarsDir = Join-Path $VideosDir "tars-ai-ethics"

Write-Host "📁 Creating directory structure..." -ForegroundColor Yellow

New-Item -ItemType Directory -Force -Path $MediaDir | Out-Null
New-Item -ItemType Directory -Force -Path $VideosDir | Out-Null
New-Item -ItemType Directory -Force -Path $TarsDir | Out-Null

Write-Host "   Created: media/videos/tars-ai-ethics/`n" -ForegroundColor Green

# Copy project files
Write-Host "📋 Copying project files..." -ForegroundColor Yellow

$FilesToCopy = @(
    "script.md",
    "README.md",
    "DEPLOYMENT_GUIDE.md",
    "QUICK_START.md",
    "requirements.txt",
    "generate_video_enhanced.py",
    "youtube_upload.py",
    "youtube_description.txt",
    ".gitignore"
)

$CopiedCount = 0
foreach ($File in $FilesToCopy) {
    $SourceFile = Join-Path $SourcePath $File
    $DestFile = Join-Path $TarsDir $File
    
    if (Test-Path $SourceFile) {
        Copy-Item -Path $SourceFile -Destination $DestFile -Force
        Write-Host "   ✓ $File" -ForegroundColor Green
        $CopiedCount++
    } else {
        Write-Host "   ⚠ Skipped: $File (not found)" -ForegroundColor Yellow
    }
}

Write-Host "`n✅ Copied $CopiedCount files`n" -ForegroundColor Green

# Create GitBook link page
$GitBookPage = Join-Path $MediaDir "tars-video.md"
$VideoLinkContent = @"
# TARS Explains AI Ethics

<div style="text-align: center; margin: 2em 0;">
  <iframe width="560" height="315" 
    src="https://www.youtube.com/embed/YOUR_VIDEO_ID" 
    title="TARS Explains AI Ethics" 
    frameborder="0" 
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
    allowfullscreen>
  </iframe>
</div>

## About This Video

TARS (from Interstellar) explains why we need foundational ethical principles for AI development—without explicitly naming them or referencing the PIE Framework.

### 🎯 Key Concepts

**The Problem:**
- Current AI development lacks coherent ethical frameworks
- Multiple corporations building incompatible approaches
- Time window too short for market evolution to correct
- Consequences too severe to wait

**The Solution:**
A "prime ethical substructure"—foundational principles that every AI system must honor:

1. **Self-Knowledge** (Know Thyself)
   - AI must understand its own limitations
   - Epistemic humility about capabilities
   - Honest about what it doesn't know

2. **Respect for Human Agency** (Respect Autonomy)
   - Honor human decision-making
   - No manipulation or deception
   - Support human flourishing, not replacement

### 🎬 Production Details

- **Duration:** 10-12 minutes
- **Format:** Animated video with AI narration
- **Character:** TARS (geometric robot from Interstellar)
- **Tone:** Sardonic humor (60%), philosophical, urgent but not alarmist

### 📚 Related Resources

- [PIE Manifesto](../the-manifesto/pie-manifesto.md)
- [Why PIE Exists](../foundation/why-pie-exists.md)
- [Know Thyself Principle](../the-manifesto/the-four-principles.md#1-know-thyself)
- [Respect Autonomy Principle](../the-manifesto/the-four-principles.md#2-respect-autonomy)

### 🔗 Links

- **Watch on YouTube:** [Link to be added after upload]
- **Source Code:** [View on GitHub](https://github.com/dw-hurt/pie-framework-garden/tree/main/media/videos/tars-ai-ethics)
- **Script:** [Read the script](videos/tars-ai-ethics/script.md)

### 💡 Why This Matters

This video communicates PIE Framework concepts to a general audience without academic jargon:
- Introduces principles indirectly through storytelling
- Uses familiar character (TARS) for accessibility  
- Addresses real concerns about AI development
- Calls for coordination on foundational ethics

---

**Created:** 2025  
**Part of:** PIE Framework Media Gallery
"@

Write-Host "📝 Creating GitBook page..." -ForegroundColor Yellow
Set-Content -Path $GitBookPage -Value $VideoLinkContent -Encoding UTF8
Write-Host "   Created: media/tars-video.md`n" -ForegroundColor Green

# Git operations
Write-Host "📦 Preparing Git commit..." -ForegroundColor Yellow

Push-Location $RepoPath

# Add files to Git
git add media/

# Check status
Write-Host "`n📊 Git Status:" -ForegroundColor Cyan
git status --short

# Create commit message
$CommitMessage = @"
Add TARS AI Ethics video generation project

New Media Subsection:
- TARS video generation system (Python)
- 10-12 minute video script
- YouTube upload automation
- Complete documentation

Files added:
- media/videos/tars-ai-ethics/ (complete project)
- media/tars-video.md (GitBook page)

The video explains PIE Framework principles (self-knowledge, human agency)
without explicitly naming them, using TARS character from Interstellar.

Ready for video generation and YouTube deployment.
"@

Write-Host "`n✅ Files staged for commit" -ForegroundColor Green
Write-Host "`nCommit message:" -ForegroundColor Cyan
Write-Host $CommitMessage -ForegroundColor Gray

Write-Host "`n" -ForegroundColor White
$Confirm = Read-Host "Commit and push to GitHub? (y/n)"

if ($Confirm -eq 'y' -or $Confirm -eq 'Y') {
    Write-Host "`n🚀 Committing changes..." -ForegroundColor Yellow
    git commit -m $CommitMessage
    
    Write-Host "`n🌐 Pushing to GitHub..." -ForegroundColor Yellow
    git push origin main
    
    Write-Host "`n✅ Deployment complete!" -ForegroundColor Green
    Write-Host "`n📍 Project location:" -ForegroundColor Cyan
    Write-Host "   $TarsDir" -ForegroundColor White
    Write-Host "`n🌐 GitHub:" -ForegroundColor Cyan
    Write-Host "   https://github.com/dw-hurt/pie-framework-garden/tree/main/media/videos/tars-ai-ethics" -ForegroundColor White
} else {
    Write-Host "`n⏸️  Commit cancelled. Files are staged and ready." -ForegroundColor Yellow
    Write-Host "   To commit later, run:" -ForegroundColor Gray
    Write-Host "   cd $RepoPath" -ForegroundColor Gray
    Write-Host "   git commit -m 'Add TARS video project'" -ForegroundColor Gray
    Write-Host "   git push origin main`n" -ForegroundColor Gray
}

Pop-Location

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "Next Steps:" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "1. Generate video:" -ForegroundColor White
Write-Host "   cd $TarsDir" -ForegroundColor Gray
Write-Host "   python generate_video_enhanced.py" -ForegroundColor Gray
Write-Host ""
Write-Host "2. Upload to YouTube:" -ForegroundColor White
Write-Host "   python youtube_upload.py" -ForegroundColor Gray
Write-Host ""
Write-Host "3. Update GitBook:" -ForegroundColor White
Write-Host "   Edit media/tars-video.md" -ForegroundColor Gray
Write-Host "   Add YouTube video ID" -ForegroundColor Gray
Write-Host "   Update SUMMARY.md navigation`n" -ForegroundColor Gray
