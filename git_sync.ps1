# git_sync.ps1
# Auto-sync ip.txt to GitHub
# Note: uses git remote URL for auth (token stored in .git/config)

Set-Location $PSScriptRoot
$null = git pull origin main --no-rebase 2>$null
$null = git add ip.txt
$commit_msg = "Update ip.txt on $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
$null = git commit -m $commit_msg 2>$null
$null = git push origin main --force
