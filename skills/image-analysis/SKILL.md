# Image Analysis 技能

图片分析与 OCR（光学字符识别）技能，用于识别图片中的文字和内容。

## 功能

- 图片文字识别（OCR）
- 支持多种图片格式（JPG, PNG, etc.）
- 提取图片中的文本内容

## 使用方法

调用 `analyze.py` 脚本进行图片分析：

```bash
python analyze.py /path/to/image.jpg
```

## 参数

- `image_path`: 图片文件路径（必需）
- `--output`: 输出文件路径（可选）

## 示例

```bash
# 分析图片并提取文字
python analyze.py ~/Downloads/receipt.jpg

# 分析截图
python analyze.py screenshot.png
```

## 依赖

- 使用 Python 标准库或轻量级 OCR 方案
