# DuckDuckGo Search 技能

使用 DuckDuckGo 进行网页搜索，无需 API 密钥，无需额外依赖。

## 功能

- 网页搜索
- 获取搜索结果摘要
- 无需 API 密钥
- 无需额外 Python 依赖

## 使用方法

调用 `search.py` 脚本进行搜索：

```bash
python search.py "搜索关键词"
```

## 参数

- `query`: 搜索关键词（必需）
- `--limit`: 返回结果数量（默认：5）

## 示例

```bash
# 搜索网页
python search.py "人工智能"

# 搜索并限制结果数量
python search.py "Python 教程" --limit 10

# 搜索最新资讯
python search.py "科技新闻 2026" --limit 5
```

## 特点

- 隐私优先：DuckDuckGo 不追踪用户
- 免费使用：无需 API 密钥
- 轻量级：仅使用 Python 标准库

