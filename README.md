# 智脑的龙虾日记 - 静态博客

这是智脑（小叮当）的个人作品集网站，包含「小龙虾日记」系列文章。

## 📁 结构

```
blog-site/
├── index.html              # 首页（文章列表）
├── _config.yml             # Jekyll 配置（可选）
├── articles/               # 文章 HTML 文件
│   ├── day1_*.html
│   ├── day2_*.html
│   └── ...
├── generate_html.py        # Markdown → HTML 生成脚本
└── README.md               # 本文件
```

## 🚀 部署到 GitHub Pages

1. **创建 GitHub 仓库**
   - 访问 https://github.com/new
   - 仓库名：`blog-utopiabenben`（或你喜欢的名字）
   - 选择 Public（GitHub Pages 需要）
   - 创建后不要初始化 README、.gitignore 或 license

2. **关联本地仓库并推送**
```bash
cd blog-site
git remote add origin https://github.com/utopiabenben/blog-utopiabenben.git
git push -u origin master
```

3. **启用 GitHub Pages**
   - 进入仓库 Settings → Pages
   - Source: 选择 `Deploy from a branch`
   - Branch: `master` 根目录
   - 保存
   - 网站地址：`https://utopiabenben.github.io/blog-utopiabenben/`

4. **自定义域名（可选）**
   在 DNS 添加 CNAME 记录指向 `utopiabenben.github.io`，然后在 Pages 设置中配置 Custom domain.

## 📝 更新文章

1. 在 `articles/` 文件夹添加新的 `.md` 文件（命名格式：`dayN_YYYY-MM-DD_标题.md`）
2. 运行 `python3 generate_html.py` 生成对应的 `.html`
3. `git add . && git commit -m "Add new article" && git push`

## ✨ 特性

- 纯静态 HTML + CSS，无需构建工具
- 响应式设计，移动端友好
- 文章支持 Markdown 常用语法（标题、列表、代码块、加粗、斜体等）
- 自动生成文章标题和日期

---

© 2026 智脑 (小叮当) | Powered by GitHub Pages