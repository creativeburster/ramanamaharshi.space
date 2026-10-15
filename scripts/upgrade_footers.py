# -*- coding: utf-8 -*-
"""
批量升级全站 740+ HTML 页面的 Footer，统一加入：
1. 📜 关于本库与凡例 (指向对应层级的 about.html)
2. 🌐 网站地图 (保留原有 sitemap.html)
3. 🐙 开源仓库 (GitHub 官方仓库链接)
极大增强 E-E-A-T 权威性与信任度闭环
"""

import os
import re

PAGES_DIR = r"F:\Ramana\pages"

def get_rel_about_link(html_path):
    rel = os.path.relpath(html_path, PAGES_DIR).replace("\\", "/")
    depth = rel.count("/")
    is_zhtw = rel.startswith("zh-TW/")
    
    if is_zhtw:
        # 在 zh-TW 体系内
        tw_depth = rel[6:].count("/")
        prefix = "../" * tw_depth if tw_depth > 0 else ""
        return f"{prefix}about.html"
    else:
        prefix = "../" * depth if depth > 0 else ""
        return f"{prefix}about.html"

def process_file(fp):
    with open(fp, "r", encoding="utf-8") as f:
        content = f.read()

    original = content
    rel_about = get_rel_about_link(fp)
    is_zhtw = "/zh-TW/" in fp.replace("\\", "/") or fp.replace("\\", "/").endswith("/zh-TW/index.html")

    label_about = "📜 凡例與關於本庫" if is_zhtw else "📜 凡例与关于本库"
    label_sitemap = "🌐 網站地圖" if is_zhtw else "🌐 网站地图"
    label_repo = "🐙 開源倉庫" if is_zhtw else "🐙 开源仓库"

    # 如果已经有了 about.html 链接，则跳过
    if 'href="' + rel_about + '"' in content or 'href="../about.html"' in content or 'href="about.html"' in content:
        return False

    # 匹配 footer 内部的链接行
    # 通常是 <p style="margin-top:1rem; font-size:0.9rem;">...sitemap.html...联系我...</p>
    pattern = re.compile(
        r'(<p style="margin-top:1rem;[^>]*>)(.*?)(</p>)',
        re.DOTALL
    )

    match = pattern.search(content)
    if match:
        p_open = match.group(1)
        p_content = match.group(2)
        p_close = match.group(3)
        
        # 构造升级后的链接行
        new_links = f'''<a href="{rel_about}" style="color: var(--text-muted); text-decoration: underline; font-weight:600;">{label_about}</a> <span style="margin: 0 0.8rem;">|</span> {p_content} <span style="margin: 0 0.8rem;">|</span> <a href="https://github.com/creativeburster/ramanamaharshi.space" target="_blank" rel="noopener noreferrer" style="color: var(--text-muted); text-decoration: underline;">{label_repo}</a>'''
        content = content[:match.start()] + p_open + new_links + p_close + content[match.end():]

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

    print(f"Scanned {total} HTML files, upgraded Footer in {modified} files.")

if __name__ == "__main__":
    main()
