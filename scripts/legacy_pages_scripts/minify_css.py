#!/usr/bin/env python3
import re

def minify_css(css):
    # 移除注释
    css = re.sub(r'/\*[\s\S]*?\*/', '', css)
    # 移除多余空白
    css = re.sub(r'\s+', ' ', css)
    # 移除分号后的空格
    css = re.sub(r';\s*', ';', css)
    # 移除冒号后的空格
    css = re.sub(r':\s*', ':', css)
    # 移除逗号后的空格
    css = re.sub(r',\s*', ',', css)
    # 移除大括号前后的空格
    css = re.sub(r'\s*{\s*', '{', css)
    css = re.sub(r'\s*}\s*', '}', css)
    # 移除开头和结尾的空白
    css = css.strip()
    return css

# 读取原始 CSS
with open('styles.css', 'r', encoding='utf-8') as f:
    original = f.read()

# 压缩
minified = minify_css(original)

# 备份原始文件
with open('styles.css.bak', 'w', encoding='utf-8') as f:
    f.write(original)

# 写入压缩后的 CSS
with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(minified)

print(f'CSS 压缩完成！')
print(f'原始大小: {len(original):,} 字节')
print(f'压缩后大小: {len(minified):,} 字节')
print(f'节省: {len(original) - len(minified):,} 字节 ({(1 - len(minified)/len(original))*100:.1f}%)')
