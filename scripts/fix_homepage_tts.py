# -*- coding: utf-8 -*-
import re
from pathlib import Path

# 1. 完善 pages/audio-reader.js 与 pages/zh-TW/audio-reader.js
should_enable_func = """        shouldEnableTTS() {
            if (!this.supported) return false;
            if (document.body && (document.body.hasAttribute('data-no-tts') || document.body.classList.contains('no-tts'))) return false;
            const loc = window.location;
            if (loc && loc.pathname) {
                const path = loc.pathname.toLowerCase().replace(/\\/index\\.html$/, '/');
                if (path === '/' || path === '' || path === '/zh-tw/' || path === '/zh-tw') return false;
                const hubPaths = ['/books/', '/concepts/', '/methods/', '/qa/', '/persons/', '/sitemap.html', '/graph.html', '/zh-tw/books/', '/zh-tw/concepts/', '/zh-tw/methods/', '/zh-tw/qa/', '/zh-tw/persons/', '/zh-tw/sitemap.html', '/zh-tw/graph.html'];
                if (hubPaths.some(hp => path.endsWith(hp) || path === hp)) return false;
                if (loc.pathname.toLowerCase().endsWith('index.html')) return false;
            }
            if (document.querySelector('.stats-grid') || document.querySelector('.books-grid') || document.querySelector('.category-grid') || document.querySelector('.topic-hub-matrix') || document.querySelector('.graph-container') || document.querySelector('.sitemap-tree')) return false;
            const topbarTitle = document.querySelector('.topbar-title');
            if (topbarTitle && (topbarTitle.textContent.includes('首页') || topbarTitle.textContent.includes('首頁'))) return false;
            this.container = document.querySelector('.content-wrapper');
            if (!this.container) return false;
            return true;
        }

        init() {
            if (!this.shouldEnableTTS()) return;
"""

for ar_file in ['pages/audio-reader.js', 'pages/zh-TW/audio-reader.js']:
    p = Path(ar_file)
    c = p.read_text(encoding='utf-8')
    if 'shouldEnableTTS' not in c:
        c = re.sub(r'init\(\)\s*\{[\s\S]*?this\.container\s*=\s*document\.querySelector\(\'\.content-wrapper\'\);[\s\S]*?if\s*\(!this\.container\)\s*return;', should_enable_func, c, count=1)
        p.write_text(c, encoding='utf-8')
        print(f"Updated {ar_file}")
    else:
        print(f"Already updated {ar_file}")

# 2. 为首页及总览页面加上 data-no-tts="true"
for idx_file in ['pages/index.html', 'pages/zh-TW/index.html', 'pages/books/index.html', 'pages/zh-TW/books/index.html', 'pages/concepts/index.html', 'pages/zh-TW/concepts/index.html', 'pages/methods/index.html', 'pages/zh-TW/methods/index.html', 'pages/qa/index.html', 'pages/zh-TW/qa/index.html', 'pages/persons/index.html', 'pages/zh-TW/persons/index.html']:
    fp = Path(idx_file)
    if fp.exists():
        text = fp.read_text(encoding='utf-8')
        if 'data-no-tts' not in text:
            text = text.replace('<body>', '<body data-no-tts="true">')
            fp.write_text(text, encoding='utf-8')
            print(f"Added data-no-tts to {idx_file}")

# 3. 重新压缩生成 bundle.min.js
def minify_js(js_path):
    with open(js_path, 'r', encoding='utf-8') as f:
        c = f.read()
    c = re.sub(r'//[^\n]*', '', c)
    c = re.sub(r'/\*.*?\*/', '', c, flags=re.DOTALL)
    c = re.sub(r'\s+', ' ', c)
    c = re.sub(r'\s*([{}();,=+\-*/<>!&|.?:])\s*', r'\1', c)
    return c.strip() + '\n'

def rebuild_bundle(dir_path):
    p = Path(dir_path)
    bundle = ''
    for name in ['script.js', 'search.js', 'audio-reader.js']:
        fp = p / name
        if fp.exists():
            bundle += minify_js(fp) + '\n'
    out_path = p / 'bundle.min.js'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(bundle)
    print(f'Rebuilt {out_path}: {len(bundle)} bytes')
    assert 'shouldEnableTTS' in bundle, f'shouldEnableTTS missing in {out_path}'

rebuild_bundle('pages')
rebuild_bundle('pages/zh-TW')
print('All Done!')
