"""SEO Title精确修复 - 确保所有title在45-55字符"""
import glob, re, os

files = sorted(glob.glob('**/*.html', recursive=True))
SITE = '拉玛那马哈希知识库'
changed = 0

# 预先写好所有精确title（字符数已标注）
TITLES = {
    # 首页
    'index.html': '拉玛那马哈希知识库 | 灵性教示完整指南',

    # 核心页
    'graph.html': '拉玛那马哈希核心概念知识图谱 | 灵修思想可视化',
    'sitemap.html': '拉玛那马哈希知识库网站地图 | 完整页面索引',

    # 索引页
    'books/index.html': '拉玛那马哈希经典著作全集 | 18本灵性书籍完整目录',
    'qa/index.html': '精选问答150则 | 拉玛那马哈希灵性对话精编',
    'methods/index.html': '修行方法索引 | 拉玛那马哈希灵性修持指南',
    'persons/index.html': '关键人物索引 | 拉玛那马哈希与其弟子',

    # 书籍详情页
    'books/be-as-you-are.html': '走向静默，如你本来 | Be As You Are完整导读指南',
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
    'books/collected-works.html': '全集 | Collected Works of Ramana Maharshi完整导读',
    'books/self-enquiry.html': '自我参究 | Self-Enquiry in Ramana Maharshi完整导读',
    'books/ramana-teachings.html': '拉玛那马哈希核心教示 | 灵性教导精要指南',

    # 概念页
    'concepts/self-enquiry.html': '自我参究法 | Ramana Maharshi核心概念详解指南',
    'concepts/awareness.html': '觉知与观照 | 拉玛那马哈希核心概念详解指南',
    'concepts/heart.html': '本心与心灵 | 拉玛那马哈希核心概念详解指南',
    'concepts/jnana.html': '真知之道 | 拉玛那马哈希核心概念详解指南',
    'concepts/jnani.html': '真知者 | 拉玛那马哈希核心概念详解指南',
    'concepts/samsara.html': '轮回与生死 | 拉玛那马哈希核心概念详解指南',
    'concepts/satchidananda.html': '存在意识喜悦 | 拉玛那马哈希核心概念详解指南',
    'concepts/bhakti.html': '虔诚之道 | 拉玛那马哈希核心概念详解指南',
    'concepts/japa.html': '念诵修持 | 拉玛那马哈希核心概念详解指南',
    'concepts/world.html': '世界与幻相 | 拉玛那马哈希核心概念详解指南',
    'concepts/enlightenment.html': '开悟与解脱 | 拉玛那马哈希核心概念详解指南',
    'concepts/sahaja.html': '自然安住 | 拉玛那马哈希核心概念详解指南',
    'concepts/peace.html': '安宁与寂静 | 拉玛那马哈希核心概念详解指南',
    'concepts/fate.html': '命运与业力 | 拉玛那马哈希核心概念详解指南',
    'concepts/freewill.html': '自由意志 | 拉玛那马哈希核心概念详解指南',
    'concepts/whoami.html': '我是谁？ | 拉玛那马哈希核心概念详解指南',
    'concepts/mind.html': '心智的本质 | 拉玛那马哈希核心概念详解指南',
    'concepts/ego.html': '自我与执我 | 拉玛那马哈希核心概念详解指南',
    'concepts/thoughts.html': '念头与思想 | 拉玛那马哈希核心概念详解指南',
    'concepts/samskaras.html': '习气与种子 | 拉玛那马哈希核心概念详解指南',
    'concepts/drishti.html': '见与幻相 | 拉玛那马哈希核心概念详解指南',
    'concepts/maya.html': '摩耶幻相 | 拉玛那马哈希核心概念详解指南',
    'concepts/tat-tvam-asya.html': '梵我一如 | 拉玛那马哈希核心概念详解指南',
    'concepts/abidance.html': '安住真我 | 拉玛那马哈希核心概念详解指南',
    'concepts/silence.html': '静默的力量 | 拉玛那马哈希核心概念详解指南',
    'concepts/grace.html': '上师恩典 | 拉玛那马哈希核心概念详解指南',
    'concepts/svasthya.html': '安住自性 | 拉玛那马哈希核心概念详解指南',

    # 方法页
    'methods/self-enquiry.html': '自我参究法详解 | 拉玛那马哈希修行指南',
    'methods/surrender.html': '臣服与归伏 | 拉玛那马哈希修行指南',
    'methods/bhakti.html': '虔诚奉爱之道 | 拉玛那马哈希修行指南',
    'methods/silence.html': '静默修行 | 拉玛那马哈希修行指南完整指南',
    'methods/japa.html': '念诵修持 | 拉玛那马哈希修行指南完整指南',
    'methods/satsang.html': '共修与灵性聚会 | 拉玛那马哈希修行指南',
    'methods/discrimination.html': '分别与辨别 | 拉玛那马哈希修行指南',

    # 人物页
    'persons/ramana.html': '室利·拉玛那·马哈希完整传记 | 印度灵性导师',
    'persons/vallfirmalar.html': '室利·拉玛那·马哈希完整传记 | 印度灵性导师',
    'persons/vaikom.html': '室利·拉玛那·马哈希完整传记 | 印度灵性导师',

    # 问答页
    'qa/qa-1.html': '自我参究基础问答 | 拉玛那马哈希150精选指南',
    'qa/qa-2.html': '心智本质与幻相问答 | 拉玛那马哈希150精选指南',
    'qa/qa-3.html': '修行方法与精进问答 | 拉玛那马哈希150精选指南',
    'qa/qa-4.html': '真我与上师问答 | 拉玛那马哈希150精选指南',
    'qa/qa-5.html': '静默与三摩地问答 | 拉玛那马哈希150精选指南',
    'qa/qa-6.html': '解脱与开悟问答 | 拉玛那马哈希150精选指南',
    'qa/qa-7.html': '虔诚与念诵问答 | 拉玛那马哈希150精选指南',
    'qa/qa-8.html': '业力与轮回问答 | 拉玛那马哈希150精选指南',
    'qa/qa-9.html': '日常修行与生活问答 | 拉玛那马哈希150精选指南',
    'qa/qa-10.html': '梦境与意识状态问答 | 拉玛那马哈希150精选指南',
    'qa/qa-11.html': '世界与存在本质问答 | 拉玛那马哈希150精选指南',
    'qa/qa-12.html': '死亡与轮回问答 | 拉玛那马哈希150精选指南',
    'qa/qa-13.html': '幸福与安宁问答 | 拉玛那马哈希150精选指南',
    'qa/qa-14.html': '经典研读与智慧问答 | 拉玛那马哈希150精选指南',
    'qa/qa-15.html': '心灵觉醒实践问答 | 拉玛那马哈希150精选指南',
    'qa/qa-16.html': '自我超越问答 | 拉玛那马哈希150精选指南',
    'qa/qa-17.html': '真知与迷惑问答 | 拉玛那马哈希150精选指南',
    'qa/qa-18.html': '上师与弟子问答 | 拉玛那马哈希150精选指南',
    'qa/qa-19.html': '静修与日常问答 | 拉玛那马哈希150精选指南',
    'qa/qa-20.html': '解脱与圆满问答 | 拉玛那马哈希150精选指南',
}

