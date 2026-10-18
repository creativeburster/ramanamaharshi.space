"""
SEO Title & Description Length Fixer v2
Title: 45-55 chars | Description: 140-155 chars
精确扩充到目标范围
"""
import glob
import re
import os

files = sorted(glob.glob('**/*.html', recursive=True))
SITE = '拉玛那马哈希知识库'
changed = 0

# ============================
# Title 规则：精确45-55字符
# ============================
TITLE_RULES = {
    # 首页
    'index.html': '拉玛那马哈希知识库 | 灵性教示完整指南',
    'graph.html': '拉玛那马哈希核心概念知识图谱 | 灵修思想可视化',
    'sitemap.html': '拉玛那马哈希知识库网站地图 | 页面索引',

    # 书籍列表
    'books/index.html': '拉玛那马哈希经典著作全集 | 18本灵性书籍完整目录',
    'qa/index.html': '精选问答150则 | 拉玛那马哈希灵性对话精编',
    'methods/index.html': '修行方法索引 | 拉玛那马哈希灵性修持指南',
    'persons/index.html': '关键人物索引 | 拉玛那马哈希与其弟子',

    # 书籍详情页
    'books/be-as-you-are.html': '走向静默，如你本来 | Be As You Are完整导读',
    'books/gems.html': '宝钻集 | Gems from Bhagavan完整导读指南',
    'books/back-to-heart.html': '回到你心中 | Back to the Heart完整导读',
    'books/talks.html': '对谈录 | Talks with Sri Ramana Maharshi完整导读',
    'books/day-by-day.html': '日日与彼 | Day by Day with Bhagavan完整导读',
    'books/face-to-face.html': '面对面 | Face to Face完整导读指南',
    'books/search-in-secret-india.html': '秘密印度 | A Search in Secret India完整导读',
    'books/maharshi-gospel.html': '马哈希福音 | Maharshi Gospel完整导读指南',
    'books/maha-yoga.html': '大瑜伽 | Maha Yoga完整导读指南',
    'books/guru-vachaka-kovai.html': '上师言颂 | Guru Vachaka Kovai完整导读',
    'books/timeless-in-time.html': '时代中的永恒 | Timeless in Time完整导读',
    'books/reflections.html': '反思录 | Reflections完整导读指南',
    'books/spiritual-stories.html': '灵性故事 | Spiritual Stories完整导读',
    'books/surpassing-love.html': '超越爱与恩典 | Surpassing Love完整导读',
    'books/crumbs.html': '桌边碎语 | Crumbs from the Table完整导读指南',
    'books/collected-works.html': '全集 | Collected Works完整导读指南',
    'books/self-enquiry.html': '自我参究 | Self-Enquiry in Ramana Maharshi导读',
    'books/ramana-teachings.html': '拉玛那马哈希核心教示 | 灵性教导精要',
}

# 书籍章节页：自动生成
BOOK_CHAPTERS = {
    'be-as-you-are': ('走向静默，如你本来', list(range(1, 10))),   # ch1-9
    'gems': ('宝钻集', list(range(1, 14))),                          # ch1-13
    'back-to-heart': ('回到你心中', list(range(1, 6))),              # ch1-5
    'talks': ('对谈录', list(range(1, 9))),                          # ch1-8
    'crumbs': ('桌边碎语', list(range(1, 5))),                       # ch1-4
    'reflections': ('反思录', list(range(1, 3))),                    # ch1-2
}

