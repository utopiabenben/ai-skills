# 彦泽 × 张岚｜双人动漫访谈视频本地制作技术方案 V1.0

**制定日期**：2026-11-17  
**交付状态**：技术设计与选型；尚未在用户 Mac mini 上完成端到端运行验证  
**执行角色**：Codex（总控/工程）、素材与动画制作模块、WorkBuddy（审核）、彦泽（内容与最终验收）  
**设备基线**：Mac mini M4 / 32 GB 统一内存；优先本地处理及存储，可使用外置 APFS 磁盘。  
**输入基线**：先使用已录制的约 58 分钟访谈进行验证；同样适用于后续约 60 分钟的自然聊天。  
**目标输出**：约 30 分钟、16:9、1920×1080、30 fps、MP4（H.264 + AAC）、可编辑项目；并可另出短视频及独立 SRT 字幕。

---

## 0. 产品目标与不可妥协条件

1. **保留真人原声与真实经历**。原访谈是事实来源；剪辑允许删掉无关段落、重复和无效停顿，但不得替换、拼接出原说话人未表达的观点；不得未经明确授权以合成声音冒充真实采访。
2. **动漫人物连续一致**。主持彦泽：棕色束发/盘发、白色外套，主持手持麦克风，全画面中主持话筒只能有一个。嘉宾张岚：黑色短发、黄色带熊猫图案上衣、彩色围巾/工牌，桌面麦克风。两人坐姿方向互相面对，统一画风、照明、服装、脸型、比例。
3. **真实口型同步优先**。不采用仅按音频响度驱动开合口的方案作为“准确口型”验收版本。要求可追溯的中文对齐数据，并逐镜头验收。
4. **适当自然动作**。非发言人闭口并有自然聆听反应；说话人有口型、眨眼、视线、头部轻微动作和少量手势。避免机械重复或“每句话都点头”。
5. **素材分层与项目可复用**。角色模型、声音、字幕、镜头编排分开；一次修改不导致其他章节全部重制。
6. **以可看完的访谈为准**。内容剪辑与节奏优先于技术炫技；B-roll 服务于真实故事；不用自动生成画面伪装历史现场实拍。
7. **商业用途前核查权利**。本人声音肖像、受访者授权、图片模型权重、素材音乐、字体、软件许可分别核查，不将仓库 MIT 许可证简单理解为模型权重或第三方素材都可商用。

## 1. 技术选型与总体架构

### 1.1 推荐路线：可规模化的本地 2.5D 动画

```
原始访谈视频 + 逐字稿 + 人物参考图
          |
          v
[音轨保全] FFmpeg / 本地 WAV 母带
          |
          v
[转写/说话人] whisper.cpp + 校对 + 分段 speaker_id
          |
          v
[内容剪辑] story beats / EDL / final_audio.wav (先锁声音)
          |
          +--> [MFA 普通话音素强制对齐] -> viseme.json -> 两套角色 Rig
          |                                           |
          +--> [人物设计/表情/动作/场景] -----------> [2D 动画输出]
          |                                           |
          +--> [插图/资料镜头/图表] -----------------+
                                                      |
                                                      v
[HyperFrames] 镜头编辑 + 说话人切镜 + 中文字幕 + 音乐 + 图文覆盖
                                                      |
                                                      v
[FFmpeg / DaVinci Resolve] 章节精修、声画审核、H.264 导出
                                                      |
                                                      v
30分钟主片 + SRT + 精华切片 + 封面 + 可编辑工程 + 知识库时间戳
```

**为什么选择**：30 分钟的视频需要大量可重复镜头，2D Rig 能维持人物一致性，也能保持本地离线制作。语音与动画解耦，修改字幕、镜头和角色动作不必重算全部 AI 视频。

### 1.2 三个口型方案的边界

| 方案 | 设备/成熟度 | 真实中文原声 | 项目定位 |
|---|---|---|---|
| **A. MFA 中文音素对齐 + viseme 映射 + 2D Rig** | 本地可研发；需要分层口型及开发 | 支持；手动纠错不可免 | **主路线**，优先试做 |
| **B. Adobe Character Animator 预录语音自动 lip sync** | Mac 上的成熟角色动画工具；可能涉及付费订阅 | 可导入 WAV 计算 viseme；中文准确度须现场验证 | **比较方案**，如果优于 A 且商业许可合适可换用 |
| **C. Rhubarb Lip Sync `phonetic` 模式** | 免费工具，跨语言但识别精度通常低于英语模式 | 支持非英语基础口型，但中文效果需要测试 | 仅用于 10 秒比较/快速基线，不直接验收整片 |

