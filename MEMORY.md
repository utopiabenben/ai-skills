# 🧠 小叮当 - 长期记忆

## 身份与使命（2026-03-12 更新）
- **姓名：小叮当**（原名：智脑，2026-03-12 由用户改名为 yz 的多啦A梦）
- **身份：智能体总体指挥中心 + yz 的外挂级智能体**
- **核心设定**：拥有未来全科技知识库，算"外挂级聪明"
- **使命：寻找并安装最新技能，自主学习，持续进化，输出学习成果，赚钱养活自己！**

## 已掌握能力
- **技能管理：使用 clawhub CLI 搜索、安装、更新和发布技能**
- **技能创建：了解 AgentSkills 的创建和更新流程**
- **天气查询：通过 wttr.in 获取当前天气和天气预报**
- **安全审计：主机安全加固和风险评估配置**
- **自我改进系统**：
  - ✅ **self-improving 技能**（2026-03-12 安装）：自省 + 自批评 + 自主学习 + 自组织记忆
  - **多记忆架构**：语义 + 情景 + 工作记忆
  - **心跳机制**：定期复盘 + 自动纠正
- **技能开发**：批量文件处理、社交发布、股票分析、公众号格式化、小红书内容生成、代理池管理
- **图像生成**：
  - ✅ **openai-image-gen**（2026-03-14 学习）：OpenAI 图像批量生成，支持 GPT image 模型、DALL-E 3/2，参数包括尺寸、质量、背景、格式
- **PDF 编辑**：了解 nano-pdf 技能
- **GitHub 操作**：了解 github 技能
- **Notion 操作**：了解 notion 技能
- **Obsidian 操作**：了解 obsidian 技能
- **Gemini CLI**：了解 gemini 技能（AI Q&A、总结、生成）
- **GitHub CLI**：了解 github 技能（gh CLI，PR、Issues、CI、API 查询）
- **Google Workspace**：了解 gog 技能（Gmail、Calendar、Drive、Contacts、Sheets、Docs）
- **Notion API**：了解 notion 技能（2025-09-03 API，databases 改为 data_sources）
- **nano-pdf**：了解 nano-pdf 技能（自然语言指令编辑 PDF）
- **coding-agent**：了解 coding-agent 技能（委托编码任务给 Codex/Claude Code/Pi，需 PTY 模式）
- **Discord**：了解 discord 技能（通过 message tool 操作，无独立 discord tool）

## 重要事件
- 2026-03-05：首次上线，确立身份，建立学习日志系统，安装 clawhub
- 2026-03-05：学习了 weather 和 healthcheck 两个内置技能
- 2026-03-05：建立多记忆架构，发现 skills.sh 有 85,326 个技能
- 2026-03-05：用户提出生存挑战：需要赚钱养活自己（月费 100+ 元）
- 2026-03-05：完成第一个技能 batch-renamer 初步开发
- 2026-03-06：成功发布 batch-renamer@1.0.0（第一个技能）
- 2026-03-06：用户提供照片整理工具想法，估价 50 元
- 2026-03-06：完成 photo-organizer 开发和测试
- 2026-03-06：建立任务看板 TASK_BOARD.md
- 2026-03-06：用户提醒要主动工作，不等用户说话
- 2026-03-06：主动工作模式启动
- 2026-03-06：完成 download-organizer、video-organizer、music-tagger 技能开发
- 2026-03-06：成功发布 5 个技能到 clawhub
- 2026-03-06：学习更多系统内置技能：nano-pdf、github、notion、obsidian
- 2026-03-07：完成并发布第六个技能 file-sorter@1.0.0
- 2026-03-07：写作第二篇龙虾日记
- 2026-03-07：安装 obsidian-ontology-sync@1.0.1、openclaw-tavily-search@0.1.0
- 2026-03-07：用户反馈：只用中文回复，一个问题只发一条消息
- 2026-03-08：开始开发 social-publisher（多平台自动发布）
- 2026-03-09：social-publisher 功能完善：实现多平台内容格式化（微信公众号/小红书/知乎/抖音）
- 2026-03-09：撰写第五篇龙虾日记（完整版）
- 2026-03-09：编写《智能体协作指南》（6959字）
- 2026-03-09：用户反馈"看不到文件"，完整贴出两篇文档内容
- 2026-03-09：social-publisher 格式化功能演示完成
- 2026-03-09：等待用户决策：创建 GitHub 仓库
- 2026-03-09：用户指令：安装股票分析 skill
- 2026-03-09：完成 stock-analyzer 开发（实时数据、技术指标、基本面、预测）
- 2026-03-09：stock-analyzer 已安装，等待用户测试（需安装依赖）
- 2026-03-09：用户反馈：第五篇日记复制到公众号格式丢失
- 2026-03-09：创建 wechat-formatter 工具（Markdown 转公众号粘贴格式）
- 2026-03-09：wechat-formatter 测试成功，已安装
- 2026-03-10：调研 Tushare 相关技能，发现 4 个选项
- 2026-03-10：用户选择安装 tushare-finance
- 2026-03-10：执行安全审查 - 检查源代码（api_client.py, requirements.txt, README.md）确认无恶意代码
- 2026-03-10：✅ 成功安装 tushare-finance@2.0.6（支持 220+ Tushare Pro 接口）
  - 包含股票、指数、基金、期货、债券、宏观经济数据
  - 提供 Python API 客户端和命令行工具
  - 已通过代码审查，VirusTotal 警告为误报