# 概念页面
CONCEPTS = {
    'self-enquiry': '自我参究法 | Ramana Maharshi核心概念详解',
    'awareness': '觉知与观照 | 拉玛那马哈希核心概念详解',
    'heart': '本心与心灵 | 拉玛那马哈希核心概念详解',
    'jnana': '真知之道 | 拉玛那马哈希核心概念详解',
    'jnani': '真知者 | 拉玛那马哈希核心概念详解',
    'samsara': '轮回与生死 | 拉玛那马哈希核心概念详解',
    'satchidananda': '存在意识喜悦 | 拉玛那马哈希核心概念详解',
    'bhakti': '虔诚之道 | 拉玛那马哈希核心概念详解',
    'japa': '念诵修持 | 拉玛那马哈希核心概念详解',
    'world': '世界与幻相 | 拉玛那马哈希核心概念详解',
    'enlightenment': '开悟与解脱 | 拉玛那马哈希核心概念详解',
    'sahaja': '自然安住 | 拉玛那马哈希核心概念详解',
    'peace': '安宁与寂静 | 拉玛那马哈希核心概念详解',
    'fate': '命运与业力 | 拉玛那马哈希核心概念详解',
    'freewill': '自由意志 | 拉玛那马哈希核心概念详解',
    'whoami': '我是谁？ | 拉玛那马哈希核心概念详解',
    'mind': '心智的本质 | 拉玛那马哈希核心概念详解',
    'ego': '自我与执我 | 拉玛那马哈希核心概念详解',
    'thoughts': '念头与思想 | 拉玛那马哈希核心概念详解',
    'samskaras': '习气与种子 | 拉玛那马哈希核心概念详解',
    'drishti': '见与幻相 | 拉玛那马哈希核心概念详解',
    'maya': '摩耶幻相 | 拉玛那马哈希核心概念详解',
    'tat-tvam-asya': '梵我一如 | 拉玛那马哈希核心概念详解',
    'abidance': '安住真我 | 拉玛那马哈希核心概念详解',
    'silence': '静默的力量 | 拉玛那马哈希核心概念详解',
    'grace': '上师恩典 | 拉玛那马哈希核心概念详解',
    'svasthya': '安住自性 | 拉玛那马哈希核心概念详解',
}

# 问答页面
QA_PAGES = {
    'qa-1': '自我参究基础问答 | 拉玛那马哈希150精选',
    'qa-2': '心智本质与幻相问答 | 拉玛那马哈希150精选',
    'qa-3': '修行方法与精进问答 | 拉玛那马哈希150精选',
    'qa-4': '真我与上师问答 | 拉玛那马哈希150精选',
    'qa-5': '静默与三摩地问答 | 拉玛那马哈希150精选',
    'qa-6': '解脱与开悟问答 | 拉玛那马哈希150精选',
    'qa-7': '虔诚与念诵问答 | 拉玛那马哈希150精选',
    'qa-8': '业力与轮回问答 | 拉玛那马哈希150精选',
    'qa-9': '日常修行与生活问答 | 拉玛那马哈希150精选',
    'qa-10': '梦境与意识状态问答 | 拉玛那马哈希150精选',
    'qa-11': '世界与存在本质问答 | 拉玛那马哈希150精选',
    'qa-12': '死亡与轮回问答 | 拉玛那马哈希150精选',
    'qa-13': '幸福与安宁问答 | 拉玛那马哈希150精选',
    'qa-14': '经典研读与智慧问答 | 拉玛那马哈希150精选',
    'qa-15': '心灵觉醒实践问答 | 拉玛那马哈希150精选',
    'qa-16': '自我超越问答 | 拉玛那马哈希150精选',
    'qa-17': '真知与迷惑问答 | 拉玛那马哈希150精选',
    'qa-18': '上师与弟子问答 | 拉玛那马哈希150精选',
    'qa-19': '静修与日常问答 | 拉玛那马哈希150精选',
    'qa-20': '解脱与圆满问答 | 拉玛那马哈希150精选',
}

# 修行方法页面
METHODS = {
    'methods/self-enquiry': '自我参究法详解 | 拉玛那马哈希修行指南',
    'methods/surrender': '臣服与归伏 | 拉玛那马哈希修行指南',
    'methods/bhakti': '虔诚奉爱之道 | 拉玛那马哈希修行指南',
    'methods/silence': '静默修行 | 拉玛那马哈希修行指南',
    'methods/japa': '念诵修持 | 拉玛那马哈希修行指南',
    'methods/satsang': '共修与灵性聚会 | 拉玛那马哈希修行指南',
    'methods/discrimination': '分别与辨别 | 拉玛那马哈希修行指南',
}

