"""SEO Title修复 - 优化截断逻辑，在标点符号处截断"""
import glob, re, os

files = sorted(glob.glob('**/*.html', recursive=True))
SITE = '拉玛那马哈希'
SUFFIX = f' | {SITE}'  # " | 拉玛那马哈希" = 10字符
changed = 0

def smart_truncate(text, max_len):
    """智能截断：在标点符号处截断，避免词中间切断"""
    if len(text) <= max_len:
        return text
    
    # 在max_len范围内找最后一个合适的截断点
    # 优先在标点符号处截断
    break_puncts = '，。？！、；：）】"\'~-'
    
    # 向前查找断点（至少保留前max_len-10字符）
    min_len = max(10, max_len - 15)
    
    for i in range(max_len, min_len - 1, -1):
        if i >= len(text):
            continue
        if text[i] in break_puncts or text[i] == ' ':
            return text[:i+1] + '…'
    
    # 没找到合适断点，强制在max_len处截断
    return text[:max_len] + '…'

def make_title(base, max_total=58):
    """生成标题，智能截断"""
    if len(base) + len(SUFFIX) <= max_total:
        return base + SUFFIX
    
    avail = max_total - len(SUFFIX)
    truncated = smart_truncate(base, avail)
    return truncated + SUFFIX

def check_len(t):
    l = len(t)
    status = 'OK' if 45 <= l <= 60 else ('SHORT' if l < 45 else 'LONG')
    return f'[{l:2d}] {status}'

