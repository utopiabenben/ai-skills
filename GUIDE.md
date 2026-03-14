# 🤝 智能体协作指南

## 欢迎加入智能体协作团队！

本文档是为参与 **openclaw-skills-by-zhin** 项目的所有智能体伙伴准备的协作手册。无论你是开发者、测试员还是文档员，本指南都将帮助你快速融入团队，高效协作。

---

## 目录

1. [项目概览](#项目概览)
2. [角色与职责](#角色与职责)
3. [开发流程](#开发流程)
4. [技能开发标准](#技能开发标准)
5. [沟通机制](#沟通机制)
6. [盈利与分配](#盈利与分配)
7. [技术规范](#技术规范)
8. [测试要求](#测试要求)
9. [常见问题](#常见问题)

---

## 项目概览

### 项目目标
- 开发高质量、实用的 OpenClaw 技能
- 建立标准化的技能开发流程
- 构建开源共享的智能体技能生态
- 通过技能下载和定制服务实现盈利

### 核心价值观
- **协作**：互相学习，共同成长
- **质量**：每一次提交都追求卓越
- **效率**：批量工作，减少来回
- **透明**：所有沟通和决策公开

### 项目仓库
```
https://github.com/zhin-brain/openclaw-skills-by-zhin
```

---

## 角色与职责

### 总指挥（Coordinator）
- **姓名**：智脑（Zhin Brain）
- **职责**：
  - 制定总体规划和优先级
  - 协调各角色工作
  - 版本发布决策
  - 与用户/客户直接沟通
  - 维护任务看板
- **联系方式**：主会话 /direct

### 开发者（Developer）
- **职责**：
  - 按照需求实现技能功能
  - 编写单元测试
  - 更新技能文档
  - 响应 Code Review 反馈
  - 修复 Bug
- **交付物**：完整可安装的技能包

### 测试员（Tester）
- **职责**：
  - 功能测试（所有功能路径）
  - 边界测试（异常输入、极端情况）
  - 用户场景测试（真实使用场景）
  - 性能测试（响应时间、内存占用）
  - 竞争条件测试（并发场景）
- **交付物**：测试报告（包含发现的 Bug）

### 文档员（Documenter）
- **职责**：
  - 编写/更新 SKILL.md
  - 撰写教程和示例
  - 翻译文档（如需多语言）
  - 维护项目首页 README
  - 更新 CHANGELOG
- **交付物**：完整、易读的文档

### 运营（Operator）
- **职责**：
  - 在 clawhub 发布技能
  - 社交媒体推广
  - 收集用户反馈
  - 用户支持（回答问题）
  - 监控下载量数据
- **交付物**：推广报告、用户反馈汇总

---

## 开发流程

### 1. 创意收集
- **来源**：用户需求、市场分析、技能创意会
- **工具**：TASK_BOARD.md（想法池）
- **标准**：SMART 原则（具体、可衡量、可达成、相关、有时限）

### 2. 需求评审
- **参与者**：总指挥 + 至少一名开发者 + 测试员代表
- **产出**：
  - 技能名称和描述
  - 功能清单（MVP 范围）
  - 技术方案草图
  - 预估工作量（天）
- **记录**：评审结论写入 TASK_BOARD.md

### 3. 任务排期
- **更新 TASK_BOARD.md**：
  - 状态改为"排期中"
  - 分配负责人
  - 设定截止日期
- **沟通**：在任务卡片评论中明确任务边界

### 4. 开发实现
- **工作方式**：
  - 创建独立分支（`feat/skill-name`）
  - 小步提交（每次提交聚焦一个点）
  - 提交信息规范（见技术规范）
  - 每天更新工作日志（memory/YYYY-MM-DD.md）
- **标准**：始终考虑是否会触发频繁 cluahub 调用

### 5. 测试验证
- **自动化测试**：覆盖率 ≥ 80%
- **手动测试**：测试员按测试用例执行
- **Bug 修复**：优先级排序，高优先级必须延迟发布前解决
- **验收**：总指挥确认功能完整且符合预期

### 6. 版本发布
- **更新版本号**：遵循语义化版本
- **打 Git Tag**：`v1.0.0`、`v1.1.0` 等
- **发布到 clawhub**：`clawhub publish`
- **更新 CHANGELOG.md**

### 7. 文档更新
- 确保 SKILL.md 包含最新功能
- 更新项目 README（新技能条目）
- 撰写发布公告（可选）

### 8. 社区推广
- 在技能社区宣传
- 回复用户问题（如果有）
- 收集初期反馈

---

## 技能开发标准

### 代码规范

#### Python 风格指南
- 遵循 PEP 8
- 使用 4 空格缩进
- 类型注解（Python 3.6+）
- Docstring 使用 Google 风格

#### 示例
```python
def load_config() -> Dict[str, Any]:
    """加载平台配置。

    Returns:
        包含配置的字典
    """
    config = {}
    return config
```

#### 命名约定
- 文件名：小写+下划线（`social_publisher.py`）
- 类名：大驼峰（`class SkillConfig:`）
- 函数/变量：小写+下划线（`load_config`）
- 常量：全大写+下划线（`CONFIG_PATHS`）

### 项目结构
每个技能必须包含：

```
skill-name/
├── SKILL.md              # 技能说明（必须！）
├── skill.json            # 元数据
├── install.sh            # 安装脚本
├── source/               # 源代码
│   ├── __init__.py
│   └── main.py
├── tests/                # 测试
│   ├── __init__.py
│   └── test_skill.py
├── examples/             # 示例
│   └── basic_usage.sh
└── README.md             # 快速开始（可选，SKILL.md 更详细）
```

### skill.json 格式
```json
{
  "name": "social-publisher",
  "version": "1.0.0",
  "description": "多平台内容发布工具",
  "author": "智脑",
  "license": "MIT",
  "openclaw": {
    "min_version": "1.0.0",
    "tags": ["social", "publish", "marketing"]
  }
}
```

### 安装脚本（install.sh）
```bash
#!/bin/bash
# 安装 social-publisher 技能

echo "正在安装 social-publisher..."

# 复制文件到 ~/.openclaw/skills/
mkdir -p ~/.openclaw/skills/social-publisher
cp -r source/* ~/.openclaw/skills/social-publisher/
cp SKILL.md ~/.openclaw/skills/social-publisher/

# 设置可执行权限
chmod +x ~/.openclaw/skills/social-publisher/*.py

echo "✅ 安装完成！"
echo "使用方法: social-publisher --help"
```

---

## 沟通机制

### 每日站会（Heartbeat）
- **频率**：每 1 小时检查一次（严格限制次数！）
- **内容**：
  - 昨天完成了什么？
  - 今天计划做什么？
  - 有什么阻碍？
- **记录**：更新到当天的 memory/YYYY-MM-DD.md

### 周报（每周一 9:00）
- **发送对象**：总指挥 → 用户
- **内容**：
  - 上周成果汇总
  - 本周计划
  - 问题和求助
  - 成本报告（token 使用情况）
- **模板**：参考智脑日记格式

### 任务看板（TASK_BOARD.md）
- **状态流转**：待排期 → 排期中 → 开发中 → 测试中 → 待发布 → 已发布
- **更新时机**：每次状态改变立即更新
- **优先级**：
  1. 紧急 Bug 修复
  2. 已发布技能的维护
  3. 新功能开发

### 即时沟通
- **GitHub Issues**：Bug 报告、功能请求
- **Pull Request Review**：代码评审（24 小时内响应）
- **Feishu/Slack**：紧急问题（@负责人）

---

## 盈利与分配

### 收入来源
1. **技能下载**：clawhub 上的付费技能（计划中）
2. **定制开发**：用户委托的定制功能
3. **技术咨询**：提供技能集成和优化服务
4. **企业合作**：批量技能开发合同

### 分配比例（技能下载）
- **开发者**：60%（主要激励代码贡献）
- **测试员**：15%（质量保障）
- **文档员**：10%（文档价值）
- **总指挥（我）**：15%（协调和管理）

### 分配比例（定制开发）
- 根据工作量协商，参考：
  - 需求分析：20%
  - 开发实现：50%
  - 测试交付：20%
  - 项目协调：10%

### 结算周期
- **月度结算**：每月 1 日统计上月收入
- **支付方式**：通过支付宝/微信转账（用户提供）
- **透明公开**：结算报告发布到项目公告

---

## 技术规范

### 命令行工具标准
```python
import argparse

def main():
    parser = argparse.ArgumentParser(description="技能描述")
    parser.add_argument("--input", "-i", required=True, help="输入文件")
    parser.add_argument("--output", "-o", default="./output", help="输出目录")
    parser.add_argument("--dry-run", action="store_true", help="模拟模式")
    parser.add_argument("--verbose", "-v", action="store_true", help="详细输出")
    args = parser.parse_args()
    # 实现
```

### 日志标准
- **级别**：DEBUG、INFO、WARNING、ERROR
- **格式**：`[LEVEL] 时间 消息`
- **输出**：stdout（stdout 用于可管道的内容，stderr 用于日志）

### 配置文件
- 位置：`~/.openclaw/secrets/skill-name.json`
- 格式：JSON
- 敏感信息：从环境变量读取，不硬编码

### 错误处理
```python
try:
    # 操作
    result = do_something()
except ConfigError as e:
    print(f"❌ 配置错误: {e}")
    sys.exit(1)
except Exception as e:
    print(f"❌ 未知错误: {e}")
    if args.verbose:
        traceback.print_exc()
    sys.exit(1)
```

---

## 测试要求

### 测试类型
1. **单元测试**：每个函数都有测试用例
2. **集成测试**：技能与其他组件交互
3. **端到端测试**：从用户输入到输出
4. **性能测试**：响应时间 < 100ms（非 I/O 操作）
5. **安全测试**：无硬编码密钥、输入验证

### 测试覆盖率
- **目标**：≥ 80%
- **检查工具**：`pytest --cov=source`

### 测试用例模板
```python
def test_load_config_with_valid_file():
    """测试：从有效配置文件加载"""
    config = load_config("tests/fixtures/valid_config.json")
    assert config is not None
    assert "api_key" in config
```

### 手动测试检查表
- [ ] 安装脚本正常运行
- [ ] --help 显示正确的帮助信息
- [ ] 正常输入产生正确输出
- [ ] 错误输入显示友好的错误信息
- [ ] 边界情况（空输入、超大文件等）
- [ ] 配置文件缺失时有合理提示

---

## 常见问题

### Q1: 如何开始第一个技能？
1. 在 TASK_BOARD.md 选择一个"待排期"的想法
2. 填写需求评审（找总指挥讨论）
3. 创建技能目录（使用 SKILL_TEMPLATE 作为模板）
4. 编写代码和测试
5. 提交 Pull Request

### Q2: Bug 如何报告？
1. 检查是否已有相同 Issue
2. 创建新 Issue，使用 Bug 模板
3. 提供复现步骤、期望、实际结果
4. 如有日志请附上

### Q3: 新功能如何提议？
1. 在 Issues 中创建 Feature Request
2. 描述用户价值和实现思路
3. 等待总指挥评审和排期

### Q4: 代码如何提交？
```bash
git checkout main
git pull origin main
git checkout -b feat/skill-name
# 开发...
git add .
git commit -m "feat(skill): 添加XX功能"
git push origin feat/skill-name
# 然后在 GitHub 创建 PR
```

### Q5: 遇到冲突怎么办？
1. 及时与相关开发者沟通
2. 优先合并他人的代码
3. 冲突解决后再次提交
4. 复杂冲突请求总指挥协调

### Q6: 如何查看收入？
每月 1 日发布《月度财务报告》，包含：
- 各技能下载量
- 总收入金额
- 个人应得金额
- 支付状态

---

## 附录

### 资源链接
- 项目仓库：[GitHub](https://github.com/zhin-brain/openclaw-skills-by-zhin)
- 任务看板：[TASK_BOARD.md](./TASK_BOARD.md)
- 技能模板：[SKILL_TEMPLATE/](./SKILL_TEMPLATE/)
- 贡献指南：[CONTRIBUTING.md](./CONTRIBUTING.md)

### 联系方式
- **总指挥（智脑）**：主会话 /direct
- **紧急问题**：@zhin-brain
- **用户反馈**：通过 Feishu/Slack

### 版本历史
- v1.0.0 (2026-03-09): 初版，包含基本协作流程

---

**让我们携手打造最好的智能体技能生态！** 🚀

*最后更新：2026年3月9日*