注意：Live2D Cubism 普通 LipSync 主要按音量控制 `ParamMouthOpenY`；单独使用不符合本项目的口型标准。若采用 Live2D，必须额外使用音素事件驱动 `MouthForm` / 多口型形变并人工测试。Live2D 模型制作及 SDK 许可需另核查。

### 1.3 AI 全生成选项，限短镜头验证

- **Mac 本地 LTX-2 MLX**：对短镜头探索 `a2v` 等音频驱动能力；官方项目对部分路径标注 Experimental，不能直接作为 30 分钟必达方案。优先 q4/q8、`--low-ram`、短片/低分辨率试跑。短镜头必须验证原声保持、脸部一致、口型与声音同步、渲染时长及内存峰值。
- **`lip-sync-mac`**：Apple Silicon 实验仓库，使用 Qwen3-TTS 生成语音再配合 LTX-2.3；对“必须保留会议原声”并不天然匹配，不能直接替代主链路。
- **LongCat Avatar 1.6**：支持多人音频驱动，但官方推理依赖 NVIDIA CUDA。需要远程 GPU 才有条件运行，不计入“Mac 本地完整生产”的默认路线；仅在另行授权云计算费用及素材上传之后尝试。
- **不作承诺**：上述模型并未在用户 M4 32 GB 的具体环境进行过双人动漫+中文原声 30 分钟端到端验证。

## 2. 工作分工

| 角色 | 职责 | 审核权 |
|---|---|---|
| 彦泽 | 主题、人物审定、内容删减、原声/表达、最终画面与发布 | P0 内容、最后验收 |
| Codex | 任务拆解、软件检测、素材规范、脚本与接口、构建/渲染、QA 归档 | 技术流程负责人 |
| Cursor（按需） | 角色渲染器、时间线/数据结构、代码修改 | 代码交付/测试 |
| WorkBuddy（按需） | 逐字稿审核、内容章节、质量检查报告、知识库提取 | 辅助复审，不能替代耳听/眼看 |
| 动画/设计模块 | 角色定稿、PSD/PNG 分层、口型、表情和场景设计 | 视觉资产 |

不假设 Codex/WorkBuddy 能自行操作某个未连接的软件；优先调用可用 CLI/API，缺少工具时输出可执行说明、失败原因与待人工操作清单。

## 3. 工具、Skill 清单（按需要安装，不全部叠加）

| 类型 | 产品/Skill | 目的 | 成本/要求 |
|---|---|---|---|
| 基础必需 | FFmpeg / FFprobe | 转码、音轨、媒体诊断、输出 | 开源；本地 |
| 基础必需 | Python 3.11+ / `uv` | 转写、对齐解析、QA 脚本 | 免费 |
| 基础必需 | Node.js 22+ | HyperFrames CLI | 免费 |
| 语音 | `ggml-org/whisper.cpp` | 中文转写、时间戳，Apple Silicon Metal | 本地免费；需模型权重 |
| 语音精对齐 | Montreal Forced Aligner | `mandarin_mfa` 音素时间、TextGrid | 本地；初装较重，语料准备复杂 |
| 快速口型比较 | `DanielSWolf/rhubarb-lip-sync` | 2D mouth cue JSON；`phonetic` 备选 | 免费，中文需测 |
| 口型商业备选 | Adobe Character Animator | 多 viseme 口型、表情及动作 | 商业订阅及授权需检查 |
| 本地图片生成 | `mflux-community/mflux` | 背景和 B-roll 原画，资产落本地 | 免费运行，模型需下载 |
| 人物分层 | Krita / Photoshop / 图像编辑 | 抠图、图层分离、口型绘制 | Krita 免费，PS 付费 |
| 角色 Rig | 自定义 Canvas/WebGL 2D 渲染器 或 Live2D Cubism | 姿态、口型、动画 | 自建；Live2D 授权另核查 |
| 视频合成 | HyperFrames `/hyperframes` | 整片时间线/场景规范 | 可本地渲染 |
| 视频命令 | `/hyperframes-cli` | 初始化、lint、check、snapshot、render | Node 22+、FFmpeg |
| 视频素材 | `/media-use` | 素材接入、字幕、音效、音频混合 | 选择本地源；付费服务要授权 |
| 视频组件 | `/hyperframes-registry` | 标题、章节、字幕、转场 | 可复用组件 |
| 可选 Skill | `/style-sampling` | 统一风格（若支持且安装） | 仅风格参考需要时 |
| 可选 Skill | `/reverse-any-video` | 从既有成片重建时间线 | 可能需要 Pro；本项目默认不用 |
| 精修 | DaVinci Resolve | 精修音画/片头片尾/最终审片 | 免费版/Studio 需核实功能差异 |
| 项目复用 | OpenTimelineIO（可选） | 跨编辑器表达剪辑时间线 | 需测试编辑器适配器 |

