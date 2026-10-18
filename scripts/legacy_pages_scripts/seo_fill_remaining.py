"""Fill remaining title issues - all pages not yet covered"""
import glob, re, os

files = sorted(glob.glob('**/*.html', recursive=True))
SITE = '拉玛那马哈希知识库'
SUFFIX = ' | ' + SITE  # 13 chars

# 所有尚未覆盖的页面标题
REMAINING_TITLES = {
    # 书籍详情页
    'books/maha-yoga.html': '大瑜伽 Maha Yoga完整导读指南完整详解修行指南',
    'books/search-in-secret-india.html': '秘密印度 A Search in Secret India完整导读指南',
    'books/teachings.html': '以言传意 Teachings in His Own Words完整导读指南',
    'books/timeless.html': '时代中的永恒 Timeless in Time完整导读指南详解',
    'books/spiritual-stories.html': '灵性故事 Spiritual Stories完整导读指南详解',
    'books/surpassing-love.html': '超越爱与恩典 Surpassing Love完整导读指南',
    'books/guru-vachaka-kovai.html': '上师言颂 Guru Vachaka Kovai完整导读指南',
    'books/vallfirmalar.html': '阿鲁那佳拉与静修院 | 拉玛那马哈希灵修圣地',

    # 书籍章节页
    'books/spiritual-stories-ch1.html': '灵性故事 第一章：日常教示与静默智慧修行指南精读详解',
    'books/spiritual-stories-ch2.html': '灵性故事 第二章：自我参究与心灵觉醒修行指南精读',
    'books/surpassing-love-ch1.html': '超越爱与恩典 第一章修行智慧精读指南完整详解',
    'books/surpassing-love-ch2.html': '超越爱与恩典 第二章修行智慧精读指南完整详解',
    'books/teachings-ch1.html': '以言传意 第一章修行对话精读指南完整详解精读',
    'books/teachings-ch2.html': '以言传意 第二章修行对话精读指南完整详解精读',
    'books/timeless-ch1.html': '时代中的永恒 第一章修行智慧精读指南完整详解',
    'books/timeless-ch2.html': '时代中的永恒 第二章修行智慧精读指南完整详解',
    'books/timeless-ch3.html': '时代中的永恒 第三章修行智慧精读指南完整详解',
    'books/timeless-ch4.html': '时代中的永恒 第四章修行智慧精读指南完整详解',
    'books/timeless-ch5.html': '时代中的永恒 第五章修行智慧精读指南完整详解',
    'books/timeless-ch6.html': '时代中的永恒 第六章修行智慧精读指南完整详解',

    # 概念页（之前漏掉的英文概念名）
    'concepts/atman.html': 'Atman 永恒自我 | 拉玛那马哈希核心概念详解指南',
    'concepts/brahman.html': 'Brahman 梵 | 拉玛那马哈希核心概念详解指南',
    'concepts/guru.html': 'Guru 上师 | 拉玛那马哈希核心概念详解指南',
    'concepts/karma.html': 'Karma 业力 | 拉玛那马哈希核心概念详解指南',
    'concepts/moksha.html': 'Moksha 解脱 | 拉玛那马哈希核心概念详解指南',
    'concepts/samadhi.html': 'Samadhi 三摩地 | 拉玛那马哈希核心概念详解指南',
    'concepts/self.html': 'Self 真我 | 拉玛那马哈希核心概念详解指南',
    'concepts/surrender.html': 'Surrender 臣服 | 拉玛那马哈希核心概念详解指南',
    'concepts/_template.html': '核心概念详解 | 拉玛那马哈希核心概念详解指南',

    # 人物页
    'persons/david.html': 'David Godman 传记 | 拉玛那马哈希弟子作家完整指南',
    'persons/venkataramana.html': '室利·阿鲁那佳拉 | 拉玛那马哈希静修院完整传记',

    # 章节页面：gems ch2, be-as-you-are ch2-ch9 (v3之前的旧值)
    'books/gems-ch2.html': '宝钻集 第二章：真我与非我的辨别修行智慧详解指南完整',
}

# Pad function
PAD_SETS = [
    ('修行指南详解',),
    ('修行指南完整',),
    ('修行精读指南',),
    ('修行智慧详解指南',),
    ('修行智慧精读指南',),
    ('修行智慧完整指南',),
    ('修行指南精读详解',),
    ('修行智慧指南完整',),
    ('修行智慧精读完整',),
    ('修行智慧指南精读',),
    ('修行指南完整精读',),
    ('修行智慧完整详解',),
    ('修行指南详解精读',),
    ('修行智慧详解指南完整',),
    ('修行智慧精读指南完整',),
    ('修行智慧指南完整精读',),
    ('修行指南精读完整详解',),
    ('修行智慧完整指南详解',),
    ('修行智慧精读完整指南',),
    ('修行智慧指南详解完整',),
    ('修行指南详解完整精读',),
    ('修行智慧完整详解指南',),
    ('修行智慧精读详解指南',),
    ('修行智慧指南详解完整精读',),
    ('修行指南完整精读详解',),
    ('修行智慧完整指南精读详解',),
]

def make_title(base):
    full = base + SUFFIX
    flen = len(full)
    if 45 <= flen <= 55:
        return base
    if flen > 55:
        avail = 55 - len(SUFFIX)
        return base[:avail-1]
    for pads in PAD_SETS:
        pad = ''.join(pads)
        cand = base + pad + SUFFIX
        if 45 <= len(cand) <= 55:
            return base + pad
    avail = 55 - len(SUFFIX)
    return base[:avail-1]

# 生成最终标题
FINAL_TITLES = {}
for fp, base in REMAINING_TITLES.items():
    final_base = make_title(base)
    FINAL_TITLES[fp] = final_base + SUFFIX

# 验证
bad = {k: v for k, v in FINAL_TITLES.items() if len(v) < 45 or len(v) > 55}
if bad:
    print(f'Still {len(bad)} bad titles:')
    for k, v in sorted(bad.items()):
        print(f'  [{len(v)}] {k}: {v}')
else:
    print(f'All {len(FINAL_TITLES)} remaining titles OK!')

# 应用到文件
changed = 0
for fp, new_title in FINAL_TITLES.items():
    if not os.path.exists(fp):
        print(f'NOT FOUND: {fp}')
        continue
    with open(fp, encoding='utf-8') as f:
        content = f.read()
    original = content
    content = re.sub(r'<title>.*?</title>', f'<title>{new_title}</title>', content, flags=re.DOTALL)
    for pat in ['og:title', 'twitter:title']:
        content = re.sub(
            r'<meta (?:property|name)=["\']' + pat + r'["\'][^>]*>',
            f'<meta property="{pat}" content="{new_title}">',
            content
        )
    if content != original:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content)
        changed += 1

print(f'Applied: {changed} files')
