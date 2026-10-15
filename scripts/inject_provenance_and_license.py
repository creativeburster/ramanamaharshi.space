# -*- coding: utf-8 -*-
"""
为 pages/books/ 和 pages/zh-TW/books/ 下的核心书籍主页注入：
1. 文献级元数据栏 (Provenance Bar: 官方底本出处、校勘日期、授权说明)
2. 规范化源文档 TXT 下载版权与凡例对勘说明
"""

import os
import re

BOOKS_DIR_CN = r"F:\Ramana\pages\books"
BOOKS_DIR_TW = r"F:\Ramana\pages\zh-TW\books"

PROVENANCE_BAR_CN = '''
                <div class="provenance-bar" style="margin-bottom:1.5rem;padding:0.75rem 1rem;background:rgba(255,255,255,0.03);border:1px solid var(--border-color);border-radius:8px;font-size:0.85rem;color:var(--text-muted);display:flex;flex-wrap:wrap;gap:1rem;" data-nosnippet>
                    <span>🏛️ <strong>底本出处</strong>：Sri Ramanasramam (Tiruvannamalai)</span>
                    <span>📜 <strong>文献体裁</strong>：灵性哲学经典导读与法语汇编</span>
                    <span>📅 <strong>最近校勘</strong>：2026-10</span>
                    <span>⚖️ <strong>研学规范</strong>：<a href="../about.html" style="color:inherit;text-decoration:underline;">校勘凡例与版权声明</a></span>
                </div>'''

PROVENANCE_BAR_TW = '''
                <div class="provenance-bar" style="margin-bottom:1.5rem;padding:0.75rem 1rem;background:rgba(255,255,255,0.03);border:1px solid var(--border-color);border-radius:8px;font-size:0.85rem;color:var(--text-muted);display:flex;flex-wrap:wrap;gap:1rem;" data-nosnippet>
                    <span>🏛️ <strong>底本出處</strong>：Sri Ramanasramam (Tiruvannamalai)</span>
                    <span>📜 <strong>文獻體裁</strong>：靈性哲學經典導讀與法語彙編</span>
                    <span>📅 <strong>最近校勘</strong>：2026-10</span>
                    <span>⚖️ <strong>研學規範</strong>：<a href="../about.html" style="color:inherit;text-decoration:underline;">校勘凡例與版權聲明</a></span>
                </div>'''

DOWNLOAD_NOTE_CN = '''
                    <p style="margin-top:0.75rem;font-size:0.85rem;color:var(--text-muted);line-height:1.5;">* 文本整理自印度阿鲁那佳拉静修院（Sri Ramanasramam）官方文献及公有领域历史底本，仅供个人非营利学术研学对勘，详见<a href="../about.html" style="text-decoration:underline;">《校勘凡例与关于本库》</a>。</p>'''

DOWNLOAD_NOTE_TW = '''
                    <p style="margin-top:0.75rem;font-size:0.85rem;color:var(--text-muted);line-height:1.5;">* 文本整理自印度阿魯那佳拉靜修院（Sri Ramanasramam）官方文獻及公有領域歷史底本，僅供個人非營利學術研學對勘，詳見<a href="../about.html" style="text-decoration:underline;">《校勘凡例與關於本庫》</a>。</p>'''

def process_book_dir(book_dir, is_tw=False):
    prov_bar = PROVENANCE_BAR_TW if is_tw else PROVENANCE_BAR_CN
    down_note = DOWNLOAD_NOTE_TW if is_tw else DOWNLOAD_NOTE_CN
    modified = 0

    for f in os.listdir(book_dir):
        if not f.endswith(".html"):
            continue
        # 排除章节分段页，专注书籍主导读页（如 gems.html, be-as-you-are.html, talks.html 等）
        if "-ch" in f:
            continue
        if f == "index.html":
            continue

        fp = os.path.join(book_dir, f)
        with open(fp, "r", encoding="utf-8") as file:
            content = file.read()

        original = content

        # 1. 注入 Provenance Bar（在 </header> 之后）
        if "class=\"provenance-bar\"" not in content:
            content = re.sub(
                r'(</header>\s*)(<div class="card")',
                rf'\1{prov_bar}\n                \2',
                content,
                count=1
            )

        # 2. 在源文档下载卡片中添加免责与凡例说明
        if "📥 源文档" in content or "📥 源文檔" in content:
            if "* 文本整理自" not in content:
                content = re.sub(
                    r'(<div class="concept-tags">\s*<a href="[^"]*?\.(?:txt|pdf)"[^>]*>.*?</a>\s*</div>)',
                    rf'\1{down_note}',
                    content,
                    count=1
                )

        if content != original:
            with open(fp, "w", encoding="utf-8") as file:
                file.write(content)
            modified += 1

    return modified

def main():
    m_cn = process_book_dir(BOOKS_DIR_CN, is_tw=False)
    m_tw = process_book_dir(BOOKS_DIR_TW, is_tw=True)
    print(f"Processed books: modified {m_cn} Simplified books, {m_tw} Traditional books.")

if __name__ == "__main__":
    main()
