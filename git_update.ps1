# Git Update Script for tg-ytdlp-NEW project (PowerShell version)
# This script performs git add, commit, and force push to newdesign branch

Write-Host "🚀 Starting git update process..." -ForegroundColor Green

# Get current directory
$CURRENT_DIR = Get-Location
Write-Host "📍 Current directory: $CURRENT_DIR" -ForegroundColor Cyan

# Check if we're in a git repository
if (-not (Test-Path ".git")) {
    Write-Host "❌ Error: Not a git repository. Please run this script from the project root directory." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Check git status
Write-Host "📊 Checking git status..." -ForegroundColor Yellow
git status --porcelain

# Check if there are any changes to commit
$status = git status --porcelain
if ([string]::IsNullOrEmpty($status)) {
    Write-Host "ℹ️  No changes to commit. Repository is clean." -ForegroundColor Blue
    Read-Host "Press Enter to exit"
    exit 0
}

# Remove any files that should be ignored but are still tracked
Write-Host "🧹 Cleaning up ignored files..." -ForegroundColor Yellow
if (Test-Path "update.sh") {
    git rm --cached "update.sh" 2>$null
}
if (Test-Path "_cursor") {
    git rm --cached -r "_cursor" 2>$null
}
if (Test-Path "TXT") {
    git rm --cached -r "TXT" 2>$null
}
if (Test-Path ".venv") {
    git rm --cached -r ".venv" 2>$null
}
if (Test-Path "git_update.sh") {
    git rm --cached "git_update.sh" 2>$null
}
if (Test-Path "git_update.ps1") {
    git rm --cached "git_update.ps1" 2>$null
}
if (Test-Path "git_update.bat") {
    git rm --cached "git_update.bat" 2>$null
}
if (Test-Path "porn.sh") {
    git rm --cached "porn.sh" 2>$null
}
if (Test-Path "porn.py") {
    git rm --cached "porn.py" 2>$null
}
if (Test-Path "porn_req.txt") {
    git rm --cached "porn_req.txt" 2>$null
}
if (Test-Path "cleanup_git.sh") {
    git rm --cached "cleanup_git.sh" 2>$null
}
if (Test-Path "cleanup_git.ps1") {
    git rm --cached "cleanup_git.ps1" 2>$null
}

# Add all changes
Write-Host "➕ Adding all changes..." -ForegroundColor Yellow
git add .

# Check if add was successful
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Error: Failed to add changes to git" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Commit changes
Write-Host "💾 Committing changes..." -ForegroundColor Yellow
git commit -m "update code"

# Check if commit was successful
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Error: Failed to commit changes" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Force push to newdesign branch
Write-Host "🚀 Force pushing to newdesign branch..." -ForegroundColor Yellow
git push origin newdesign --force

# Check if push was successful
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Error: Failed to push to newdesign branch" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "✅ Git update completed successfully!" -ForegroundColor Green

# Show last commit info
$lastCommit = git log -1 --format="%H - %s (%cr)"
Write-Host "📅 Last commit: $lastCommit" -ForegroundColor Cyan

Read-Host "Press Enter to exit"
