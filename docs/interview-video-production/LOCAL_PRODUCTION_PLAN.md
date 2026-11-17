# 彦泽 × 张岚｜本地动漫访谈视频制作方案 V2

**确定方向：** 半写实日系动漫；Rigby2D 骨骼动画 + 动态漫画 + AI 插画。  
**执行工具：** Cursor + Rigby2D MCP + HyperFrames Skills + FFmpeg。  
**设备：** Mac mini M4 / 32GB 统一内存。  
**声音：** 使用真实访谈原声，不合成声音替代。  
**目标：** 约30分钟、16:9、1920×1080、30fps、MP4/H.264/AAC。  
**状态：** 设计方案，需在本机逐关验证；没有任何阶段预先标记为已通过。

---

## 1. 方向决策与本次技术调整

### 1.1 已确认的制作方向

- **人物画风：半写实日系动漫。** 两人都采用成年人物正常比例，统一头身比例、线稿、上色、光影和细节密度。
- **主制作模式：骨骼动画。** 两位角色分别建立可复用 Rig，完成口型、眼神、表情、头部、肩颈和手臂动作。
- **辅助模式：动态漫画。** 访谈讲到故事、经历、地点、业务流程时，切换插画分镜、推拉摇移、景深视差和信息图。
- **辅助素材：AI 插画。** 用于地点、旅行场景、物件、环境、流程示意；主角人物尽量复用固定 Rig，避免 AI 每张图重新画脸。
- **最终剪辑：HyperFrames。** 编排 Rigby2D 输出片段、动态漫画、AI 插画、字幕、章节卡、音效和音乐。

### 1.2 对旧方案的修正

旧方案把 MFA 作为中文口型的必选项，并把 HyperFrames 当作主要动画引擎。V2 调整为：

1. Rigby2D 原生支持本地 Whisper 自动转写，语言选项包含 Chinese；支持从词语时间、Whisper word-timing JSON 等输入生成九类 viseme。
2. 第一轮先测 Rigby2D 原生 Chinese transcription；如果时间戳或口型质量不足，再使用外部 Whisper word-timing JSON。MFA 仅作为有明确失败证据时的备选，不设为必装依赖。
3. Rigby2D 本身已有 Film workspace、双角色 Scene、镜头相机、背景视差和 MP4/WebM/PNG 渲染。主角色动画优先由 Rigby2D 完成。
4. Rigby2D MCP 可通过 Cursor 调用；MCP 能编辑、验证、加音轨和生成口型，但不能直接渲染 MP4/WebM/PNG，最终渲染需要打开编辑器执行。
5. HyperFrames 负责动态漫画和最终节目时间线，不再用 HTML/CSS 贴图方式替代角色骨骼动画。

---

## 2. 工具分工

| 工具 | 主要职责 | 是否主链路 |
|---|---|---|
| Rigby2D 0.5.1 | 分层角色 AutoRig、骨骼动画、viseme 口型、双人 Scene、相机、视差、视频渲染 | **是** |
| Cursor | 调度 MCP、生成/检查工程文件、编写时间轴脚本、修复错误、调用 Skills | **是** |
| Krita | 角色重绘、拆层、修补遮挡、绘制口型和表情 | **是** |
| HyperFrames + Skills | 动态漫画、插画运镜、字幕、片头片尾、章节、总时间线、最终渲染 | **是** |
| FFmpeg / FFprobe | 提取音轨、转码、合并、音量检查、黑帧和媒体信息检测 | **是** |
| whisper.cpp / WhisperX | 逐字稿、词级时间戳、说话人段落辅助 | 按测试选用 |
| MFLUX | 本地生成场景/物件/地点 AI 插画 | 可选 |
| DaVinci Resolve | 复杂人工精修、最终声音微调 | 可选 |
| Adobe Character Animator / Live2D | 对照测试，不作为当前主工程 | 暂不采用 |

### 工具与版本基线

