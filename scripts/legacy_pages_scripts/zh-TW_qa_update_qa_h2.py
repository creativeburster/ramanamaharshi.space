#!/usr/bin/env python3
"""
批量更新QA文件，将<div class="qa-q">改为<h2 class="qa-q">
"""

import os
import re
from pathlib import Path

def update_qa_file(filepath):
    """更新单个QA文件"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 将 <div class="qa-q">...</div> 改为 <h2 class="qa-q">...</h2>
    # 注意：只改开始标签，结束标签在 qa-item 内部，需要特殊处理
    
    # 匹配 <div class="qa-q">内容</div> 中的 <div class="qa-q">
    pattern = r'<div class="qa-q">([^<]+)</div>'
    replacement = r'<h2 class="qa-q">\1</h2>'
    
    new_content = re.sub(pattern, replacement, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✓ 已更新: {filepath.name}")
        return True
    else:
        print(f"  无变化: {filepath.name}")
        return False

def main():
    qa_dir = Path(__file__).parent
    updated = 0
    
    for i in range(1, 40):  # qa-1.html 到 qa-39.html
        filepath = qa_dir / f"qa-{i}.html"
        if filepath.exists():
            if update_qa_file(filepath):
                updated += 1
        else:
            print(f"✗ 不存在: qa-{i}.html")
    
    print(f"\n总计更新: {updated} 个文件")

if __name__ == "__main__":
    main()