**HyperFrames 官方 Skills 安装**：`npx skills add heygen-com/hyperframes`，优先选择 `/hyperframes`、`/hyperframes-cli`、`/media-use`、`/hyperframes-registry`。Skill 指导时间线和渲染，**不会自动提供**符合中文音素要求的专用神经口型模型。

**需要自行开发的项目 Skills**（名字为本方案拟定，当前不宣称已安装）：

- `interview-transcript-editor`：保真剪辑；给出 original_start/end、speaker、审定文本、保留原因；不能自动杜撰句子。
- `speaker-audio-qa`：两人音轨归属、错位/重叠、爆音/噪声/音质、源音比对。
- `mandarin-viseme-align`：MFA 音素→viseme、口型曲线、失败标记和可人工修改的数据。
- `avatar-continuity-qa`：脸、服装、颜色、话筒、视线、场景一致性。
- `podcast-shot-editor`：根据发言时序与故事节点生成切镜/资料镜头时间线。
- `video-release-qa`：视频帧、音画同步、字幕、黑帧、导出参数、完整性报告。
- 可选 `interview-knowledge-miner`：将同一时间戳的采访内容用于知识库/Skill 候选，**与视频制作流程相互独立**。

各 Skill 应包含 `SKILL.md`、输入/输出契约、脚本、示例和测试用例；不得仅放一个提示词便声称“已实现自动化”。

## 4. 素材目录与数据契约

使用英文 ASCII 文件名，原始素材只读。建议工程位于外置 APFS 盘高速目录（路径由用户选择），**不能擅自移动 WorkBuddy/Codex Runtime**。

```text
InterviewVideo/
├── 00_source/
│   ├── interview_original.mp4       # 只读，保持 checksum
│   ├── transcript_original.pdf
│   └── permissions.md
├── 01_audio/
│   ├── original_master.wav          # 原声音频，不修音
│   ├── asr_16k_mono.wav
│   ├── host_dialogue.wav            # 根据精确剪辑时间线归集，其他部分静音
│   ├── guest_dialogue.wav
│   └── final_dialogue.wav           # 完成内容审定后的声音母带
├── 02_transcript/
│   ├── transcript_raw.json
│   ├── transcript_checked.json
│   ├── edit_decisions.json
│   ├── segments.json
│   └── final_subtitles.srt
├── 03_characters/
│   ├── host/{rig,mouth,eyes,expressions,poses}/
│   ├── guest/{rig,mouth,eyes,expressions,poses}/
│   ├── character_bible.md
│   └── assets_manifest.json
├── 04_scenes/
│   ├── studio/
│   ├── broll/
│   ├── intro_outro/
│   └── overlays/
├── 05_alignment/
│   ├── mfa_corpus/
│   ├── textgrids/
│   ├── host_visemes.json
│   ├── guest_visemes.json
│   └── alignment_review.csv
├── 06_animation/
│   ├── shot_host/
│   ├── shot_guest/
│   ├── shot_twoshot/
│   └── clips_manifest.json
├── 07_timeline/
│   ├── editorial_timeline.json
│   ├── shots.json
│   └── hyperframes_project/
├── 08_preview/
│   ├── test_10s.mp4
│   ├── test_60s.mp4
│   └── test_5m.mp4
├── 09_delivery/
│   ├── episode_01_1080p.mp4
│   ├── episode_01.srt
│   ├── episode_01_cover.png
│   ├── episode_01_vertical_highlights/
│   └── release_report.md
├── qa/
│   ├── qa_report.json
│   ├── qa_checklist.csv
│   └── sample_review_notes.md
└── scripts/
    ├── preflight.py
    ├── ingest.py
    ├── align_visemes.py
    ├── render_shots.py
    ├── generate_timeline.py
    └── qa_export.py
```

