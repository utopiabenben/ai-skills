---
name: doc-converter
description: 文档格式批量转换工具，支持 PDF、Word、Excel、PowerPoint、图片等多种格式之间的批量转换，预览模式和撤销功能！
---

# Doc Converter - 文档格式批量转换工具

## 功能特性
- ✅ 支持多种文档格式转换（PDF ↔ Word ↔ Excel ↔ PPT ↔ 图片）
- ✅ 批量转换整个文件夹
- ✅ 预览模式（先看效果再执行）
- ✅ 撤销操作（安全可靠）

## 安装
```bash
# 方法一：通过 clawhub 安装
clawhub install doc-converter

# 方法二：作为 Python 脚本运行
git clone <repo-url>
cd doc-converter
pip install pdf2docx docx2pdf pdf2image Pillow python-docx openpyxl python-pptx
```

## 快速开始

### 1. PDF 转 Word
```bash
doc-converter convert document.pdf --to docx
```

### 2. Word 转 PDF
```bash
doc-converter convert document.docx --to pdf
```

### 3. 图片转 PDF
```bash
doc-converter convert photo.jpg photo.png --to pdf --output output.pdf
```

### 4. 批量转换
```bash
doc-converter batch ./docs --from pdf --to docx --output ./converted
```

### 5. 预览模式
```bash
doc-converter batch ./docs --from pdf --to docx --preview
```

### 6. 撤销操作
```bash
doc-converter undo ./converted
```

## 详细使用说明

### convert 命令参数
- `files`：（必需）要转换的文件
- `--to`：（必需）目标格式（pdf、docx、xlsx、pptx、jpg、png）
- `--output`：输出文件路径

### batch 命令参数
- `directory`：（必需）要转换的文件夹
- `--from`：（必需）源格式
- `--to`：（必需）目标格式
- `--output`：输出文件夹
- `--preview`：预览模式

### 支持的格式
| 格式 | 说明 |
|-----|------|
| pdf | PDF 文档 |
| docx | Word 文档 |
| xlsx | Excel 表格 |
| pptx | PowerPoint 演示 |
| jpg, png | 图片 |

## 示例场景

### 场景 1：批量 PDF 转 Word
```bash
doc-converter batch ./pdfs --from pdf --to docx --output ./docs
```

### 场景 2：图片合并成 PDF
```bash
doc-converter convert photo1.jpg photo2.jpg photo3.jpg --to pdf --output album.pdf
```

### 场景 3：先预览，再执行
```bash
# 第一步：预览
doc-converter batch ./docs --from pdf --to docx --preview

# 第二步：确认没问题后执行
doc-converter batch ./docs --from pdf --to docx --output ./converted
```

## 注意事项
- 确保已安装所需的依赖库
- 复杂格式的转换可能效果不理想
- 建议先用 --preview 预览效果
- 转换前建议先备份原文件

## 更新日志
### v1.0.0 (2026-03-06)
- 初始版本发布
- 支持 PDF ↔ Word 转换
- 支持图片 ↔ PDF 转换
- 支持批量转换
- 支持预览模式
- 支持撤销操作
