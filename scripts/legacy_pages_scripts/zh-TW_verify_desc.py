import glob, re

files = sorted(glob.glob('**/*.html', recursive=True))
issues = []
for fp in files:
    with open(fp, encoding='utf-8') as f:
        content = f.read()
    m = re.search(r'<meta name=["\']description["\'][^>]*content=["\'](.*?)["\']', content, re.DOTALL)
    if m:
        dlen = len(m.group(1).strip())
        if dlen > 0 and (dlen < 140 or dlen > 155):
            issues.append((fp, dlen, m.group(1).strip()[:80]))

total = len(files)
ok = total - len(issues)
print(f'Desc Status: {ok}/{total} OK, {len(issues)} issues')
for fp, l, d in issues[:20]:
    print(f'  [{l:3d}] {fp}: {d}')
if len(issues) > 20:
    print(f'  ... and {len(issues)-20} more')