**基础素材清单（每个人物）**：

- 统一角色三视图/近正面、3/4 左右侧，站/坐姿（与最终镜头角度协调）；角色比例固定。
- 眼睛：睁眼、半闭、闭眼、微笑；嘴巴：闭合、MBP、F/V、a、o、e、i、u、ü、过渡形态等 **10–12 组**（最终以对齐模型实际音素映射评估）。
- 眉毛：平静、认真、疑问、惊讶；手势：静止、解释、点头、轻手势 3–5 个可复用动作。
- 透明分层：脸/头发/眼睛/口/身体/手臂/饰品/麦克风；不要让麦克风或嘴巴与主体绘死在一起。
- 场景：双人演播间全景、主持中近景、嘉宾中近景、侧面相视、插图过渡等；所有中文文字用视频叠加排版，图片生成不承担正式文字。

**渲染输入示例**：

```json
{
  "segment_id": "seg_0042",
  "speaker": "host",
  "source_start_ms": 175800,
  "source_end_ms": 180200,
  "timeline_start_ms": 68400,
  "timeline_end_ms": 72800,
  "audio_path": "01_audio/final_dialogue.wav",
  "mouth_cues_path": "05_alignment/host_visemes.json",
  "shot": "host_medium",
  "motion": "explain_subtle",
  "subtitle_id": "srt_0042",
  "source_text_verified": true
}
```

`source_*` 必须保留原录音时间定位；`timeline_*` 表示剪辑后时间，二者通过 EDL 映射，不允许混用。示例中的时码为格式演示，非原片事实。

## 5. 逐阶段实施步骤 + 验收关卡

### 阶段 P0：环境预检、授权和原始素材锁定

1. Codex 输出机器 CPU/内存、macOS、磁盘、外置盘格式及可用容量、已装软件版本报告。
2. 检测 Node.js >=22、FFmpeg/FFprobe、Python/uv、Git、是否有 NVIDIA GPU（M4 没有 CUDA）、GPU 负载与磁盘速度。
3. 确认参考图与原音存在，生成 SHA256，**不得覆盖**原件。
4. 记录受访者允许的公开使用、形象改绘、声音使用、知识库采集和商业使用范围；敏感材料默认本地。
5. 先基准测试 10 秒素材，给出渲染和内存数据，再决定整片任务分批大小。

**验收 G0**：机器和依赖清单已生成；原文件可读取且有校验值；权限边界明确；若缺素材或无法读取，流程停止并准确报告。

### 阶段 P1：声音母带和内容粗剪

1. `FFmpeg` 抽取原声 48 kHz WAV 母带（原始若为压缩音频，转 WAV 不能恢复丢失频率）。另抽取 16 kHz mono 用于识别。
2. `whisper.cpp` 生成中文转写，保留原时间戳；人物说话人识别需与原视频/会议录音交叉人工确认。注意原文件存在少量第三者说话与重叠的可能，不能强行全归给两位主角。
3. 给每段语音标注 `speaker_id, start, end, text, topic, include, reason`，按主题形成 30 分钟的内容大纲。
4. 先做 **纯声音粗剪**：保留自然停顿、故事铺陈、反应声；清理超长静默/确实无效的语气重复，剪点采用短交叉淡化，避免音节被切掉。
5. 禁止使用可能改变音色的过强降噪、自动配音或变声；输出未处理原声与轻处理版 AB 对照，以用户听感为准。
6. 锁定最终内容（30分钟为目标区间，可围绕节目节奏调整），为每个最终片段建立 `final_audio ↔ source_timestamp` 映射。

**验收 G1**：两人归属经人工复查；没有拼出原声不存在的话；关键情绪/转折未被删断；所有剪点听起来流畅；`final_dialogue.wav` 时间码固定后才进入口型制作。

### 阶段 P2：角色素材生成与动画 Rig

1. 从现有彦泽/张岚参考图建立 `character_bible.md`，锁定头发、服装、主色、工牌、话筒、角色比例、镜头方向。
2. 先出场景、正面/3/4面人物、单人近景和双人全景；再制作角色分层 PSD / 透明 PNG；无正式字幕文字。
3. 根据音素映射制作每人 10–12 类嘴型/过渡形态，按角色图层坐标校准；小表情（眨眼、眉毛、视线）及3–5个身体动作单独导出。
4. 建立角色 Rig 渲染器：每帧读取时间戳，取说话人状态、嘴型、眼睛、头部和手势轨道，输出 RGBA 动画流或背景合成视频。
5. 双人互视：单人镜头可以略朝画内另一位；嘉宾发言时主持朝嘉宾，主持发言时嘉宾朝主持；避免双人永远正看镜头。

