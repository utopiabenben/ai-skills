
# 📂 文件智能分类工具 - 技术方案规划

## 项目名称
暂命名：**file-sorter**

## 功能需求
1. **多种分类规则**：
   - 按文件类型分类（支持自定义类型）
   - 按文件大小分类（大文件、小文件、中等文件）
   - 按文件日期分类（创建日期、修改日期）
   - 按关键词分类（文件名或内容中的关键词）
   - 组合规则（同时满足多个条件）

2. **灵活的操作**：
   - 移动文件到对应文件夹
   - 复制文件到对应文件夹
   - 创建符号链接
   - 支持自定义文件夹结构

3. **用户交互**：
   - 预览模式（先看效果再执行）
   - 支持撤销操作
   - 配置文件保存用户偏好
   - 保存/加载分类规则预设

---

## 技术选型

### Python 库
1. **pathlib**：Python 内置，处理文件路径
2. **mimetypes**：Python 内置，识别文件类型
3. **datetime**：Python 内置，处理日期
4. **click**：命令行界面
5. **json**：Python 内置，保存配置和规则
6. **shutil**：Python 内置，文件操作

---

## 核心功能模块

### 1. 文件类型识别模块
```python
def get_file_type(file_path):
    """根据扩展名识别文件类型"""
    pass

def get_file_category(file_type, custom_categories=None):
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

DEFAULT_SIZE_RULES = {
    "small": (0, 1024 * 1024),  # 小于 1MB
    "medium": (1024 * 1024, 100 * 1024 * 1024),  # 1MB - 100MB
    "large": (100 * 1024 * 1024, None),  # 大于 100MB
}
```

### 3. 分类规则引擎
```python
def match_rule(file_path, rule):
    """检查文件是否匹配规则"""
    pass

def apply_rules(file_path, rules):
    """应用规则返回目标文件夹"""
    pass
```

### 4. 文件操作模块
```python
def organize_files(input_dir, rules, action="move", output_dir=None):
    """整理文件"""
    pass

def create_folder_structure(base_path, folder_names):
    """创建文件夹结构"""
    pass

def backup_operation(operation_log):
    """保存操作日志用于撤销"""
    pass
```

### 5. 用户交互模块
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
# 按类型整理
file-sorter organize ~/Downloads --by-type --output ~/Sorted

# 按大小整理
file-sorter organize ~/Downloads --by-size --output ~/Sorted

# 按日期整理（按修改日期）
file-sorter organize ~/Downloads --by-date modified --output ~/Sorted

# 预览模式
file-sorter organize ~/Downloads --by-type --preview

# 撤销操作
file-sorter undo ~/Sorted

# 保存/加载规则
file-sorter save-rules my_rules.json
file-sorter load-rules my_rules.json organize ~/Downloads
```

### 配置文件
```json
{
  "output_dir": "~/Sorted",
  "action": "move",
  "categories": {
    "documents": [".pdf", ".doc"],
    "images": [".jpg", ".png"]
  },
  "size_rules": {
    "small": [0, 1048576],
    "medium": [1048576, 104857600],
    "large": [104857600, null]
  },
  "backup_original": true
}
```

---

## 开发计划

### 第一阶段（MVP）
1. 项目初始化
2. 按文件类型分类功能
3. 基础命令行界面
4. 预览模式
5. 移动/复制操作

### 第二阶段
1. 按文件大小分类
2. 按文件日期分类
3. 自定义分类规则
4. 配置文件
5. 撤销操作

### 第三阶段
1. 按关键词分类
2. 组合规则
3. 规则预设保存/加载
4. 更智能的文件识别（内容识别）
5. GUI 界面（可选）

---

风险和挑战
1. **规则冲突：多个规则同时匹配时的处理逻辑
2. **大量文件处理：需要优化性能，处理成千上万的文件
3. **用户错误操作：需要良好的预览和撤销机制
4. **跨平台兼容性：确保在 Windows/macOS/Linux 上都能正常工作

---

## 参考资源
- Python mimetypes 文档
- Python pathlib 文档
- Python click 文档
