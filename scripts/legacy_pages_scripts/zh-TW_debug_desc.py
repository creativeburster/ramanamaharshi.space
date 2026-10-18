import re

# 测试
fp = 'books/be-as-you-are-ch1.html'
with open(fp, encoding='utf-8') as f:
    content = f.read()

# 查找description
m = re.search(r'<meta name=["\']description["\'][^>]*>', content)
print('Meta tag found:', m.group(0) if m else None)

# 测试替换
desc = '测试描述内容' * 30  # 长的
result = re.sub(r'<meta name=["\']description["\'][^>]*>', f'<meta name="description" content="{desc}">', content)
print('Replacement worked:', result != content)
