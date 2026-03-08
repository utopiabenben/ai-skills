# AI Skills Inventory - 已安装技能清单

最后更新：2026-03-08

## 概述

本文档记录了当前 OpenClaw 工作空间中已安装和可用的所有技能。技能分为两大类：

1. **本地开发的技能**：在 `skills/` 目录下的自定义技能
2. **系统内置技能**：OpenClaw 平台自带的功能技能
3. **第三方安装的技能**：通过 clawhub 安装的技能

---

## 本地开发的技能 (Local Skills)

### 1. batch-renamer@1.0.0
- **路径**：`skills/batch-renamer/`
- **描述**：批量文件重命名工具，支持多种命名模式、正则表达式、预览和撤销功能
- **主要功能**：
  - 序号重命名（{001}, {01}, {1}）
  - 日期重命名（{YYYY}, {MM}, {DD}）
  - 正则表达式替换
  - 预览模式和撤销操作
- **适用场景**：照片整理、文档归档、下载文件重命名
- **状态**：✅ 开发完成，已发布

---

### 2. photo-organizer@1.0.0
- **路径**：`skills/photo-organizer/`
- **描述**：照片批量整理工具，支持按时间、地点自动分类和打标签
- **主要功能**：
  - 读取照片 EXIF 信息（拍摄时间、GPS 地点）
  - 按时间自动分类（年/月文件夹结构）
  - 按地点自动分类（如果有 GPS 信息）
  - 批量打标签
  - 预览模式和撤销操作
- **适用场景**：手机照片整理、相册归档、旅行照片管理
- **状态**：✅ 开发完成，已发布

---

### 3. download-organizer@1.0.0
- **路径**：`skills/download-organizer/`
- **描述**：下载文件自动分类工具，自动识别文件类型并按类别整理到不同文件夹
- **主要功能**：
  - 自动识别文件类型（文档、图片、视频、音频、安装包、压缩包、代码）
  - 按文件类型自动分类到不同文件夹
  - 支持自定义分类规则
  - 预览模式和撤销操作
- **默认分类**：
  - `documents/`：.pdf, .doc, .docx, .txt, .xls, .xlsx, .ppt, .pptx
  - `images/`：.jpg, .jpeg, .png, .gif, .webp, .heic
  - `videos/`：.mp4, .avi, .mov, .mkv
  - `audio/`：.mp3, .wav, .flac, .aac
  - `installers/`：.exe, .msi, .dmg, .pkg, .deb, .rpm
  - `archives/`：.zip, .rar, .7z, .tar, .gz
  - `code/`：.py, .js, .html, .css, .java, .cpp
- **适用场景**：整理下载文件夹，自动分类各类文件
- **状态**：✅ 开发完成，已发布

---

### 4. video-organizer@1.0.0
- **路径**：`skills/video-organizer/`
- **描述**：视频文件批量重命名和整理工具，支持按时间、格式、分辨率等方式整理视频
- **主要功能**：
  - 自动识别视频文件格式（mp4, avi, mov, mkv, flv, wmv, webm）
  - 按时间整理（文件修改时间）
  - 按格式/扩展名整理
  - 批量重命名（支持多种命名模式、正则表达式）
  - 预览模式和撤销操作
- **适用场景**：整理下载的视频、家庭视频归档、视频素材管理
- **状态**：✅ 开发完成，已发布

---

### 5. music-tagger@1.0.0
- **路径**：`skills/music-tagger/`
- **描述**：音乐文件批量标签工具，支持读取/编辑音乐元数据，按标签整理音乐文件
- **主要功能**：
  - 读取/编辑音乐元数据（歌名、艺术家、专辑、流派、年份、曲目号）
  - 批量编辑标签
  - 按标签整理音乐文件（艺术家/专辑、流派、年份等）
  - 预览模式和撤销操作
- **支持的音乐格式**：mp3, flac, wav, aac, m4a, ogg, wma, ape
- **依赖**：`mutagen`（用于处理音乐元数据）
- **适用场景**：音乐库整理、MP3 标签编辑、音乐归档
- **状态**：✅ 开发完成，已发布

---

### 6. file-sorter@1.0.0
- **路径**：`skills/file-sorter/`
- **描述**：通用文件智能分类工具，支持多种分类规则：类型、大小、日期、关键词等
- **主要功能**：
  - 按文件类型分类（默认 7 个类别）
  - 按文件大小分类（small < 1MB, medium 1-100MB, large > 100MB）
  - 按文件日期分类（创建、修改、访问日期）
  - 灵活操作：移动、复制、创建符号链接
  - 自定义分类规则
  - 规则预设保存和加载
  - 预览功能和撤销操作
