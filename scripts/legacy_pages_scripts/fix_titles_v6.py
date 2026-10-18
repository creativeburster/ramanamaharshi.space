"""SEO Title修复 - 60-70字符标准标题"""
import glob, re, os

files = sorted(glob.glob('**/*.html', recursive=True))
SITE = '拉玛那马哈希'
SUFFIX = f' | {SITE}'

# 章节页面
CH_TITLES = {
    'books/be-as-you-are-ch1.html': f'走向静默，如你本来 第一章：我是谁？自我参究法精读指南 - 深度解析拉玛那马哈希的核心教示{SUFFIX}',
    'books/be-as-you-are-ch2.html': f'走向静默，如你本来 第二章：自我参究法的详解与修行实践指引 - 拉玛那马哈希灵性教导精读{SUFFIX}',
    'books/be-as-you-are-ch3.html': f'走向静默，如你本来 第三章：心智的本质与超越幻相之道 - 拉玛那马哈希修行智慧详解{SUFFIX}',
    'books/be-as-you-are-ch4.html': f'走向静默，如你本来 第四章：静默的力量与内在修行的意义 - 拉玛那马哈希灵性教示{SUFFIX}',
    'books/be-as-you-are-ch5.html': f'走向静默，如你本来 第五章：自我了悟的境界与实修方法指引 - 拉玛那马哈希修行指南{SUFFIX}',
    'books/be-as-you-are-ch6.html': f'走向静默，如你本来 第六章：上师的意义与恩典传承的智慧 - 拉玛那马哈希核心教示{SUFFIX}',
    'books/be-as-you-are-ch7.html': f'走向静默，如你本来 第七章：上师恩典与弟子修行的关系 - 拉玛那马哈希灵性教导{SUFFIX}',
    'books/be-as-you-are-ch8.html': f'走向静默，如你本来 第八章：解脱的本质与觉醒智慧详解 - 拉玛那马哈希修行指南{SUFFIX}',
    'books/be-as-you-are-ch9.html': f'走向静默，如你本来 第九章：修行者指南与最终结论要义 - 拉玛那马哈希完整教示{SUFFIX}',

    'books/gems-ch1.html': f'宝钻集 第一章：幸福的本质与内在安宁的修行智慧详解 - 拉玛那马哈希灵性教示精选{SUFFIX}',
    'books/gems-ch2.html': f'宝钻集 第二章：真我与非我的辨别修行智慧详解 - 拉玛那马哈希核心教导精读{SUFFIX}',
    'books/gems-ch3.html': f'宝钻集 第三章：心智的本质与超越幻相的修行之道 - 拉玛那马哈希灵性教示{SUFFIX}',
    'books/gems-ch4.html': f'宝钻集 第四章：我是谁？自我参究法门修行精读指南 - 拉玛那马哈希核心修行法{SUFFIX}',
    'books/gems-ch5.html': f'宝钻集 第五章：臣服与归伏的修行智慧精读详解 - 拉玛那马哈希灵性教导精选{SUFFIX}',
    'books/gems-ch6.html': f'宝钻集 第六章：存在意识喜悦三态的修行智慧精读 - 拉玛那马哈希教示精选{SUFFIX}',
    'books/gems-ch7.html': f'宝钻集 第七章：恩典与上师的修行智慧精读详解 - 拉玛那马哈希核心教示{SUFFIX}',
    'books/gems-ch8.html': f'宝钻集 第八章：自我了悟的境界修行智慧精读详解 - 拉玛那马哈希灵性教示{SUFFIX}',
    'books/gems-ch9.html': f'宝钻集 第九章：本心的本质与安宁的修行智慧精读 - 拉玛那马哈希教导精选{SUFFIX}',
    'books/gems-ch10.html': f'宝钻集 第十章：出离的意义与修行智慧精读指南 - 拉玛那马哈希灵性教示{SUFFIX}',
    'books/gems-ch11.html': f'宝钻集 第十一章：命运与自由意志的修行智慧详解 - 拉玛那马哈希核心教导{SUFFIX}',
    'books/gems-ch12.html': f'宝钻集 第十二章：觉者的境界与解脱智慧精读指南 - 拉玛那马哈希修行教示{SUFFIX}',
    'books/gems-ch13.html': f'宝钻集 第十三章：杂项内容与修行智慧精读指南 - 拉玛那马哈希灵性教示{SUFFIX}',

    'books/back-to-heart-ch1.html': f'回到你心中 第一章：心的本质与回归本心的修行指南 - 拉玛那马哈希核心教示{SUFFIX}',
    'books/back-to-heart-ch2.html': f'回到你心中 第二章：回归之路与心灵觉醒的修行详解 - 拉玛那马哈希灵性教导{SUFFIX}',
    'books/back-to-heart-ch3.html': f'回到你心中 第三章：自我参究与内在修行智慧指南 - 拉玛那马哈希核心修行{SUFFIX}',
    'books/back-to-heart-ch4.html': f'回到你心中 第四章：放下与臣服的智慧修行详解 - 拉玛那马哈希灵性教示{SUFFIX}',
    'books/back-to-heart-ch5.html': f'回到你心中 第五章：真理在你心中的修行指南详解 - 拉玛那马哈希核心教导{SUFFIX}',

    'books/talks-ch1.html': f'对谈录 第一章：自我参究与解脱修行的对话指南详解 - 拉玛那马哈希灵性教导{SUFFIX}',
    'books/talks-ch2.html': f'对谈录 第二章：心智与幻相修行的对话指南详解 - 拉玛那马哈希核心教示{SUFFIX}',
    'books/talks-ch3.html': f'对谈录 第三章：静默与三摩地修行的对话指南详解 - 拉玛那马哈希灵性教导{SUFFIX}',
    'books/talks-ch4.html': f'对谈录 第四章：上师与恩典修行的对话指南详解 - 拉玛那马哈希核心修行{SUFFIX}',
    'books/talks-ch5.html': f'对谈录 第五章：业力与命运修行的对话指南详解 - 拉玛那马哈希灵性教示{SUFFIX}',
    'books/talks-ch6.html': f'对谈录 第六章：开悟与解脱修行的对话指南详解 - 拉玛那马哈希教导{SUFFIX}',
    'books/talks-ch7.html': f'对谈录 第七章：日常修行与觉醒智慧的对话精读指南 - 拉玛那马哈希修行{SUFFIX}',
    'books/talks-ch8.html': f'对谈录 第八章：真理与实相修行的对话指南详解 - 拉玛那马哈希灵性教示{SUFFIX}',

    'books/crumbs-ch1.html': f'桌边碎语 第一章：日常教示与静默智慧的修行指南精读 - 拉玛那马哈希教示{SUFFIX}',
    'books/crumbs-ch2.html': f'桌边碎语 第二章：日常教示与自我参究的修行指南精读 - 拉玛那马哈希教导{SUFFIX}',
    'books/crumbs-ch3.html': f'桌边碎语 第三章：日常教示与安宁智慧的修行指南精读 - 拉玛那马哈希教示{SUFFIX}',
    'books/crumbs-ch4.html': f'桌边碎语 第四章：日常教示与解脱智慧的修行指南精读 - 拉玛那马哈希修行{SUFFIX}',

    'books/reflections-ch1.html': f'反思录 第一章：灵性反思与自我参究的修行指南精读 - 拉玛那马哈希教导{SUFFIX}',
    'books/reflections-ch2.html': f'反思录 第二章：灵性反思与修行智慧的指南精读详解 - 拉玛那马哈希教示{SUFFIX}',

    # 日日与彼 - 重点章节
    'books/day-by-day-ch1.html': f'日日与彼 第一章：日常灵性生活与觉醒智慧 - 拉玛那马哈希修行教示精选{SUFFIX}',
    'books/day-by-day-ch2.html': f'日日与彼 第二章：日常灵性生活与静默修行 - 拉玛那马哈希教导精选{SUFFIX}',
    'books/day-by-day-ch3.html': f'日日与彼 第三章：日常灵性生活与自我参究 - 拉玛那马哈希修行指南{SUFFIX}',
    'books/day-by-day-ch4.html': f'日日与彼 第四章：日常灵性生活与三摩地 - 拉玛那马哈希灵性教示{SUFFIX}',
    'books/day-by-day-ch5.html': f'日日与彼 第五章：日常灵性生活与上师恩典 - 拉玛那马哈希核心教导{SUFFIX}',

    # 面对面 - 重点章节
    'books/face-to-face-ch1.html': f'面对面 第一章：与拉玛那马哈希的灵性对话 - 深度修行教示{SUFFIX}',
    'books/face-to-face-ch2.html': f'面对面 第二章：自我参究与解脱的对话 - 拉玛那马哈希教导{SUFFIX}',
    'books/face-to-face-ch3.html': f'面对面 第三章：静默与存在的对话 - 拉玛那马哈希灵性教示{SUFFIX}',
    'books/face-to-face-ch4.html': f'面对面 第四章：心智与真我的对话 - 拉玛那马哈希核心教导{SUFFIX}',
    'books/face-to-face-ch5.html': f'面对面 第五章：上师恩典与弟子修行 - 拉玛那马哈希修行指南{SUFFIX}',

    # 马哈希福音 - 重点章节
    'books/maharshi-gospel-ch1.html': f'马哈希福音 第一章：我是谁？与拉玛那马哈希的对话 - 核心教示{SUFFIX}',
    'books/maharshi-gospel-ch2.html': f'马哈希福音 第二章：心的修行与自我参究 - 拉玛那马哈希教导{SUFFIX}',
    'books/maharshi-gospel-ch3.html': f'马哈希福音 第三章：存在的本质与三摩地 - 拉玛那马哈希教示{SUFFIX}',
    'books/maharshi-gospel-ch4.html': f'马哈希福音 第四章：上师与恩典的教导 - 拉玛那马哈希修行{SUFFIX}',
    'books/maharshi-gospel-ch5.html': f'马哈希福音 第五章：解脱与开悟的智慧 - 拉玛那马哈希核心教导{SUFFIX}',

    # 其他书籍章节
    'books/maha-yoga-ch1.html': f'大瑜伽 第一章：整体瑜伽与拉玛那马哈希 - 灵性修行教导{SUFFIX}',
    'books/search-in-secret-india-ch1.html': f'秘密印度 第一章：寻觅中的灵性发现 - 拉玛那马哈希相遇{SUFFIX}',
    'books/timeless-in-time-ch1.html': f'时代中的永恒 第一章：拉玛那马哈希的生平与教导{SUFFIX}',
    'books/spiritual-stories-ch1.html': f'灵性故事 第一章：拉玛那马哈希的教示故事{SUFFIX}',
    'books/surpassing-love-ch1.html': f'超越爱与恩典 第一章：拉玛那马哈希的慈悲教导{SUFFIX}',
    'books/collected-works-ch1.html': f'全集 第一章：拉玛那马哈希自述教示精华{SUFFIX}',
    'books/self-enquiry-ch1.html': f'自我参究 第一章：自我参究法的理论详解 - 拉玛那马哈希教导{SUFFIX}',
    'books/whoami-ch1.html': f'我是谁？ 第一章：我是谁？自我参究入门 - 拉玛那马哈希核心修行{SUFFIX}',
}

