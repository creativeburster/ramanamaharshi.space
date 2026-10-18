"""
全面修复概念页 HTML 结构。
问题根源：上一个批量脚本插入相关书籍卡片时：
1. 把卡片放到了 </article></div>（content-wrapper关闭）之后
2. 卡片缺少 </div> 关闭外层 card
3. 导致 footer 被挤到错误位置

正确结构：
  <main>
    <topbar>...</topbar>
    <div class="content-wrapper">
      <article>
        ... 内容卡片 ...
        ... 相关概念卡片 ...
      </article>
      ... 相关书籍卡片 ...
    </div>  ← 关闭 content-wrapper
    <footer>...</footer>
  </main>
"""
import os, glob, re

base = r'c:\Users\willp\Desktop\2026年4月\kb01\pages\concepts'
fixed = 0
skipped = 0
errors = 0

for fpath in sorted(glob.glob(os.path.join(base, '*.html'))):
    with open(fpath, 'r', encoding='utf-8') as fh:
        content = fh.read()
    
    name = os.path.basename(fpath)
    
    if 'related-books' not in content:
        skipped += 1
        continue
    
    # Find key landmarks
    article_close = content.find('</article>')
    if article_close < 0:
        errors += 1
        print(f'  ERROR no article: {name}')
        continue
    
    footer_start = content.find('<footer')
    if footer_start < 0:
        errors += 1
        print(f'  ERROR no footer: {name}')
        continue
    
    # Find the books card (📚 相关书籍)
    books_heading = content.find('📚 相关书籍')
    if books_heading < 0:
        skipped += 1
        continue
    
    # Check if books card is AFTER </article> but BEFORE <footer>
    # (meaning it's in the right zone but possibly misnested)
    
    # Find the books card's outer <div class="card">
    search_back = content[max(0, books_heading-500):books_heading]
    card_start_rel = search_back.rfind('<div class="card">')
    if card_start_rel < 0:
        errors += 1
        print(f'  ERROR no card wrapper: {name}')
        continue
    card_start = max(0, books_heading-500) + card_start_rel
    
    # Find the card end by counting div depth
    depth = 0
    pos = card_start
    card_end = None
    while pos < len(content):
        ch = content[pos:pos+4]
        if ch == '<div' and (pos+4 >= len(content) or not content[pos+4].isalpha()):
            depth += 1
        elif content[pos:pos+6] == '</div>':
            depth -= 1
            if depth == 0:
                card_end = pos + 6
                break
        pos += 1
    
    if card_end is None:
        # Card is not properly closed - find where it should end
        # Look for the last </div> before footer
        before_footer = content[card_start:footer_start]
        last_close = before_footer.rfind('</div>')
        if last_close >= 0:
            card_end = card_start + last_close + 6
        else:
            errors += 1
            print(f'  ERROR cannot find card end: {name}')
            continue
    
    books_card = content[card_start:card_end]
    
    # Now we need to restructure:
    # 1. Remove the books card from its current position
    content_no_card = content[:card_start] + content[card_end:]
    
    # 2. Find </article> in the new content
    art_close_new = content_no_card.find('</article>')
    if art_close_new < 0:
        errors += 1
        print(f'  ERROR: {name}')
        continue
    
    # 3. Find where content-wrapper closes (should be right after </article>)
    after_art = content_no_card[art_close_new + len('</article>'):art_close_new + len('</article>') + 200]
    
    # Look for the pattern: </article>\n</div>\n\n and maybe another </div>
    # The correct insertion point is right after </article>, before </div> (content-wrapper close)
    
    # 4. Find content-wrapper close
    # Count: after removing books card, the structure should be:
    # </article>\n</div>  (article div wrapper) \n</div> (content-wrapper)
    # OR just </article>\n</div> (content-wrapper directly contains article)
    
    # Find <footer> in content_no_card
    footer_new = content_no_card.find('<footer')
    
    # The content between </article> and <footer> should be just </div>s
    between = content_no_card[art_close_new + len('</article>'):footer_new]
    
    # Count </div> in between
    div_closes_in_between = len(re.findall(r'</div>', between))
    
    # Remove the books card area from between (already done since we removed it)
    # Now we want: </article>\n\n{books_card}\n</div> (content-wrapper close)
    
    # Insert books card after </article>, before the closing </div>(s)
    insert_pos = art_close_new + len('</article>')
    
    new_content = content_no_card[:insert_pos] + '\n\n' + books_card + content_no_card[insert_pos:]
    
    # Verify the new structure
    footer_check = new_content.find('<footer')
    art_check = new_content.find('</article>')
    books_check = new_content.find('📚 相关书籍')
    
    # Books should be after article but before footer
    if books_check > art_check and books_check < footer_check:
        with open(fpath, 'w', encoding='utf-8') as fh:
            fh.write(new_content)
        fixed += 1
        print(f'  Fixed: {name}')
    else:
        errors += 1
        print(f'  FAILED structural check: {name} (art={art_check}, books={books_check}, footer={footer_check})')

print(f'\nFixed: {fixed}, Skipped: {skipped}, Errors: {errors}')