- Rigby2D：先固定 0.5.1，升级前重新跑回归测试。
- Rigby2D 官方下载提供 macOS universal DMG，支持 Apple Silicon；首次启动按官方安装说明处理 macOS Gatekeeper。
- Rigby2D MCP 使用 Node.js 20+；HyperFrames CLI Skill 要求 Node.js 22+ 和 FFmpeg。项目统一使用 Node.js 22+。
- HyperFrames Skills 使用 npx hyperframes skills update 安装/更新匹配当前 CLI 版本的核心 Skills。
- 不登录 HeyGen，不使用收费云 API、云 GPU 或云渲染。AI 图片优先本地 MFLUX；本地能力不足时先报告，不自动转云端。

---

## 3. Rigby2D 在本项目中的角色

### 3.1 它负责什么

- 将分层 PSD、SVG 或同尺寸 PNG 图层导入。
- AutoRig 自动识别身体部件，创建骨骼、网格和 IK。
- 通过 mouth slot 的多种嘴型附件生成 viseme 口型。
- 眼睛、瞳孔、眉毛、头部、手臂和头发建立独立控制。
- Film workspace 里配置输出尺寸、帧率、背景、音轨和镜头。
- Scene 中放入多个 Actor，各自播放角色动画片段；舞台有背景层、前景层、相机和视差。
- 导出 MP4/H.264、WebM/VP9（支持透明）或 PNG 序列。

### 3.2 它不负责什么

- 不会把一张扁平人物图自动切成完整人体图层。
- AutoRig 不能替代美术修补；关节、网格权重、遮挡和手部需要检查。
- 不能仅靠九类通用 viseme 保证中文每个音素都完美；必须用真实普通话音频验收。
- MCP 不提供最终视频渲染命令；需在 Rigby2D 编辑器中执行 File ▸ Render animation。
- 不负责完整30分钟节目内容剪辑、知识点插图、复杂字幕包装和多平台版本管理。

### 3.3 Rigby2D 项目组织

建议一个角色一个 .rigby 工程，一个场景一个 .rigby 工程：

    InterviewVideo/
    ├── 00_source/
    │   ├── original_video.mp4
    │   ├── transcript_original.docx
    │   └── permissions.md
    ├── 01_audio/
    │   ├── original_master.wav
    │   ├── host_guide.wav
    │   ├── guest_guide.wav
    │   └── final_master.wav
    ├── 02_character_art/
    │   ├── host/host_layered.psd
    │   ├── guest/guest_layered.psd
    │   └── character_bible.md
    ├── 03_rigby/
    │   ├── host/host.rigby
    │   ├── guest/guest.rigby
    │   ├── scenes/studio_scene.rigby
    │   └── poses/
    ├── 04_timing/
    │   ├── speaker_turns.json
    │   ├── host_word_timing.json
    │   ├── guest_word_timing.json
    │   └── alignment_review.csv
    ├── 05_illustrations/
    │   ├── generated/
    │   ├── approved/
    │   └── source_ledger.json
    ├── 06_hyperframes/
    │   ├── index.html
    │   ├── compositions/
    │   ├── assets/
    │   └── SPEC.md
    ├── 07_preview/
    ├── 08_delivery/
    └── qa/

原始视频和逐字稿只读；所有剪辑都必须能映射回原片时间戳。

---

## 4. 人物资产制作：从现有图到可动画角色

### 4.1 现有图只作为外观参考

当前彦泽参考图是偏半写实成年动漫；张岚参考图是 Q 版角色设定。两张图不能直接放到同一个场景中，也不能直接交给 AutoRig。

必须重新设计张岚，使她与彦泽统一为半写实日系动漫、成年人物比例。彦泽也需制作适合坐姿访谈的完整角色资产，避免只用一张胸像硬拉成全身。

### 4.2 人物视觉规范

**彦泽（主持人）**
- 保留棕色头发/束发、白色西装外套、深色内搭。
- 成年女性比例，半写实日系动漫。
- 坐姿朝画面右侧，主要视线落在张岚身上。
- 手持一支主持麦克风；不得出现第二支主持麦克风、复制麦克风或悬浮麦克风。
- 手指与麦克风接触关系自然；麦克风与手部绑定。

