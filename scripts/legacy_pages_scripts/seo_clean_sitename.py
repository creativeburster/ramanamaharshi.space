#!/usr/bin/env python3
"""
清理 title 和 og:title 中残留的 "- 拉玛那马哈希Space" 字符串
"""
import os
import re
import glob

PAGES_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_NAME = "拉玛那马哈希知识库"

def clean_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # 移除 title 和 og:title 中的 " - 拉玛那马哈希Space"
    def clean_value(v):
        v = re.sub(r'\s*-\s*拉玛那马哈希Space', '', v)
        v = re.sub(r'\s*拉玛那马哈希Space\s*\|?\s*', '', v)
        # 清理多余的 | 分隔符
        v = re.sub(r'\s*\|\s*\|\s*', ' | ', v)
        v = v.strip().strip('|').strip()
        return v

    def fix_title(m):
        inner = clean_value(m.group(1))
        if f'| {SITE_NAME}' not in inner and inner != SITE_NAME:
            inner = f'{inner} | {SITE_NAME}'
        return f'<title>{inner}</title>'

    def fix_og_title(m):
        inner = clean_value(m.group(1))
        if f'| {SITE_NAME}' not in inner and inner != SITE_NAME:
            inner = f'{inner} | {SITE_NAME}'
        return f'<meta property="og:title" content="{inner}">'

    content = re.sub(r'<title>(.*?)</title>', fix_title, content)
    content = re.sub(r'<meta property="og:title" content="(.*?)">', fix_og_title, content)
    
    # 同时修复 BreadcrumbList 中的 "拉玛那马哈希Space" → 正确名称
    content = content.replace('"拉玛那马哈希Space"', f'"{SITE_NAME}"')
    content = content.replace('"name": "拉玛那马哈希Space"', f'"name": "{SITE_NAME}"')
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    html_files = glob.glob(os.path.join(PAGES_DIR, '**', '*.html'), recursive=True)
    exclude = {'_template.html', 'sitemap.html'}
    
    fixed = 0
    for fp in sorted(html_files):
        if os.path.basename(fp) in exclude:
            continue
        if clean_file(fp):
            with open(fp, 'r', encoding='utf-8') as f:
                content = f.read()
            m = re.search(r'<title>(.*?)</title>', content)
            print(f'[CLEANED] {os.path.relpath(fp, PAGES_DIR)} → {m.group(1) if m else "?"}')
            fixed += 1
    
    print(f'\n完成: 清理 {fixed} 个文件')

if __name__ == '__main__':
    main()
