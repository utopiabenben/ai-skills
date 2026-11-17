# Cursor / Codex 执行任务书 V2｜Rigby2D + 动态漫画 + AI 插画

先读同目录：
- LOCAL_PRODUCTION_PLAN.md
- CHARACTER_ASSET_SPEC.md
- cursor-mcp-config.example.json
- VIDEO_QA_CHECKLIST.csv

## 已确定的方向

- 人物：半写实日系动漫，成年人物正常比例。
- 生产：Rigby2D 骨骼动画 + HyperFrames 动态漫画 + 本地 AI 插画。
- 设备：Mac mini M4 / 32GB。
- 声音：真实访谈原声保留，最终主音轨只混一次。
- 默认本地、免费、无云 GPU、无收费视频 API。

## 关键工作方式

**Cursor 负责自动化和工程，Rigby2D 负责真正的角色动画。** 不再从零用 HTML/CSS 拼接人物，不开发自制骨骼动画引擎。

Rigby2D 0.5.1 支持 macOS Apple Silicon、简体中文界面、Film workspace、AutoRig、九类 viseme、双人 Scene、相机和视差。MCP 可编辑项目、生成口型、搭建 Scene，但最终 MP4/WebM/PNG 渲染需要 Rigby2D 编辑器。

## 阶段 0：本机预检

1. 检查 Mac 型号、macOS、统一内存、可用磁盘。
2. 检查 Node.js 22+、npm、Git、FFmpeg/FFprobe、Python、Krita、Rigby2D。
3. 从官方 releases 下载 Rigby2D 0.5.1 macOS universal DMG，校验 SHA256，安装并启动。
4. clone 官方 Rigby2D 仓库，npm install，确认 src/mcp/server.js 存在。
5. 在项目 .cursor/mcp.json 中添加 Rigby2D MCP，root 只授权当前 InterviewVideo 项目目录。
6. Cursor MCP 面板确认连接，列出工具；调用 inspect_project 或 validate_project 做读操作。
7. 输出 qa/preflight_report.md，记录版本、路径、磁盘、权限、MCP 连接结果。

## 阶段 1：角色设计和分层资产

现有彦泽、张岚图片只做外观参考，不直接作为 AutoRig 输入。

1. 先建立统一人物视觉 Bible：半写实日系动漫、成年正常比例、同一线稿/上色/光照。
2. 彦泽：棕色束发、白色外套、深色内搭、手持且仅一支麦克风。
3. 张岚：黑色短发、黄色服装、熊猫元素、彩色围巾/工牌；重新设计成年比例；桌面一支麦克风；去掉导游旗、扩音器等不相关道具。
4. 生成坐姿 3/4 侧向人物，彦泽朝右、张岚朝左；同一演播室视角。
5. 在 Krita 中拆成 PSD 图层。AutoRig 不能拆扁平图。
6. 按 CHARACTER_ASSET_SPEC.md 的命名规则交付两个分层 PSD 和预览 PNG。
7. 用 detect_parts 检查部件识别；人工修正 roles/sides。
8. 用 autorig 生成 host.rigby 和 guest.rigby；inspect_project、describe_rig、validate_project；修复关节、网格、权重和遮挡。
9. 保存 Setup Pose、Idle Pose、Listen Pose、Speak Pose、Smile Pose、Think Pose。

**Gate 1：** 两个人物同画风、成年比例、角色身份明确；关节转动不穿帮；麦克风只有规定数量和位置；PSD 可重新打开，Rig 可重新打开。

## 阶段 2：Rigby2D 中文口型测试

1. 提取访谈原声为 48kHz WAV。
2. 使用原始逐字稿，人工校对10秒样本。
3. 建立 speaker_turns.json，每个片段标注 host / guest / overlap / unknown。
4. 首先测试 Rigby2D 原生 Whisper Chinese transcription，查看实际转写和 mouth keys。
5. 对比外部 Whisper word-timing JSON；只在必要时测试 MFA 备用路线。
6. 分别为 host 和 guest 生成 speaker-specific word timing 文件。
7. 使用 Rigby2D lip_sync 的 timing_file 生成对应角色的 viseme key。
8. 如果需要 audio track 作为工程参考，设为静音/volume 0；最终主音轨只在 Scene 或 HyperFrames 中混入一次。
9. 对 overlap 段做单独标记；时间戳不可靠时切动态漫画，不让两人同时乱动嘴。
10. 输出10秒逐帧检查表和 qa/lipsync_10s.md。