**张岚（嘉宾/导游）**
- 保留黑色短发、黄色服装、熊猫元素、彩色围巾/工牌。
- 重新绘制为成年人物比例，不能保留 Q 版大头比例。
- 坐姿朝画面左侧，主要视线落在彦泽身上。
- 使用一支固定位置的桌面麦克风；不使用导游旗、扩音器等与访谈无关道具。
- 说话和倾听表情自然。

**统一风格**
- 统一头身比例、眼睛尺寸、线稿粗细、皮肤明暗、发丝细节、衣料质感、色彩饱和度和光源方向。
- 半写实、干净、温暖、有电影感；避免幼儿绘本、Q 版、大眼娃娃风。
- 主场景采用温暖的山景访谈空间，但人物必须与桌椅、光线、透视真正融合，不能像贴纸贴在背景上。
- 画面内不得出现生成模型画出的乱码文字，所有标题字幕由 HyperFrames 文字层制作。

### 4.3 分层 PSD 交付

AutoRig 需要分层 PSD/SVG/同尺寸 PNG；它不会拆解一张扁平图。分层命名和拆分要求见 CHARACTER_ASSET_SPEC.md。

每个人物至少准备：
- 面部、头、脖子、躯干、骨盆。
- 左右上臂、前臂、手掌。
- 后发、前发、刘海。
- 左右眼白、瞳孔、眼睑、眉毛。
- 鼻子、下颌/嘴部区域。
- 口型附件：A、E、I、O、U、MBP、FV、L、rest；优先确保 MBP、A、O 清晰。
- 表情附件：微笑、认真、疑问、惊讶、思考、笑。
- 道具：麦克风、耳饰、围巾、工牌等独立图层。

每个图层必须同画布尺寸、透明背景、锚点一致。需要遮挡修补，不能只把整张人物抠成一张 PNG。

---

## 5. Rigby2D 安装与 Cursor MCP

### 5.1 安装 Rigby2D

官方入口：
- 下载：https://github.com/jaisurya-dev-art/rigby2d/releases/latest
- macOS 文件：Rigby2D_universal.dmg
- 在线体验：https://rigby2d.com/editor/
- 文档：https://rigby2d.com/docs/

优先使用 macOS Desktop App。浏览器编辑器可做快速体验，但正式工程优先使用桌面版并存储在本地项目目录。

### 5.2 MCP 接入

Rigby2D MCP 文档：
https://rigby2d.com/docs/mcp.html

MCP server 运行于 Node.js 20+。为了让 PSD 解析和 Python scripting 可用，按官方文档 clone Rigby2D 仓库并在其目录 npm install。Cursor 使用项目级 .cursor/mcp.json。

配置模板见 cursor-mcp-config.example.json。把示例里的路径替换成真实绝对路径：

- command: node
- args[0]: <RIGBY2D_REPO>/src/mcp/server.js
- args[1]: --root
- args[2]: <INTERVIEW_PROJECT_ROOT>

配置后在 Cursor MCP 面板确认 rigby2d 已连接，再调用 inspect_project 或 validate_project 验证。MCP 只开放项目根目录，不允许访问整个用户 Home 或系统盘。

### 5.3 Cursor 应调用的 Rigby2D MCP 工具

| 工具 | 用途 |
|---|---|
| detect_parts | 检查 PSD 图层识别是否正确 |
| autorig | 从分层 PSD 生成角色 Rig |
| inspect_project / describe_rig | 检查骨骼、图层和资源 |
| validate_project | 检查缺失图片、动画和工程结构 |
| sample_pose | 采样姿势、检查角色位置 |
| add_animation / batch_edit | 创建动画与批量设置关键帧 |
| save_pose / apply_pose | 保存并复用表情和姿势 |
| add_face_control / set_face_control | 眉、眼、情绪控制 |
| add_audio_track / lip_sync | 添加音轨并生成 viseme 口型 |
| set_workspace / set_output | 设置 Film workspace、1080p、30fps |
| add_actor / add_clip / set_actor | 建立双人场景与角色片段 |
| set_layer_depth | 设置背景视差 |

