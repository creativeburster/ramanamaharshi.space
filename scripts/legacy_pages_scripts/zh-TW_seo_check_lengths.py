import glob
import re
import os

files = sorted(glob.glob('**/*.html', recursive=True))
print(f'Total files: {len(files)}')

title_issues = []
desc_issues = []

for fp in files:
    with open(fp, encoding='utf-8') as f:
        content = f.read()

    m_title = re.search(r'<title>(.*?)</title>', content, re.DOTALL)
    m_desc = re.search(r'name=["\']description["\'][^>]*content=["\'](.*?)["\']', content, re.DOTALL)

    title = m_title.group(1).strip() if m_title else ''
    desc = m_desc.group(1).strip() if m_desc else ''

    tlen = len(title)
    dlen = len(desc)

    if tlen < 45 or tlen > 55:
        title_issues.append((fp, tlen, title))
    if dlen > 0 and (dlen < 140 or dlen > 155):
        desc_issues.append((fp, dlen, desc[:80]))

print(f'Title issues (not 45-55 chars): {len(title_issues)}')
print(f'Desc issues (not 140-155 chars): {len(desc_issues)}')
print()
print('=== TITLE ISSUES ===')
for fp, l, t in title_issues:
    print(f'  [{l:2d}] {fp}: {t}')
print()
print('=== DESC ISSUES ===')
for fp, l, d in desc_issues[:30]:
    print(f'  [{l:3d}] {fp}: {d}')
if len(desc_issues) > 30:
    print(f'  ... and {len(desc_issues)-30} more desc issues')
