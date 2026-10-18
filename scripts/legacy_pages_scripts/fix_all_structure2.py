"""
全面修复所有概念页的 HTML 结构（第二版，处理无 article 标签的文件）。
问题：书籍卡片缺少外层 </div> 闭合，导致 footer 被吞入卡片内。
"""
import os, glob, re

base = r'c:\Users\willp\Desktop\2026年4月\kb01\pages\concepts'
fixed = 0

for fpath in sorted(glob.glob(os.path.join(base, '*.html'))):
    with open(fpath, 'r', encoding='utf-8') as fh:
        content = fh.read()
    
    name = os.path.basename(fpath)
    
    if 'related-books' not in content:
        continue
    
    # Find the pattern: </div> closing related-books, then immediately <footer
    # This means the outer card div is not closed
    
    # Find 📚 相关书籍 heading
    books_heading = content.find('📚 相关书籍')
    if books_heading < 0:
        continue
    
    # Find the card start
    search_back = content[max(0, books_heading-500):books_heading]
    card_start_rel = search_back.rfind('<div class="card">')
    if card_start_rel < 0:
        continue
    card_start = max(0, books_heading-500) + card_start_rel
    
    # Find footer
    footer_pos = content.find('<footer')
    if footer_pos < 0:
        continue
    
    # Find the last </div> before <footer in the card area
    between = content[card_start:footer_pos]
    
    # Count div opens and closes in this region
    div_opens = len(re.findall(r'<div[\s>]', between))
    div_closes = len(re.findall(r'</div>', between))
    
    # If closes < opens, card is not properly closed
    if div_closes >= div_opens:
        continue  # Already balanced
    
    # The card needs (div_opens - div_closes) more </div> before footer
    missing = div_opens - div_closes
    
    # Insert the missing </div> tags right before <footer
    closing_tags = '\n                </div>' * missing  # Close card and any other unclosed divs
    new_content = content[:footer_pos] + closing_tags + '\n\n' + content[footer_pos:]
    
    # Verify: check if books card is now properly closed
    new_footer_pos = new_content.find('<footer')
    new_between = new_content[card_start:new_footer_pos]
    new_opens = len(re.findall(r'<div[\s>]', new_between))
    new_closes = len(re.findall(r'</div>', new_between))
    
    if new_opens == new_closes:
        with open(fpath, 'w', encoding='utf-8') as fh:
            fh.write(new_content)
        fixed += 1
        print(f'  Fixed: {name} (added {missing} </div>)')
    else:
        print(f'  WARN: {name} still unbalanced (opens={new_opens}, closes={new_closes})')

print(f'\nTotal fixed: {fixed}')
