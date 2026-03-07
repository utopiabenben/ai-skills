# Doc Converter - 文档格式批量转换工具

一个简单但强大的文档格式批量转换工具，支持多种常用格式之间的转换！

## 功能特性
- ✅ 支持多种文档格式转换（PDF ↔ Word ↔ Excel ↔ PPT ↔ 图片）
- ✅ 批量转换整个文件夹
- ✅ 预览模式（先看效果再执行）
- ✅ 撤销操作（安全可靠）

## 安装

### 方法一：通过 clawhub 安装
```bash
clawhub install doc-converter
```

### 方法二：作为 Python 脚本运行
```bash
# 克隆或下载项目
git clone <repo-url>
cd doc-converter

# 安装依赖（需要实际转换功能时）
pip install pdf2docx docx2pdf pdf2image Pillow python-docx openpyxl python-pptx
```

## 依赖说明
当前版本是简化版，主要演示框架。要启用实际转换功能，请安装：
- `pdf2docx`：PDF 转 Word
- `docx2pdf`：Word 转 PDF
- `pdf2image`：PDF 转图片
- `Pillow`：图片处理
- `python-docx`：Word 文档处理
- `openpyxl`：Excel 表格处理
- `python-pptx`：PowerPoint 处理

## 快速开始

### 1. PDF 转 Word
```bash
python3 doc_converter.py convert document.pdf --to docx
```

### 2. Word 转 PDF
```bash
python3 doc_converter.py convert document.docx --to pdf
```

### 3. 图片转 PDF
```bash
python3 doc_converter.py convert photo.jpg photo.png --to pdf --output output.pdf
```

### 4. 批量转换
```bash
python3 doc_converter.py batch ./docs --from pdf --to docx --output ./converted
```

### 5. 预览模式（不实际执行，先看效果）
```bash
python3 doc_converter.py batch ./docs --from pdf --to docx --preview
```

### 6. 撤销操作
```bash
python3 doc_converter.py undo ./converted
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
| jpg, jpeg | JPEG 图片 |
| png | PNG 图片 |

## 示例场景

### 场景 1：批量 PDF 转 Word
```bash
# 将整个文件夹的 PDF 转为 Word
python3 doc_converter.py batch ./pdfs --from pdf --to docx --output ./docs
```

### 场景 2：图片合并成 PDF
```bash
# 将多张图片合并成一个 PDF
python3 doc_converter.py convert photo1.jpg photo2.jpg photo3.jpg --to pdf --output album.pdf
```

### 场景 3：先预览，再执行
```bash
# 第一步：预览
python3 doc_converter.py batch ./docs --from pdf --to docx --preview

# 第二步：确认没问题后执行
python3 doc_converter.py batch ./docs --from pdf --to docx --output ./converted
```

## 安全性
- 工具默认使用模拟转换（当前版本）
- 执行前会自动保存备份
- 支持一键撤销操作
- 建议先用 --preview 预览效果

## 故障排除

### 问题：找不到依赖库
**解决方法**：
```bash
pip install pdf2docx docx2pdf pdf2image Pillow python-docx openpyxl python-pptx
```

### 问题：撤销失败
**原因**：备份文件可能被删除或修改
**解决方法**：确保在同一目录下执行，且备份文件未被删除

## 开发计划
- [ ] 完善 PDF ↔ Word 实际转换功能
- [ ] 添加 Excel 相关转换
- [ ] 添加 PowerPoint 相关转换
- [ ] 添加 Markdown 相关转换
- [ ] 配置文件支持
- [ ] GUI 界面（可选）

## 贡献
欢迎提交 Issue 和 Pull Request！

## 许可证
MIT License

---

**Doc Converter** - 让文档格式转换变得简单！📄
