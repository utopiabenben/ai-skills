# 彦泽 × 张岚｜双人动漫访谈视频本地制作技术方案 V1.0

**制定日期：** 2026-11-17  
**状态：** 技术设计与选型；尚未在用户 Mac mini 上完成端到端运行验证。  
**设备基线：** Mac mini M4 / 32GB 统一内存；优先本地处理及存储，可使用外置 APFS 磁盘。  
**输入基线：** 已录制的约58分钟访谈视频、逐字稿、两位人物参考图。  
**目标输出：** 约30分钟、16:9、1920×1080、30fps、MP4（H.264 + AAC）、可编辑工程、独立 SRT 字幕及可选精华切片。

---

## 0. 产品目标与不可妥协条件

1. **保留真人原声与真实经历。** 原访谈是事实来源。剪辑可以删除无关段落、重复和无效停顿，但不得拼接出原说话人未表达的观点；未经明确授权，不得以合成声音冒充真实采访。
2. **动漫人物连续一致。** 主持彦泽：棕色束发/盘发、白色外套，主持手持麦克风，全画面只能有一个主持话筒。嘉宾张岚：黑色短发、黄色带熊猫图案上衣、彩色围巾/工牌，桌面麦克风。两人坐姿方向互相面对，统一画风、照明、服装、脸型和比例。
3. **真实口型同步优先。** 不采用仅按音频响度驱动嘴巴开合的方式作为准确口型方案。要求中文语音对齐数据、音素到口型映射，并逐镜头验收。
4. **自然动作。** 非发言人闭口并有自然倾听反应；发言人有口型、眨眼、视线、头部轻微动作和少量手势。避免机械重复和每句话都点头。
5. **素材分层与项目可复用。** 角色、声音、字幕、镜头编排分离；修改一处不应导致其他章节全部重制。
6. **内容优先。** 先保证访谈好看、表达完整，再追求动画效果。B-roll 服务于真实故事，不得用 AI 生成画面伪装历史现场实拍。
7. **商业用途前核查权利。** 分别核查人物肖像、声音、图片模型权重、音乐、字体、软件和第三方素材许可。开源代码许可证不代表模型权重或素材自动获得商业授权。

## 1. 总体技术路线

### 1.1 推荐主路线：本地分层 2.5D 动画

原始访谈视频 + 逐字稿 + 人物参考图  
→ FFmpeg 提取原声母带  
→ whisper.cpp 中文转写及时间戳  
→ 人工校对逐字稿、标记说话人和内容剪辑点  
→ 先锁定最终声音时间线  
→ 普通话音素强制对齐  
→ 音素映射到多类 viseme（口型）  
→ 两套分层角色 Rig 驱动嘴、眼、眉、头、手势  
→ HyperFrames 编排镜头、字幕、插图和音乐  
→ FFmpeg / DaVinci Resolve 精修与导出  
→ 30分钟成片、SRT、封面、工程和 QA 报告。

选择这条路线的原因：30分钟访谈需要大量可重复镜头。分层2D Rig 更容易维持人物一致性、离线运行和重复渲染。语音与动画解耦，修改字幕、镜头和动作时无需重新生成整段 AI 视频。

### 1.2 口型方案与边界

| 方案 | 能力与限制 | 项目定位 |
|---|---|---|
| MFA 普通话强制对齐 + viseme 映射 + 2D Rig | 通过校对文本和声学模型得到音素时间，再驱动多类嘴型；需补充口音词典及人工纠错 | **主路线，优先试做** |
| Adobe Character Animator | 可从预录音频计算多种口型；中文识别准确度、Mac 版本能力和商业许可须实际测试 | **成熟产品对照组**，不预先采购 |
| Rhubarb Lip Sync phonetic 模式 | 免费、可输出口型 cue；非英语识别通常较粗糙，中文需实测 | 10秒对照/基线，不直接作为整片验收方案 |
| Live2D Cubism 常规 LipSync | 常见自动嘴型参数主要根据音量控制张合，单独使用不满足本项目的中文音素口型要求 | 不作为单独主方案；若使用须增加音素事件驱动 |
| LTX-2 MLX | Apple Silicon 本地视频生成实验路线；部分音频驱动能力仍需验证，模型大、耗时及内存需实测 | 只做短镜头增强实验 |
| LongCat Avatar 1.6 | 官方推理依赖 NVIDIA CUDA，不适合作为 M4 本地主生产线 | 仅在另行批准 GPU 环境、费用和素材上传范围后评估 |
| lip-sync-mac | Apple Silicon 实验项目；需核对其语音合成依赖是否能保留原始采访声音 | 技术参考，不默认替代原声主链路 |

