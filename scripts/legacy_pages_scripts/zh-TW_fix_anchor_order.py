"""
修复锚点链接末尾斜杠：methods/index/#whoami/ → methods/index/#whoami
"""
import re, os

BASE = r'c:\Users\willp\WorkBuddy\20260410104230\pages'

# 匹配 href 中的 #anchor 在斜杠之前的情况: xxx/#anchor/
RE = re.compile(r'href=(["\'])([^"\']+/\#[^"\']+)/+(["\'])')

def fix(m):
    return f'href={m.group(1)}{m.group(2)}{m.group(3)}'

count = 0
for root, dirs, files in os.walk(BASE):
    for fname in files:
        if fname.endswith('.html'):
            fpath = os.path.join(root, fname)
            with open(fpath, encoding='utf-8') as f:
                c = f.read()
            new_c = RE.sub(fix, c)
            if new_c != c:
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(new_c)
                count += 1
                print(f'  ✓ {os.path.relpath(fpath, BASE)}')
print(f'\n修复了 {count} 个文件')
