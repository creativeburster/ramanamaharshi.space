#!/usr/bin/env python3
"""
最终 SEO title 修复脚本
解决：
1. 重复的 "| 拉玛那马哈希知识库" 
2. 首页 title 多出一个 "| 拉玛那马哈希知识库"
3. persons 页面 title 前面的 "· " "·· " 符号
4. "index | 知识库" 类的无意义标题
5. "qa-N | 知识库" 改为有意义的标题
"""
import os
import re
import glob

PAGES_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_NAME = "拉玛那马哈希知识库"

# 手动映射一些特殊标题
TITLE_MAP = {
    'books/index.html': '经典著作 | 拉玛那马哈希知识库',
    'concepts/index.html': '核心概念 | 拉玛那马哈希知识库',
    'qa/index.html': '精选问答 | 拉玛那马哈希知识库',
    'persons/index.html': '关键人物 | 拉玛那马哈希知识库',
    'methods/index.html': '修行方法 | 拉玛那马哈希知识库',
    'graph.html': '知识图谱 | 拉玛那马哈希知识库',
    'index.html': '拉玛那马哈希知识库 | 灵性教示完整指南',
}

QA_TITLES = {
    'qa/qa-1.html': '自我参究基础 | 拉玛那马哈希知识库',
    'qa/qa-2.html': '心智的本性 | 拉玛那马哈希知识库',
    'qa/qa-3.html': '静默与修行 | 拉玛那马哈希知识库',
    'qa/qa-4.html': '解脱与觉悟 | 拉玛那马哈希知识库',
    'qa/qa-5.html': '上师与恩典 | 拉玛那马哈希知识库',
    'qa/qa-6.html': '臣服与祈祷 | 拉玛那马哈希知识库',
    'qa/qa-7.html': '真我与存在 | 拉玛那马哈希知识库',
    'qa/qa-8.html': '自我了悟 | 拉玛那马哈希知识库',
    'qa/qa-9.html': '修行方法 | 拉玛那马哈希知识库',
    'qa/qa-10.html': '念头与专注 | 拉玛那马哈希知识库',
    'qa/qa-11.html': '业力与命运 | 拉玛那马哈希知识库',
    'qa/qa-12.html': '世界与幻象 | 拉玛那马哈希知识库',
    'qa/qa-13.html': '在家修行 | 拉玛那马哈希知识库',
    'qa/qa-14.html': '三摩地与参究 | 拉玛那马哈希知识库',
    'qa/qa-15.html': '觉悟者的境界 | 拉玛那马哈希知识库',
    'qa/qa-16.html': '轮回与解脱 | 拉玛那马哈希知识库',
    'qa/qa-17.html': '幸福的本质 | 拉玛那马哈希知识库',
    'qa/qa-18.html': '灵性修行杂谈 | 拉玛那马哈希知识库',
}

def clean_title(t):
    # 去除前后的点号
    t = re.sub(r'^[·\s]+', '', t)
    # 去除重复的 site name
    t = re.sub(r'(\|\s*拉玛那马哈希知识库\s*)+', '| 拉玛那马哈希知识库', t)
    # 清理多余空格
    t = re.sub(r'\s+', ' ', t).strip()
    return t

def fix_file(filepath, rel_path):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    rel_path_unix = rel_path.replace('\\', '/')
    
    # 检查是否有手动映射
    new_title = None
    if rel_path_unix in TITLE_MAP:
        new_title = TITLE_MAP[rel_path_unix]
    elif rel_path_unix in QA_TITLES:
        new_title = QA_TITLES[rel_path_unix]
    else:
        # 自动清理
        m = re.search(r'<title>(.*?)</title>', content)
        if m:
            cleaned = clean_title(m.group(1))
            # 若 title 是 "xxx | 知识库 | 知识库" 或者以 "index" 开头
            if f'| {SITE_NAME}' in cleaned:
                new_title = cleaned
            elif cleaned == SITE_NAME:
                new_title = cleaned
            else:
                new_title = cleaned
    
    if new_title:
        content = re.sub(r'<title>.*?</title>', f'<title>{new_title}</title>', content)
        content = re.sub(
            r'<meta property="og:title" content=".*?">',
            f'<meta property="og:title" content="{new_title}">',
            content
        )
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, new_title
    return False, None

def main():
    html_files = glob.glob(os.path.join(PAGES_DIR, '**', '*.html'), recursive=True)
    exclude = {'_template.html', 'sitemap.html'}
    
    fixed = 0
    for fp in sorted(html_files):
        bn = os.path.basename(fp)
        if bn in exclude:
            continue
        rel = os.path.relpath(fp, PAGES_DIR)
        changed, new_title = fix_file(fp, rel)
        if changed:
            print(f'[OK] {rel} → {new_title}')
            fixed += 1
    
    print(f'\n完成: 修复 {fixed} 个文件')

if __name__ == '__main__':
    main()
