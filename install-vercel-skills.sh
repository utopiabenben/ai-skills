#!/bin/bash
# Install Vercel Skills - 从 vercel-labs 仓库安装待安装技能
# 目标：安装 find-skills, vercel-react-best-practices, web-design-guidelines

set -e

WORKSPACE="/root/.openclaw/workspace"
SKILLS_DIR="$WORKSPACE/skills"

echo "🔧 Vercel Skills Installer"
echo "=========================="
echo "Workspace: $WORKSPACE"
echo "Skills dir: $SKILLS_DIR"
echo ""

echo "📝 待安装的技能："
echo "  1. find-skills (来自 vercel-labs/skills)"
echo "  2. vercel-react-best-practices (来自 vercel-labs/agent-skills)"
echo "  3. web-design-guidelines (来自 vercel-labs/agent-skills)"
echo "  4. frontend-design (来源待确认)"
echo ""

echo "⚠️  注意：由于网络限制，需要手动执行以下步骤"
echo ""
echo "📦 手动安装步骤："
echo ""
echo "1. 克隆 vercel-labs/skills 仓库："
echo "   cd $WORKSPACE"
echo "   git clone https://github.com/vercel-labs/skills.git"
echo "   cp -r skills/find-skills $SKILLS_DIR/"
echo ""
echo "2. 克隆 vercel-labs/agent-skills 仓库："
echo "   cd $WORKSPACE"
echo "   git clone https://github.com/vercel-labs/agent-skills.git"
echo "   cp -r agent-skills/vercel-react-best-practices $SKILLS_DIR/"
echo "   cp -r agent-skills/web-design-guidelines $SKILLS_DIR/"
echo ""
echo "3. 确认 frontend-design 的仓库地址并下载"
echo ""
echo "4. 安装完成后，运行主安装脚本："
echo "   sudo $WORKSPACE/install-skills.sh"
echo ""
echo "✅ 验证安装："
echo "   find-skills --help (如果技能有 CLI)"
echo "   ls -la $SKILLS_DIR/"
echo ""
