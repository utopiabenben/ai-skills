# 📸 照片整理工具 - 技术方案规划

## 项目名称
暂命名：**photo-organizer**

## 功能需求
1. **读取照片元数据**：
   - 拍摄时间（EXIF 信息）
   - 拍摄地点（GPS 信息，如果有的话）
   - 照片尺寸、格式等

2. **批量打标签**：
   - 按时间标签（年、月、日）
   - 按地点标签（如果有 GPS 信息）
   - 支持自定义标签

3. **自动分类**：
   - 按时间文件夹（如 2026/03/）
   - 按地点文件夹（如果有 GPS）
   - 按事件分组（相似时间和地点的照片放在一起）

4. **用户交互**：
   - 预览模式（先看效果，再执行）
   - 支持撤销操作
   - 配置文件保存用户偏好

---

## 技术选型

### Python 库（推荐）
1. **Pillow**：读取 EXIF 信息
2. **exifread**：专门读取 EXIF 数据
3. **GPSPhoto**：处理 GPS 信息
4. **geopy**：GPS 坐标转地点名称（可选）
5. **click** 或 **argparse**：命令行界面

---

## 核心功能模块

### 1. EXIF 读取模块
```python
def get_exif_data(photo_path):
    """读取照片的 EXIF 信息"""
    pass

def get_capture_time(exif_data):
    """获取拍摄时间"""
    pass

def get_gps_info(exif_data):
    """获取 GPS 信息（如果有）"""
    pass
```

### 2. 文件整理模块
```python
def organize_by_date(photos, output_dir):
    """按时间整理照片"""
    pass

def organize_by_location(photos, output_dir):
    """按地点整理照片"""
    pass

def create_folder_structure(base_path, structure):
    """创建文件夹结构"""
    pass
```

### 3. 标签管理模块
```python
def add_tags(photo_path, tags):
    """给照片添加标签"""
    pass

def read_tags(photo_path):
    """读取照片标签"""
    pass
```

### 4. 用户交互模块
```python
def preview_changes(photos, plan):
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
# 按时间整理
photo-organizer organize ./photos --by date --output ./organized

# 按地点整理（如果有 GPS）
photo-organizer organize ./photos --by location --output ./organized

# 预览模式
photo-organizer organize ./photos --by date --preview

# 撤销操作
photo-organizer undo ./organized
```

### 配置文件
```json
{
  "output_dir": "./organized",
  "folder_structure": "{year}/{month}",
  "auto_tag": true,
  "backup_original": true
}
```

---

## 开发计划

### 第一阶段（MVP）
1. ✅ 项目初始化
2. EXIF 读取功能
3. 按时间整理功能
4. 基础命令行界面
5. 预览模式

### 第二阶段
1. GPS 读取和地点转换
2. 按地点整理功能
3. 标签功能
4. 配置文件

### 第三阶段
1. 人脸识别（可选）
2. 智能事件分组
3. GUI 界面（可选）

---

## 风险和挑战
1. **EXIF 信息缺失**：有些照片可能没有 EXIF 或 GPS 信息
2. **文件格式兼容性**：需要支持 JPG、PNG、HEIC 等常见格式
3. **大量文件处理**：需要优化性能，处理成千上万张照片
4. **用户错误操作**：需要良好的预览和撤销机制

---

## 参考资源
- Pillow 文档：https://pillow.readthedocs.io/
- ExifRead 文档：https://github.com/ianare/exifread
- 照片 EXIF 格式说明
