# 🎵 音乐文件批量标签工具 - 技术方案规划

## 项目名称
暂命名：**music-tagger**

## 功能需求
1. **自动识别音乐文件**：
   - 支持常见格式：.mp3, .flac, .wav, .aac, .m4a, .ogg, .wma, .ape 等

2. **读取/编辑音乐元数据**：
   - 歌名（Title）
   - 艺术家（Artist）
   - 专辑（Album）
   - 流派（Genre）
   - 年份（Year）
   - 曲目号（Track Number）
   - 专辑封面（Album Art）

3. **批量编辑标签**：
   - 批量设置相同字段
   - 从文件名提取标签信息
   - 正则表达式替换
   - 从在线数据库获取标签（可选，未来版本）

4. **按标签整理音乐**：
   - 按艺术家/专辑整理到文件夹
   - 按流派整理
   - 按年份整理

5. **用户交互**：
   - 预览模式（先看效果再执行）
   - 支持撤销操作
   - 配置文件保存用户偏好

---

## 技术选型

### Python 库
1. **mutagen**：处理音乐元数据（支持 MP3, FLAC, MP4, OGG 等）
2. **pathlib**：Python 内置，处理文件路径
3. **click** 或 **argparse**：命令行界面

---

## 核心功能模块

### 1. 音乐文件识别模块
```python
def is_music_file(file_path):
    """判断是否是音乐文件"""
    pass

def get_music_files(input_dir):
    """获取目录下所有音乐文件"""
    pass
```

### 2. 音乐元数据模块
```python
def read_tags(file_path):
    """读取音乐文件标签"""
    pass

def write_tags(file_path, tags):
    """写入音乐文件标签"""
    pass

def get_supported_formats():
    """获取支持的音乐格式列表"""
    pass
```

### 3. 批量编辑模块
```python
def batch_set_tag(music_files, tag_name, tag_value):
    """批量设置相同标签"""
    pass

def extract_tags_from_filename(music_files, pattern):
    """从文件名提取标签信息"""
    pass

def regex_replace_tags(music_files, tag_name, pattern, replacement):
    """正则表达式替换标签"""
    pass
```

### 4. 文件整理模块
```python
def organize_by_artist_album(music_files, output_dir):
    """按艺术家/专辑整理音乐"""
    pass

def organize_by_genre(music_files, output_dir):
    """按流派整理音乐"""
    pass

def organize_by_year(music_files, output_dir):
    """按年份整理音乐"""
    pass
```

### 5. 用户交互模块
```python
def preview_changes(files, plan):
    """预览编辑/整理方案"""
    pass

def confirm_execution():
    """确认执行"""
    pass
```

---

## 命令行界面设计

### 基础用法
```bash
# 读取音乐文件标签
music-tagger read song.mp3

# 编辑音乐文件标签
music-tagger edit song.mp3 --title "My Song" --artist "My Artist"

# 批量设置标签
music-tagger batch ./music --artist "My Artist"

# 按艺术家/专辑整理
music-tagger organize ./music --by artist-album --output ./organized

# 预览模式
music-tagger organize ./music --by artist-album --preview

# 撤销操作
music-tagger undo ./organized
```

---

## 开发计划

### 第一阶段（MVP）
1. ✅ 项目初始化
2. 音乐文件识别功能
3. 读取/编辑基本标签（歌名、艺术家、专辑）
4. 基础命令行界面
5. 预览模式

### 第二阶段
1. 批量编辑功能
2. 按标签整理功能
3. 配置文件
4. 撤销操作

### 第三阶段
1. 从文件名提取标签
2. 正则表达式替换
3. 专辑封面处理
4. GUI 界面（可选）

---

## 风险和挑战
1. **元数据格式兼容性**：不同格式的元数据存储方式不同
2. **元数据丢失风险**：编辑标签时可能丢失现有数据
3. **大文件处理**：需要优化性能，处理大量音乐文件
4. **用户错误操作**：需要良好的预览和撤销机制

---

## 参考资源
- Mutagen 文档：https://mutagen.readthedocs.io/
- 音乐元数据格式说明（ID3, Vorbis Comments, etc.）