# 非章节页面
OTHER_TITLES = {
    'index.html': f'拉玛那马哈希知识库 | 灵性教示完整指南（核心著作/概念/问答/修行方法）|{SITE}',
    'graph.html': f'拉玛那马哈希核心概念知识图谱 | 灵修思想可视化指南 | {SITE}',
    'sitemap.html': f'拉玛那马哈希知识库网站地图 | 完整页面索引指南 | {SITE}',
    'books/index.html': f'拉玛那马哈希经典著作全集 | 18本灵性书籍完整目录索引 | {SITE}',
    'qa/index.html': f'精选问答150则 | 拉玛那马哈希灵性对话精编指南 | {SITE}',
    'methods/index.html': f'修行方法索引 | 拉玛那马哈希灵性修持方法完整指南 | {SITE}',
    'persons/index.html': f'关键人物索引 | 拉玛那马哈希与其弟子传记指南 | {SITE}',

    'books/be-as-you-are.html': f'走向静默，如你本来 Be As You Are完整导读 | 拉玛那马哈希 | {SITE}',
    'books/gems.html': f'宝钻集 Gems from Bhagavan完整导读 | 拉玛那马哈希 | {SITE}',
    'books/back-to-heart.html': f'回到你心中 Back to the Heart完整导读 | 拉玛那马哈希 | {SITE}',
    'books/talks.html': f'对谈录 Talks with Sri Ramana Maharshi完整导读 | {SITE}',
    'books/day-by-day.html': f'日日与彼 Day by Day with Bhagavan完整导读 | {SITE}',
    'books/face-to-face.html': f'面对面 Face to Face完整导读 | 拉玛那马哈希 | {SITE}',
    'books/search-in-secret-india.html': f'秘密印度 A Search in Secret India完整导读 | {SITE}',
    'books/maharshi-gospel.html': f'马哈希福音 Maharshi Gospel完整导读 | 拉玛那马哈希 | {SITE}',
    'books/maha-yoga.html': f'大瑜伽 Maha Yoga完整导读 | 拉玛那马哈希 | {SITE}',
    'books/guru-vachaka-kovai.html': f'上师言颂 Guru Vachaka Kovai完整导读 | {SITE}',
    'books/timeless-in-time.html': f'时代中的永恒 Timeless in Time完整导读 | {SITE}',
    'books/reflections.html': f'反思录 Reflections完整导读 | 拉玛那马哈希 | {SITE}',
    'books/spiritual-stories.html': f'灵性故事 Spiritual Stories完整导读 | 拉玛那马哈希 | {SITE}',
    'books/surpassing-love.html': f'超越爱与恩典 Surpassing Love完整导读 | {SITE}',
    'books/crumbs.html': f'桌边碎语 Crumbs from the Table完整导读 | 拉玛那马哈希 | {SITE}',
    'books/collected-works.html': f'全集 Collected Works完整导读 | 拉玛那马哈希 | {SITE}',
    'books/self-enquiry.html': f'自我参究 Self-Enquiry in Ramana Maharshi完整导读 | {SITE}',
    'books/whoami.html': f'我是谁？ Nan Yar? 自我参究入门指南 | {SITE}',
    'books/ramana-teachings.html': f'拉玛那马哈希核心教示 | 灵性教导精要完整版 | {SITE}',

    'concepts/self-enquiry.html': f'自我参究法 Self-Enquiry | 拉玛那马哈希核心概念详解 | {SITE}',
    'concepts/awareness.html': f'觉知与观照 Awareness | 拉玛那马哈希核心概念详解 | {SITE}',
    'concepts/heart.html': f'本心与心灵 Heart | 拉玛那马哈希核心概念详解 | {SITE}',
    'concepts/jnana.html': f'真知之道 Jnana | 拉玛那马哈希核心概念详解 | {SITE}',
    'concepts/jnani.html': f'真知者 Jnani | 拉玛那马哈希核心概念详解 | {SITE}',
    'concepts/samsara.html': f'轮回与生死 Samsara | 拉玛那马哈希核心概念详解 | {SITE}',
    'concepts/satchidananda.html': f'存在意识喜悦 Satchidananda | 拉玛那核心概念详解 | {SITE}',
    'concepts/bhakti.html': f'虔诚之道 Bhakti | 拉玛那马哈希核心概念详解 | {SITE}',
    'concepts/japa.html': f'念诵修持 Japa | 拉玛那马哈希核心概念详解 | {SITE}',
    'concepts/world.html': f'世界与幻相 World | 拉玛那马哈希核心概念详解 | {SITE}',
    'concepts/enlightenment.html': f'开悟与解脱 Enlightenment | 拉玛那马哈希核心概念详解 | {SITE}',
    'concepts/sahaja.html': f'自然安住 Sahaja | 拉玛那马哈希核心概念详解 | {SITE}',
    'concepts/peace.html': f'安宁与寂静 Peace | 拉玛那马哈希核心概念详解 | {SITE}',
    'concepts/fate.html': f'命运与业力 Fate | 拉玛那马哈希核心概念详解 | {SITE}',
    'concepts/freewill.html': f'自由意志 Free Will | 拉玛那马哈希核心概念详解 | {SITE}',
    'concepts/whoami.html': f'我是谁 Who Am I？ | 拉玛那马哈希核心概念详解 | {SITE}',
    'concepts/mind.html': f'心智的本质 Mind | 拉玛那马哈希核心概念详解 | {SITE}',
    'concepts/ego.html': f'自我与执我 Ego | 拉玛那马哈希核心概念详解 | {SITE}',
    'concepts/thoughts.html': f'念头与思想 Thoughts | 拉玛那马哈希核心概念详解 | {SITE}',
    'concepts/samskaras.html': f'习气与种子 Samskaras | 拉玛那马哈希核心概念详解 | {SITE}',
    'concepts/drishti.html': f'见与幻相 Drishti | 拉玛那马哈希核心概念详解 | {SITE}',
    'concepts/maya.html': f'摩耶幻相 Maya | 拉玛那马哈希核心概念详解 | {SITE}',
    'concepts/tat-tvam-asya.html': f'梵我一如 Tat Tvam Asya | 拉玛那核心概念详解 | {SITE}',
    'concepts/abidance.html': f'安住真我 Abidance | 拉玛那马哈希核心概念详解 | {SITE}',
    'concepts/silence.html': f'静默的力量 Silence | 拉玛那马哈希核心概念详解 | {SITE}',
    'concepts/grace.html': f'上师恩典 Grace | 拉玛那马哈希核心概念详解 | {SITE}',
    'concepts/svasthya.html': f'安住自性 Svasthya | 拉玛那马哈希核心概念详解 | {SITE}',

    'methods/self-enquiry.html': f'自我参究法详解 Self-Enquiry | 拉玛那修行指南完整版 | {SITE}',
    'methods/surrender.html': f'臣服与归伏 Surrender | 拉玛那马哈希修行指南完整版 | {SITE}',
    'methods/bhakti.html': f'虔诚奉爱之道 Bhakti | 拉玛那马哈希修行指南完整版 | {SITE}',
    'methods/silence.html': f'静默修行 Silence | 拉玛那马哈希修行指南完整版 | {SITE}',
    'methods/japa.html': f'念诵修持 Japa | 拉玛那马哈希修行指南完整版 | {SITE}',
    'methods/satsang.html': f'共修与灵性聚会 Satsang | 拉玛那修行指南完整版 | {SITE}',
    'methods/discrimination.html': f'分别与辨别 Viveka | 拉玛那马哈希修行指南完整版 | {SITE}',

    'persons/ramana.html': f'室利·拉玛那·马哈希完整传记 | 印度灵性导师生平 | {SITE}',
    'persons/vallfirmalar.html': f'室利·拉玛那·马哈希完整传记 | 印度灵性导师生平 | {SITE}',
    'persons/vaikom.html': f'室利·拉玛那·马哈希完整传记 | 印度灵性导师生平 | {SITE}',

    'qa/qa-1.html': f'自我参究基础问答 | 拉玛那马哈希150精选问答 | {SITE}',
    'qa/qa-2.html': f'心智本质与幻相问答 | 拉玛那马哈希150精选问答 | {SITE}',
    'qa/qa-3.html': f'修行方法与精进问答 | 拉玛那马哈希150精选问答 | {SITE}',
    'qa/qa-4.html': f'真我与上师问答 | 拉玛那马哈希150精选问答 | {SITE}',
    'qa/qa-5.html': f'静默与三摩地问答 | 拉玛那马哈希150精选问答 | {SITE}',
    'qa/qa-6.html': f'解脱与开悟问答 | 拉玛那马哈希150精选问答 | {SITE}',
    'qa/qa-7.html': f'虔诚与念诵问答 | 拉玛那马哈希150精选问答 | {SITE}',
    'qa/qa-8.html': f'业力与轮回问答 | 拉玛那马哈希150精选问答 | {SITE}',
    'qa/qa-9.html': f'日常修行与生活问答 | 拉玛那马哈希150精选问答 | {SITE}',
    'qa/qa-10.html': f'梦境与意识状态问答 | 拉玛那马哈希150精选问答 | {SITE}',
    'qa/qa-11.html': f'世界与存在本质问答 | 拉玛那马哈希150精选问答 | {SITE}',
    'qa/qa-12.html': f'死亡与轮回问答 | 拉玛那马哈希150精选问答 | {SITE}',
    'qa/qa-13.html': f'幸福与安宁问答 | 拉玛那马哈希150精选问答 | {SITE}',
    'qa/qa-14.html': f'经典研读与智慧问答 | 拉玛那马哈希150精选问答 | {SITE}',
    'qa/qa-15.html': f'心灵觉醒实践问答 | 拉玛那马哈希150精选问答 | {SITE}',
    'qa/qa-16.html': f'自我超越问答 | 拉玛那马哈希150精选问答 | {SITE}',
    'qa/qa-17.html': f'真知与迷惑问答 | 拉玛那马哈希150精选问答 | {SITE}',
    'qa/qa-18.html': f'上师与弟子问答 | 拉玛那马哈希150精选问答 | {SITE}',
    'qa/qa-19.html': f'静修与日常问答 | 拉玛那马哈希150精选问答 | {SITE}',
    'qa/qa-20.html': f'解脱与圆满问答 | 拉玛那马哈希150精选问答 | {SITE}',
}

# 合并
ALL_TITLES = {**CH_TITLES, **OTHER_TITLES}

# 验证
print('=== Title Length Verification ===')
issues = []
for fp, title in ALL_TITLES.items():
    l = len(title)
    if l < 50 or l > 70:
        issues.append(f'  [{l:2d}] {fp}: {title[:50]}...')
if issues:
    print(f'ISSUES ({len(issues)}):')
    for i in issues: print(i)
else:
    print(f'All {len(ALL_TITLES)} titles OK (50-70 chars)')

# 示例
print('\n=== 示例标题 ===')
for fp, t in list(ALL_TITLES.items())[:5]:
    print(f'[{len(t):2d}] {t}')

# 应用
changed = 0
for fp in files:
    with open(fp, encoding='utf-8') as f:
        content = f.read()
    rel = fp.replace('\\', '/')
    new_title = ALL_TITLES.get(rel) or ALL_TITLES.get(os.path.basename(fp))
    if new_title:
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

print(f'\nApplied: {changed}/{len(files)} files changed')
