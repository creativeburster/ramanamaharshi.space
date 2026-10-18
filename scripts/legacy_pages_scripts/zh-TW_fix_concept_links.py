#!/usr/bin/env python3
import os
import re

def fix_concept_links(directory):
    """
    修复概念页面中多余的 concepts/ 前缀
    """
    total_fixed = 0
    files_updated = 0
    
    print(f'开始修复 {directory} 目录下的链接...\n')
    
    for filename in os.listdir(directory):
        if filename.endswith('.html') and filename != '_template.html':
            filepath = os.path.join(directory, filename)
            
            # 读取文件内容
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 修复侧边栏链接
            # 匹配 <a href="concepts/xxx.html" 模式
            pattern = r'<a href="concepts/([a-z-]+\.html)"'
            replaced = re.sub(pattern, r'<a href="\1"', content)
            
            # 修复相关概念链接
            # 匹配 <a href="concepts/xxx.html" 模式
            pattern2 = r'<a href="concepts/([a-z-]+\.html)"\s+class="tag"'
            replaced = re.sub(pattern2, r'<a href="\1" class="tag"', replaced)
            
            # 计算修复数量
            original_count = content.count('concepts/')
            fixed_count = original_count - replaced.count('concepts/')
            
            if fixed_count > 0:
                # 写入修复后的内容
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(replaced)
                
                print(f'{filename}: 修复了 {fixed_count} 个链接')
                total_fixed += fixed_count
                files_updated += 1
    
    print(f'\n修复完成！')
    print(f'共更新 {files_updated} 个文件')
    print(f'共修复 {total_fixed} 个链接')

if __name__ == '__main__':
    fix_concept_links('concepts')