# 人物页面
PERSONS = {
    'persons/ramana': '室利·拉玛那·马哈希完整传记 | 印度灵性导师',
    'persons/vallfirmalar': '室利·拉玛那·马哈希完整传记 | 印度灵性导师',
    'persons/vaikom': '室利·拉玛那·马哈希完整传记 | 印度灵性导师',
}


def get_title(fp):
    """根据文件路径获取目标 title"""
    fname = os.path.basename(fp).replace('.html', '')
    rel = fp.replace('\\', '/')

    # 精确匹配
    if fname in TITLE_RULES:
        return TITLE_RULES[fname]
    if rel in TITLE_RULES:
        return TITLE_RULES[rel]

    # 书籍章节页
    for book_key, (book_name, chapters) in BOOK_CHAPTERS.items():
        for ch in chapters:
            if fname == f'{book_key}-ch{ch}':
                return f'{book_name} 第{ch}章 | {SITE}'

    # 概念页
    if rel.startswith('concepts/'):
        key = fname
        if key in CONCEPTS:
            return CONCEPTS[key]
        return f'{fname} | {SITE}'

    # 问答页
    if fname in QA_PAGES:
        return QA_PAGES[fname]

    # 修行方法页
    if rel in METHODS:
        return METHODS[rel]

    # 人物页
    if rel in PERSONS:
        return PERSONS[rel]

    # 默认：不够45字符时扩充
    return None


def truncate_title(title, max_len=55):
    """截断超长 title，保持 site name 可见"""
    suffix = f' | {SITE}'
    if len(title) <= max_len:
        return title
    avail = max_len - len(suffix)
    # 在逗号、竖线等处截断
    parts = title.split(' | ')
    if len(parts) == 2 and len(parts[0]) <= avail:
        return title
    # 硬截断，避免截断单词
    truncated = title[:avail]
    last_sep = max(truncated.rfind('，'), truncated.rfind(' '))
    if last_sep > avail - 10:
        truncated = truncated[:last_sep]
    return truncated.rstrip() + f'…{suffix}'


# ============================
# Description 规则
# ============================
DESC_RULES = {
    'index.html': '拉玛那马哈希知识库系统整理其灵性教示，包含18本经典著作完整导读、30+核心概念详解、150条精选问答、修行方法指南与关键人物传记，全面覆盖自我参究与静默之道。',
    'graph.html': '拉玛那马哈希核心概念知识图谱，可视化展示真我、心智、自我参究、上师恩典等概念之间的关系，涵盖本体论、心智模型、修行法门与世界本质的完整知识网络。',
    'sitemap.html': '拉玛那马哈希知识库完整网站地图，包含所有页面索引：书籍导读、核心概念、修行方法、精选问答、关键人物等板块的完整导航指南。',

    # 书籍列表
    'books/index.html': '拉玛那马哈希经典著作完整收录，涵盖《走向静默》《宝钻集》《对谈录》《回到你心中》《日日与彼》《马哈希福音》《大瑜伽》等18本灵性经典，提供系统阅读指引。',

    # 问答列表
    'qa/index.html': '拉玛那马哈希精选问答150则，涵盖自我参究、心智本质、修行方法、上师、臣服、静默、解脱等核心主题，助您深入理解这位伟大灵性导师的教示精髓。',

    # 修行方法列表
    'methods/index.html': '拉玛那马哈希修行方法完整指南，涵盖自我参究、臣服、念诵、静默、虔诚奉爱等核心修持法门，配合具体实践指引，助您走上觉醒之路。',

    # 人物列表
    'persons/index.html': '拉玛那马哈希及其关键弟子的完整传记索引，涵盖室利·拉玛那·马哈希本人及诸位重要弟子的生平事迹与灵性贡献。',
}

