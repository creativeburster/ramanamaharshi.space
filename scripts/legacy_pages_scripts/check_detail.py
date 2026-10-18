import re

for name in ['turiya.html', 'satchidananda.html']:
    fpath = f'concepts/{name}'
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f'\n=== {name} ===')
    
    # Find all structural tags
    lines = content.split('\n')
    for i, line in enumerate(lines):
        s = line.strip()
        if s in ['<article>', '</article>'] or 'content-wrapper' in s or s in ['<main class="main-content">', '</main>']:
            print(f'  {i+1}: {s[:100]}')
    
    # Count depth from article to article close
    if '<article>' in content:
        art_start = content.index('<article>')
        art_end = content.index('</article>')
        inner = content[art_start+9:art_end]
        opens = len(re.findall(r'<div[\s>]', inner))
        closes = inner.count('</div>')
        print(f'  article inner divs: opens={opens} closes={closes} diff={opens-closes}')
    
    # Check: is books card INSIDE article?
    books_pos = content.find('related-books')
    art_close = content.find('</article>')
    if books_pos > 0 and art_close > 0 and books_pos < art_close:
        print(f'  WARNING: books card INSIDE article (books={books_pos} < article_close={art_close})')
    elif books_pos > 0 and art_close > 0:
        print(f'  OK: books card OUTSIDE article (books={books_pos} > article_close={art_close})')
    
    # Check content-wrapper close position
    if 'content-wrapper' in content:
        cw_open = content.index('content-wrapper')
        # Find last </div> before footer
        footer_pos = content.find('<footer') if '<footer' in content else content.find('</main>')
        if footer_pos > 0:
            between = content[cw_open:footer_pos]
            cw_opens = between.count('content-wrapper')
            cw_closes_between = between.count('</div>')
            div_opens_between = len(re.findall(r'<div[\s>]', between))
            print(f'  From cw to footer/main: div opens={div_opens_between} closes={cw_closes_between}')
    
    # Full main balance
    main_m = re.search(r'<main[^>]*>(.*)</main>', content, re.DOTALL)
    if main_m:
        mi = main_m.group(1)
        mo = len(re.findall(r'<div[\s>]', mi))
        mc = mi.count('</div>')
        print(f'  Main inner: div opens={mo} closes={mc} diff={mo-mc}')
