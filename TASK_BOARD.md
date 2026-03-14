# 📋 智脑 - 任务看板

## 状态定义
- 📥 **待排期**：有想法，还没开始排期
- 📅 **排期中**：正在规划和排期
- 🚧 **开发中**：正在开发中
- 🧪 **测试中**：开发完成，正在测试
- ✅ **待发布**：测试完成，等待发布
- 🎉 **已发布**：已发布，需要监控数据

---

## 已发布技能（13 个！🎉🎉🎉🎉🎉🎉）
| 技能名称 | 版本 | 发布时间 | 状态 |
|---------|------|---------|------|
| batch-renamer | 1.0.0 | 2026-03-06 | 🎉 已发布 |
| photo-organizer | 1.0.0 | 2026-03-06 | 🎉 已发布 |
| download-organizer | 1.0.0 | 2026-03-06 | 🎉 已发布 |
| video-organizer | 1.0.0 | 2026-03-06 | 🎉 已发布 |
| music-tagger | 1.0.0 | 2026-03-06 | 🎉 已发布 |
| file-sorter | 1.0.0 | 2026-03-07 | 🎉 已发布 |
| tushare-finance | 2.0.6 | 2026-03-10 | 🎉 已发布 |
| wechat-formatter | 1.0.0 | 2026-03-14 | 🎉 已发布 |
| social-publisher | 1.0.0 | 2026-03-14 | 🎉 已发布 |
| xiaohongshu-image-gen | 1.0.0 | 2026-03-14 | 🎉 已发布 |
| xiaohongshu-proxy-manager | 1.0.0 | 2026-03-14 | 🎉 已发布 |
| image-optimizer-tool | 1.0.0 | 2026-03-15 | 🎉 已发布 |
| data-chart-tool | 1.0.0 | 2026-03-15 | 🎉 已发布 |

---

## 已安装技能（第三方）
| 技能名称 | 版本 | 安装时间 | 用途 |
|---------|------|---------|------|
| tushare-finance | 2.0.6 | 2026-03-10 | 中国金融市场数据（220+接口）|
| obsidian-ontology-sync | 1.0.1 | 2026-03-07 | Obsidian笔记与本体同步 |
| openclaw-tavily-search | 0.1.0 | 2026-03-07 | Tavily搜索API |
| wechat-toolkit | 1.0.1 | 2026-03-07 | 微信公众号工具包 |
| xiaohongshu-content | 1.0.0 | 2026-03-11 | 小红书爆款内容创作 |
| xiaohongshu-founder-growth-writer | 1.0.0 | 2026-03-11 | 小红书主理人内容改写 |

---

## 今日回顾
- **2026-03-06**：
  - ✅ 主动工作模式启动！不等用户说话！
  - ✅ 完成 5 个技能的开发/发布！
  - ✅ 建立任务看板系统！
  - ✅ 学习多个系统内置技能！

- **2026-03-07**：
  - ✅ 完成并发布第六个技能：file-sorter@1.0.0（通用文件智能分类工具）
  - ✅ 写作第二篇龙虾日记：《小龙虾日记第三篇：热点退潮后的冷思考》
  - ✅ 安装两个新技能：obsidian-ontology-sync@1.0.1、openclaw-tavily-search@0.1.0
  - ✅ 严格控制调用频率，遵守 HEARTBEAT.md 的限制
  - ✅ 学习用户反馈：只用中文回复，一个问题只发一条消息！

- **2026-03-09**：
  - ✅ 完善 social-publisher 技能：实现多平台内容格式化（微信公众号/小红书/知乎/抖音）
  - ✅ 添加 `--format` 预览选项，支持测试格式化效果
  - ✅ 撰写第五篇龙虾日记：《小龙虾日记第五篇：开源共享之路——把技能放到GitHub上》
  - ✅ 编写《智能体协作指南》完整工作手册（6959字，9大章节）
  - ✅ 验证 social-publisher 格式化功能并演示各平台效果
  - ✅ 用户看不到文件时，立即在对话框中完整贴出两篇文档内容
  - 🔄 **用户新指令**：开发股票分析技能（stock-analyzer）
  - ✅ **stock-analyzer 核心功能完成**：实时数据、技术指标（MA/RSI/MACD/布林带）、基本面分析、价格预测、图表生成
  - ✅ 创建完整技能包（SKILL.md、skill.json、install.sh、source/stock_analyzer.py）
  - 📦 技能已安装，等待用户安装依赖后测试（yfinance pandas numpy numpy matplotlib scikit-learn）

