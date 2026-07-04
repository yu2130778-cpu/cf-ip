#!/bin/bash
# git_sync.sh
# Auto-sync ip.txt to GitHub
# Note: uses git remote URL for auth (token stored in .git/config)

cd "$(dirname "$0")" || exit 1

git pull origin main --no-rebase

git add ip.txt
commit_msg="Update ip.txt on $(date "+%Y-%m-%d %H:%M:%S")"
git commit -m "$commit_msg"

git push origin main --force

echo "ip.txt pushed to GitHub"
