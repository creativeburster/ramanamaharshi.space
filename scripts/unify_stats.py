# -*- coding: utf-8 -*-
"""
统一全站统计口径为单一真相来源 (Single Source of Truth):
- 经典著作: 18
- 核心概念: 50+
- 精选问答: 800+
- 修行方法: 12
- 关键人物: 3
"""

import os
import re

PAGES_DIR = r"F:\Ramana\pages"

def process_file(fp):
    with open(fp, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    # 1. 替换侧边栏中的概念数字 39+ -> 50+
    content = re.sub(
        r'(核心概念\s*<span class="count">)39\+(</span>)',
        r'\g<1>50+\g<2>',
        content
    )

    # 2. 替换侧边栏中的问答数字 28 / 500+ / 800 -> 800+
    content = re.sub(
        r'(修行[问問]答\s*<span class="count">)(?:28|500\+|800)(</span>)',
        r'\g<1>800+\g<2>',
        content
    )

    # 3. 首页卡片中的 500+ 精选问答 -> 800+
    content = re.sub(
        r'(<div class="number">)500\+(</div>\s*<div class="label">精[选選][问問]答</div>)',
        r'\g<1>800+\g<2>',
        content
    )

    # 4. Meta 描述与 JSON-LD 中的 500+ 精选问答 / 500+问答 -> 800+精选问答
    content = content.replace("500+精选问答", "800+精选问答")
    content = content.replace("500+精選問答", "800+精選問答")
    content = content.replace("500+精选问答", "800+精选问答")
    content = content.replace("500+问答", "800+问答")
    content = content.replace("500+問答", "800+問答")

    if content != original:
        with open(fp, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False

def main():
    modified = 0
    total = 0
    for root, dirs, files in os.walk(PAGES_DIR):
        if '.git' in dirs:
            dirs.remove('.git')
        for f in files:
            if f.lower().endswith('.html'):
                total += 1
                fp = os.path.join(root, f)
                if process_file(fp):
                    modified += 1
    print(f"Scanned {total} HTML files, unified statistics in {modified} files.")

if __name__ == "__main__":
    main()
