import glob, re

files = sorted(glob.glob('**/*.html', recursive=True))
issues = []
for fp in files:
    with open(fp, encoding='utf-8') as f:
        content = f.read()
    m = re.search(r'<title>(.*?)</title>', content, re.DOTALL)
    if m:
        tlen = len(m.group(1).strip())
        if tlen < 45 or tlen > 55:
            issues.append((fp, tlen, m.group(1).strip()[:70]))

total = len(files)
ok = total - len(issues)
print(f'Title Status: {ok}/{total} OK, {len(issues)} issues')
for fp, l, t in issues:
    print(f'  [{l:2d}] {fp}: {t}')