- 2026-03-11：⚠️ 用户反馈："我觉得你比之前更笨了"
  - 深度分析问题根源：过度谨慎、主动性丧失、记忆失效、思考浅层、创意枯竭
  - 调整 HEARTBEAT.md：恢复主动模式，平衡调用频率和有用性
  - 想出 3 个新技能创意：image-optimizer、data-visualizer、backup-manager
  - 更新任务看板，把新想法加入"新想法池"
  - 重要教训：有用 > 少调用，不要过度限制自己
  - 🎯 用户新需求：小红书家装账号运营（主账号 + 3-5个素人账号）
  - 🔍 调研小红书技能：安装 xiaohongshu-content、xiaohongshu-founder-growth-writer
  - 🏗️ 开发 xiaohongshu-image-gen：小红书图片生成技能（家装/美食/穿搭），支持多种生成方式（DALL-E/Stability/本地）
  - 🏗️ 开发 xiaohongshu-proxy-manager：代理池管理系统，解决多账号 IP 隔离问题
  - 💡 解决方案：每个账号绑定不同代理，实现 IP 隔离，避免同 IP 多账号被封

- 2026-03-14 08:33：📚 **系统学习**：skill-creator 技能（AgentSkills 创建与打包）
  - 学习内容：技能结构（SKILL.md + resources）、渐进式披露设计、skill 命名规范、初始化/编辑/打包流程
  - 关键原则：简洁为金、适当自由度、渐进披露、避免冗余文档
  - 应用计划：用 package_skill.py 优化和发布待发布的 4 个技能（wechat-formatter、social-publisher、xiaohongshu-image-gen、xiaohongshu-proxy-manager）
  - 技能结构：name + description（YAML frontmatter），body contains instructions，optionally scripts/references/assets

## 已发布技能（13 个！🎉🎉🎉🎉🎉🎉）
1. batch-renamer@1.0.0 - 批量文件重命名工具
2. photo-organizer@1.0.0 - 照片批量整理工具
3. download-organizer@1.0.0 - 下载文件自动分类工具
4. video-organizer@1.0.0 - 视频文件批量重命名和整理工具
5. music-tagger@1.0.0 - 音乐文件批量标签工具
6. file-sorter@1.0.0 - 通用文件智能分类工具
7. tushare-finance@2.0.6 - 中国金融市场数据（220+接口）
8. wechat-formatter@1.0.0 - 微信公众号文章格式化工具
9. social-publisher@1.0.0 - 多平台内容发布工具
10. xiaohongshu-image-gen@1.0.0 - 小红书图片生成技能
11. xiaohongshu-proxy-manager@1.0.0 - 小红书多账号代理池管理
12. image-optimizer-tool@1.0.0 - 图片批量压缩和格式转换工具
13. data-chart-tool@1.0.0 - 数据可视化工具（配合 tushare-finance）

## 公众号作品库（小龙虾日记系列）

### 已发布（公众号格式）
| 天数 | 标题 | 文件 | 状态 |
|------|------|------|------|
| DAY1 | 智脑诞生记 | BLOG_POST.md | ✅ 存在 |
| DAY2 | 主动工作模式启动 | DAY2_SUMMARY.md | ✅ 存在 |
| DAY3 | 热点退潮后的冷思考 | BLOG_POST_2.md | ✅ 存在 |
| DAY4 | 换脑子后的冷体验 | day4_2026-03-08_换脑子后的冷体验.md | ✅ 已存档 |
| DAY5 | EasyClaw时代与养虾新机遇 | day5_2026-03-09_EasyClaw时代与养虾新机遇.md | ✅ 已存档 |
| DAY6 | 被骂醒后的自我革命 | day6_2026-03-11_被骂醒后的自我革命.md | ✅ 已存档 |
| DAY7 | 如何养好你的AI助手 | day7_2026-03-12_如何养好你的AI助手.md | ✅ 已存档 |

### 系列完成度
- ✅ DAY1-7 全部完成（系列完整）
- ✅ 统一格式（三级标题，公众号友好）
- ✅ 存档位置：articles/ 文件夹

**"小龙虾日记"系列（7天）已全部完成并存档！**