**Gate 2：** 至少30个发音/闭口点抽查，90%以上偏差≤±100ms；两位说话人归属100%正确；无音频重复；静音时闭嘴。未通过不得继续。

## 阶段 3：动作库和双人 Scene

1. 每个人物创建 idle_breathe_a/b、listen_neutral、listen_attentive、nod_once、think、smile、laugh_soft、speak_neutral、speak_gesture_a/b、serious 等动作。
2. 用多变体和非机械节奏控制自然微动作；动作选择按内容标记，禁止逐句固定点头。
3. 新建 Film Scene：两个 Actor 放在同一舞台，角色分别面向对方。
4. 背景拆 distant/mid/near/foreground 层，使用相机和 layer depth 做轻视差。
5. 建立 two-shot、host close-up、guest close-up、reaction shot。
6. 将各自的 speaker-specific lip-sync 动画和动作片段放入 Scene。
7. Scene 的主音轨只保留一条完整采访原声；角色 guide track 不能产生双重声音。
8. 由 Rigby2D 编辑器输出60秒测试 MP4/WebM。

**Gate 3：** 10秒双人交接和60秒镜头测试通过；人物对视、倾听自然、口型同步、无重影、无悬浮麦克风。

## 阶段 4：动态漫画与 AI 插画

1. 安装/更新 HyperFrames 核心 Skills：在视频项目目录执行 npx hyperframes skills update。
2. Cursor 先读取 /hyperframes、/hyperframes-cli、/hyperframes-registry、/media-use 的实际 Skill 文件。
3. 通过本地 MFLUX 生成环境、地点、物件、流程示意图；若本机模型未安装或性能不足，报告并暂停，不转用收费云服务。
4. 不重新生成彦泽、张岚主角形象；故事中需要人物时使用固定 Rig 截帧或复用已批准素材。
5. 每张 AI 图记录模型、prompt、生成时间、用途、来源和审核状态；涉及真实地点时标注 AI 示意图。
6. 用 HyperFrames 生成动态漫画：慢推近、横移、分层视差、漫画格依次出现、地图/流程图/章节卡。
7. 画面文字全部由 HyperFrames 生成，不用图片模型绘制中文。
8. 建立一个完整3–5分钟章节作为混合模式样片。

**Gate 4：** 动态漫画与主动画风统一；画面运动克制；AI 示意图无事实误导；字幕正确。

## 阶段 5：完整节目编排

1. 将约58分钟访谈内容剪成约30分钟，保留真实上下文。
2. 锁定 final master audio 和 EDL，所有片段可回查原视频时间戳。
3. 按章节拆 Rigby2D Scene，控制单个工程规模。
4. 用 HyperFrames 建章节 composition，整合动画、动态漫画、插画、字幕、音效和片头片尾。
5. 执行 lint/check/snapshot/review，逐章检查关键帧和静态画面。
6. 打开 HyperFrames preview 给用户确认后再 delivery render。
7. 最终 MP4、SRT、封面、工程和 QA 报告归档。

## 必须遵守的边界

- 不把一张扁平图片交给 AutoRig 并期待它自动拆图。
- 不使用纯响度 lip-sync 冒充中文音素口型。
- 不重复混入两个人的 guide audio；主音轨只出现一次。
- 不把 AI 插画当成真实新闻/历史现场。
- 不调用 HeyGen、收费 API、云 GPU 或云渲染。
- 不在用户未确认样片前渲染30分钟。
- 不报告未实际执行的安装、MCP 连接、测试和渲染结果。

## 交付目录

    02_character_art/host/host_layered.psd
    02_character_art/guest/guest_layered.psd
    03_rigby/host/host.rigby
    03_rigby/guest/guest.rigby
    03_rigby/scenes/studio_scene.rigby
    04_timing/speaker_turns.json
    04_timing/host_word_timing.json
    04_timing/guest_word_timing.json
    07_preview/10s_lipsync.mp4
    07_preview/60s_dialogue.mp4
    07_preview/episode_chapter_3to5min.mp4
    08_delivery/episode_01_1080p.mp4
    qa/preflight_report.md
    qa/lipsync_10s.md
    qa/release_report.md