**重要：** MCP 不能渲染 MP4、WebM 或 PNG 序列。Cursor 负责准备和验证工程；最终渲染由 Rigby2D 编辑器执行。

---

## 6. 中文口型与双人声音时间线

### 6.1 首选：Rigby2D 原生中文转写

Rigby2D 的 Lip-sync 文档列出 Chinese 语言，使用本机 Whisper 处理音频，不上传声音；支持词语时间和九类 viseme：

- A、E、I、O、U
- MBP（闭唇）
- FV（唇齿）
- L（舌位）
- rest（静音）

官方文档：https://rigby2d.com/docs/lip-sync.html

先用真实中文原声做10秒测试，观察它的转写文本、时间戳和嘴型，不得仅凭“支持 Chinese”就宣称达到高准确度。

### 6.2 双人访谈的说话人归属

双人不能共用同一条未区分说话人的口型轨道，否则两个人会同时跟着对方说话。

流程：
1. 逐字稿和原视频建立 speaker_turns.json，每段标注 host、guest、overlap 或 unknown。
2. 人工确认每个说话人起止时间；重叠发言单独标记。
3. 为彦泽、张岚分别生成 speaker-specific word timing JSON。
4. 将各自 timing JSON 用于各自角色 .rigby 的 lip_sync。Rigby2D 支持 Whisper word-timing JSON 或 {word,start,end} 格式；时间以音轨起点为基准。
5. 每个角色动画工程可以有一个音频参考轨，设置为静音/音量0；最终节目只在场景或 HyperFrames 中混入一次原始主音轨，避免双重音频。
6. 对重叠段，两人可同时按各自 timing 动嘴；如果时间戳不可靠，切动态漫画/插画覆盖，保留原始声音。
7. lead 默认2帧，min_hold 约0.05秒；需用10秒样片调整，不能照搬默认值而不验收。

### 6.3 备用口型方案

- 如果 Rigby2D 原生 Chinese transcription 对专有名词、方言、快速语音不够准确，先人工校正文本。
- 可导入 Whisper word-timing JSON 或其他支持的词级时间戳。
- MFA 只作为确有必要时的备选；它的音素结果需要额外 G2P/音素到 viseme 映射，不能直接当作可用口型轨道。
- 不使用纯响度开合嘴作为正式版口型。

---

## 7. 双人骨骼动画与镜头设计

### 7.1 两套角色 Rig

每人独立 .rigby，先单人 Rig、单人动作、单人口型通过，再进入双人 Scene。

基础骨骼：
- root / hip / chest / neck / head
- upperarm / forearm / hand（左右）
- hair_back / hair_front / bangs
- eye_l / eye_r / pupil_l / pupil_r / brow_l / brow_r
- jaw / mouth slot
- prop_mic / prop_scarf / prop_badge（按角色）

手持麦克风必须绑定到彦泽手部或手臂骨骼，不能作为一个独立悬浮图层。张岚桌面麦克风绑定到场景道具层，位置固定。

### 7.2 动作库

每个角色至少建立：
- idle_breathe_a / idle_breathe_b：不同呼吸微动作。
- listen_neutral：自然倾听。
- listen_attentive：轻微前倾。
- nod_once：一次轻点头，不能循环。
- think：思考/短暂停顿。
- smile：自然微笑。
- laugh_soft：轻笑。
- speak_neutral：自然讲话身体状态。
- speak_gesture_a / speak_gesture_b：两种轻手势。
- surprised / serious：按真实谈话内容触发。

口型轨道与身体动作需要共存。若当前 Rigby2D 版本不能在同一角色动画中按需要叠加，Cursor 必须采用组合动画或生成合并后的关键帧，不得在未测试前假定支持多动画轨道混合。

### 7.3 双人 Scene

Rigby2D Film Scene 可把多个 .rigby 角色作为 Actor 放在同一舞台，角色各有动画片段，场景有相机、背景层和视差层。

主场景层级：
1. distant：窗外山景/天空。
2. mid：墙面、窗框、书架、灯。
3. near：绿植、桌面、杯子、麦克风底座。
4. actors：彦泽、张岚。
5. foreground：必要时的桌沿/前景装饰。

