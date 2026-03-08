# 📥 下载文件自动分类工具 - 技术方案规划

## 项目名称
暂命名：**download-organizer**

## 功能需求
1. **自动识别文件类型**：
   - 文档类（.pdf, .doc, .docx, .txt, .xls, .xlsx, .ppt, .pptx 等）
   - 图片类（.jpg, .jpeg, .png, .gif, .webp, .heic 等）
   - 视频类（.mp4, .avi, .mov, .mkv 等）
   - 音频类（.mp3, .wav, .flac, .aac 等）
   - 安装包类（.exe, .msi, .dmg, .pkg, .deb, .rpm 等）
   - 压缩包类（.zip, .rar, .7z, .tar, .gz 等）
   - 代码类（.py, .js, .html, .css, .java, .cpp 等）
   - 其他类

2. **自动分类**：
   - 按文件类型自动创建文件夹
   - 移动文件到对应文件夹
   - 支持自定义分类规则

3. **用户交互**：
   - 预览模式（先看效果再执行）
   - 支持撤销操作
   - 配置文件保存用户偏好

---

## 技术选型

### Python 库
1. **pathlib**：Python 内置，处理文件路径
2. **mimetypes**：Python 内置，识别文件类型
3. **python-magic**（可选）：更强大的文件类型识别
4. **click** 或 **argparse**：命令行界面

---

## 核心功能模块

### 1. 文件类型识别模块
```python
def get_file_type(file_path):
    """根据扩展名识别文件类型"""
    pass

def get_file_category(file_type):
    """将文件类型归类到文件夹"""
    pass
```

### 2. 默认分类规则
```python
DEFAULT_CATEGORIES = {
    "documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".heic"],
    "videos": [".mp4", ".avi", ".mov", ".mkv"],
    "audio": [".mp3", ".wav", ".flac", ".aac"],
    "installers": [".exe", ".msi", ".dmg", ".pkg", ".deb", ".rpm"],
    "archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "code": [".py", ".js", ".html", ".css", ".java", ".cpp"],
}
```

### 3. 文件整理模块
```python
def organize_files(input_dir, output_dir, categories=None):
    """整理下载文件"""
    pass

def create_folder_structure(base_path, categories):
    """创建文件夹结构"""
    pass
```

### 4. 用户交互模块
```python
def preview_changes(files, plan):
    """预览整理方案"""
    pass

def confirm_execution():
    """确认执行"""
    pass
```

---

## 命令行界面设计

### 基础用法
```bash
# 整理下载文件夹
download-organizer organize ~/Downloads --output ~/Downloads/Organized

# 预览模式
download-organizer organize ~/Downloads --preview

# 撤销操作
download-organizer undo ~/Downloads/Organized
```

### 配置文件
```json
{
  "output_dir": "~/Downloads/Organized",
  "categories": {
    "documents": [".pdf", ".doc"],
    "images": [".jpg", ".png"]
  },
  "backup_original": true
}
```

---

## 开发计划

### 第一阶段（MVP）
1. ✅ 项目初始化
2. 文件类型识别功能
3. 按默认规则整理功能
4. 基础命令行界面
5. 预览模式

### 第二阶段
1. 自定义分类规则
2. 配置文件
3. 撤销操作

### 第三阶段
1. 更智能的文件识别（内容识别）
2. GUI 界面（可选）
3. 自动监控下载文件夹，新文件自动整理

---

风险和挑战
1. **文件类型误判：有些文件扩展名可能不准确
2. **大量文件处理：需要优化性能，处理成千上万的文件
3. **用户错误操作：需要良好的预览和撤销机制

---

## 参考资源
- Python mimetypes 文档
- Python pathlib 文档