不得将音量开合嘴称为音素级口型同步。任何 AI 视频生成镜头都必须单独检查原声是否保留、人物是否变形、口型是否同步和角色是否漂移。

## 2. 工具、产品与 Skills 清单

### 2.1 基础工具

| 环节 | 产品/工具 | 用途 | 备注 |
|---|---|---|---|
| 总控 | Codex | 拆解任务、安装、开发、运行、测试、修复 | 主要执行者 |
| 视频/音频 | FFmpeg、FFprobe | 提取、转码、合成、黑帧/媒体检查、响度分析 | 开源，本地 |
| 语音识别 | ggml-org/whisper.cpp | 中文转写、时间戳 | 本地模型权重需下载 |
| 强制对齐 | Montreal Forced Aligner | 普通话音素时间、TextGrid | 本地安装，语料与词典需校验 |
| 快速口型对照 | DanielSWolf/rhubarb-lip-sync | 输出 mouth cue JSON | 中文效果需实测 |
| 图片生成 | MFLUX / 已授权图像生成工具 | 背景、插图和角色参考探索 | 不把 AI 生成文字用于正式字幕 |
| 图层编辑 | Krita / Photoshop | 抠图、分层、补绘嘴型和表情 | Krita 免费；PS 付费 |
| 角色动画 | 自定义 Canvas/WebGL 2D Rig；可选 Live2D | 角色嘴、眼、头、手势动画 | 主路线为可控分层 Rig |
| 自动剪辑 | HyperFrames | 时间线、场景、字幕、镜头和本地合成 | 需要按官方文档实现 |
| 精修 | DaVinci Resolve | 最终节奏、音频、字幕、片头片尾复审 | 可选；免费版能力需核对 |

### 2.2 HyperFrames Skills

官方仓库：https://github.com/heygen-com/hyperframes

优先安装和核验：

- /hyperframes：项目与场景编排。
- /hyperframes-cli：lint、check、snapshot、render。
- /media-use：接入和管理音频、图片、音效等素材；选择本地来源，第三方付费服务须审批。
- /hyperframes-registry：复用标题、章节、字幕、转场等组件。

安装参考：npx skills add heygen-com/hyperframes

安装后必须读取实际 SKILL.md 和当前版本 CLI help；不能只凭本方案假设参数存在。HyperFrames 负责视频编排和合成，不负责保证中文音素与嘴型准确对应。

### 2.3 需要自行开发的项目 Skills

以下是本项目拟开发的 Skills，不代表已安装或已经实现：

| Skill | 责任 |
|---|---|
| interview-transcript-editor | 保真剪辑；输出原片时间、说话人、审定文本、保留原因；禁止杜撰 |
| speaker-audio-qa | 两人音轨归属、重叠、错位、爆音、噪声和原声对照 |
| mandarin-viseme-align | MFA 音素到 viseme 映射、口型时间轴、低置信度标记和人工修订 |
| avatar-continuity-qa | 检查脸、服装、颜色、工牌、话筒、视线和镜头连续性 |
| podcast-shot-editor | 根据说话人、内容节点和动作生成镜头时间线 |
| video-release-qa | 检查视频帧、音画同步、字幕、黑帧、音轨、导出参数和完整性 |
| interview-knowledge-miner（可选） | 从同一访谈时间戳提取行业知识；与视频制作流水线分开 |

每个自研 Skill 至少包含 SKILL.md、输入输出契约、脚本、示例和测试用例。不得仅放一个提示词便声称自动化已经实现。

## 3. 角色与视觉资产规范

### 3.1 人物设定

