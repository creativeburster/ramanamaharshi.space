import os, glob, re

base = 'concepts'
issues = []

for fpath in sorted(glob.glob(os.path.join(base, '*.html'))):
    name = os.path.basename(fpath)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'related-books' not in content:
        continue
    
    has_article = '<article' in content
    has_footer = '<footer' in content
    
    # Check 1: books inside article (for article files)
    if has_article:
        books_pos = content.find('related-books')
        art_close = content.find('</article>')
        if books_pos > 0 and art_close > 0 and books_pos < art_close:
            issues.append((name, 'BOOKS_INSIDE_ARTICLE'))
    
    # Check 2: For no-article files, check if books are before </main>
    if not has_article:
        books_pos = content.find('related-books')
        main_close = content.find('</main>')
        cw_pos = content.find('content-wrapper')
        if books_pos > 0 and cw_pos > 0 and main_close > 0:
            # Books should be inside content-wrapper
            # Find content-wrapper close
            region = content[cw_pos:main_close]
            div_opens = len(re.findall(r'<div[\s>]', region))
            div_closes = region.count('</div>')
            if div_opens != div_closes:
                issues.append((name, f'CW_UNBALANCED opens={div_opens} closes={div_closes}'))
            
            # Check books not inside any stray div
            # Find the card before books
            card_before = content.rfind('<div class="card">', 0, books_pos)
            card_after = content.find('<div class="card">', books_pos)
            if card_before < 0:
                issues.append((name, 'BOOKS_CARD_NO_WRAPPER'))

print(f'Issues: {len(issues)}')
for name, issue in sorted(issues):
    print(f'  {name}: {issue}')