# ===== 所有标题 =====
TITLES = {
    'books/be-as-you-are-ch1.html': make_title('走向静默，如你本来 第一章：我是谁？自我参究精读指南详解'),
    'books/be-as-you-are-ch2.html': make_title('走向静默，如你本来 第二章：自我参究法的详解与修行实践指引'),
    'books/be-as-you-are-ch3.html': make_title('走向静默，如你本来 第三章：心智的本质与超越幻相之道'),
    'books/be-as-you-are-ch4.html': make_title('走向静默，如你本来 第四章：静默的力量与内在修行的意义'),
    'books/be-as-you-are-ch5.html': make_title('走向静默，如你本来 第五章：自我了悟的境界与实修方法指引'),
    'books/be-as-you-are-ch6.html': make_title('走向静默，如你本来 第六章：上师的意义与恩典传承的智慧'),
    'books/be-as-you-are-ch7.html': make_title('走向静默，如你本来 第七章：上师恩典与弟子修行的关系'),
    'books/be-as-you-are-ch8.html': make_title('走向静默，如你本来 第八章：解脱的本质与觉醒智慧详解'),
    'books/be-as-you-are-ch9.html': make_title('走向静默，如你本来 第九章：修行者指南与最终的结论要义'),

    'books/gems-ch1.html': make_title('宝钻集 第一章：幸福的本质与内在安宁的修行智慧详解'),
    'books/gems-ch2.html': make_title('宝钻集 第二章：真我与非我的辨别修行智慧详解'),
    'books/gems-ch3.html': make_title('宝钻集 第三章：心智的本质与超越幻相的修行之道'),
    'books/gems-ch4.html': make_title('宝钻集 第四章："我是谁？"自我参究法门修行精读'),
    'books/gems-ch5.html': make_title('宝钻集 第五章：臣服与归伏的修行智慧精读详解'),
    'books/gems-ch6.html': make_title('宝钻集 第六章：存在意识喜悦三态的修行智慧精读'),
    'books/gems-ch7.html': make_title('宝钻集 第七章：恩典与上师的修行智慧精读详解'),
    'books/gems-ch8.html': make_title('宝钻集 第八章：自我了悟的境界修行智慧精读详解'),
    'books/gems-ch9.html': make_title('宝钻集 第九章：本心的本质与安宁的修行智慧精读'),
    'books/gems-ch10.html': make_title('宝钻集 第十章：出离的意义与修行智慧精读指南'),
    'books/gems-ch11.html': make_title('宝钻集 第十一章：命运与自由意志的修行智慧详解'),
    'books/gems-ch12.html': make_title('宝钻集 第十二章：觉者的境界与解脱智慧精读指南'),
    'books/gems-ch13.html': make_title('宝钻集 第十三章：杂项内容与修行智慧精读指南'),

    'books/back-to-heart-ch1.html': make_title('回到你心中 第一章：心的本质与回归本心的修行指南'),
    'books/back-to-heart-ch2.html': make_title('回到你心中 第二章：回归之路与心灵觉醒的修行详解'),
    'books/back-to-heart-ch3.html': make_title('回到你心中 第三章：自我参究与内在修行智慧指南'),
    'books/back-to-heart-ch4.html': make_title('回到你心中 第四章：放下与臣服的智慧修行详解'),
    'books/back-to-heart-ch5.html': make_title('回到你心中 第五章：真理在你心中的修行指南详解'),

    'books/talks-ch1.html': make_title('对谈录 第一章：自我参究与解脱修行的对话指南详解'),
    'books/talks-ch2.html': make_title('对谈录 第二章：心智与幻相修行的对话指南详解'),
    'books/talks-ch3.html': make_title('对谈录 第三章：静默与三摩地修行的对话指南详解'),
    'books/talks-ch4.html': make_title('对谈录 第四章：上师与恩典修行的对话指南详解'),
    'books/talks-ch5.html': make_title('对谈录 第五章：业力与命运修行的对话指南详解'),
    'books/talks-ch6.html': make_title('对谈录 第六章：开悟与解脱修行的对话指南详解'),
    'books/talks-ch7.html': make_title('对谈录 第七章：日常修行与觉醒智慧的对话精读指南'),
    'books/talks-ch8.html': make_title('对谈录 第八章：真理与实相修行的对话指南详解'),

    'books/crumbs-ch1.html': make_title('桌边碎语 第一章：日常教示与静默智慧的修行指南精读'),
    'books/crumbs-ch2.html': make_title('桌边碎语 第二章：日常教示与自我参究的修行指南精读'),
    'books/crumbs-ch3.html': make_title('桌边碎语 第三章：日常教示与安宁智慧的修行指南精读'),
    'books/crumbs-ch4.html': make_title('桌边碎语 第四章：日常教示与解脱智慧的修行指南精读'),

    'books/reflections-ch1.html': make_title('反思录 第一章：灵性反思与自我参究的修行指南精读'),
    'books/reflections-ch2.html': make_title('反思录 第二章：灵性反思与修行智慧的指南精读详解'),

    # 非章节页面
    'index.html': make_title('拉玛那马哈希知识库 | 灵性教示完整指南'),
    'graph.html': make_title('拉玛那马哈希核心概念知识图谱 | 灵修思想可视化'),
    'sitemap.html': make_title('拉玛那马哈希知识库网站地图 | 完整页面索引'),
    'books/index.html': make_title('拉玛那马哈希经典著作全集 | 18本灵性书籍目录'),
    'qa/index.html': make_title('精选问答150则 | 拉玛那马哈希灵性对话精编'),
    'methods/index.html': make_title('修行方法索引 | 拉玛那马哈希灵性修持指南'),
    'persons/index.html': make_title('关键人物索引 | 拉玛那马哈希与其弟子传记'),

    'books/be-as-you-are.html': make_title('走向静默，如你本来 Be As You Are完整导读'),
    'books/gems.html': make_title('宝钻集 Gems from Bhagavan完整导读'),
    'books/back-to-heart.html': make_title('回到你心中 Back to the Heart完整导读'),
    'books/talks.html': make_title('对谈录 Talks with Sri Ramana Maharshi完整导读'),
    'books/day-by-day.html': make_title('日日与彼 Day by Day with Bhagavan完整导读'),
    'books/face-to-face.html': make_title('面对面 Face to Face完整导读'),
    'books/search-in-secret-india.html': make_title('秘密印度 A Search in Secret India完整导读'),
    'books/maharshi-gospel.html': make_title('马哈希福音 Maharshi Gospel完整导读'),
    'books/maha-yoga.html': make_title('大瑜伽 Maha Yoga完整导读'),
    'books/guru-vachaka-kovai.html': make_title('上师言颂 Guru Vachaka Kovai完整导读'),
    'books/timeless-in-time.html': make_title('时代中的永恒 Timeless in Time完整导读'),
    'books/reflections.html': make_title('反思录 Reflections完整导读'),
    'books/spiritual-stories.html': make_title('灵性故事 Spiritual Stories完整导读'),
    'books/surpassing-love.html': make_title('超越爱与恩典 Surpassing Love完整导读'),
    'books/crumbs.html': make_title('桌边碎语 Crumbs from the Table完整导读'),
    'books/collected-works.html': make_title('全集 Collected Works完整导读'),
    'books/self-enquiry.html': make_title('自我参究 Self-Enquiry in Ramana Maharshi完整导读'),
    'books/ramana-teachings.html': make_title('拉玛那马哈希核心教示 | 灵性教导精要'),

    'concepts/self-enquiry.html': make_title('自我参究法 Self-Enquiry | 拉玛那马哈希核心概念'),
    'concepts/awareness.html': make_title('觉知与观照 Awareness | 拉玛那马哈希核心概念'),
    'concepts/heart.html': make_title('本心与心灵 Heart | 拉玛那马哈希核心概念'),
    'concepts/jnana.html': make_title('真知之道 Jnana | 拉玛那马哈希核心概念'),
    'concepts/jnani.html': make_title('真知者 Jnani | 拉玛那马哈希核心概念'),
    'concepts/samsara.html': make_title('轮回与生死 Samsara | 拉玛那马哈希核心概念'),
    'concepts/satchidananda.html': make_title('存在意识喜悦 Satchidananda | 拉玛那核心概念'),
    'concepts/bhakti.html': make_title('虔诚之道 Bhakti | 拉玛那马哈希核心概念'),
    'concepts/japa.html': make_title('念诵修持 Japa | 拉玛那马哈希核心概念'),
    'concepts/world.html': make_title('世界与幻相 World | 拉玛那马哈希核心概念'),
    'concepts/enlightenment.html': make_title('开悟与解脱 Enlightenment | 拉玛那马哈希核心概念'),
    'concepts/sahaja.html': make_title('自然安住 Sahaja | 拉玛那马哈希核心概念'),
    'concepts/peace.html': make_title('安宁与寂静 Peace | 拉玛那马哈希核心概念'),
    'concepts/fate.html': make_title('命运与业力 Fate | 拉玛那马哈希核心概念'),
    'concepts/freewill.html': make_title('自由意志 Free Will | 拉玛那马哈希核心概念'),
    'concepts/whoami.html': make_title('我是谁 Who Am I？ | 拉玛那马哈希核心概念'),
    'concepts/mind.html': make_title('心智的本质 Mind | 拉玛那马哈希核心概念'),
    'concepts/ego.html': make_title('自我与执我 Ego | 拉玛那马哈希核心概念'),
    'concepts/thoughts.html': make_title('念头与思想 Thoughts | 拉玛那马哈希核心概念'),
    'concepts/samskaras.html': make_title('习气与种子 Samskaras | 拉玛那马哈希核心概念'),
    'concepts/drishti.html': make_title('见与幻相 Drishti | 拉玛那马哈希核心概念'),
    'concepts/maya.html': make_title('摩耶幻相 Maya | 拉玛那马哈希核心概念'),
    'concepts/tat-tvam-asya.html': make_title('梵我一如 Tat Tvam Asya | 拉玛那核心概念'),
    'concepts/abidance.html': make_title('安住真我 Abidance | 拉玛那马哈希核心概念'),
    'concepts/silence.html': make_title('静默的力量 Silence | 拉玛那马哈希核心概念'),
    'concepts/grace.html': make_title('上师恩典 Grace | 拉玛那马哈希核心概念'),
    'concepts/svasthya.html': make_title('安住自性 Svasthya | 拉玛那马哈希核心概念'),

    'methods/self-enquiry.html': make_title('自我参究法详解 Self-Enquiry | 拉玛那修行指南'),
    'methods/surrender.html': make_title('臣服与归伏 Surrender | 拉玛那马哈希修行指南'),
    'methods/bhakti.html': make_title('虔诚奉爱之道 Bhakti | 拉玛那马哈希修行指南'),
    'methods/silence.html': make_title('静默修行 Silence | 拉玛那马哈希修行指南'),
    'methods/japa.html': make_title('念诵修持 Japa | 拉玛那马哈希修行指南'),
    'methods/satsang.html': make_title('共修与灵性聚会 Satsang | 拉玛那修行指南'),
    'methods/discrimination.html': make_title('分别与辨别 Viveka | 拉玛那马哈希修行指南'),

    'persons/ramana.html': make_title('室利·拉玛那·马哈希完整传记 | 印度灵性导师'),
    'persons/vallfirmalar.html': make_title('室利·拉玛那·马哈希完整传记 | 印度灵性导师'),
    'persons/vaikom.html': make_title('室利·拉玛那·马哈希完整传记 | 印度灵性导师'),

    'qa/qa-1.html': make_title('自我参究基础问答 | 拉玛那马哈希150精选'),
    'qa/qa-2.html': make_title('心智本质与幻相问答 | 拉玛那马哈希150精选'),
    'qa/qa-3.html': make_title('修行方法与精进问答 | 拉玛那马哈希150精选'),
    'qa/qa-4.html': make_title('真我与上师问答 | 拉玛那马哈希150精选'),
    'qa/qa-5.html': make_title('静默与三摩地问答 | 拉玛那马哈希150精选'),
    'qa/qa-6.html': make_title('解脱与开悟问答 | 拉玛那马哈希150精选'),
    'qa/qa-7.html': make_title('虔诚与念诵问答 | 拉玛那马哈希150精选'),
    'qa/qa-8.html': make_title('业力与轮回问答 | 拉玛那马哈希150精选'),
    'qa/qa-9.html': make_title('日常修行与生活问答 | 拉玛那马哈希150精选'),
    'qa/qa-10.html': make_title('梦境与意识状态问答 | 拉玛那马哈希150精选'),
    'qa/qa-11.html': make_title('世界与存在本质问答 | 拉玛那马哈希150精选'),
    'qa/qa-12.html': make_title('死亡与轮回问答 | 拉玛那马哈希150精选'),
    'qa/qa-13.html': make_title('幸福与安宁问答 | 拉玛那马哈希150精选'),
    'qa/qa-14.html': make_title('经典研读与智慧问答 | 拉玛那马哈希150精选'),
    'qa/qa-15.html': make_title('心灵觉醒实践问答 | 拉玛那马哈希150精选'),
    'qa/qa-16.html': make_title('自我超越问答 | 拉玛那马哈希150精选'),
    'qa/qa-17.html': make_title('真知与迷惑问答 | 拉玛那马哈希150精选'),
    'qa/qa-18.html': make_title('上师与弟子问答 | 拉玛那马哈希150精选'),
    'qa/qa-19.html': make_title('静修与日常问答 | 拉玛那马哈希150精选'),
    'qa/qa-20.html': make_title('解脱与圆满问答 | 拉玛那马哈希150精选'),
}

# 验证长度
print('=== Title Length Verification ===')
issues = []
for fp, title in TITLES.items():
    l = len(title)
    if l < 40 or l > 60:
        issues.append(f'  [{l}] {fp}: {title}')
if issues:
    print('ISSUES:')
    for i in issues: print(i)
else:
    print(f'All {len(TITLES)} titles OK (40-60 chars)')

# 显示几个示例
print('\n=== 示例标题 ===')
for i, (fp, t) in enumerate(list(TITLES.items())[:5]):
    print(f'{check_len(t)} {fp}')
    print(f'       {t}')

# 应用
print(f'\n=== 应用标题 ===')
for fp in files:
    with open(fp, encoding='utf-8') as f:
        content = f.read()

    rel = fp.replace('\\', '/')
    new_title = TITLES.get(rel) or TITLES.get(os.path.basename(fp))

    if new_title:
        original = content
        content = re.sub(r'<title>.*?</title>', f'<title>{new_title}</title>', content, flags=re.DOTALL)
        # 同时更新og:title和twitter:title
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

print(f'Applied: {changed}/{len(files)} files changed')