**彦泽（主持人）**
- 棕色束发/盘发，白色外套。
- 手持一个麦克风；全片不得额外出现第二支主持麦克风。
- 主要镜头为面对张岚的中景、近景和双人全景。
- 发言时自然解释手势；倾听时视线看向张岚。

**张岚（嘉宾）**
- 黑色短发，黄色带熊猫图案上衣，彩色围巾/工牌。
- 使用固定桌面麦克风。
- 发言时自然转头、轻微手势；倾听时闭口并对视。

两人需要统一线条、比例、色彩、照明和背景。不得擅自改变服装、发型、麦克风数量和角色身份。

### 3.2 每个角色需要准备的资产

- 正面、左右3/4面等常用视角；坐姿比例一致。
- 眼睛：睁眼、半闭、闭眼、微笑。
- 嘴型：闭合、MBP闭唇、F/V齿唇、主要元音的张口/圆口/扁口等，建议初版10–12类，最终按中文音素映射校准。
- 眉毛：平静、认真、疑问、惊讶等。
- 头部动作：轻点头、转向对方、轻微倾斜、静止。
- 手势：静止、解释、轻微强调等3–5个可复用动作。
- 分层图：脸、头发、眼睛、嘴、身体、手臂、服装、饰品、麦克风分别可控。
- 场景：双人全景、主持中近景、嘉宾中近景、侧面互视、章节卡片和插图镜头。

正式字幕必须由排版层生成，不能依赖图片模型绘制中文文字。

### 3.3 视觉连续性规则

- 双人坐姿始终互相面对，单人镜头视线朝向画内另一人。
- 主持彦泽只持一支麦克风；张岚桌面麦克风位置固定。
- 听众在对方讲话时不抢嘴；允许自然眨眼、微动作和偶发点头，不得逐句机械点头。
- 动作前后平滑，避免闪烁、换脸、手部断裂、衣服和工牌变化。
- B-roll 使用真实授权素材或明确标注为示意的 AI 插图，不得冒充历史现场影像。

## 4. 工程目录与数据结构

建议工程放在用户指定的本地工作盘；原始素材只读，不能覆盖原文件。

    InterviewVideo/
    ├── 00_source/              原始视频、逐字稿、授权记录
    ├── 01_audio/               原始 WAV、识别音频、最终声音母带
    ├── 02_transcript/          原始转写、校对稿、剪辑决策、字幕
    ├── 03_characters/           两套角色 Rig、口型、眼睛、表情、动作
    ├── 04_scenes/               演播室、B-roll、片头片尾、叠加层
    ├── 05_alignment/            MFA 语料、TextGrid、音素与 viseme 数据
    ├── 06_animation/            主持、嘉宾、双人镜头动画
    ├── 07_timeline/             剪辑时间线、shots、HyperFrames 工程
    ├── 08_preview/              10秒、60秒、5分钟样片
    ├── 09_delivery/             正式 MP4、SRT、封面、精华切片
    ├── qa/                      检查表、报告、复审记录
    └── scripts/                 预检、转写、对齐、渲染、验收脚本

### 时间轴数据必须分开

每段语音记录：
- segment_id
- speaker_id（host / guest / overlap / unknown）
- source_start_ms / source_end_ms：原片时间戳
- timeline_start_ms / timeline_end_ms：剪辑后时间戳
- text_verified：人工校对文本
- audio_path
- viseme_path
- shot_id
- motion_preset
- subtitle_id
- source_text_verified

原片时间和成片时间必须通过 EDL 映射，不允许混用。所有成片片段应可反查到原片位置。

## 5. 分阶段生产流程

### P0：环境预检、授权和原始素材锁定

1. Codex 检查 macOS、芯片、统一内存、磁盘空间、外置盘格式和读写速度。
2. 检查 Node.js 22+、FFmpeg/FFprobe、Python 3.11+、uv、Git、MFA、HyperFrames CLI 的实际版本。
3. 检查原始视频、逐字稿、人物参考图是否存在且可读取；计算 SHA256。
4. 记录音频、肖像、图片、音乐、字体、模型权重和商业使用许可。
5. 原始素材设为只读；任何敏感素材默认留在本机。
6. 先运行10秒性能基准，不得直接渲染30分钟。