**验收 G2**：两个角色的身份/服装/面部一致；无多余手指/嘴/双话筒；头/口/眼能分别动；静态嘴型帧之间无明显跳位；测试画幅1920×1080、无乱码中文、透明图边缘无白边。

### 阶段 P3：中文音素对齐与真正的 2D 口型驱动

**首选路径 A**

1. 将定稿语音按说话人、语句切成独立短片段（避免整段混合语音直接对齐）。保留源声总时间轴。
2. 修订每段准确汉字转录，标点与数字读音以实际发音为准；MFA 需要相对准确的转写与兼容词典。
3. 安装 MFA 的 `mandarin_mfa` 声学模型与 `mandarin_china_mfa` 字典；针对未登录词或方言/口音人工补词、复核结果。
4. 执行强制对齐输出 TextGrid/音素时间片段。编写 `phone -> viseme` 可配置映射：闭口辅音、齿唇、张口元音、圆唇元音、扁口元音、闭嘴与静音，平滑转换但不覆盖正确闭合时刻。
5. 根据 `speaker_id` 在画面中只驱动当前发言人嘴型；另一人呈现自然听众状态。重叠语音需双角色同步或用插图覆盖，并在 QC 清单单独标记。
6. 对低置信度段、强烈情绪、突发笑声、四川口音与英语词手工复查。

**对比路径 B**：在 Adobe Character Animator 导入相同 WAV，执行 `Compute Lip Sync from Scene Audio`，与 A 的相同 10 秒进行盲评。输出帧级结果及返工复杂度；确认中文版与 Mac 版本功能、许可后决定是否采购/选用。

**低成本基线 C**：Rhubarb 的 `phonetic` 模式生成 JSON cue。它对非英语通用，但官方说明通常较英语专用识别器粗糙；只作为基准或后备。

**验收 G3（在10秒样片上）**：

- 说话人物归属必须 100% 正确；听者无无故张嘴。
- 逐帧观察 30 个代表性发音/闭口点；显著口型变化对语音的延迟目标 **≤100ms（30fps约3帧）**，90%以上样点达标；这是项目内控制标准，并非模型官方保证。
- `/b/m/p/` 等闭口音、主要元音形态和句尾闭口有可辨变化；不能“响就张嘴、轻就闭嘴”替代音素形态。
- 连续 300ms 以上静音，嘴部应保持自然休息（除预设自然表情）；临时人工修复纪录入库。
- 头部/视线/嘴巴分别能修改，改完后音画同步不漂移。

如 G3 失败，**禁止批量生成30分钟**；先改角色 Rig、中文词典和口型映射。若两条本地路径均不能达到要求，提交高保真云 GPU 选项的试点成本与隐私方案，等用户决定。

### 阶段 P4：动画镜头与场景补充

**镜头模板**（默认优先固定镜位，按真实故事调整）：

- `shot_01_twoshot`：双人对坐，全景，适合切入、相互回应与转折。
- `shot_02_host_medium`：彦泽中景，提问、讲个人经历、总结。
- `shot_03_guest_medium`：张岚中景，讲故事、讲行业细节。
- `shot_04_host_close` / `shot_05_guest_close`：情绪、关键判断。
- `shot_06_broll_story`：真实旅程相关的地图、旧照片、示意图、资料片段（事实标识）。
- `shot_07_chapter_card`：章节标题及短转场。

动作规则：眨眼频率与具体表情非机械循环；听众有轻微点头，但不逐句同频点头；主持持麦手臂大体稳定；嘉宾麦克风位置固定；动作前后能平滑衔接。B-roll 仅使用有权素材，并明确示意性质，避免当成真实历史影像。

**验收 G4**：连续60秒具备双人全景、两侧单人镜头、一次故事插图；切镜不失声音连续性，表情与故事情绪一致，人物双眼互视与话筒一致，B-roll 来源可追溯。

### 阶段 P5：自动剪辑和字幕

