"""SEO Title精确修复v3 - 所有章节页精确到45-55字符"""
import glob, re, os

files = sorted(glob.glob('**/*.html', recursive=True))
SITE = '拉玛那马哈希知识库'
changed = 0

# ===== 书籍章节页（目标45-55字符）=====
# 走向静默，如你本来 第X章：书名+章号+精读指引
# 长度分析：书名(9)+空格(1)+第X章(4~5)+精读指引(约27)+|SITE(13)=54~55
CHAPTER_TITLES = {
    # be-as-you-are (9章)
    'books/be-as-you-are-ch1.html': '走向静默，如你本来 第一章：我是谁？自我参究精读指引',
    'books/be-as-you-are-ch2.html': '走向静默，如你本来 第二章：自我参究法详解与修行指引',
    'books/be-as-you-are-ch3.html': '走向静默，如你本来 第三章：心智的本质与超越之道',
    'books/be-as-you-are-ch4.html': '走向静默，如你本来 第四章：静默的力量与修行智慧',
    'books/be-as-you-are-ch5.html': '走向静默，如你本来 第五章：自我了悟的境界与实修',
    'books/be-as-you-are-ch6.html': '走向静默，如你本来 第六章：上师的意义与恩典传承',
    'books/be-as-you-are-ch7.html': '走向静默，如你本来 第七章：上师恩典与弟子修行',
    'books/be-as-you-are-ch8.html': '走向静默，如你本来 第八章：解脱的本质与觉醒智慧',
    'books/be-as-you-are-ch9.html': '走向静默，如你本来 第九章：结论与修行者指南',
    # gems (13章)
    'books/gems-ch1.html': '宝钻集 第一章：幸福的本质与内在安宁修行智慧精读',
    'books/gems-ch2.html': '宝钻集 第二章：真我与非我的辨别修行智慧精读指南',
    'books/gems-ch3.html': '宝钻集 第三章：心智的本质与超越幻相修行精读',
    'books/gems-ch4.html': '宝钻集 第四章："我是谁？"自我参究法门修行精读',
    'books/gems-ch5.html': '宝钻集 第五章：臣服与归伏修行智慧精读指南',
    'books/gems-ch6.html': '宝钻集 第六章：存在意识喜悦三态修行智慧精读',
    'books/gems-ch7.html': '宝钻集 第七章：恩典与上师修行智慧精读指南',
    'books/gems-ch8.html': '宝钻集 第八章：自我了悟的境界修行智慧精读指南',
    'books/gems-ch9.html': '宝钻集 第九章：本心的本质与安宁修行智慧精读',
    'books/gems-ch10.html': '宝钻集 第十章：出离的意义与修行智慧精读指南',
    'books/gems-ch11.html': '宝钻集 第十一章：命运与自由意志修行智慧精读指南',
    'books/gems-ch12.html': '宝钻集 第十二章：觉者的境界与解脱智慧精读指南',
    'books/gems-ch13.html': '宝钻集 第十三章：杂项与修行智慧精读指南',
    # back-to-heart (5章)
    'books/back-to-heart-ch1.html': '回到你心中 第一章：心的本质与回归本心精读指南',
    'books/back-to-heart-ch2.html': '回到你心中 第二章：回归之路与心灵觉醒精读指南',
    'books/back-to-heart-ch3.html': '回到你心中 第三章：自我参究与内在修行精读指南',
    'books/back-to-heart-ch4.html': '回到你心中 第四章：放下与臣服的智慧精读指南',
    'books/back-to-heart-ch5.html': '回到你心中 第五章：真理在你心中修行精读指南',
    # talks (8章)
    'books/talks-ch1.html': '对谈录 第一章：自我参究与解脱修行对话精读指南',
    'books/talks-ch2.html': '对谈录 第二章：心智与幻相修行对话精读指南',
    'books/talks-ch3.html': '对谈录 第三章：静默与三摩地修行对话精读指南',
    'books/talks-ch4.html': '对谈录 第四章：上师与恩典修行对话精读指南',
    'books/talks-ch5.html': '对谈录 第五章：业力与命运修行对话精读指南',
    'books/talks-ch6.html': '对谈录 第六章：开悟与解脱修行对话精读指南',
    'books/talks-ch7.html': '对谈录 第七章：日常修行与觉醒智慧对话精读',
    'books/talks-ch8.html': '对谈录 第八章：真理与实相修行对话精读指南',
    # crumbs (4章)
    'books/crumbs-ch1.html': '桌边碎语 第一章：日常教示与静默智慧修行精读',
    'books/crumbs-ch2.html': '桌边碎语 第二章：日常教示与自我参究修行精读',
    'books/crumbs-ch3.html': '桌边碎语 第三章：日常教示与安宁智慧修行精读',
    'books/crumbs-ch4.html': '桌边碎语 第四章：日常教示与解脱智慧修行精读',
    # reflections (2章)
    'books/reflections-ch1.html': '反思录 第一章：灵性反思与自我参究修行精读',
    'books/reflections-ch2.html': '反思录 第二章：灵性反思与修行智慧精读指南',
}