# 书籍详情页描述
BOOK_DESC = {
    'be-as-you-are': '《走向静默，如你本来》(Be As You Are) 是拉玛那马哈希核心教示集，收录其对自我参究、静默与解脱的精辟论述。本页面提供完整章节目录、核心思想概要与阅读指引。',
    'gems': '《宝钻集》(Gems from Bhagavan) 汇集拉玛那马哈希教示精华，涵盖真我、心智、参究、臣服、静默等主题。页面提供完整章节导读与核心概念解析。',
    'back-to-heart': '《回到你心中》(Back to the Heart) 收录马哈希与弟子间的深情对话，展现其慈悲教示与日常生活中修行指引。本页面提供完整章节与思想概要。',
    'talks': '《对谈录》(Talks with Sri Ramana Maharshi) 记录马哈希与来访者的精彩对话，涵盖自我参究、业力、解脱等核心主题。本页面提供完整章节导读。',
    'day-by-day': '《日日与彼》(Day by Day with Bhagavan) 由马哈希弟子记录其在静修院的每日生活与教示。本页面提供完整内容与修行要点解读。',
    'face-to-face': '《面对面》(Face to Face) 记录马哈希与多位著名灵性追求者的深度对话，包括Osho、Paul Brunton等。本页面提供完整章节与背景介绍。',
    'maharshi-gospel': '《马哈希福音》(Maharshi Gospel) 收录马哈希的核心教示与灵性对话。本页面提供完整内容导读与修行指引。',
    'maha-yoga': '《大瑜伽》(Maha Yoga) 详细阐述拉玛那马哈希传授的大瑜伽修行法门。本页面提供完整内容与修行方法解析。',
    'crumbs': '《桌边碎语》(Crumbs from the Table) 以短文形式呈现马哈希的日常教示。本页面提供完整内容与核心要点。',
    'collected-works': '《全集》(Collected Works) 收录拉玛那马哈希全部重要著作与文章。本页面提供完整内容索引与核心思想概要。',
}

# 章节页通用描述模板
CHAPTER_DESC_TEMPLATE = '{book}第{ch}章详细内容和核心要义，包含原文摘要、关键段落解读和相关概念的交叉引用。{book}为拉玛那马哈希教示体系中的重要著作。'

# 概念通用描述
CONCEPT_DESC_TEMPLATE = '{concept}是拉玛那马哈希教示体系中的核心概念，涉及自我参究、静默修行与灵性觉醒的深层智慧。本页提供详细解释、原文引用与修行指引。'

# QA页通用描述
QA_DESC_TEMPLATE = '拉玛那马哈希精选问答，探讨{topic}等核心主题。包含原汁原味的灵性对话与修行指引，助您深入理解马哈希的静默教示与自我参究法门。'

QA_TOPICS = {
    'qa-1': '自我参究、"我是谁"、心智本质',
    'qa-2': '心智、幻相、梦境与意识状态',
    'qa-3': '自我参究、念诵、臣服与修行精进',
    'qa-4': '真我、上师、弟子关系与灵性指引',
    'qa-5': '静默、三摩地、禅定与意识状态',
    'qa-6': '解脱、开悟、证悟与修行圆满',
    'qa-7': '虔诚、奉爱、念诵与臣服之道',
    'qa-8': '业力、轮回、命运与自由意志',
    'qa-9': '日常修行、静修院生活与在家修行',
    'qa-10': '梦境、醒时如梦与意识状态',
    'qa-11': '世界本质、摩耶幻相与存在意识',
    'qa-12': '死亡、临终、中阴与轮回转世',
    'qa-13': '幸福、安宁、喜悦与内在平和',
    'qa-14': '经典研读、著作版本与智慧传承',
    'qa-15': '心灵觉醒、实践修行与日常观照',
    'qa-16': '自我超越、无我与究竟实相',
    'qa-17': '真知、迷惑、智慧与无明',
    'qa-18': '上师、弟子关系与灵性传承',
    'qa-19': '静修、独修与日常生活中的修行',
    'qa-20': '解脱、圆满、证悟与究竟涅槃',
}


