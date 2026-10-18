import os, glob, re

base = 'concepts'
issues = []
for fpath in sorted(glob.glob(os.path.join(base, '*.html'))):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check main div balance
    main_match = re.search(r'<main[^>]*>(.*)</main>', content, re.DOTALL)
    if not main_match:
        issues.append((os.path.basename(fpath), 'NO_MAIN'))
        continue
    
    main_inner = main_match.group(1)
    opens = len(re.findall(r'<div[\s>]', main_inner))
    closes = len(re.findall(r'</div>', main_inner))
    
    if opens != closes:
        issues.append((os.path.basename(fpath), f'UNBALANCED: opens={opens} closes={closes} diff={opens-closes}'))

print(f'Issues: {len(issues)}')
for name, issue in issues:
    print(f'  {name}: {issue}')