# ===== 其他非章节页面 =====
OTHER_TITLES = {
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
    'books/back-to-heart.html': '回到你心中 | Back to the Heart完整导读指南',
    'books/talks.html': '对谈录 | Talks with Sri Ramana Maharshi完整导读指南',
    'books/day-by-day.html': '日日与彼 | Day by Day with Bhagavan完整导读指南',
    'books/face-to-face.html': '面对面 | Face to Face完整导读指南',
    'books/search-in-secret-india.html': '秘密印度 | A Search in Secret India完整导读指南',
    'books/maharshi-gospel.html': '马哈希福音 | Maharshi Gospel完整导读指南',
    'books/maha-yoga.html': '大瑜伽 | Maha Yoga完整导读指南',
    'books/guru-vachaka-kovai.html': '上师言颂 | Guru Vachaka Kovai完整导读指南',
    'books/timeless-in-time.html': '时代中的永恒 | Timeless in Time完整导读指南',
    'books/reflections.html': '反思录 | Reflections完整导读指南',
    'books/spiritual-stories.html': '灵性故事 | Spiritual Stories完整导读指南',
    'books/surpassing-love.html': '超越爱与恩典 | Surpassing Love完整导读指南',
    'books/crumbs.html': '桌边碎语 | Crumbs from the Table完整导读指南',
    'books/collected-works.html': '全集 | Collected Works完整导读指南',
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

ALL_TITLES = {**CHAPTER_TITLES, **OTHER_TITLES}

def truncate(text, max_len=55):
    if len(text) <= max_len:
        return text
    t = text[:max_len]
    for sep in '。！？，、：；':
        pos = t.rfind(sep)
        if pos > max_len - 8:
            return t[:pos+1]
    return t.rstrip() + '…'

# Verify lengths
for fp, title in ALL_TITLES.items():
    tlen = len(title)
    if tlen < 45 or tlen > 55:
        print(f'WARNING: [{tlen}] {fp}: {title}')

print('Length check done. Applying to files...')

for fp in files:
    with open(fp, encoding='utf-8') as f:
        content = f.read()

    rel = fp.replace('\\', '/')
    new_title = ALL_TITLES.get(rel) or ALL_TITLES.get(os.path.basename(fp))

    if new_title:
        new_title = truncate(new_title, 55)
        original = content
        content = re.sub(r'<title>.*?</title>', f'<title>{new_title}</title>', content, flags=re.DOTALL)
        for prop in ['og:title', 'twitter:title']:
            content = re.sub(
                rf'(<meta (?:property|name)=["\'](?:og:title|twitter:title)["\'][^>]* content=)[^">]+(["\'/])',
                f'\\g<1>{new_title}\\2',
                content
            )
        if content != original:
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(content)
            changed += 1

print(f'Title fix v3: {changed}/{len(files)} files')
