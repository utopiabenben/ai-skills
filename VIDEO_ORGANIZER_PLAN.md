# 🎬 视频文件批量重命名/整理工具 - 技术方案规划

## 项目名称
暂命名：**video-organizer**

## 功能需求
1. **自动识别视频文件**：
   - 支持常见格式：.mp4, .avi, .mov, .mkv, .flv, .wmv, .webm 等
   - 读取视频元数据（时长、分辨率、编码等，可选）

2. **批量整理**：
   - 按时间整理（文件修改时间或拍摄时间）
   - 按格式/扩展名整理
   - 按分辨率整理（720p, 1080p, 4K 等）

3. **批量重命名**：
   - 支持多种命名模式
   - 序号、日期、自定义前缀/后缀
   - 正则表达式支持

4. **用户交互**：
   - 预览模式（先看效果再执行）
   - 支持撤销操作
   - 配置文件保存用户偏好

---

## 技术选型

### Python 库
1. **pathlib**：Python 内置，处理文件路径
2. **mimetypes**：Python 内置，识别文件类型
3. **opencv-python**（可选）：读取视频元数据
4. **moviepy**（可选）：更高级的视频处理
5. **click** 或 **argparse**：命令行界面

---

## 核心功能模块

### 1. 视频文件识别模块
```python
def is_video_file(file_path):
    """判断是否是视频文件"""
    pass

def get_video_files(input_dir):
    """获取目录下所有视频文件"""
    pass
```

### 2. 视频元数据读取（可选）
```python
def get_video_metadata(file_path):
    """读取视频元数据（时长、分辨率等）"""
    pass

def get_resolution_category(resolution):
    """将分辨率分类（720p, 1080p, 4K 等）"""
    pass
```

### 3. 文件整理/重命名模块
```python
def organize_by_date(video_files, output_dir):
    """按时间整理视频"""
    pass

def organize_by_format(video_files, output_dir):
    """按格式整理视频"""
    pass

def organize_by_resolution(video_files, output_dir):
    """按分辨率整理视频（可选）"""
    pass

def batch_rename(video_files, pattern):
    """批量重命名视频"""
    pass
```

### 4. 用户交互模块
```python
def preview_changes(files, plan):
    """预览整理/重命名方案"""
    pass

def confirm_execution():
    """确认执行"""
    pass
```

---

## 命令行界面设计

### 基础用法
```bash
# 按时间整理视频
video-organizer organize ./videos --by date --output ./organized

# 按格式整理视频
video-organizer organize ./videos --by format --output ./organized

# 批量重命名视频
video-organizer rename ./videos --pattern "video_{001}.mp4"

# 预览模式
video-organizer organize ./videos --by date --preview

# 撤销操作
video-organizer undo ./organized
```

---

## 开发计划

### 第一阶段（MVP）
1. ✅ 项目初始化
2. 视频文件识别功能
3. 按时间/格式整理功能
4. 基础命令行界面
5. 预览模式

### 第二阶段
1. 批量重命名功能
2. 配置文件
3. 撤销操作
4. 按分辨率整理（可选）

### 第三阶段
1. 视频元数据读取
2. 更高级的整理/重命名规则
3. GUI 界面（可选）

---

## 风险和挑战
1. **视频元数据读取**：不同格式的元数据可能不一致
2. **大文件处理**：需要优化性能，处理大视频文件
3. **用户错误操作**：需要良好的预览和撤销机制

---

## 参考资源
- Python pathlib 文档
- OpenCV-Python 文档
- MoviePy 文档
