# 双人动漫访谈视频生产方案 V2

本目录是「彦泽 × 张岚」双人动漫访谈的可复用制作规范。当前确认的视觉与制作方向：

- 人物画风：半写实日系动漫，成年人物比例。
- 制作方式：Rigby2D 骨骼动画 + 动态漫画 + AI 插画。
- 主设备：Mac mini M4 / 32GB。
- 声音：保留真实访谈原声。
- 主动画：Rigby2D 0.5.1 Film workspace / Scene。
- 自动化：Cursor + Rigby2D MCP。
- 后期编排：HyperFrames + FFmpeg；DaVinci Resolve 作为可选人工精修工具。
- 默认本地优先，不调用收费视频 API 或云 GPU。

## 文件

- [完整技术方案 V2](./LOCAL_PRODUCTION_PLAN.md)
- [Cursor / Codex 执行任务书 V2](./CODEX_IMPLEMENTATION_BRIEF.md)
- [角色分层资产制作规范](./CHARACTER_ASSET_SPEC.md)
- [Cursor MCP 配置模板](./cursor-mcp-config.example.json)
- [视频 QA 验收清单](./VIDEO_QA_CHECKLIST.csv)

## 核心原则

1. 不再用 HTML/CSS 把扁平人物图贴到背景上，主角动画交给 Rigby2D。
2. Rigby2D AutoRig 只能处理已经拆分好的 PSD/SVG/PNG 图层，不能把一张扁平图自动拆成人体部件。
3. Rigby2D 的中文自动转写和九类 viseme 先做真实音频测试；不把响度驱动的张嘴闭嘴当成精准口型。
4. Rigby2D MCP 可以检查、修改、绑定音轨、生成口型、搭建 Scene；MP4/WebM/PNG 最终渲染仍需打开 Rigby2D 编辑器执行。
5. 动态漫画和 AI 插画通过 HyperFrames 编排；AI 插画只做场景/物件/地点示意，不重绘真实人物来破坏角色一致性。
6. 先完成10秒、60秒、5分钟样片，逐级验收后再生产30分钟节目。

## 官方工具入口

- Rigby2D：https://rigby2d.com/
- Rigby2D 下载：https://github.com/jaisurya-dev-art/rigby2d/releases/latest
- Rigby2D 文档：https://rigby2d.com/docs/
- HyperFrames：https://github.com/heygen-com/hyperframes
- Cursor MCP 文档：https://docs.cursor.com/context/model-context-protocol
