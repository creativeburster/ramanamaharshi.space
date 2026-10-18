"""
Fix: Move books card from INSIDE article to AFTER article (but inside content-wrapper).

Pattern to find (wrong):
    </div>  (close last concept-tags or card)
    <div class="card">
        <h2>📚 相关书籍</h2>
        ...
    </div>
</article>
</div>  (close content-wrapper)

Should be (correct):
    </div>  (close last concept-tags or card)
</article>
    <div class="card">
        <h2>📚 相关书籍</h2>
        ...
    </div>
</div>  (close content-wrapper)
"""
import os, glob, re

base = 'concepts'
fixed = 0

for fpath in sorted(glob.glob(os.path.join(base, '*.html'))):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'related-books' not in content or '<article' not in content:
        continue
    
    # Find the books card block
    books_start = content.find('<div class="card">\n                    <h2 style="color:var(--primary)')
    if books_start < 0:
        # Try alternate pattern
        books_start = content.find('<div class="card">\r\n                    <h2 style="color:var(--primary)')
    if books_start < 0:
        continue
    
    # Find </article> after books
    art_close = content.find('</article>', books_start)
    if art_close < 0:
        continue
    
    # Check if books card is inside article (books_start < art_close)
    if books_start > art_close:
        continue  # Already correct
    
    # Find end of books card (matching </div>)
    # The card structure: <div class="card"> ... <div class="related-books"> ... </div> ... </div>
    # We need to find the </div> that closes the card
    depth = 0
    pos = books_start
    card_end = -1
    while pos < len(content):
        next_open = content.find('<div', pos)
        next_close = content.find('</div>', pos)
        
        if next_close < 0:
            break
        
        # Only count divs before article close
        if next_open >= 0 and next_open < next_close and next_open < art_close:
            depth += 1
            pos = next_open + 4
        else:
            depth -= 1
            if depth == 0:
                card_end = content.index('</div>', next_close) + 6
                break
            pos = next_close + 6
    
    if card_end < 0:
        print(f'  SKIP {os.path.basename(fpath)}: could not find card end')
        continue
    
    # Extract books card
    books_card = content[books_start:card_end]
    
    # Check that </article> comes right after (with possible whitespace)
    after_card = content[card_end:art_close + len('</article>')].strip()
    if after_card != '</article>':
        print(f'  SKIP {os.path.basename(fpath)}: unexpected content between card and article_close')
        continue
    
    # Remove books card from old position
    new_content = content[:books_start].rstrip() + '\n' + content[card_end:]
    
    # Insert books card after </article>
    art_close_new = new_content.find('</article>')
    insertion = '\n\n                ' + books_card.strip('\n\r')
    new_content = new_content[:art_close_new + len('</article>')] + insertion + new_content[art_close_new + len('</article>'):]
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    fixed += 1
    print(f'  Fixed {os.path.basename(fpath)}')

print(f'\nTotal fixed: {fixed}')
