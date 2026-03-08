#!/bin/bash
# OpenClaw Skills Installer
# 将 skills/ 目录中的技能安装到系统 PATH

set -e

WORKSPACE="/root/.openclaw/workspace"
SKILLS_DIR="$WORKSPACE/skills"
BIN_DIR="/usr/local/bin"

# 颜色定义
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo "🔧 OpenClaw Skills Installer"
echo "============================"
echo "Workspace: $WORKSPACE"
echo "Skills dir: $SKILLS_DIR"
echo "Bin dir: $BIN_DIR"
echo ""

# 检查权限
if [ "$EUID" -ne 0 ]; then
   echo -e "${YELLOW}⚠️  需要 root 权限安装到 /usr/local/bin${NC}"
   echo "请使用 sudo 运行此脚本，或手动创建符号链接"
   exit 1
fi

# 遍历所有技能目录
echo "📦 正在安装技能..."
for skill_dir in "$SKILLS_DIR"/*/; do
    skill_name=$(basename "$skill_dir")
    main_script=""

    # 查找主要的可执行脚本
    if [ -f "$skill_dir/${skill_name}.py" ]; then
        main_script="$skill_dir/${skill_name}.py"
    elif [ -f "$skill_dir/${skill_name//-/_}.py" ]; then
        main_script="$skill_dir/${skill_name//-/_}.py"
    else
        # 查找任何 .py 文件
        main_script=$(find "$skill_dir" -name "*.py" -type f | head -1)
    fi

    if [ -n "$main_script" ] && [ -f "$main_script" ]; then
        # 创建符号链接
        target_name=$(echo "$skill_name" | tr '-' '_')
        target_path="$BIN_DIR/$target_name"

        echo "正在安装: $skill_name"
        ln -sf "$main_script" "$target_path"
        chmod +x "$main_script"
        echo -e "  ✅ $target_name -> $main_script"
    else
        echo -e "${YELLOW}  ⚠️  未找到主脚本: $skill_name${NC}"
    fi
done

echo ""
echo "✅ 所有技能已安装！"
echo ""
echo "验证安装："
for skill_name in batch-renamer photo-organizer download-organizer video-organizer music-tagger file-sorter doc-converter; do
    cmd_name=$(echo "$skill_name" | tr '-' '_')
    if [ -L "$BIN_DIR/$cmd_name" ]; then
        echo "  ✅ $cmd_name"
    else
        echo "  ❌ $cmd_name (未安装)"
    fi
done

echo ""
echo "💡 使用示例："
echo "  batch_renamer --help"
echo "  photo_organizer --help"
echo "  file_sorter --help"
echo ""
echo "📝 注意："
echo "  1. 某些技能可能需要额外的 Python 依赖"
echo "  2. 使用前请阅读相应技能的 README.md"
echo "  3. 可以通过 'which <command>' 验证安装"
