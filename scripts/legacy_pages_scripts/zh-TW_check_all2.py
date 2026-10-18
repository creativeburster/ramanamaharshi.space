import re, os, glob

issues = []
for fpath in sorted(glob.glob('concepts/*.html')):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'related-books' not in content:
        continue
    
    name = os.path.basename(fpath)
    has_article = '<article>' in content
    has_footer = '<footer' in content
    
    # Check 1: books inside article
    if has_article:
        books_pos = content.find('related-books')
        art_close = content.find('</article>')
        if books_pos > 0 and art_close > 0 and books_pos < art_close:
            issues.append((name, 'BOOKS_INSIDE_ARTICLE'))
    
    # Check 2: content-wrapper balance (from cw to footer or main_close)
    if 'content-wrapper' in content:
        cw_open = content.index('content-wrapper')
        # Find where to stop
        stop = content.find('<footer') if has_footer else content.find('</main>')
        if stop < 0:
            continue
        between = content[cw_open:stop]
        div_opens = len(re.findall(r'<div[\s>]', between))
        div_closes = between.count('</div>')
        if div_opens != div_closes:
            issues.append((name, f'CW_UNBALANCED: opens={div_opens} closes={div_closes}'))

print(f'Total issues: {len(issues)}')
for name, issue in sorted(issues):
    print(f'  {name}: {issue}')
