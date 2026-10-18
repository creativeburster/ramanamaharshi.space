"""
给不带 .html 的内部链接统一加斜杠
books/be-as-you-are → books/be-as-you-are/
books/index/ → 跳过（已有斜杠）
index → index/
"""
import re
import os

BASE = r'c:\Users\willp\WorkBuddy\20260410104230\pages'

# 匹配相对路径且不以 .html / 斜杠 结尾的链接
RE_LINK = re.compile(r'(href=["\'])(?!https?://|ftp://|//|#)([^\s"\'<>]+)(["\'])')

def transform_url(url):
    # 已有斜杠 或 已有扩展名 → 不改
    if url.endswith('/') or '.html' in url or '.' in url.split('/')[-1]:
        return url
    return url + '/'

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
changed_files = []
for root, dirs, files in os.walk(BASE):
    for fname in files:
        if fname.endswith('.html'):
            total += 1
            fpath = os.path.join(root, fname)
            if process_file(fpath):
                rel = os.path.relpath(fpath, BASE)
                changed_files.append(rel)
                changed += 1

for f in changed_files:
    print(f'  ✓ {f}')
print(f'\n完成：{changed}/{total} 个文件已修改')