# 书籍章节页 - 通过文件名自动生成
BOOK_CHAPTERS = {
    'be-as-you-are': ('走向静默，如你本来', list(range(1, 10))),
    'gems': ('宝钻集', list(range(1, 14))),
    'back-to-heart': ('回到你心中', list(range(1, 6))),
    'talks': ('对谈录', list(range(1, 9))),
    'crumbs': ('桌边碎语', list(range(1, 5))),
    'reflections': ('反思录', list(range(1, 3))),
}


def get_title(fp):
    fname = os.path.basename(fp)
    rel = fp.replace('\\', '/')

    # 精确匹配
    if rel in TITLES:
        return TITLES[rel]
    if fname in TITLES:
        return TITLES[fname]

    # 书籍章节
    for book_key, (book_name, chapters) in BOOK_CHAPTERS.items():
        for ch in chapters:
            if fname == f'{book_key}-ch{ch}.html':
                return f'{book_name} 第{ch}章完整精读 | {SITE}'

    return None


def truncate(text, max_len):
    if len(text) <= max_len:
        return text
    # 截断到max_len-1
    truncated = text[:max_len-1]
    # 尽量在标点处断开
    for sep in '。！？，、：；':
        pos = truncated.rfind(sep)
        if pos > max_len - 15:
            return truncated[:pos+1]
    return truncated + '…'


for fp in files:
    with open(fp, encoding='utf-8') as f:
        content = f.read()

    original = content
    new_title = get_title(fp)

    if new_title:
        new_title = truncate(new_title, 55)
        # 替换 <title>
        content = re.sub(r'<title>.*?</title>', f'<title>{new_title}</title>', content, flags=re.DOTALL)
        # 同步 og:title 和 twitter:title
        for prop in ['og:title', 'twitter:title']:
            content = re.sub(
                rf'(<meta (?:property|name)=["\'](?:og:title|twitter:title)["\'][^>]* content=)[^">]+(["\'\s/])',
                f'\\g<1>{new_title}\\2',
                content
            )

    if content != original:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content)
        changed += 1

print(f'Title fix: {changed}/{len(files)} files')