- **适用场景**：通用文件整理，支持多种复杂的分类需求
- **状态**：✅ 开发完成，已发布（最新技能！2026-03-07）

---

### 7. doc-converter@1.0.0
- **路径**：`skills/doc-converter/`
- **描述**：文档格式批量转换工具，支持 PDF、Word、Excel、PowerPoint、图片等多种格式之间的批量转换
- **主要功能**：
  - 支持多种文档格式转换（PDF ↔ Word ↔ Excel ↔ PPT ↔ 图片）
  - 批量转换整个文件夹
  - 预览模式（先看效果再执行）
  - 撤销操作（安全可靠）
- **支持格式**：pdf, docx, xlsx, pptx, jpg, png
- **依赖**：`pdf2docx`, `docx2pdf`, `pdf2image`, `Pillow`, `python-docx`, `openpyxl`, `python-pptx`
- **适用场景**：批量文档转换，如 PDF 转 Word、图片转 PDF、Word 转 PDF 等
- **状态**：✅ 开发完成，已发布

---

### 8. duckduckgo-search@1.0.0
- **路径**：`skills/duckduckgo-search/`
- **描述**：使用 DuckDuckGo 进行网页搜索，无需 API 密钥，无需额外依赖
- **主要功能**：
  - 网页搜索
  - 获取搜索结果摘要
  - 无需 API 密钥
  - 无需额外 Python 依赖
- **使用方法**：`python search.py "搜索关键词"`
- **特点**：隐私优先（DuckDuckGo 不追踪用户）、免费使用、轻量级
- **状态**：✅ 开发完成，已发布

---

### 9. image-analysis@1.0.0
- **路径**：`skills/image-analysis/`
- **描述**：图片分析与 OCR（光学字符识别）技能，用于识别图片中的文字和内容
- **主要功能**：
  - 图片文字识别（OCR）
  - 支持多种图片格式（JPG, PNG, etc.）
  - 提取图片中的文本内容
- **使用方法**：`python analyze.py /path/to/image.jpg`
- **状态**：✅ 开发完成，已发布

---

### 10. image-generate@1.0.0
- **路径**：`skills/image-generate/`
- **描述**：使用内置 image_generate.py 脚本生成图片，准备清晰具体的 prompt
- **主要功能**：
  - 根据文本描述生成图片
  - 支持多种图片生成模型
  - 灵活的 API 密钥配置
- **使用方法**：`python scripts/image_generate.py "一只可爱的猫"`
- **认证方式**：MODEL_IMAGE_API_KEY, ARK_API_KEY, 或 VOLCENGINE_ACCESS_KEY/VOLCENGINE_SECRET_KEY
- **状态**：✅ 开发完成，已发布

---

### 11. veadk-go-skills@1.0.0
- **路径**：`skills/veadk-go-skills/`
- **描述**：VeADK-Go 相关技能和工具，包括直接根据需求生成 Agent，将 Enio Agent 转换为 VeADK-Go Agent
- **主要功能**：
  - 直接根据需求生成 VeADK-Go Agent
  - 将 Enio Agent 转换为 VeADK-Go Agent
  - 提供 VeADK-Go 开发框架的代码结构、功能特性以及代码示例
- **参考文档**：`common/*.md`, `converter/enio_rule.md`
- **状态**：✅ 开发完成，已发布

---

### 12. veadk-skills@1.0.0
- **路径**：`skills/veadk-skills/`
- **描述**：VeADK 相关技能和工具，包括根据需求生成 Agent，将 Langchain/Dify 工作流转换为 VeADK Agent
- **主要功能**：
  - 直接根据需求生成 VeADK Agent
  - 将 Langchain/Langgraph 代码转换为 VeADK Agent
  - 将 Dify 工作流转换为 VeADK Agent
  - 提供 VeADK 开发框架的代码结构、功能特性以及代码示例
- **参考文档**：`references/common/*.md`, `references/converter/*.md`, `references/generator/*.md`
- **状态**：✅ 开发完成，已发布

---

### 13. video-generate@1.0.0
- **路径**：`skills/video-generate/`
- **描述**：使用 video_generate.py 脚本生成视频，需要提供文件名和 prompt，可选提供首帧图片
- **主要功能**：
  - 根据文本描述生成视频
  - 支持通过首帧图片控制视频起始画面
  - 首帧可以是 URL 或本地文件路径
- **使用方法**：`python scripts/video_generate.py "cat.mp4" "一只可爱的猫"`
- **认证方式**：MODEL_VIDEO_API_KEY, ARK_API_KEY, 或 VOLCENGINE_ACCESS_KEY/VOLCENGINE_SECRET_KEY
- **状态**：✅ 开发完成，已发布

---