镜头：
- two_shot_master：双人全景。
- host_closeup：彦泽中近景。
- guest_closeup：张岚中近景。
- host_over_shoulder / guest_over_shoulder：过肩镜头（若资产允许）。
- reaction_guest / reaction_host：倾听反应镜头。

镜头切换遵循谈话内容和情绪，不设固定秒数机械轮换。单人特写必须让人物视线指向画内对方；双人镜头保持对视关系。

---

## 8. 动态漫画与 AI 插画

### 8.1 什么时候切动态漫画

- 受访者讲到过去经历、某次旅行、某个城市。
- 讲行业流程、资源协作、经营方式。
- 讲具体案例、难题、突发事件。
- 需要解释一个概念或展示数据。
- 双人对话长时间停留在同一镜头，需要适度视觉变化。

### 8.2 动态漫画镜头类型

- 单张插画 + 慢推近/拉远。
- 2–4层拆分图 + 轻微视差。
- 3–5格漫画分镜依次出现。
- 地图、路线、地点标签和时间线。
- 关键句大字卡、引用卡、章节卡。
- 同一插画做不同裁切和镜头运动，但不能重复得像循环背景。

### 8.3 AI 插画规则

- 优先使用本地 MFLUX（若 M4 环境可运行）或已有授权素材。
- HyperFrames media-use 可以通过本地 FLUX（MFLUX）生成图片；本项目明确使用 local-only，不使用 HeyGen/云生成/收费模型。
- AI 插画重点生成环境、地点、物件、流程示意，不要每个镜头重新生成彦泽和张岚。
- 真实地点的建筑、景区、酒店等，如果画面不是实拍或经核实的真实照片，必须标注“AI示意图/情景示意”。
- 不得用 AI 插画伪装成采访中真实发生的历史现场。
- 画面内不生成中文文字，标题、地名和说明由 HyperFrames 文字层添加。
- 每张图记录 prompt、模型/版本、来源、生成日期、审核状态。

### 8.4 镜头占比建议（可按内容调整）

- 60–70%：Rigby2D 双人对话/单人特写。
- 20–30%：动态漫画和 AI 插画。
- 5–10%：章节、信息图、标题卡。

这只是第一期的剪辑参考，不作为强制配比。观众能否看下去优先于配比。

---

## 9. HyperFrames 最终编排

HyperFrames 负责：
- 接入 Rigby2D 输出的对话片段。
- 插入动态漫画与 AI 插画。
- 章节卡、字幕、引用、人物标签、信息图。
- 片头、片尾、转场、BGM、音效。
- 统一时间线、预览、检查和本地渲染。

Skills：
- /hyperframes：视频结构、HTML 场景和渲染契约。
- /hyperframes-cli：初始化、检查、截图、预览、渲染、时间线。
- /hyperframes-registry：查找标题、转场、字幕和图形组件。
- /media-use：本地图片、音效、音乐和素材管理；本项目不走付费 provider。

安装/更新核心 Skills：在项目目录执行 npx hyperframes skills update，再由 Cursor 读取实际 Skill 文件。

生产流程：
1. npx hyperframes init <project-dir> --skip-skills。
2. 建立一个章节一个 composition。
3. 把 Rigby2D 渲染片段放入 assets/，素材台账保留来源。
4. 动态漫画以固定素材 + 时间轴动画实现，所有动作必须可按帧确定性重现。
5. 加 SRT/字幕层；所有中文字体随项目存档并核实授权。
6. npx hyperframes lint、npx hyperframes check --json。
7. npx hyperframes snapshot --review，检查每个章节中段和镜头切换点。
8. 打开 HyperFrames desktop preview 给彦泽检查；确认后才执行 delivery render。
9. ffprobe 检查时长、帧率、分辨率、编码；FFmpeg 检查音量和黑帧。

---

## 10. 30分钟生产步骤

