"""SEO Title 严格45-55字符 - 最终版"""
import glob, re, os

files = sorted(glob.glob('**/*.html', recursive=True))
SITE = '拉玛那马哈希知识库'
changed = 0

TITLES = {
    # ===== 书籍章节页 =====
    'books/be-as-you-are-ch1.html': '走向静默，如你本来 第一章：我是谁？自我参究精读指南详解 | 拉玛那马哈希知识库',
    'books/be-as-you-are-ch2.html': '走向静默，如你本来 第二章：自我参究法详解与修行实践指引 | 拉玛那马哈希知识库',
    'books/be-as-you-are-ch3.html': '走向静默，如你本来 第三章：心智的本质与超越幻相之道修行指南 | 拉玛那马哈希知识库',
    'books/be-as-you-are-ch4.html': '走向静默，如你本来 第四章：静默的力量与内在修行的意义指南 | 拉玛那马哈希知识库',
    'books/be-as-you-are-ch5.html': '走向静默，如你本来 第五章：自我了悟的境界与实修方法指引详解 | 拉玛那马哈希知识库',
    'books/be-as-you-are-ch6.html': '走向静默，如你本来 第六章：上师的意义与恩典传承的智慧详解 | 拉玛那马哈希知识库',
    'books/be-as-you-are-ch7.html': '走向静默，如你本来 第七章：上师恩典与弟子修行的关系详解 | 拉玛那马哈希知识库',
    'books/be-as-you-are-ch8.html': '走向静默，如你本来 第八章：解脱的本质与觉醒智慧详解修行指南 | 拉玛那马哈希知识库',
    'books/be-as-you-are-ch9.html': '走向静默，如你本来 第九章：修行者指南与最终结论要义详解 | 拉玛那马哈希知识库',

    'books/gems-ch1.html': '宝钻集 第一章：幸福的本质与内在安宁的修行智慧详解指南 | 拉玛那马哈希知识库',
    'books/gems-ch2.html': '宝钻集 第二章：真我与非我的辨别修行智慧详解指南精读 | 拉玛那马哈希知识库',
    'books/gems-ch3.html': '宝钻集 第三章：心智的本质与超越幻相的修行之道详解 | 拉玛那马哈希知识库',
    'books/gems-ch4.html': '宝钻集 第四章：我是谁？自我参究法门修行精读指南详解 | 拉玛那马哈希知识库',
    'books/gems-ch5.html': '宝钻集 第五章：臣服与归伏的修行智慧精读指南详解 | 拉玛那马哈希知识库',
    'books/gems-ch6.html': '宝钻集 第六章：存在意识喜悦三态的修行智慧精读指南 | 拉玛那马哈希知识库',
    'books/gems-ch7.html': '宝钻集 第七章：恩典与上师的修行智慧精读指南详解 | 拉玛那马哈希知识库',
    'books/gems-ch8.html': '宝钻集 第八章：自我了悟的境界修行智慧精读指南详解 | 拉玛那马哈希知识库',
    'books/gems-ch9.html': '宝钻集 第九章：本心的本质与安宁的修行智慧精读指南 | 拉玛那马哈希知识库',
    'books/gems-ch10.html': '宝钻集 第十章：出离的意义与修行智慧精读指南详解 | 拉玛那马哈希知识库',
    'books/gems-ch11.html': '宝钻集 第十一章：命运与自由意志的修行智慧详解指南 | 拉玛那马哈希知识库',
    'books/gems-ch12.html': '宝钻集 第十二章：觉者的境界与解脱智慧精读指南详解 | 拉玛那马哈希知识库',
    'books/gems-ch13.html': '宝钻集 第十三章：杂项与修行智慧精读指南完整详解 | 拉玛那马哈希知识库',

    'books/back-to-heart-ch1.html': '回到你心中 第一章：心的本质与回归本心修行指南详解 | 拉玛那马哈希知识库',
    'books/back-to-heart-ch2.html': '回到你心中 第二章：回归之路与心灵觉醒修行详解指南 | 拉玛那马哈希知识库',
    'books/back-to-heart-ch3.html': '回到你心中 第三章：自我参究与内在修行智慧指南详解 | 拉玛那马哈希知识库',
    'books/back-to-heart-ch4.html': '回到你心中 第四章：放下与臣服的智慧修行详解指南 | 拉玛那马哈希知识库',
    'books/back-to-heart-ch5.html': '回到你心中 第五章：真理在你心中修行指南详解精读 | 拉玛那马哈希知识库',

    'books/talks-ch1.html': '对谈录 第一章：自我参究与解脱修行对话指南详解精读 | 拉玛那马哈希知识库',
    'books/talks-ch2.html': '对谈录 第二章：心智与幻相修行对话指南详解精读 | 拉玛那马哈希知识库',
    'books/talks-ch3.html': '对谈录 第三章：静默与三摩地修行对话指南详解精读 | 拉玛那马哈希知识库',
    'books/talks-ch4.html': '对谈录 第四章：上师与恩典修行对话指南详解精读 | 拉玛那马哈希知识库',
    'books/talks-ch5.html': '对谈录 第五章：业力与命运修行对话指南详解精读 | 拉玛那马哈希知识库',
    'books/talks-ch6.html': '对谈录 第六章：开悟与解脱修行对话指南详解精读 | 拉玛那马哈希知识库',
    'books/talks-ch7.html': '对谈录 第七章：日常修行与觉醒智慧对话精读指南 | 拉玛那马哈希知识库',
    'books/talks-ch8.html': '对谈录 第八章：真理与实相修行对话指南详解精读 | 拉玛那马哈希知识库',

    'books/crumbs-ch1.html': '桌边碎语 第一章：日常教示与静默智慧修行指南精读详解 | 拉玛那马哈希知识库',
    'books/crumbs-ch2.html': '桌边碎语 第二章：日常教示与自我参究修行指南精读详解 | 拉玛那马哈希知识库',
    'books/crumbs-ch3.html': '桌边碎语 第三章：日常教示与安宁智慧修行指南精读详解 | 拉玛那马哈希知识库',
    'books/crumbs-ch4.html': '桌边碎语 第四章：日常教示与解脱智慧修行指南精读详解 | 拉玛那马哈希知识库',

    'books/reflections-ch1.html': '反思录 第一章：灵性反思与自我参究修行指南精读详解 | 拉玛那马哈希知识库',
    'books/reflections-ch2.html': '反思录 第二章：灵性反思与修行智慧指南精读详解 | 拉玛那马哈希知识库',

    # ===== 其他页面 =====
    'index.html': '拉玛那马哈希知识库 | 灵性教示完整指南 | 拉玛那马哈希知识库',
    'graph.html': '拉玛那马哈希核心概念知识图谱 | 灵修思想可视化 | 拉玛那马哈希知识库',
    'sitemap.html': '拉玛那马哈希知识库网站地图 | 完整页面索引 | 拉玛那马哈希知识库',
    'books/index.html': '拉玛那马哈希经典著作全集 | 18本灵性书籍完整目录 | 拉玛那马哈希知识库',
    'qa/index.html': '精选问答150则 | 拉玛那马哈希灵性对话精编指南 | 拉玛那马哈希知识库',
    'methods/index.html': '修行方法索引 | 拉玛那马哈希灵性修持指南完整版 | 拉玛那马哈希知识库',
    'persons/index.html': '关键人物索引 | 拉玛那马哈希与其弟子传记指南 | 拉玛那马哈希知识库',

    'books/be-as-you-are.html': '走向静默，如你本来 Be As You Are完整导读指南详解 | 拉玛那马哈希知识库',
    'books/gems.html': '宝钻集 Gems from Bhagavan完整导读指南详解 | 拉玛那马哈希知识库',
    'books/back-to-heart.html': '回到你心中 Back to the Heart完整导读指南详解 | 拉玛那马哈希知识库',
    'books/talks.html': '对谈录 Talks with Sri Ramana Maharshi完整导读指南 | 拉玛那马哈希知识库',
    'books/day-by-day.html': '日日与彼 Day by Day with Bhagavan完整导读指南 | 拉玛那马哈希知识库',
    'books/face-to-face.html': '面对面 Face to Face完整导读指南详解 | 拉玛那马哈希知识库',
    'books/search-in-secret-india.html': '秘密印度 A Search in Secret India完整导读指南 | 拉玛那马哈希知识库',
    'books/maharshi-gospel.html': '马哈希福音 Maharshi Gospel完整导读指南详解 | 拉玛那马哈希知识库',
    'books/maha-yoga.html': '大瑜伽 Maha Yoga完整导读指南详解 | 拉玛那马哈希知识库',
    'books/guru-vachaka-kovai.html': '上师言颂 Guru Vachaka Kovai完整导读指南 | 拉玛那马哈希知识库',
    'books/timeless-in-time.html': '时代中的永恒 Timeless in Time完整导读指南 | 拉玛那马哈希知识库',
    'books/reflections.html': '反思录 Reflections完整导读指南详解 | 拉玛那马哈希知识库',
    'books/spiritual-stories.html': '灵性故事 Spiritual Stories完整导读指南详解 | 拉玛那马哈希知识库',
    'books/surpassing-love.html': '超越爱与恩典 Surpassing Love完整导读指南 | 拉玛那马哈希知识库',
    'books/crumbs.html': '桌边碎语 Crumbs from the Table完整导读指南详解 | 拉玛那马哈希知识库',
    'books/collected-works.html': '全集 Collected Works完整导读指南详解 | 拉玛那马哈希知识库',
    'books/self-enquiry.html': '自我参究 Self-Enquiry in Ramana Maharshi完整导读 | 拉玛那马哈希知识库',
    'books/ramana-teachings.html': '拉玛那马哈希核心教示 | 灵性教导精要指南 | 拉玛那马哈希知识库',

    'concepts/self-enquiry.html': '自我参究法 Self-Enquiry | 拉玛那马哈希核心概念详解指南 | 拉玛那马哈希知识库',
    'concepts/awareness.html': '觉知与观照 Awareness | 拉玛那马哈希核心概念详解指南 | 拉玛那马哈希知识库',
    'concepts/heart.html': '本心与心灵 Heart | 拉玛那马哈希核心概念详解指南 | 拉玛那马哈希知识库',
    'concepts/jnana.html': '真知之道 Jnana | 拉玛那马哈希核心概念详解指南 | 拉玛那马哈希知识库',
    'concepts/jnani.html': '真知者 Jnani | 拉玛那马哈希核心概念详解指南 | 拉玛那马哈希知识库',
    'concepts/samsara.html': '轮回与生死 Samsara | 拉玛那马哈希核心概念详解指南 | 拉玛那马哈希知识库',
    'concepts/satchidananda.html': '存在意识喜悦 Satchidananda | 拉玛那核心概念详解指南 | 拉玛那马哈希知识库',
    'concepts/bhakti.html': '虔诚之道 Bhakti | 拉玛那马哈希核心概念详解指南 | 拉玛那马哈希知识库',
    'concepts/japa.html': '念诵修持 Japa | 拉玛那马哈希核心概念详解指南 | 拉玛那马哈希知识库',
    'concepts/world.html': '世界与幻相 World | 拉玛那马哈希核心概念详解指南 | 拉玛那马哈希知识库',
    'concepts/enlightenment.html': '开悟与解脱 Enlightenment | 拉玛那马哈希核心概念详解指南 | 拉玛那马哈希知识库',
    'concepts/sahaja.html': '自然安住 Sahaja | 拉玛那马哈希核心概念详解指南 | 拉玛那马哈希知识库',
    'concepts/peace.html': '安宁与寂静 Peace | 拉玛那马哈希核心概念详解指南 | 拉玛那马哈希知识库',
    'concepts/fate.html': '命运与业力 Fate | 拉玛那马哈希核心概念详解指南 | 拉玛那马哈希知识库',
    'concepts/freewill.html': '自由意志 Free Will | 拉玛那马哈希核心概念详解指南 | 拉玛那马哈希知识库',
    'concepts/whoami.html': '我是谁 Who Am I？ | 拉玛那马哈希核心概念详解指南 | 拉玛那马哈希知识库',
    'concepts/mind.html': '心智的本质 Mind | 拉玛那马哈希核心概念详解指南 | 拉玛那马哈希知识库',
    'concepts/ego.html': '自我与执我 Ego | 拉玛那马哈希核心概念详解指南 | 拉玛那马哈希知识库',
    'concepts/thoughts.html': '念头与思想 Thoughts | 拉玛那马哈希核心概念详解指南 | 拉玛那马哈希知识库',
    'concepts/samskaras.html': '习气与种子 Samskaras | 拉玛那马哈希核心概念详解指南 | 拉玛那马哈希知识库',
    'concepts/drishti.html': '见与幻相 Drishti | 拉玛那马哈希核心概念详解指南 | 拉玛那马哈希知识库',
    'concepts/maya.html': '摩耶幻相 Maya | 拉玛那马哈希核心概念详解指南 | 拉玛那马哈希知识库',
    'concepts/tat-tvam-asya.html': '梵我一如 Tat Tvam Asya | 拉玛那核心概念详解指南 | 拉玛那马哈希知识库',
    'concepts/abidance.html': '安住真我 Abidance | 拉玛那马哈希核心概念详解指南 | 拉玛那马哈希知识库',
    'concepts/silence.html': '静默的力量 Silence | 拉玛那马哈希核心概念详解指南 | 拉玛那马哈希知识库',
    'concepts/grace.html': '上师恩典 Grace | 拉玛那马哈希核心概念详解指南 | 拉玛那马哈希知识库',
    'concepts/svasthya.html': '安住自性 Svasthya | 拉玛那马哈希核心概念详解指南 | 拉玛那马哈希知识库',

    'methods/self-enquiry.html': '自我参究法详解 Self-Enquiry | 拉玛那修行指南 | 拉玛那马哈希知识库',
    'methods/surrender.html': '臣服与归伏 Surrender | 拉玛那马哈希修行指南 | 拉玛那马哈希知识库',
    'methods/bhakti.html': '虔诚奉爱之道 Bhakti | 拉玛那马哈希修行指南 | 拉玛那马哈希知识库',
    'methods/silence.html': '静默修行 Silence | 拉玛那马哈希修行指南详解 | 拉玛那马哈希知识库',
    'methods/japa.html': '念诵修持 Japa | 拉玛那马哈希修行指南详解 | 拉玛那马哈希知识库',
    'methods/satsang.html': '共修与灵性聚会 Satsang | 拉玛那修行指南 | 拉玛那马哈希知识库',
    'methods/discrimination.html': '分别与辨别 Viveka | 拉玛那马哈希修行指南 | 拉玛那马哈希知识库',

    'persons/ramana.html': '室利·拉玛那·马哈希完整传记 | 印度灵性导师 | 拉玛那马哈希知识库',
    'persons/vallfirmalar.html': '室利·拉玛那·马哈希完整传记 | 印度灵性导师 | 拉玛那马哈希知识库',
    'persons/vaikom.html': '室利·拉玛那·马哈希完整传记 | 印度灵性导师 | 拉玛那马哈希知识库',

    'qa/qa-1.html': '自我参究基础问答 | 拉玛那马哈希150精选指南 | 拉玛那马哈希知识库',
    'qa/qa-2.html': '心智本质与幻相问答 | 拉玛那马哈希150精选指南 | 拉玛那马哈希知识库',
    'qa/qa-3.html': '修行方法与精进问答 | 拉玛那马哈希150精选指南 | 拉玛那马哈希知识库',
    'qa/qa-4.html': '真我与上师问答 | 拉玛那马哈希150精选指南 | 拉玛那马哈希知识库',
    'qa/qa-5.html': '静默与三摩地问答 | 拉玛那马哈希150精选指南 | 拉玛那马哈希知识库',
    'qa/qa-6.html': '解脱与开悟问答 | 拉玛那马哈希150精选指南 | 拉玛那马哈希知识库',
    'qa/qa-7.html': '虔诚与念诵问答 | 拉玛那马哈希150精选指南 | 拉玛那马哈希知识库',
    'qa/qa-8.html': '业力与轮回问答 | 拉玛那马哈希150精选指南 | 拉玛那马哈希知识库',
    'qa/qa-9.html': '日常修行与生活问答 | 拉玛那马哈希150精选指南 | 拉玛那马哈希知识库',
    'qa/qa-10.html': '梦境与意识状态问答 | 拉玛那马哈希150精选指南 | 拉玛那马哈希知识库',
    'qa/qa-11.html': '世界与存在本质问答 | 拉玛那马哈希150精选指南 | 拉玛那马哈希知识库',
    'qa/qa-12.html': '死亡与轮回问答 | 拉玛那马哈希150精选指南 | 拉玛那马哈希知识库',
    'qa/qa-13.html': '幸福与安宁问答 | 拉玛那马哈希150精选指南 | 拉玛那马哈希知识库',
    'qa/qa-14.html': '经典研读与智慧问答 | 拉玛那马哈希150精选指南 | 拉玛那马哈希知识库',
    'qa/qa-15.html': '心灵觉醒实践问答 | 拉玛那马哈希150精选指南 | 拉玛那马哈希知识库',
    'qa/qa-16.html': '自我超越问答 | 拉玛那马哈希150精选指南 | 拉玛那马哈希知识库',
    'qa/qa-17.html': '真知与迷惑问答 | 拉玛那马哈希150精选指南 | 拉玛那马哈希知识库',
    'qa/qa-18.html': '上师与弟子问答 | 拉玛那马哈希150精选指南 | 拉玛那马哈希知识库',
    'qa/qa-19.html': '静修与日常问答 | 拉玛那马哈希150精选指南 | 拉玛那马哈希知识库',
    'qa/qa-20.html': '解脱与圆满问答 | 拉玛那马哈希150精选指南 | 拉玛那马哈希知识库',
}

# 验证
bad = {k: v for k, v in TITLES.items() if len(v) < 45 or len(v) > 55}
if bad:
    print(f'WARNING: {len(bad)} titles out of range')
    for k, v in sorted(bad.items()):
        print(f'  [{len(v)}] {k}: {v}')
else:
    print(f'All {len(TITLES)} titles OK (45-55 chars)')

# 应用
for fp in files:
    with open(fp, encoding='utf-8') as f:
        content = f.read()

    rel = fp.replace('\\', '/')
    new_title = TITLES.get(rel) or TITLES.get(os.path.basename(fp))

    if new_title:
        # 截断超长标题
        if len(new_title) > 55:
            new_title = new_title[:54] + '…'
        original = content
        content = re.sub(r'<title>.*?</title>', f'<title>{new_title}</title>', content, flags=re.DOTALL)
        # 同步 og:title 和 twitter:title
        for pat, attr in [('og:title', 'property'), ('twitter:title', 'name')]:
            content = re.sub(
                rf'<meta {attr}=["\']' + pat + r'["\'][^>]*>',
                f'<meta {attr}="{pat}" content="{new_title}">',
                content
            )
        if content != original:
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(content)
            changed += 1

print(f'Applied: {changed}/{len(files)} files changed')