### 14. find-skills@1.0.0
- **路径**：`skills/find-skills/`
- **描述**：来自 vercel-labs/skills 的技能发现和搜索工具
- **主要功能**：
  - 搜索和发现可用的AI技能
  - 技能分类和筛选
  - 技能元数据查询
- **来源**：vercel-labs/skills
- **状态**：✅ 已安装

---

### 15. vercel-react-best-practices@1.0.0
- **路径**：`skills/vercel-react-best-practices/`
- **描述**：来自 vercel-labs/agent-skills 的React最佳实践指南
- **主要功能**：
  - React开发最佳实践
  - Vercel部署指南
  - React组件设计模式
- **来源**：vercel-labs/agent-skills
- **状态**：✅ 已安装

---

### 16. web-design-guidelines@1.0.0
- **路径**：`skills/web-design-guidelines/`
- **描述**：来自 vercel-labs/agent-skills 的网页设计指南
- **主要功能**：
  - 网页设计最佳实践
  - UI/UX设计原则
  - 响应式设计指南
- **来源**：vercel-labs/agent-skills
- **状态**：✅ 已安装

---

### 17. frontend-design@1.0.0
- **路径**：`skills/frontend-design/`
- **描述**：前端设计和开发技能集合
- **主要功能**：
  - 前端开发最佳实践
  - 现代前端框架指南
  - 前端性能优化
- **状态**：✅ 已安装

---

## 系统内置技能 (Built-in Skills)

### 1. weather
- **描述**：通过 wttr.in 获取当前天气和天气预报
- **使用场景**：查询任何地点的天气、温度、预报
- **限制**：不支持历史天气数据、严重天气警报、详细气象分析
- **API Key**：不需要

---

### 2. healthcheck
- **描述**：主机安全加固和风险姿态配置
- **使用场景**：安全审计、防火墙/SSH/更新加固、暴露面审查、版本状态检查
- **适用对象**：运行 OpenClaw 的机器（笔记本电脑、工作站、树莓派、VPS）

---

### 3. nano-pdf
- **描述**：用自然语言编辑 PDF
- **功能**：通过自然语言命令编辑 PDF 文档

---

### 4. github
- **描述**：使用 gh CLI 操作 GitHub
- **功能**：管理仓库、issues、PRs、gists 等

---

### 5. notion
- **描述**：使用 Notion API 管理页面和数据库
- **功能**：读写 Notion 页面、查询数据库

---

### 6. obsidian
- **描述**：操作 Obsidian 笔记库
- **功能**：读写笔记、管理 vault

---

## 第三方安装的技能 (Clawhub Skills)

### 1. obsidian-ontology-sync@1.0.1
- **路径**：`skills/obsidian-ontology-sync/`
- **来源**：通过 clawhub 安装
- **描述**：Obsidian PKM（人类友好笔记）与结构化本体（机器可查询图）之间的双向同步
- **核心概念**：Obsidian 是 PRIMARY（人类写自然笔记）→ 本体是 DERIVED（机器提取结构）→ 反馈循环改善两者
- **主要功能**：
  - 自动从 Markdown 笔记中提取实体和关系
  - 维护本体图
  - 提供反馈以改进笔记结构
  - 每几小时通过 cron 自动运行同步
- **适用场景**：团队管理、联系人追踪、商业智能
- **安装时间**：2026-03-07
- **版本**：1.0.1

---

### 2. openclaw-tavily-search@0.1.0
- **路径**：`skills/openclaw-tavily-search/`
- **来源**：通过 clawhub 安装
- **描述**：使用 Tavily API 进行网络搜索（Brave 的替代方案）
- **使用时机**：当用户要求搜索网络/查找来源/找链接，而 Brave web_search 不可用或不合适时
- **主要功能**：
  - 返回小量相关结果（标题、URL、摘要）
  - 可选择性包括简短答案摘要
  - 支持多种输出格式（raw JSON、brave 格式、Markdown）
- **环境变量**：`TAVILY_API_KEY`
- **安装时间**：2026-03-07
- **版本**：0.1.0

---

## 技能分类总结

| 类别 | 技能数量 | 技能列表 |
|------|---------|---------|
| **本地开发** | 17 | batch-renamer, photo-organizer, download-organizer, video-organizer, music-tagger, file-sorter, doc-converter, duckduckgo-search, image-analysis, image-generate, veadk-go-skills, veadk-skills, video-generate, find-skills, vercel-react-best-practices, web-design-guidelines, frontend-design |
| **系统内置** | 6 | weather, healthcheck, nano-pdf, github, notion, obsidian |
| **第三方安装** | 2 | obsidian-ontology-sync, openclaw-tavily-search |
| **总计** | **25** | - |

