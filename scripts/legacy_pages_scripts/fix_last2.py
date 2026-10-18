import re

# 快速修复最后2个
for fp, title in [
    ('books/maha-yoga.html', '大瑜伽 Maha Yoga完整导读指南完整详解修行 | 拉玛那马哈希知识库'),
    ('books/ramana-teachings.html', '拉玛那马哈希核心教示 | 灵性教导精要指南完整修行 | 拉玛那马哈希知识库'),
]:
    with open(fp, encoding='utf-8') as f:
        content = f.read()
    new_title = title if len(title) <= 55 else title[:54] + '...'
    content = re.sub(r'<title>.*?</title>', f'<title>{new_title}</title>', content, flags=re.DOTALL)
    for pat in ['og:title', 'twitter:title']:
        content = re.sub(
            r'<meta (?:property|name)=["\']' + pat + r'["\'][^>]*>',
            f'<meta property="{pat}" content="{new_title}">',
            content
        )
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Fixed {fp}: [{len(new_title)}] {new_title}')