1. 内容剪辑：从约58分钟原访谈选出完整约30分钟内容，锁定最终原声。
2. 转写：Whisper 本地识别，人工校对；说话人和重叠段落确认。
3. 角色素材：完成两张统一风格的分层 PSD。
4. 单人 Rig：彦泽、张岚分别 AutoRig，人工修关节和权重。
5. 口型：先做10秒中文口型；过关后按章节生成完整时间轴。
6. 动作：建立角色动作库，按内容标记自然动作。
7. 双人 Scene：构建演播室、两个 Actor、背景层、相机镜头。
8. 动态漫画：挑选关键故事和行业知识点制作插画分镜。
9. HyperFrames：把 Rigby2D 片段、漫画、AI 插画、字幕和音效编排为章节。
10. QA：10秒 → 60秒 → 5分钟 → 全片；不跳级。
11. 导出：1080p MP4、SRT、封面、可编辑工程、素材清单和验收报告。

---

## 11. 测试与验收门槛

| Gate | 内容 | 必须通过 |
|---|---|---|
| G0 | 软件安装、Cursor MCP、目录权限 | MCP 能列出工具；只访问项目目录 |
| G1 | 两套分层 PSD 和 AutoRig | 角色比例统一；部件识别正确；关节无明显穿帮 |
| G2 | 单人中文10秒口型 | 说话人、中文转写、viseme、静音和原声均通过 |
| G3 | 双人10秒对话 | 两人互视、发言交接、倾听者闭口、麦克风正确 |
| G4 | 60秒完整镜头 | 双人/特写/反应镜头、动作、字幕自然 |
| G5 | 3–5分钟章节 | 骨骼动画 + 动态漫画 + AI 插画混合效果通过 |
| G6 | 30分钟全片 | 内容、画面、音频、字幕、授权、导出全部通过 |

### 关键指标

- 10秒样片：说话人归属100%正确。
- 口型：至少抽查30个闭唇/张口/圆口/扁口及静音点，90%以上时间偏差不超过±100ms；未通过就修复对齐和嘴型。
- 听众：对方说话时，听众嘴巴自然闭合；有真实倾听反应，不能每句话机械点头。
- 人物：脸型、发型、服装、熊猫元素、围巾、工牌、麦克风位置一致。
- 动作：同一动作循环不得连续重复超过两次；需要多种 Idle/Reaction 变体。
- 画面：无重影、浮空、贴纸边缘、透视错位、背景穿插、手指和麦克风畸形。
- 动态漫画：每个 AI 示意图有来源记录；不得冒充实拍。
- 音频：最终原始主音轨只混入一次；无双重回声、爆音、截断。
- 导出：1920×1080、30fps、H.264/AAC、48kHz；目标约-16 LUFS（立体声网络节目参考）且 True Peak ≤ -1 dBTP，最终以实际听感复核。
- 30分钟成片必须完整播放检查。

---

## 12. 最终交付

- episode_01_1080p.mp4
- episode_01.srt
- episode_01_cover.png
- episode_01_highlights/（可选）
- host.rigby、guest.rigby、studio_scene.rigby
- 两个人物分层 PSD
- speaker_turns.json、word timing JSON、口型 QA 记录
- HyperFrames 工程、动态漫画插画、素材台账
- qa/release_report.md
- permissions.md

---

## 13. 官方文档

- Rigby2D 官网：https://rigby2d.com/
- Rigby2D 安装：https://rigby2d.com/docs/installation.html
- Rigby2D AutoRig：https://rigby2d.com/docs/autorig.html
- Rigby2D Lip-sync：https://rigby2d.com/docs/lip-sync.html
- Rigby2D Film workspace：https://rigby2d.com/docs/film.html
- Rigby2D Scenes：https://rigby2d.com/docs/scenes.html
- Rigby2D MCP：https://rigby2d.com/docs/mcp.html
- Rigby2D MCP 工具参考：https://rigby2d.com/docs/mcp-tools.html
- Cursor MCP：https://docs.cursor.com/context/model-context-protocol
- HyperFrames：https://github.com/heygen-com/hyperframes

**状态纪律：** 方案和工程文件提交 GitHub 不等于本机安装或样片通过。每个 Gate 必须保存真实运行证据、预览文件和人工验收结果。