**G0 通过标准：** 机器和依赖报告完整；源文件可读且校验值已记录；授权边界明确；缺失素材必须报告并停止依赖该素材的环节。

### P1：原声母带、转写与内容剪辑

1. FFmpeg 提取48kHz WAV 母带。若原始音频为压缩格式，转 WAV 不会恢复丢失频率；同时制作16kHz mono 识别副本。
2. whisper.cpp 生成中文转写和时间戳。
3. 人工校对人名、地名、行业词、数字、方言词；按视频/音轨复核 speaker_id。重叠发言或第三人发言不得强行归给两位主角。
4. 按真实故事和主题形成约30分钟节目大纲。允许删无关内容、重复和无效静默，不得拼接出未表达的观点。
5. 先做纯声音粗剪；保留自然停顿、笑声和情绪；剪点不得切掉音节。对降噪和音色处理提供 A/B，不能过度处理。
6. 锁定最终声音母带，并建立每段成片音频到原片时间戳的映射。

**G1 通过标准：** 两人身份人工确认；原声内容真实；重要情绪和故事转折未被误删；剪点流畅；final_audio.wav 时间轴固定。

### P2：角色素材与动画 Rig

1. 根据参考图建立 character_bible.md，锁定服装、脸型、发型、比例、配色、工牌和麦克风。
2. 生成双人全景、主持/嘉宾中近景、互视角度；制作分层 PSD 或透明 PNG。
3. 补齐10–12类嘴型、眼睛、眉毛和3–5个身体动作。
4. 建立角色渲染器：每帧读取说话人状态、口型、眼睛、头部和手势轨道，输出透明动画流或合成视频。
5. 根据当前发言人和镜头方向驱动互视；听众保持自然闭口状态。

**G2 通过标准：** 人物身份、服装和面部稳定；无多余手指、嘴、话筒；头、口、眼可独立控制；嘴型切换无明显跳位；1920×1080无中文乱码、无透明边缘白边。

### P3：普通话音素对齐与口型驱动

**主路径：MFA 普通话强制对齐 + viseme 映射 + 2D Rig**

1. 按说话人和语句切分音频，保留原始总时间轴。
2. 使用准确的逐字稿；数字、英文、方言词按实际发音标注。
3. 安装并核对 MFA 的 mandarin_mfa 声学模型与 mandarin_china_mfa 字典。
4. 生成 TextGrid 音素时间；处理未登录词、口音和低置信度段。
5. 配置 phone-to-viseme 映射，覆盖闭唇、齿唇、张口元音、圆唇元音、扁口元音、闭嘴静音等。
6. 只驱动当前说话人；重叠语音需双人同步或用资料镜头覆盖，并单独标注。
7. 对笑声、强烈情绪、方言、英文词和低置信度段人工复核。

**对照测试：** Adobe Character Animator 使用同一 WAV 计算预录音频口型；Rhubarb phonetic 输出基线 cue。只比较实际效果，不预先假设哪种最好。

**G3 通过标准（10秒样片）：**
- 说话人归属100%正确。
- 抽查至少30个代表性发音/闭口点，90%以上口型变化与音频偏差不超过±100ms（30fps约3帧）。
- 闭唇音、主要元音、句尾闭口有清楚区别；不能只按音量张合。
- 连续300ms以上静音时嘴巴保持自然休息。
- 听众不抢嘴；头、眼、嘴独立可编辑。
- 未通过不得批量生成30分钟。

### P4：镜头与动作

建议镜头：
- 双人全景：开场、互相回应、重要转折。
- 彦泽中景/近景：提问、个人经历、总结。
- 张岚中景/近景：讲故事、行业细节和判断。
- 侧面互视：强调交流关系。
- B-roll：真实路线、旧照片、资料、地图或明确标注为示意的 AI 插图。
- 章节卡：章节标题和轻转场。

动作规则：眨眼频率自然；听众有轻微反应但不机械点头；手势不破坏麦克风位置；动作前后平滑。

**G4 通过标准：** 连续60秒含双人全景、两侧单人镜头和一次故事插图；声音不断裂；情绪与动作相符；人物、视线和麦克风一致；B-roll 来源可追溯。

