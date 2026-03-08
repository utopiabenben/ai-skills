# Vervel Skills 离线安装指南

## 📦 需要安装的技能

从 skills.sh 排行榜确认的 4 个技能：

| 技能名 | 排名 | 来源仓库 | 下载次数 |
|--------|------|---------|---------|
| find-skills | #1 | vercel-labs/skills | 446.4K |
| vercel-react-best-practices | #2 | vercel-labs/agent-skills | 183.4K |
| web-design-guidelines | #3 | vercel-labs/agent-skills | 143.2K |
| frontend-design | #4 | anthropics/skills (不是 vercel) | 131.1K |

**注意**：frontend-design 来自 `anthropics/skills` 仓库，不是 vercel-labs！

---

## 安装方式 1：直接下载 ZIP（推荐，避开 git 网络问题）

### 1. find-skills

```bash
cd /root/.openclaw/workspace

# 下载 ZIP
wget https://github.com/vercel-labs/skills/archive/refs/heads/main.zip -O vercel-skills-main.zip

# 解压
unzip vercel-skills-main.zip

# 复制技能文件夹
cp -r vercel-skills-main/find-skills /root/.openclaw/workspace/skills/

# 清理
rm vercel-skills-main.zip
rm -rf vercel-skills-main
```

### 2. vercel-react-best-practices + web-design-guidelines

```bash
cd /root/.openclaw/workspace

# 下载 ZIP
wget https://github.com/vercel-labs/agent-skills/archive/refs/heads/main.zip -O vercel-agent-skills-main.zip

# 解压
unzip vercel-agent-skills-main.zip

# 复制两个技能文件夹
cp -r vercel-agent-skills-main/vercel-react-best-practices /root/.openclaw/workspace/skills/
cp -r vercel-agent-skills-main/web-design-guidelines /root/.openclaw/workspace/skills/

# 清理
rm vercel-agent-skills-main.zip
rm -rf vercel-agent-skills-main
```

### 3. frontend-design

```bash
cd /root/.openclaw/workspace

# 下载 ZIP (来自 anthropics/skills)
wget https://github.com/anthropics/skills/archive/refs/heads/main.zip -O anthropics-skills-main.zip

# 解压
unzip anthropics-skills-main.zip

# 复制技能文件夹
cp -r anthropics-skills-main/frontend-design /root/.openclaw/workspace/skills/

# 清理
rm anthropics-skills-main.zip
rm -rf anthropics-skills-main
```

---

## 安装方式 2：使用 git sparse-checkout（如果网络稳定）

```bash
# find-skills
cd /root/.openclaw/workspace
git init vercel-skills
cd vercel-skills
git remote add origin https://github.com/vercel-labs/skills.git
git config core.sparseCheckout true
echo "find-skills/" >> .git/info/sparse-checkout
git pull --depth=1 origin main
cp -r find-skills /root/.openclaw/workspace/skills/
cd ..
rm -rf vercel-skills

# vercel-react-best-practices + web-design-guidelines
git init vercel-agent-skills
cd vercel-agent-skills
git remote add origin https://github.com/vercel-labs/agent-skills.git
git config core.sparseCheckout true
echo "vercel-react-best-practices/" >> .git/info/sparse-checkout
echo "web-design-guidelines/" >> .git/info/sparse-checkout
git pull --depth=1 origin main
cp -r vercel-react-best-practices /root/.openclaw/workspace/skills/
cp -r web-design-guidelines /root/.openclaw/workspace/skills/
cd ..
rm -rf vercel-agent-skills

# frontend-design (from anthropics)
git init anthropics-skills
cd anthropics-skills
git remote add origin https://github.com/anthropics/skills.git
git config core.sparseCheckout true
echo "frontend-design/" >> .git/info/sparse-checkout
git pull --depth=1 origin main
cp -r frontend-design /root/.openclaw/workspace/skills/
cd ..
rm -rf anthropics-skills
```

---

## 安装后步骤

```bash
# 1. 安装所有技能命令
sudo /root/.openclaw/workspace/install-skills.sh

# 2. 验证安装
ls -la /root/.openclaw/workspace/skills/
find-skills --help 2>/dev/null || echo "find-skills installed but may not have CLI"

# 3. 更新技能清单
# SKILLS_INVENTORY.md 已更新，但需要手动确认这些技能确实已安装
```

---

## 使用 skillsadd 的方式（如果需要）

skillsadd 是官方工具，但可能需要 API 访问：

```bash
# 安装 skillsadd CLI
npm install -g skillsadd

# 安装技能
skillsadd install vercel-labs/skills/find-skills
skillsadd install vercel-labs/agent-skills/vercel-react-best-practices
skillsadd install vercel-labs/agent-skills/web-design-guidelines
skillsadd install anthropics/skills/frontend-design
```

**注意**：skillsadd 可能会限制下载速度，这就是为什么我推荐直接下载 ZIP。

---

## 故障排除

### 问题 1：wget 下载失败（超时）
**解决**：多次尝试，或使用 curl：
```bash
curl -L https://github.com/.../main.zip -o filename.zip
```

### 问题 2：unzip 命令不存在
**解决**：安装 unzip：
```bash
apt-get update && apt-get install -y unzip
```

### 问题 3：权限问题
**解决**：确保使用 root 或正确的用户权限

### 问题 4：技能没有 SKILL.md
**解决**：从原始仓库检查，可能需要另外下载 README 或文档

---

## 验证清单

- [ ] find-skills 文件夹存在且包含完整代码
- [ ] vercel-react-best-practices 文件夹存在且包含完整代码
- [ ] web-design-guidelines 文件夹存在且包含完整代码
- [ ] frontend-design 文件夹存在且包含完整代码
- [ ] 每个技能都有 `SKILL.md` 文件
- [ ] 运行 `install-skills.sh` 安装命令（如果需要）
- [ ] 更新 `SKILLS_INVENTORY.md` 为 ✅ 可用状态
- [ ] 提交更新到 GitHub

---

## 技能详情

### find-skills
- **仓库**：https://github.com/vercel-labs/skills/tree/main/find-skills
- **用途**：在代码库中查找和搜索内容
- **排行榜下载量**：446,400+

### vercel-react-best-practices
- **仓库**：https://github.com/vercel-labs/agent-skills/tree/main/vercel-react-best-practices
- **用途**：React 最佳实践指南
- **排行榜下载量**：183,400+

### web-design-guidelines
- **仓库**：https://github.com/vercel-labs/agent-skills/tree/main/web-design-guidelines
- **用途**：网页设计指南
- **排行榜下载量**：143,200+

### frontend-design
- **仓库**：https://github.com/anthropics/skills/tree/main/frontend-design
- **用途**：前端设计技能
- **排行榜下载量**：131,100+

---

**建议**：由于网络不稳定，优先使用**方式 1（ZIP 下载）**，可以断点续传或多次尝试。
