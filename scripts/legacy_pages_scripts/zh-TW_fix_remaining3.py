import re

SITE = '拉玛那马哈希知识库'
SUFFIX = ' | ' + SITE

def fix_file(fp, base):
    full = base + SUFFIX
    title = full if len(full) <= 55 else full[:54] + '…'
    with open(fp, encoding='utf-8') as f:
        content = f.read()
    original = content
    content = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', content, flags=re.DOTALL)
    for pat in ['og:title', 'twitter:title']:
        content = re.sub(
            r'<meta (?:property|name)=["\']' + pat + r'["\'][^>]*>',
            f'<meta property="{pat}" content="{title}">',
            content
        )
    if content != original:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content)
    print(f'Fixed [{len(title)}] {fp}: {title}')

# search-secret-india (当前40字符)
fix_file('books/search-secret-india.html', '秘密印度 A Search in Secret India完整导读指南详解完整')
# guru-vachaka-kovai 不存在，跳过
# vallfirmalar 不存在，跳过