### P5：HyperFrames 自动剪辑与字幕

1. 按实际内容划分章节，不得硬造未说过的观点。
2. podcast-shot-editor 根据 speaker_id、时码、故事节点、动作和插图生成镜头表。
3. HyperFrames 按章节建立 composition，使用本地 assets；先 lint、check、snapshot，再渲染。
4. 字幕从校对稿生成 SRT；每屏优先不超过两行，避免遮挡人物；人名、地名和专业词人工复核。
5. 插图、地图、照片保留来源；音乐轻铺不盖人声；没有授权的音乐直接不用。
6. 可用 DaVinci Resolve 做最终节奏、声音和字幕精修；若 HyperFrames 已满足要求，不重复建立两套工程。

**G5 通过标准：** 字幕与说话内容对应；人名、地名无错；无乱码和越界；随机检查每章首、中、尾；镜头与原声一致。

### P6：分级集成与正式导出

按10秒 → 60秒 → 5分钟 → 30分钟推进，每一关通过后再进入下一关。

| Gate | 样片 | 必须验证 |
|---|---|---|
| G0 | 环境/素材预检 | 原声、角色、文件、许可、依赖 |
| G1 | 10秒 | 两人发言交接、中文口型、听众状态、原声 |
| G2 | 60秒 | 至少3个镜头、一次交接、一次自然反应、字幕、插图 |
| G3 | 5分钟 | 完整章节、动作与人物一致性、渲染稳定、观看感受 |
| G4 | 30分钟 | 完整内容、技术 QA、声音、授权、完整播放 |

**最终导出参数：**
- 1920×1080，16:9，30fps。
- MP4 / H.264 High Profile / AAC。
- 音频48kHz立体声。
- 在线视频参考码率8–16 Mbps，按平台测试调整。
- 音频目标约-16 LUFS（立体声网络视频参考），True Peak不高于-1 dBTP；以实际听感为准，不为达数值过度降噪或压缩。
- 同时输出可独立使用的 SRT。

## 6. 自动验收与人工抽检

| 类别 | 项目阈值 | 检查方法 |
|---|---|---|
| 原声保真 | 不误导性拼接，所有片段可反查原片 | EDL + 人工回听 |
| 说话人 | 10秒首测100%正确；整片错位零容忍 | 时间线 + 人工 |
| 口型 | 30个点抽查，90%以上在±100ms内 | 音频/帧对照 |
| 听众状态 | 静音超过300ms时自然闭口 | 音轨与画面 |
| 口型种类 | 多类口型，禁止仅开/闭两态 | Rig 资产和样片 |
| 人物一致性 | 脸、服装、发型、工牌、麦克风稳定 | 关键帧对照 |
| 对视和动作 | 视线方向正确，无机械重复 | 人工回看 |
| 字幕 | 人名地名零错，无乱码和越界 | SRT 检查 + 画面抽检 |
| 镜头 | 无不合理跳切、黑帧、音频断口、重复素材突变 | FFprobe + 黑帧检测 |
| 音频 | 参考-16±1 LUFS，True Peak≤-1 dBTP | ebur128 + 听感 |
| 导出 | 1080p、30fps、H.264/AAC、48kHz | FFprobe |
| 权利 | 肖像、声音、音乐、字体、素材许可齐备 | 权利清单 |

抽检要求：10秒逐帧；60秒完整回看；5分钟完整回看；30分钟检查首尾、每章关键段、至少10处说话人切换。正式发布前由彦泽完整观看一次。

所有阈值属于项目验收标准，不代表任何模型官方保证。首轮测试后可以依据实测调整，但必须记录变更理由。

## 7. 安装与运行参考

以下命令仅供 Codex 核对；必须先检查本机现有版本、CLI help 和官方文档，不得假定参数永远不变。

    brew install ffmpeg sox uv node@22
    node -v
    ffmpeg -version
    ffprobe -version
    python3 --version

    npx skills add heygen-com/hyperframes
    npx hyperframes doctor