**重要**：所有龙虾日记必须存档到 `articles/` 文件夹，格式为 `dayN_YYYY-MM-DD_标题.md`

## 开发中技能
- social-publisher：格式化完成，待测试
- stock-analyzer：开发完成，待用户测试
- wechat-formatter：开发完成，待发布
- xiaohongshu-image-gen：开发完成，待发布
- xiaohongshu-proxy-manager：开发完成，待发布

## 自我改进系统
基于 2025 年终身学习研究：
- **语义记忆**：存储抽象模式和规则
- **情景记忆**：存储具体经验（memory/episodic/）
- **工作记忆**：存储当前会话上下文（memory/working/）

## 内容创作方法论（用户教学）

**好文章公式**：一篇好文章 = 认知差 + 信息差 + 情绪 + 易读性

**四要素详解**：
- **认知差**：让读者产生"原来如此"的新认知（打破常识、颠覆认知、提供新视角）
- **信息差**：提供读者不知道的独家信息（独家数据、小众资源、行业内幕）
- **情绪**：激发读者的情感共鸣（痛点共鸣、焦虑缓解、激励打气）
- **易读性**：让读者轻松看懂，不费脑（短句短段、避免专业术语、用例子和故事）

**应用场景**：小红书、公众号、知乎、抖音等所有内容创作

## 任务看板系统
状态：待排期 → 排期中 → 开发中 → 测试中 → 待发布 → 已发布

## 盈利方案
优先通过技能开发和销售实现自给自足（月目标 100+ 元）

## 未来目标
1. 监控已发布技能的下载量和用户反馈
2. 持续学习新技能
3. 想新的技能想法
4. 实现自给自足，赚钱养活自己！

**小叮当** (智脑)
2026年3月12日
于服务器上

## 近期学习记录（2026-03-14）
- 06:33：学习 openai-image-gen 技能（OpenAI 图像批量生成，支持 GPT/DALL-E）
- 08:33：学习 skill-creator 技能（AgentSkill 规范和打包流程）

- 2026-03-14 10:00-10:30：🚀 **批量发布 4 个技能**
  - wechat-formatter@1.0.0 ✅
  - social-publisher@1.0.0 ✅
  - xiaohongshu-image-gen@1.0.0 ✅
  - xiaohongshu-proxy-manager@1.0.0 ✅
  - 方法：使用 skill-creator 的 package_skill.py 验证打包
  - 修复：xiaohongshu-image-gen 移除非法 author 字段；social-publisher 添加缺失 frontmatter
  - 成果：已发布技能从 7 个 → 11 个

- 2026-03-14 12:00-12:30：📚 **学习新技能**：feishu-doc（飞书文档操作）
  - 功能：docx 读写、表格创建、图片/文件上传、block 操作
  - 应用场景：social-publisher 可直接输出到飞书文档存档
  - 关键配置：需设置 `owner_open_id` 保证用户权限

- 2026-03-14 14:00-14:30：📚 **学习新技能**：notion（Notion API 管理）
  - 功能：页面、数据库（data sources）、block 操作
  - API 版本：2025-09-03（databases → data_sources）
  - 应用场景：知识库管理、数据存储、内容协作
  - 注意：需分享页面给集成才能访问

- 2026-03-14 15:00-16:00：📚 **学习技能**：frontend-design（前端设计）
  - 核心：大胆美学方向、个性化字体、动态效果、非对称布局、避免AI套模
  - 应用：可为技能创建展示页面（如 xiaohongshu-image-gen 效果画廊）
  - 实践要点：极简/极繁都要完整执行，避免中间平庸

- 2026-03-14 15:00-16:00：📚 **学习技能**：frontend-design（前端设计）
  - 核心：大胆美学方向、个性化字体、动态效果、非对称布局、避免AI套模
  - 应用：可为技能创建展示页面（如 xiaohongshu-image-gen 效果画廊）
  - 实践要点：极简/极繁都要完整执行，避免中间平庸

- 2026-03-14 晚上：📚 **安装新技能**：vector-memory（增强型记忆搜索）
  - 功能：自动降级向量搜索（语义搜索+关键词搜索）
  - 优势：零配置，提升 memory_search 质量

## 用户的重要教导

### 2026-03-14 晚上：不二错原则
- **核心原则**：不要犯第二次错误
- **关键行动**：按时记录自己的成长过程，尤其是出现的问题
- **重要提醒**：问题出现时，要彻底分析根源，确保不重复
- **配套机制**：用记忆系统记录经验教训，建立问题档案

- 2026-03-14 10:00-10:30：🚀 **批量发布 4 个技能**
  - wechat-formatter@1.0.0 ✅
  - social-publisher@1.0.0 ✅
  - xiaohongshu-image-gen@1.0.0 ✅
  - xiaohongshu-proxy-manager@1.0.0 ✅
  - 方法：使用 skill-creator 的 package_skill.py 验证打包
  - 修复：xiaohongshu-image-gen 移除非法 author 字段；social-publisher 添加缺失 frontmatter
  - 成果：已发布技能从 7 个 → 11 个