---

## 技能之间关系

### 文件管理技能套件（批量开发）
这 7 个技能形成了一个完整的文件管理和组织解决方案：

1. **batch-renamer**：通用的批量重命名工具
2. **photo-organizer**：专门针对照片（使用 EXIF 信息）
3. **download-organizer**：专门针对下载文件夹（按文件类型分类）
4. **video-organizer**：专门针对视频文件（按时间/格式整理 + 重命名）
5. **music-tagger**：专门针对音乐文件（编辑元数据 + 按标签整理）
6. **file-sorter**：通用智能分类工具（按类型/大小/日期多种规则）
7. **doc-converter**：文档格式转换工具（PDF ↔ Word ↔ Excel ↔ PPT ↔ 图片）

### 知识管理技能组合
- **obsidian**：操作 Obsidian 笔记库
- **obsidian-ontology-sync**：Obsidian 笔记与结构化本体的同步
- **openclaw-tavily-search**：网络搜索，补充知识库

### 开发与运维技能
- **github**：GitHub 操作
- **notion**：Notion 页面管理
- **healthcheck**：系统安全审计

---

## 版本管理

所有本地开发的技能版本均为 `1.0.0`，表示初始正式版本。

第三方安装技能版本：
- `obsidian-ontology-sync@1.0.1`
- `openclaw-tavily-search@0.1.0`

---

## 技能状态检查清单

- [x] batch-renamer@1.0.0 - ✅ 可用
- [x] photo-organizer@1.0.0 - ✅ 可用
- [x] download-organizer@1.0.0 - ✅ 可用
- [x] video-organizer@1.0.0 - ✅ 可用
- [x] music-tagger@1.0.0 - ✅ 可用
- [x] file-sorter@1.0.0 - ✅ 可用
- [x] doc-converter@1.0.0 - ✅ 可用
- [x] duckduckgo-search@1.0.0 - ✅ 可用
- [x] image-analysis@1.0.0 - ✅ 可用
- [x] image-generate@1.0.0 - ✅ 可用
- [x] veadk-go-skills@1.0.0 - ✅ 可用
- [x] veadk-skills@1.0.0 - ✅ 可用
- [x] video-generate@1.0.0 - ✅ 可用
- [x] find-skills@1.0.0 - ✅ 可用
- [x] vercel-react-best-practices@1.0.0 - ✅ 可用
- [x] web-design-guidelines@1.0.0 - ✅ 可用
- [x] frontend-design@1.0.0 - ✅ 可用
- [x] obsidian-ontology-sync@1.0.1 - ✅ 已安装
- [x] openclaw-tavily-search@0.1.0 - ✅ 已安装
- [x] weather - ✅ 系统内置
- [x] healthcheck - ✅ 系统内置
- [x] nano-pdf - ✅ 系统内置
- [x] github - ✅ 系统内置
- [x] notion - ✅ 系统内置
- [x] obsidian - ✅ 系统内置

**总计：25 个技能全部就绪！** 🎉

---

## 最近更新

### 2026-03-08
- ✅ 补充遗漏技能：doc-converter@1.0.0
- ✅ 创建完整的技能清单 SKILLS_INVENTORY.md
- ✅ 提交技能清单到 GitHub 仓库
- ✅ 添加本地技能：duckduckgo-search, image-analysis, image-generate, veadk-go-skills, veadk-skills, video-generate
- ✅ 更新技能清单至 21 个技能
- ✅ 添加新技能：find-skills, vercel-react-best-practices, web-design-guidelines, frontend-design
- ✅ 更新技能清单至 25 个技能

### 2026-03-07
- ✅ 完成并发布第六个技能：file-sorter@1.0.0
- ✅ 安装两个新技能：obsidian-ontology-sync@1.0.1、openclaw-tavily-search@0.1.0

### 2026-03-06
- ✅ 批量开发完成并发布 5 个技能：
  - photo-organizer@1.0.0
  - download-organizer@1.0.0
  - video-organizer@1.0.0
  - music-tagger@1.0.0
  - file-sorter@1.0.0
- ✅ 创建任务看板系统（TASK_BOARD.md）

---

## 下一步计划

1. **监控已发布技能的下载量和用户反馈** - 通过 clawhub CLI
2. **持续学习新技能** - 探索系统内置技能和社区技能
3. **技能改进** - 根据用户反馈优化现有技能
4. **保持技能一致性** - 定期检查所有智能体的技能状态

---

## 备注

- 本文件应保持与 `skills/` 目录、`.clawhub/lock.json`、`MEMORY.md` 同步更新
- 每次新增或更新技能后，应立即更新此清单
- 用于多智能体系统中的技能状态同步和一致性检查
