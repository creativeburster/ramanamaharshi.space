"""恢复 HTML 文件中的 .html 扩展名"""
import re, os, glob

BASE = r'c:\Users\willp\WorkBuddy\20260410104230\pages'
REL_LINK_RE = re.compile(r'(href=["\'])(?!https?://|ftp://|//|#)([^\"\']+)(["\'])')

def restore_html_ext(url):
    if '.' in (url.split('/')[-1] if '/' in url else url):
        return url
    if url.startswith('#') or not url:
        return url
    return url.rstrip('/') + '.html'

def process_file(filepath):
    with open(filepath, encoding='utf-8') as f:
        content = f.read()
    original = content
    def replace_link(m):
        return m.group(1) + restore_html_ext(m.group(2)) + m.group(3)
    content = REL_LINK_RE.sub(replace_link, content)
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return 1
    return 0

html_files = [f for f in glob.glob(os.path.join(BASE, '**/*.html'), recursive=True) if 'node_modules' not in f]
changed = sum(process_file(f) for f in html_files)
print(f'完成：{changed}/{len(html_files)} 个文件已修改')
