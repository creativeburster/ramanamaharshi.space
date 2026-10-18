"""
修复带锚点的 .html 链接
如: methods/index.html#whoami → methods/index/#whoami
"""
import re

BASE = r'c:\Users\willp\WorkBuddy\20260410104230\pages'

# 匹配带锚点的 .html 链接: xxx.html#anchor
RE_ANCHOR = re.compile(r'(href=["\'])(?!https?://)([^"\']+\.html)(#[^\"\']*)?(["\'])')

def clean_url(url_and_anchor):
    url = url_and_anchor.group(2)
    anchor = url_and_anchor.group(3) or ''
    if url.endswith('.html'):
        url = url[:-5]
    if url.endswith('/index'):
        url = url + '/'
    return url_and_anchor.group(1) + url + anchor + url_and_anchor.group(4)

count = 0
for root, dirs, files in __import__('os').walk(BASE):
    for fname in files:
        if fname.endswith('.html'):
            fpath = __import__('os').path.join(root, fname)
            with open(fpath, encoding='utf-8') as f:
                c = f.read()
            new_c = RE_ANCHOR.sub(clean_url, c)
            if new_c != c:
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(new_c)
                count += 1

print(f'修复了 {count} 个文件中的带锚点 .html 链接')
