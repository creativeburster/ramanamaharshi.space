#!/usr/bin/env python3
"""
SEO修复脚本 - 批量修复:
1. title 格式: "内容 — Space" → "内容 | 拉玛那马哈希知识库"
2. og:title 同步修复
3. og:site_name: "拉玛那马哈希Space" → "拉玛那马哈希知识库"
4. 首页 canonical: /index → /
5. 首页 og:url: /index → /
6. 首页 title: "Space —" → "拉玛那马哈希知识库 | 灵性教示完整指南"
"""
import os
import re
import glob

PAGES_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_NAME = "拉玛那马哈希知识库"
BASE_URL = "https://ramanamaharshi.space"

def fix_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    changed = False

    # 1. 修复 og:site_name
    content = re.sub(
        r'<meta property="og:site_name" content="拉玛那马哈希Space">',
        f'<meta property="og:site_name" content="{SITE_NAME}">',
        content
    )

    # 2. 修复 title 格式
    # 模式1: "内容 — Space" → "内容 | 拉玛那马哈希知识库"
    def fix_title_tag(m):
        inner = m.group(1)
        if inner == 'Space —':
            # 首页特殊处理
            return f'<title>拉玛那马哈希知识库 | 灵性教示完整指南</title>'
        # "某内容 — Space" → "某内容 | 拉玛那马哈希知识库"
        inner = re.sub(r'\s*—\s*Space$', '', inner)
        inner = re.sub(r'^Space\s*—\s*', '', inner)
        if inner and inner != SITE_NAME:
            return f'<title>{inner} | {SITE_NAME}</title>'
        return f'<title>{SITE_NAME}</title>'

    content = re.sub(r'<title>(.*?)</title>', fix_title_tag, content)

    # 3. 修复 og:title
    def fix_og_title(m):
        inner = m.group(1)
        if inner == 'Space —':
            return f'<meta property="og:title" content="拉玛那马哈希知识库 | 灵性教示完整指南">'
        inner = re.sub(r'\s*—\s*Space$', '', inner)
        inner = re.sub(r'^Space\s*—\s*', '', inner)
        if inner and inner != SITE_NAME:
            return f'<meta property="og:title" content="{inner} | {SITE_NAME}">'
        return f'<meta property="og:title" content="{SITE_NAME}">'

    content = re.sub(
        r'<meta property="og:title" content="(.*?)">',
        fix_og_title,
        content
    )

    # 4. 首页 canonical: /index → /
    if os.path.basename(filepath) == 'index.html' and os.path.dirname(filepath) == PAGES_DIR:
        content = re.sub(
            r'<link rel="canonical" href="https://ramanamaharshi\.space/index">',
            '<link rel="canonical" href="https://ramanamaharshi.space/">',
            content
        )
        content = re.sub(
            r'<meta property="og:url" content="https://ramanamaharshi\.space/index">',
            '<meta property="og:url" content="https://ramanamaharshi.space/">',
            content
        )

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        changed = True

    return changed

def main():
    html_files = glob.glob(os.path.join(PAGES_DIR, '**', '*.html'), recursive=True)
    # 排除模板和辅助文件
    exclude = {'_template.html', 'sitemap.html'}
    
    fixed = 0
    skipped = 0
    for fp in sorted(html_files):
        if os.path.basename(fp) in exclude:
            continue
        if fix_html_file(fp):
            print(f'[FIXED] {os.path.relpath(fp, PAGES_DIR)}')
            fixed += 1
        else:
            skipped += 1

    print(f'\n完成: 修复 {fixed} 个文件, {skipped} 个无需修改')

if __name__ == '__main__':
    main()
