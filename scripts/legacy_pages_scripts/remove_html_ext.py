"""
批量移除 HTML 文件中的 .html 扩展名
- books/index.html → books/
- books/be-as-you-are.html → books/be-as-you-are
- 仅处理内部链接，不改外部 URL
"""
import re
import os

BASE = r'c:\Users\willp\WorkBuddy\20260410104230\pages'

# 正则：匹配 href="xxx.html" 或 href='xxx.html'
HTML_LINK_RE = re.compile(r'(href=["\'])([^\"\']+\.html)(["\'])')

def clean_url(url):
    """将 xxx.html 转换为干净 URL"""
    # 末尾的 .html 去掉
    if url.endswith('.html'):
        url = url[:-5]
    # index.html → 转为目录，末尾加 /
    if url.endswith('/index'):
        url = url + '/'
    return url

# 正则：仅匹配相对路径的 .html 链接，排除 http/https/ftp 等绝对URL
REL_HTML_RE = re.compile(r'(href=["\'])(?!https?://|ftp://|//)([^\"\']+\.html)(["\'])')

def process_file(filepath):
    with open(filepath, encoding='utf-8') as f:
        content = f.read()

    # 替换
    def replacer(m):
        prefix = m.group(1)
        url = m.group(2)
        suffix = m.group(3)
        return prefix + clean_url(url) + suffix

    new_content = REL_HTML_RE.sub(replacer, content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

# 扫描所有 .html 文件
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