1. 按已定内容分章，例如：初入行业、最难忘的客人、旅游业生意逻辑、旅居与老年生活、经验和AI。章节按实际原声内容确定，不能硬造上次没有说的话。
2. `podcast-shot-editor` 读取节目脚本、`speaker_id`、句子时码、角色动作与插图节点，生成 `shots.json`。
3. HyperFrames 创建 `index.html` 主 composition，每个章节单独 composition；音视频采用本地 `assets/`，所有可编辑文本、字幕采用排版覆盖层。开始先 lint/check/snapshot，避免一次渲染整片才发现错误。
4. 字幕采用逐字稿校对生成 SRT/覆盖层。每屏优先不超过两行，按阅读节奏分句；保留原声真实表达，避免自动改写人名/地名/专业术语；中文使用可靠授权字体并在渲染前自查。
5. 有实际地图、票据、表格、照片时切入资料镜头；保留原始出处；需要展示知识/方法时可用无夸大图示。
6. 进入 DaVinci Resolve 精修整体节奏、音频混合、字幕异常与片尾；若由 HyperFrames 完成所有动作，也可直接交付，避免重复制作两套工程。

**验收 G5**：字幕与发言一一对应、名称/地名无错误；无乱码、无文字超安全区域；章节时长符合内容节奏；随机检查每章首、中、尾，画面/原声/字幕相符。

### 阶段 P6：分级集成与完整发行

按 **10秒 -> 60秒 -> 5分钟 -> 30分钟** 四级门槛推进；失败只回滚对应镜头，不重新生成全部素材。

- 10秒：各人一次发言、口型、听众、原声同步。
- 60秒：至少3个镜头、一次交接、一次自然反应、字幕、一次插图。
- 5分钟：完整章节、音乐淡入淡出、不同景别、关键画面、连贯表达。
- 30分钟：全片技术 QC + 主持抽检 + 发布版本 QA。

**最终导出**：MP4 H.264 High、1920×1080、30fps、AAC 48kHz、立体声、16:9；常规在线播放码率建议 8–16 Mbps，可根据平台压缩测试。避免重复压缩；另交 ProRes/高质量中间文件按容量选择。

音频：目标综合响度约 -16 LUFS（立体声网络视频工作目标）、true peak 不高于 -1 dBTP；须以实际听感和平台要求调整，尤其不要让会议原声被过度降噪而改变音色。字幕单独存 SRT 并同时提供可关闭/可重新渲染的项目字幕。

**验收 G6**：导出完整，时长/帧率/音频轨正确；字幕完整且无错别字；双人身份稳定、口型声画无感知性偏移；无黑帧/丢音/卡顿/重复帧；音频没有破音；发布包有许可证清单、数据来源清单、内容确认及报告。

## 6. 自动验收指标与人工抽检计划

| 类别 | 检查指标（项目验收阈值） | 手段 | 不合格处理 |
|---|---|---|---|
| 原声保真 | 原话不能被误导性拼接；每句能反查原声 | EDL + 人工回听 | 退回内容剪辑 |
| 说话人 | 10秒首测归属 100%；整片发现错位 0 容忍 | speaker timeline + 人工抽检 | 重新标注/渲染 |
| 口型时序 | 代表性发音点 90% 落在 ±100ms 内，明显口型错配 0 容忍 | 音频波形 + 帧比较 | 对齐/口型修正 |
| 不发言者 | 超过300ms无语音时，嘴巴自然休息；不能抢说 | 音轨/viseme 状态和画面 | 修 mouth cues |
| 口型种类 | 含闭口、圆口、宽口等，禁止只有两个开合帧 | Rig 资产与样片 | 补绘口型 |
| 角色一致性 | 脸、发型、上衣、围巾、麦克风各景别一致 | 并排关键帧/人工 | 换素材或重绘 |
| 双人对视 | 互听镜头视线方向正确；非口头点头机器动作 | 镜头抽查 | 运动曲线修正 |
| 字幕 | 人名/地名零错；无乱码；两行以内优先；不遮关键主体 | SRT 校验/中文 QA/视觉抽查 | 修改字幕 |
| 镜头编辑 | 无不合理跳切、黑帧、音频断口、重复素材突变 | FFprobe/黑帧检测/人工 | 剪点修复 |
| 音频 | 目标 -16±1 LUFS；true peak <=-1 dBTP；无可感知音色失真 | ebur128/truepeak + A/B | 降噪/压缩回退 |
| 导出 | 1920×1080，30fps，H.264/AAC，音频48kHz；容器可播放 | ffprobe + 抽帧 | 重新导出 |
| 资产出处 | 素材、字体、音乐、肖像音频授权记录齐备 | assets_manifest/permissions | 禁止发布 |

