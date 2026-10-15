# -*- coding: utf-8 -*-
"""
批量为 pages/ 目录下所有 HTML 的外围导航、侧边栏、顶部栏、页脚添加 data-nosnippet 属性
避免搜索引擎爬虫（Googlebot）将导航控件文字与按钮误提取为正文摘要或大模型生成答案
"""

import os
import re

PAGES_DIR = r"F:\Ramana\pages"

def process_html_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    # 1. <aside class="sidebar" ...>
    content = re.sub(
        r'<aside\s+class="sidebar"([^>]*?)>',
        lambda m: f'<aside class="sidebar"{m.group(1)}>' if 'data-nosnippet' in m.group(0) else f'<aside class="sidebar" data-nosnippet{m.group(1)}>',
        content
    )

    # 2. <header class="topbar" ...>
    content = re.sub(
        r'<header\s+class="topbar"([^>]*?)>',
        lambda m: f'<header class="topbar"{m.group(1)}>' if 'data-nosnippet' in m.group(0) else f'<header class="topbar" data-nosnippet{m.group(1)}>',
        content
    )

    # 3. <button class="hamburger" ...>
    content = re.sub(
        r'<button\s+class="hamburger"([^>]*?)>',
        lambda m: f'<button class="hamburger"{m.group(1)}>' if 'data-nosnippet' in m.group(0) else f'<button class="hamburger" data-nosnippet{m.group(1)}>',
        content
    )

    # 4. <div class="page-nav" ...>
    content = re.sub(
        r'<div\s+class="page-nav"([^>]*?)>',
        lambda m: f'<div class="page-nav"{m.group(1)}>' if 'data-nosnippet' in m.group(0) else f'<div class="page-nav" data-nosnippet{m.group(1)}>',
        content
    )

    # 5. <footer class="site-footer" ...>
    content = re.sub(
        r'<footer\s+class="site-footer"([^>]*?)>',
        lambda m: f'<footer class="site-footer"{m.group(1)}>' if 'data-nosnippet' in m.group(0) else f'<footer class="site-footer" data-nosnippet{m.group(1)}>',
        content
    )

    if content != original:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False

def main():
    modified_count = 0
    total_count = 0
    for root, dirs, files in os.walk(PAGES_DIR):
        if '.git' in dirs:
            dirs.remove('.git')
        for f in files:
            if f.lower().endswith('.html'):
                total_count += 1
                fp = os.path.join(root, f)
                if process_html_file(fp):
                    modified_count += 1

    print(f"Scanned {total_count} HTML files, successfully injected data-nosnippet into {modified_count} files.")

if __name__ == "__main__":
    main()
