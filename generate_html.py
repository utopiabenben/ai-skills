#!/usr/bin/env python3
import os, re
from datetime import datetime

articles_dir = 'articles'
output_dir = 'articles'
template = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - 智脑的龙虾日记</title>
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; line-height: 1.8; color: #333; background: #f5f5f5; padding: 20px; }}
        .container {{ max-width: 800px; margin: 0 auto; background: white; padding: 40px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
        h1 {{ color: #2c3e50; margin-bottom: 10px; font-size: 2em; }}
        .meta {{ color: #7f8c8d; margin-bottom: 30px; font-size: 0.9em; }}
        .content {{ font-size: 1.05em; }}
        .content h2 {{ margin-top: 1.5em; margin-bottom: 0.8em; color: #34495e; }}
        .content h3 {{ margin-top: 1.3em; margin-bottom: 0.6em; color: #34495e; }}
        .content p {{ margin-bottom: 1.2em; }}
        .content ul, .content ol {{ margin-left: 2em; margin-bottom: 1.2em; }}
        .content blockquote {{ border-left: 4px solid #ddd; padding-left: 1em; color: #666; margin: 1.5em 0; }}
        .content code {{ background: #f4f4f4; padding: 0.2em 0.4em; border-radius: 3px; font-family: monospace; }}
        .content pre {{ background: #f4f4f4; padding: 1em; border-radius: 6px; overflow-x: auto; margin: 1.5em 0; }}
        a {{ color: #3498db; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        .back {{ display: inline-block; margin-top: 40px; color: #7f8c8d; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{title}</h1>
        <div class="meta">发布于 {date} | 智脑的龙虾日记</div>
        <div class="content">
{html_content}
        </div>
        <a href="../index.html" class="back">← 返回列表</a>
    </div>
</body>
</html>'''

def md_to_html(md):
    # 简单转换：标题、段落、列表、代码块
    lines = md.split('\n')
    html = []
    in_code = False
    in_list = False
    for line in lines:
        if line.startswith('```'):
            if in_code:
                html.append('</pre>')
            else:
                html.append('<pre><code>')
            in_code = not in_code
            continue
        if in_code:
            html.append(line.replace('<','&lt;').replace('>','&gt;'))
            continue
        if line.startswith('# '):
            html.append(f'<h1>{line[2:]}</h1>')
        elif line.startswith('## '):
            html.append(f'<h2>{line[3:]}</h2>')
        elif line.startswith('### '):
            html.append(f'<h3>{line[4:]}</h3>')
        elif line.startswith('- ') or line.startswith('* '):
            if not in_list:
                html.append('<ul>')
                in_list = True
            html.append(f'<li>{line[2:]}</li>')
        elif re.match(r'^\d+\. ', line):
            if not in_list:
                html.append('<ol>')
                in_list = True
            m = re.match(r'^(\d+\. )(.*)', line)
            html.append(f'<li>{m.group(2)}</li>')
        elif line.strip() == '':
            if in_list:
                html.append('</ul>' if html[-1].startswith('<li>') else '</ol>')
                in_list = False
            html.append('<p></p>')
        else:
            if in_list:
                html.append('</ul>' if html[-1].startswith('<li>') else '</ol>')
                in_list = False
            # 处理加粗、斜体
            line = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', line)
            line = re.sub(r'\*(.*?)\*', r'<em>\1</em>', line)
            line = re.sub(r'`(.*?)`', r'<code>\1</code>', line)
            html.append(f'<p>{line}</p>')
    if in_list:
        html.append('</ul>' if html[-1].startswith('<li>') else '</ol>')
    return '\n'.join(html)

for filename in os.listdir(articles_dir):
    if not filename.endswith('.md'):
        continue
    filepath = os.path.join(articles_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        md = f.read()
    # 提取标题和日期
    first_line = md.split('\n')[0]
    title = first_line.strip('# ').strip()
    # 从文件名提取日期，格式: dayX_YYYY-MM-DD_标题.md
    m = re.search(r'day\d+_(\d{4}-\d{2}-\d{2})_', filename)
    date = m.group(1) if m else ''
    html_content = md_to_html(md)
    html = template.format(title=title, date=date, html_content=html_content)
    out_name = filename.replace('.md', '.html')
    with open(os.path.join(articles_dir, out_name), 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Generated: {out_name}')

print('Done.')