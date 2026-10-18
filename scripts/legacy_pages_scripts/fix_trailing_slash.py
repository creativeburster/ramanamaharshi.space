"""
批量还原 .html 链接并改为斜杠结尾
- books/be-as-you-are → books/be-as-you-are/
- books/index/ → books/index/（已正确，跳过）
- index/ → index/（根目录特殊处理）
"""
import re
import os

BASE = r'c:\Users\willp\WorkBuddy\20260410104230\pages'

# 匹配相对路径的 .html 链接
RE_LINK = re.compile(r'(href=["\'])(?!https?://|ftp://|//)([^\s"\'<>]+\.html)(["\'])')

def transform_url(url):
    if url.endswith('.html'):
        url = url[:-5]  # 去掉 .html
    # index.html 变成 index/，其他变成 xxx/
    if not url.endswith('/'):
        url = url + '/'
    return url

def process_file(filepath):
    with open(filepath, encoding='utf-8') as f:
        content = f.read()

    def replacer(m):
        return m.group(1) + transform_url(m.group(2)) + m.group(3)

    new_content = RE_LINK.sub(replacer, content)
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

changed = 0
total = 0
for root, dirs, files in os.walk(BASE):
    for fname in files:
        if fname.endswith('.html'):
            total += 1
            fpath = os.path.join(root, fname)
            if process_file(fpath):
                rel = os.path.relpath(fpath, BASE)
                print(f'  ✓ {rel}')
                changed += 1

print(f'\n完成：{changed}/{total} 个文件已修改')
