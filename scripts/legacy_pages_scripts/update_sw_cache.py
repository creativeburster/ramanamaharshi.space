"""
更新 sw.js CORE_ASSETS 为斜杠结尾格式，并升级缓存版本
"""
import re

sw = open(r'c:\Users\willp\WorkBuddy\20260410104230\pages\sw.js', encoding='utf-8').read()

# 替换 .html 为 /（但目录的 /index.html 改为 /index/）
def fix_url(url):
    url = url.strip()
    # 已经是斜杠结尾的目录
    if url.endswith('/') and not url.endswith('.html'):
        return url
    # /index.html → /index/
    if url.endswith('/index.html'):
        return url[:-5] + '/'
    # xxx.html → xxx/
    if url.endswith('.html'):
        return url[:-5] + '/'
    return url + '/'

# 提取 CORE_ASSETS 数组内容
match = re.search(r'const CORE_ASSETS = \[\s*(.*?)\s*\];', sw, re.DOTALL)
if not match:
    print('ERROR: CORE_ASSETS not found')
    exit()

old_assets = match.group(1)
# 解析每一项（去掉逗号和换行）
items = [i.strip().rstrip(',').strip("'").strip('"') for i in old_assets.split('\n') if i.strip() and not i.strip().startswith('//')]
fixed_items = [fix_url(i) for i in items]

# 构建新数组
new_lines = ['const CORE_ASSETS = [']
for item in fixed_items:
    new_lines.append(f"  '{item}',")
new_lines.append('];')

new_assets = '\n'.join(new_lines)

# 更新版本号和 CORE_ASSETS
sw = re.sub(r"const CACHE_NAME = '(ramana-kb-v\d+)'", lambda m: f"const CACHE_NAME = 'ramana-kb-v{int(m.group(1)[-1])+1}'", sw)
sw = re.sub(r'const CORE_ASSETS = \[.*?\];', new_assets, sw, flags=re.DOTALL)

with open(r'c:\Users\willp\WorkBuddy\20260410104230\pages\sw.js', 'w', encoding='utf-8') as f:
    f.write(sw)

print('SW 缓存版本已升级，预缓存URL已更新为斜杠格式')
print(f'示例: {fixed_items[:5]}')
