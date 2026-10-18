#!/usr/bin/env python3
"""
修复章节页面的 title 标签 - 从页面内容提取真实标题
将 "1 | 拉玛那马哈希知识库" 改为 "第一章：我是谁？ - 走向静默 | 拉玛那马哈希知识库"
"""
import os
import re
import glob

PAGES_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_NAME = "拉玛那马哈希知识库"

def get_real_title(filepath):
    """从页面中提取真实标题，优先从topbar-title提取"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. 优先从 topbar-title 提取 (格式: "第一章：XXX - 书名")
    m = re.search(r'<span class="topbar-title">(.*?)</span>', content)
    if m:
        raw = m.group(1)
        # 去掉emoji图标
        title = re.sub(r'[\U00010000-\U0010ffff📖💬🧘🔗🙏💎📕📗📅👁️🔍📜⏳💭💝🍞📚]+\s*', '', raw).strip()
        if title:
            return title
    
    # 2. 从 breadcrumb 最后一项提取
    m = re.search(r'<span>([^<]+)</span>\s*</nav>', content)
    if m:
        title = m.group(1).strip()
        if title and len(title) > 2:
            return title
    
    # 3. 从 h1 提取
    m = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.DOTALL)
    if m:
        title = re.sub(r'<[^>]+>', '', m.group(1)).strip()
        if title and len(title) > 2:
            return title
    
    return None

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # 检查 title 是否是短数字格式 "N | 拉玛那马哈希知识库"
    m_title = re.search(r'<title>(.*?)</title>', content)
    if not m_title:
        return False
    
    current_title = m_title.group(1)
    # 只修复 "数字 | 知识库" 这类有问题的title
    if not re.match(r'^\d+\s*\|', current_title):
        return False
    
    real_title = get_real_title(filepath)
    if not real_title:
        return False
    
    new_title = f"{real_title} | {SITE_NAME}"
    
    # 修复 title 标签
    content = re.sub(r'<title>.*?</title>', f'<title>{new_title}</title>', content)
    # 修复 og:title
    content = re.sub(
        r'<meta property="og:title" content=".*?">',
        f'<meta property="og:title" content="{new_title}">',
        content
    )
    
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
        if fix_file(fp):
            with open(fp, 'r', encoding='utf-8') as f:
                content = f.read()
            m = re.search(r'<title>(.*?)</title>', content)
            print(f'[FIXED] {os.path.relpath(fp, PAGES_DIR)} → {m.group(1) if m else "?"}')
            fixed += 1
    
    print(f'\n完成: 修复 {fixed} 个章节页面')

if __name__ == '__main__':
    main()
