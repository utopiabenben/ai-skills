#!/bin/bash
# 部署博客到 GitHub Pages
# 使用前请修改 REMOTE_URL 为你的仓库地址

set -e

REMOTE_URL="https://github.com/utopiabenben/blog-utopiabenben.git"
BRANCH="master"

echo "=== 部署博客到 GitHub Pages ==="
echo "仓库: $REMOTE_URL"
echo "分支: $BRANCH"
echo ""

# 确保已提交所有更改
git add -A
git commit -m "Deploy $(date '+%Y-%m-%d %H:%M')" || echo "Nothing to commit"

# 推送到远程
git push -u $BRANCH origin:$BRANCH

echo ""
echo "✅ 推送完成！"
echo "📌 下一步："
echo "1. 访问 https://github.com/$(echo $REMOTE_URL | cut -d'/' -f4-5)/settings/pages"
echo "2. 在 Pages 设置中选择 Source: Deploy from a branch"
echo "3. 选择 branch: $BRANCH, folder: / (root)"
echo "4. 保存后网站将在几分钟内生效"
echo ""
echo "你的网站地址：https://$(echo $REMOTE_URL | cut -d'/' -f4 | cut -d'.' -f1).github.io/$(echo $REMOTE_URL | cut -d'/' -f5 | cut -d'.' -f1)/"