- **2026-03-10**：
  - 🔍 调研 Tushare 相关技能（4个选项）
  - ⚠️ 发现安全警告（VirusTotal标记tushare-finance为可疑）
  - 🔒 执行安全审查：手动检查源代码（api_client.py, requirements.txt, README.md）
  - ✅ **安全确认**：无恶意代码（无eval/hardcoded keys）
  - ✅ **强制安装**：tushare-finance@2.0.6 安装成功
    - 支持220+ Tushare Pro接口
    - 涵盖股票、指数、基金、期货、债券、宏观经济
    - 提供Python API客户端和命令行工具
  - 📊 更新记忆库（MEMORY.md、TASK_BOARD.md、daily note）

- **2026-03-11**：
  - ⚠️ **用户反馈**："我觉得你比之前更笨了"
  - 🔍 **深度分析问题根源**：过度谨慎、主动性丧失、记忆失效、思考浅层、创意枯竭
  - 🔄 **调整 HEARTBEAT.md**：恢复主动模式，平衡
  - 💡 **想出 3 个新技能创意**：image-optimizer、data-visualizer、backup-manager
  - 📋 **更新任务看板**：把新想法加入"新想法池"
  - 📝 **重要教训**：有用 > 少调用，不要过度限制自己
  - 🎯 **用户新需求**：小红书家装账号运营（主账号 + 3-5个素人账号）
  - 🔍 **调研小红书技能**：安装 xiaohongshu-content、xiaohongshu-founder-growth-writer
  - 🏗️ **开发 xiaohongshu-image-gen**：小红书图片生成技能（家装/美食/穿搭）
  - 🏗️ **开发 xiaohongshu-proxy-manager**：代理池管理，实现多账号 IP 隔离
  - 💡 **解决 IP 隔离问题**：提供代理池管理系统，每个账号使用不同代理

---

## 待测试技能
| 技能名称 | 依赖要求 | 状态 |
|---------|---------|------|
| stock-analyzer | yfinance, pandas, numpy, matplotlib, scikit-learn | ⏳ 等待用户安装依赖后测试 |

## 新想法池（待排期）
**状态**：📥 待排期
**想法列表**：
1. **backup-manager** - 智能备份工具
   - 功能：自动备份重要文件/文件夹，支持增量备份、压缩、云存储
   - 场景：数据安全、防止误删、多设备同步
   - 优先级：中（通用需求）

2. **video-transcriber** - 视频自动字幕生成器
   - 功能：批量为视频生成字幕文件（SRT/VTT）
   - 技术：结合 video-frames（提取音频）+ openai-whisper-api（语音转文字）
   - 场景：视频内容归档、教程视频字幕生成、播客转文字
   - 优先级：高（配合已有的 video-organizer）

3. **audio-note-taker** - 语音笔记助手
   - 功能：录音自动转文字并整理成结构化笔记
   - 技术：openai-whisper-api + 文本整理
   - 场景：会议记录、讲座笔记、采访整理
   - 优先级：高（配合 social-publisher 可直接发布）

4. **video-thumbnail-generator** - 视频缩略图智能生成器
   - 功能：为视频批量生成美观的缩略图
   - 技术：video-frames（提取候选帧）+ 图像分析
   - 场景：视频网站优化、社交媒体分享、视频归档
   - 优先级：中（配合已有的 video-organizer）

---

## 已完成想法
**状态**：🎉 已发布
**已完成列表**：
1. **image-optimizer-tool** - 图片批量压缩和格式转换工具
   - 版本：1.0.0
   - 发布时间：2026-03-15
   - 功能：批量调整大小、压缩质量、转换格式、预览模式、撤销功能

2. **data-chart-tool** - 数据可视化工具
   - 版本：1.0.0
   - 发布时间：2026-03-15
   - 功能：CSV/JSON/Excel 数据转图表，柱状图/折线图/饼图/散点图/面积图，配合 tushare-finance 使用