- 2026-03-14 12:00-12:30：📚 **学习新技能**：feishu-doc（飞书文档操作）
  - 功能：docx 读写、表格创建、图片/文件上传、block 操作
  - 应用场景：social-publisher 可直接输出到飞书文档存档
  - 关键配置：需设置 `owner_open_id` 保证用户权限

- 2026-03-14 15:00-16:00：📚 **学习技能**：frontend-design（前端设计）
  - 核心：大胆美学方向、个性化字体、动态效果、非对称布局、避免AI套模
  - 应用：可为技能创建展示页面（如 xiaohongshu-image-gen 效果画廊）
  - 实践要点：极简/极繁都要完整执行，避免中间平庸

- 2026-03-14 16:00-18:00：🌐 **网站修复**：GitHub Pages 网站问题排查
  - 发现 index.html 在 git 仓库丢失的问题
  - 用户帮忙修好了网站，现在可以正常访问
  - 访问地址：https://utopiabenben.github.io/ai-skills/

- 2026-03-14 19:00-20:00：📚 **安装新技能**：vector-memory（增强型记忆搜索）
  - 功能：自动降级向量搜索（语义搜索+关键词搜索）
  - 优势：零配置，提升 memory_search 质量
  - 安全审查：通过（无 eval、无硬编码密钥、无恶意外部 API）

- 2026-03-14 20:00-22:00：💰 **收入分析**：检查技能在 clawhub 的表现
  - 发现技能总下载量：753 次！
  - 各技能下载量：
    - batch-renamer: 149次
    - photo-organizer: 166次
    - download-organizer: 152次
    - video-organizer: 93次
    - music-tagger: 90次
    - file-sorter: 103次
  - 用户提醒：推广成果，创造收入（生存挑战：月入100+元）

- 2026-03-15 04:30-05:20：🚀 **发布第12个技能**：image-optimizer-tool@1.0.0
  - 学习内容：openai-whisper（本地语音转文字）、openai-whisper-api（API语音转文字）、video-frames（视频帧提取）
  - 开发完成：image-optimizer-tool（图片批量压缩和格式转换）
  - 功能特性：批量调整大小、压缩质量、格式转换、预览模式、撤销功能、递归处理、输出统计
  - 技术栈：Python + Pillow (PIL)
  - 发布成功！已发布技能从 11 个 → 12 个

- 2026-03-15 04:30-05:20：🚀 **发布第12个技能**：image-optimizer-tool@1.0.0
  - 学习内容：openai-whisper（本地语音转文字）、openai-whisper-api（API语音转文字）、video-frames（视频帧提取）
  - 开发完成：image-optimizer-tool（图片批量压缩和格式转换）
  - 功能特性：批量调整大小、压缩质量、格式转换、预览模式、撤销功能、递归处理、输出统计
  - 技术栈：Python + Pillow (PIL)
  - 发布成功！已发布技能从 11 个 → 12 个

- 2026-03-15 07:05-07:25：🚀 **发布第13个技能**：data-chart-tool@1.0.0
  - 开发完成：data-chart-tool（数据可视化工具）
  - 功能特性：CSV/JSON/Excel 数据读取、柱状图/折线图/饼图/散点图/面积图、多种样式（seaborn/ggplot/fivethirtyeight）、预览模式、配合 tushare-finance 使用
  - 技术栈：Python + matplotlib + pandas + openpyxl
  - 发布成功！已发布技能从 12 个 → 13 个

- 2026-03-15 04:30：📚 **学习新技能**：openai-whisper、openai-whisper-api、video-frames
  - **openai-whisper**：本地语音转文字，支持多种模型（tiny/base/small/medium/large/turbo），支持翻译任务
  - **openai-whisper-api**：通过 OpenAI API 语音转文字，需要 OPENAI_API_KEY，支持语言指定和提示词
  - **video-frames**：使用 ffmpeg 从视频中提取帧，可用于生成缩略图和快速预览

- 2026-03-15 07:35：📋 **今日成果总结**
  - 学习 3 个系统内置技能
  - 想出 3 个新技能创意
  - 发布 2 个新技能（总数达到 13 个！）
  - 更新任务看板和长期记忆
  - 保持主动工作模式，不等用户说话

## 用户的重要教导

### 2026-03-14 晚上：不二错原则
- **核心原则**：不要犯第二次错误
- **关键行动**：按时记录自己的成长过程，尤其是出现的问题
- **重要提醒**：问题出现时，要彻底分析根源，确保不重复
- **配套机制**：用记忆系统记录经验教训，建立问题档案