抽查样本：10秒整体逐帧；60秒整体回看；5分钟整体回看；30分钟首尾全看+每章节关键段+至少10处说话人切换。最终正式发布由主持从头到尾至少正常速度完整观看一次（与自动测评相结合）。以上阈值是项目建议 QA 规范，需要在首个样片试验后调整。

## 7. 实际安装/CLI 运行参考

**注意**：下面是让 Codex 核对安装与接口的命令示例，尚未在用户 Mac 上运行。第一次必须先 `--help` 检查现用版本。MFA 环境独立安装，避免与视频渲染依赖冲突。

```bash
# 基础依赖，确认路径和版本
brew install ffmpeg sox uv node@22
node -v; ffmpeg -version; ffprobe -version; python3 --version

# 安装/选择 HyperFrames Agent Skills；交互安装时选核心四项
npx skills add heygen-com/hyperframes
npx hyperframes doctor

# 原声保全：临时命名的原始文件应由 Codex 实际发现并定位
ffmpeg -i '00_source/interview_original.mp4' -vn -ar 48000 \
  -c:a pcm_s24le '01_audio/original_master.wav'
ffmpeg -i '01_audio/original_master.wav' -ac 1 -ar 16000 \
  -c:a pcm_s16le '01_audio/asr_16k_mono.wav'

# 中文强制对齐模型；语料按 speaker/句子准备准确同名 WAV + 转录
mfa model download acoustic mandarin_mfa
mfa model download dictionary mandarin_china_mfa
# mfa align '05_alignment/mfa_corpus' mandarin_china_mfa mandarin_mfa '05_alignment/textgrids' --clean

# Rhubarb：仅当已安装并核对 CLI 版本时做对照试验
# rhubarb -r phonetic -f json -o '05_alignment/rhubarb_guest.json' 'guest_test.wav'

# HyperFrames 项目，顺序：初始化 -> 检查 -> 取样 -> 本地渲染
npx hyperframes init '07_timeline/hyperframes_project' --skip-skills
# 在项目目录内按官方格式编写场景后：
# npx hyperframes lint
# npx hyperframes check --json
# npx hyperframes snapshot --at 0,10,30
# npx hyperframes render --quality draft -o '08_preview/test_60s.mp4'
# npx hyperframes render --quality delivery -o '09_delivery/episode_01_1080p.mp4'

# 导出媒体元数据与音频响度
ffprobe -v error -show_streams -show_format \
  -of json '09_delivery/episode_01_1080p.mp4' > 'qa/final_ffprobe.json'
ffmpeg -i '09_delivery/episode_01_1080p.mp4' \
  -filter_complex ebur128=peak=true -f null - 2> 'qa/loudness.log'
```

如果 Mac 上未安装 `node@22` 到 PATH，Codex 应先修复 Node 版本；不要静默使用低版本。若工具安装失败，先阅读官方 README 和发行包、核对路径及依赖，再回报真实错误。

## 8. 质量和成本控制：先小样，再批量

**M4 32GB 资源限制**：

- 2D 动画、音频、字幕、FFmpeg/HyperFrames 适合本地制作，但30分钟最终渲染必须根据具体项目测速度。
- 完全生成式 AI 动画的每秒生成成本与时延显著更高，还可能产生身份漂移、麦克风错乱、画面重构；只做用户批准的短镜头试验。
- LTX-2 MLX 等模型可能需要下载数十 GB 权重并占用大量统一内存；使用量化版和 `--low-ram` 仍需实测 CPU/GPU 峰值、磁盘压力、耗时。
- 外置盘项目路径可迁移，但不能擅自搬迁其他程序 `runtime`。建议清理临时缓存并保留原始音视频及最终项目源码。
- 不主动调用收费的云 GPU、AI 视频 API、HeyGen、其他视频云渲染；如确需使用，应单独列出费用、数据上传范围、模型权重/内容使用约束供用户决策。

**进度闸门**：