原声提取参考：

    ffmpeg -i 00_source/interview_original.mp4 -vn -ar 48000 -c:a pcm_s24le 01_audio/original_master.wav
    ffmpeg -i 01_audio/original_master.wav -ac 1 -ar 16000 -c:a pcm_s16le 01_audio/asr_16k_mono.wav

MFA 模型参考：

    mfa model download acoustic mandarin_mfa
    mfa model download dictionary mandarin_china_mfa

HyperFrames 项目参考：

    npx hyperframes init 07_timeline/hyperframes_project --skip-skills
    npx hyperframes lint
    npx hyperframes check --json
    npx hyperframes snapshot --at 0,10,30
    npx hyperframes render --quality draft -o 08_preview/test_60s.mp4

导出检查：

    ffprobe -v error -show_streams -show_format -of json 09_delivery/episode_01_1080p.mp4
    ffmpeg -i 09_delivery/episode_01_1080p.mp4 -filter_complex ebur128=peak=true -f null -

如果 CLI 参数或模型接口变化，以当前官方版本为准。安装失败先读 README 和错误信息，不凭猜测宣布不可用。

## 8. M4 32GB 资源与费用控制

- 分层2D动画、音频、字幕、FFmpeg/HyperFrames 是本地生产主线。
- 完全生成式 AI 动画耗时更长，容易发生人物身份漂移和道具变化，只用于获批的短镜头实验。
- LTX-2 MLX 模型可能需要下载较大权重并占用大量统一内存，需用量化版本和低内存模式先测峰值、耗时与磁盘压力。
- Mac M4 没有 NVIDIA CUDA，LongCat Avatar 1.6 官方 CUDA 路线不作为本地生产依赖。
- 不主动调用收费云 GPU、AI 视频 API、HeyGen 或云渲染。需要时先提交费用、素材上传范围和隐私风险，等待用户批准。
- 可以使用外置 APFS 磁盘保存工程，但不得擅自搬迁其他程序 Runtime 目录。

## 9. 权利与隐私

- 分别确认主持人、受访者对声音、肖像、动漫化形象和公开传播的授权。
- 采访原声、逐字稿和未公开业务资料默认留在本地。
- 需要第三方模型、云 GPU 或素材站时，先说明将上传的文件、服务商、费用和保留政策。
- 记录字体、音乐、插图、模型权重和软件许可证。
- 不得把“开源代码”直接等同于“模型权重、生成素材和商业使用均无限制”。

## 10. 最终交付清单

- episode_01_1080p.mp4：横版正式成片。
- episode_01.srt：中文校对字幕。
- episode_01_cover.png：横版封面；分享方图按平台另做。
- episode_01_vertical_highlights/：可选精华切片。
- HyperFrames 工程及必要的 DaVinci 工程。
- 两个人物分层资产和 Rig 定义。
- 音素对齐、viseme 和人工校对记录。
- qa/release_report.md：工具版本、测试、性能、问题与修复。
- permissions.md、assets_manifest.json：授权和素材来源。
- knowledge_markers.json：采访知识片段对应的原片时间戳，供后续行业知识库使用。

## 11. 官方参考链接

- HyperFrames Skills：https://github.com/heygen-com/hyperframes
- whisper.cpp：https://github.com/ggml-org/whisper.cpp
- Montreal Forced Aligner：https://montreal-forced-aligner.readthedocs.io/
- Rhubarb Lip Sync：https://github.com/DanielSWolf/rhubarb-lip-sync
- Adobe Character Animator：https://www.adobe.com/products/character-animator.html
- Live2D LipSync 说明：https://docs.live2d.com/en/cubism-sdk-manual/mouthmovement-unity/
- LTX-2 MLX：https://github.com/dgrauet/ltx-2-mlx
- lip-sync-mac：https://github.com/mmzz164/lip-sync-mac
- MFLUX：https://github.com/mflux-community/mflux
- OpenTimelineIO：https://github.com/AcademySoftwareFoundation/OpenTimelineIO
- LongCat Video：https://github.com/meituan-longcat/LongCat-Video

**最终状态原则：** 本文是可实施方案与验收设计。只有 Mac 本地真实10秒样片通过彦泽验收，且所需依赖经 Codex 实测，才可把对应模块标记为“已验证可用”。
