#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量更新QA文件：将<h2 class="qa-q">改回<h3 class="qa-q">
"""

import os
import re
import glob

def update_qa_file(filepath):
    """更新单个QA文件"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 记录原始内容用于比较
    original = content
    
    # 替换 <h2 class="qa-q"> 为 <h3 class="qa-q">
    content = re.sub(r'<h2 class="qa-q">', '<h3 class="qa-q">', content)
    
    # 替换 </h2> 为 </h3>（只替换qa-q相关的）
    # 使用更精确的模式：在qa-q内容后的</h2>
    content = re.sub(r'(<h3 class="qa-q">[^<]+)</h2>', r'\1</h3>', content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    qa_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 获取所有qa文件
    qa_files = sorted(glob.glob(os.path.join(qa_dir, 'qa-*.html')))
    
    updated = 0
    for filepath in qa_files:
        filename = os.path.basename(filepath)
        if update_qa_file(filepath):
            print(f'✓ 已更新: {filename}')
            updated += 1
        else:
            print(f'  无需更新: {filename}')
    
    print(f'\n总计: {updated} 个文件已更新')

if __name__ == '__main__':
    main()