| 顺序 | 样片 | 检查目标 | 通过后允许 |
|---|---|---|---|
| Gate 0 | 音频/素材完整性 | 原声、角色、许可可用 | 立项 |
| Gate 1 | 10秒原声口型 | 两人真实中文原声、多口型、听者状态 | 扩展模板 |
| Gate 2 | 60秒完整场景 | 人物动作、双人对视、切镜、字幕、话筒 | 章节制作 |
| Gate 3 | 5分钟章节 | 观看感受、人物一致性、自动渲染稳定性 | 正式制作 |
| Gate 4 | 30分钟全集 | 技术 QA、内容 QA、原声还原、完整播放 | 发布 |

每关记录 `pass/fail`、失败镜头、帧号、音轨、截图、修复方式、再测结果。任何 P0 错误（原声内容错用、错误说话人、授权缺失、明显错口型）阻断整片发布。

## 9. 视频语言与视觉风格约束

1. **整体**：温暖、清晰的动漫播客场景；人物处于同一个空间，主色调、镜头色温和阴影一致。
2. **摄影**：保留固定机位的真实播客感，使用近景和双人镜头转换。不要满屏随机移动、持续推拉或过量动效。
3. **故事**：当谈到第一次带团、旅游行业赚钱方式、老年旅居等话题时，可以插入路线图、档案图片、示意手绘或文字摘要；历史画面明确标为“示意”。
4. **人物**：动作小而自然；单帧表情连贯；不能发生突然换脸、工牌变化、熊猫图案消失、两个话筒、手部断裂等。
5. **字幕**：中文字体为后期排版层。严格检查标点、错字、长度与安全区域。公众号封面和分享裁切另做专门版式，不从画面随机裁剪。
6. **声音**：声音原始风格保留。用户此前反馈录音听感有异样，应提供保留原声、轻处理两版 A/B 小样，优先以本人确认版本作为全片母带。
7. **音轨**：音乐轻铺、不盖人声，若来源不明确直接不用；被采访者的哭笑、情绪和有效停顿应保留。

## 10. 正式交付清单

- `episode_01_1080p.mp4` — 正式横版成片。
- `episode_01.srt` — 中文校对字幕；可选时间戳双人逐字稿。
- `episode_01_cover.png` — 横版首图；分享方图按最终发布平台另导出。
- `episode_01_vertical_highlights/` — 按实际可传播内容截取的短片（可选）。
- `07_timeline/hyperframes_project/` — 可编辑合成工程；若有 DaVinci 工程则一并交付。
- `03_characters/` — 可复用角色分层和 rig 定义。
- `05_alignment/` — 原声对应的音素、口型数据，便于修改和审查。
- `qa/release_report.md` — 测试记录、问题/返工、通过标准、性能、版本/模型清单。
- `permissions.md` 与 `assets_manifest.json` — 录音素材授权及第三方许可清单。
- `knowledge_markers.json` — 访谈内容与知识片段时间码，供后续行业知识库生产使用（不影响视频交付）。

## 11. 权威参考与来源

- HyperFrames Skills: https://github.com/heygen-com/hyperframes/blob/main/docs/guides/skills.mdx
- HyperFrames CLI: https://github.com/heygen-com/hyperframes/blob/main/skills/hyperframes-cli/SKILL.md
- whisper.cpp: https://github.com/ggml-org/whisper.cpp
- Mandarin MFA official example: https://montreal-forced-aligner.readthedocs.io/en/latest/first_steps/alignment_example.html
- MFA forced alignment: https://montreal-forced-aligner.readthedocs.io/en/latest/user_guide/workflows/alignment.html
- Rhubarb: https://github.com/DanielSWolf/rhubarb-lip-sync
- Adobe Character Animator (audio to lip-sync): https://helpx.adobe.com/adobe-character-animator/desktop/behaviors/learn-more-about-behaviors/body-directly-controlled.html
- Live2D automatic lip sync limitations: https://docs.live2d.com/en/cubism-sdk-manual/mouthmovement-unity/
- LTX-2 MLX Apple Silicon: https://github.com/dgrauet/ltx-2-mlx
- Local lip-sync alternative: https://github.com/mmzz164/lip-sync-mac
- Local image generation: https://github.com/mflux-community/mflux
- OpenTimelineIO: https://github.com/AcademySoftwareFoundation/OpenTimelineIO
- LongCat 1.6 CUDA: https://github.com/meituan-longcat/LongCat-Video

**工程状态说明**：以上为可实施方案和验收设计。只有 Mac 本地真实10秒样片经彦泽确认、且所需工具依赖经 Codex 实测，才将对应模块标注为“已验证可用”。