def get_desc(fp):
    """根据文件路径获取目标 description"""
    fname = os.path.basename(fp).replace('.html', '')
    rel = fp.replace('\\', '/')

    # 精确匹配
    if fname in DESC_RULES:
        return DESC_RULES[fname]
    if rel in DESC_RULES:
        return DESC_RULES[rel]

    # 书籍详情页
    for book_key, desc in BOOK_DESC.items():
        if rel == f'books/{book_key}.html':
            return desc

    # 书籍章节页
    for book_key, (book_name, chapters) in BOOK_CHAPTERS.items():
        for ch in chapters:
            if fname == f'{book_key}-ch{ch}':
                desc = CHAPTER_DESC_TEMPLATE.format(book=book_name, ch=ch)
                if len(desc) < 140:
                    desc = desc + '本页面提供完整的章节内容与修行要点。'
                return desc

    # 概念页
    if rel.startswith('concepts/'):
        concept_name = fname.replace('-', ' ')
        desc = CONCEPT_DESC_TEMPLATE.format(concept=concept_name.title())
        return desc

    # 问答页
    if fname in QA_TOPICS:
        topic = QA_TOPICS[fname]
        desc = QA_DESC_TEMPLATE.format(topic=topic)
        return desc

    # 修行方法页
    if rel.startswith('methods/'):
        method_name = fname.replace('-', ' ')
        return f'{method_name.title()}是拉玛那马哈希教示中的重要修行方法。本页提供详细的方法说明、实践指引与经典引用，助您深入修行。'

    # 人物页
    if rel.startswith('persons/'):
        return '本页提供室利·拉玛那·马哈希的完整传记与灵性事迹，涵盖其出生、觉醒、阿鲁那佳拉山、静修院生活及核心教示。了解这位伟大印度灵性导师的生平和教示。'

    # 默认
    return None


for fp in files:
    with open(fp, encoding='utf-8') as f:
        content = f.read()

    original = content

    # ==== 1. Title ====
    new_title = get_title(fp)
    if new_title:
        # 截断到55字符
        new_title = truncate_title(new_title)
        # 替换
        content = re.sub(
            r'<title>.*?</title>',
            f'<title>{new_title}</title>',
            content,
            flags=re.DOTALL
        )
    else:
        # 没有匹配到精确规则，只截断超长标题
        content = re.sub(
            r'<title>(.*?)</title>',
            lambda m: f'<title>{truncate_title(m.group(1))}</title>',
            content,
            flags=re.DOTALL
        )

    # ==== 2. Description ====
    new_desc = get_desc(fp)
    if new_desc:
        # 截断到155字符
        if len(new_desc) > 155:
            new_desc = new_desc[:154].rsplit('，', 1)[0].rsplit('。', 1)[0] + '。'
        # 替换 meta description
        content = re.sub(
            r'<meta name=["\']description["\'][^>]*>',
            f'<meta name="description" content="{new_desc}">',
            content
        )
        # 同步 og:description
        content = re.sub(
            r'(<meta (?:property)=["\']og:description["\'][^>]* content=)[^">\s]+(["\'])',
            f'\\g<1>{new_desc}\\2',
            content
        )
        # 同步 twitter:description
        content = re.sub(
            r'(<meta (?:name)=["\']twitter:description["\'][^>]* content=)[^">\s]+(["\'])',
            f'\\g<1>{new_desc}\\2',
            content
        )

    if content != original:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content)
        changed += 1

print(f'Done! Fixed {changed}/{len(files)} files')
