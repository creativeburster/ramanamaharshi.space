"""SEO标题批量更新：统一为「页面名 | 拉玛那·马哈希知识库」"""
import os, re, glob

SUFFIX = " | 拉玛那·马哈希知识库"

title_map = {
    # books/
    'books/index.html': ('📚 书籍总览', '拉玛那·马哈希18本核心著作：走向静默、宝钻集、对谈录等经典灵性书籍'),
    'books/be-as-you-are.html': ('📖 走向静默，如你本来', 'Be As You Are — 马哈希最权威问答汇编，探讨真我、心智与自我了悟'),
    'books/gems.html': ('💎 宝钻集', 'Gems from Bhagavan — 马哈希语录精华，涵盖幸福、真我、心智与解脱'),
    'books/talks.html': ('💬 对谈录', 'Talks with Sri Ramana Maharshi — 记录马哈希与访客的经典对话'),
    'books/back-to-heart.html': ('📕 回到你心中', '回到心中 — 马哈希关于心、自我参究与解脱的教导'),
    'books/day-by-day.html': ('📅 日日与彼', 'Day by Day with Bhagavan — 详尽记录马哈希在阿鲁那佳拉的生活'),
    'books/face-to-face.html': ('👁️ 面对面', 'Face to Face — 记录马哈希与求道者的对话'),
    'books/maha-yoga.html': ('🧘 大瑜伽', 'Maha Yoga — 斯瓦米·苏卡·南达上师记录的马哈希教导'),
    'books/collected-works.html': ('📚 全集', 'Collected Works — 马哈希诗作与著作汇编'),
    'books/spiritual-stories.html': ('📖 灵性故事', '灵性故事 — 阿鲁那佳拉静修院的真实故事'),
    'books/reflections.html': ('💭 反思录', 'Reflections — 马哈希对生命与修行的反思'),
    'books/surpassing-love.html': ('💝 超越爱与恩典', 'Surpassing Love and Grace — 虔诚与恩典之道'),
    'books/crumbs.html': ('🍞 桌边碎语', 'Crumbs from the Table — 静修院日常对话录'),
    'books/teachings.html': ('📗 以言传意', 'Teachings in His Own Words — 马哈希原文语录精选'),
    'books/maharshi-gospel.html': ('📜 马哈希福音', "Maharshi's Gospel — 马哈希自述其教法核心"),
    'books/search-secret-india.html': ('🔍 秘密印度', 'A Search in Secret India — 发现马哈希的经典之旅'),
    'books/timeless.html': ('⏳ 时代中的永恒', 'Timeless in Time — 记录马哈希的最后岁月'),
    # concepts/
    'concepts/index.html': ('🔮 核心概念', '30+核心概念详解：真我、心智、解脱、参究法、恩典等'),
    # methods/
    'methods/index.html': ('🛤️ 修行方法', '马哈希核心修行方法：自我参究、臣服、念诵、禅定详解'),
    # persons/
    'persons/index.html': ('👤 人物索引', '马哈希知识库关键人物传记'),
    'persons/ramana.html': ('🙏 室利·拉玛那·马哈希', '印度20世纪最伟大的灵性导师之一，阿鲁那佳拉圣山静修院创建者'),
    'persons/david.html': ('📝 大卫·高德曼', '马哈希英文著作主要编辑者，《对谈录》《宝钻集》编纂者'),
    'persons/venkataramana.html': ('👩 韦卡罗达·南达', '马哈希的姨妈与早期护持者，静修院传统的重要建立者'),
    # qa/
    'qa/index.html': ('💬 修行问答', '150+修行问答，关于真我、心智、轮回、上师与解脱的问答精选'),
    # root
    'index.html': ('🙏 首页', '拉玛那·马哈希知识库 — 传承自阿鲁那佳拉圣山的灵性修行指南'),
    'graph.html': ('🕸️ 知识图谱', '拉玛那·马哈希知识图谱 — 概念、人物、书籍与修行方法的关联网络'),
}

# chapter titles
chapter_titles = {
    'be-as-you-are': {
        'ch1': ('第一章：我是谁？', '自我参究的第一步 — 追问最根本的问题'),
        'ch2': ('第二章：真我', '永恒的真我 — 超越身体与心智的存在'),
        'ch3': ('第三章：心智', '心智的本质 — 念头与感知的器官'),
        'ch4': ('第四章：静默', '上师的静默 — 最深沉的教导'),
        'ch5': ('第五章：自我了悟', '证悟真我 — 从幻相中醒来'),
        'ch6': ('第六章：臣服', '臣服上师 — 放下自我的道路'),
        'ch7': ('第七章：恩典', '上师的恩典 — 觉醒的关键'),
        'ch8': ('第八章：修行', '日常修行 — 如何在生活中参究'),
        'ch9': ('第九章：解脱', '解脱 — 从轮回中彻底自由'),
    },
    'gems': {
        'ch1': ('第一章：幸福', '真正的幸福 — 源自内在而非外在'),
        'ch2': ('第二章：真我与非我', '真我与非我 — 辨别真实与虚假'),
        'ch3': ('第三章：心智', '心智 — 幻相的制造者'),
        'ch4': ('第四章："我是谁？"', '自我参究 — 最直接的修行法门'),
        'ch5': ('第五章：臣服', '臣服 — 放下自我的最高智慧'),
        'ch6': ('第六章：三态', '三态 — 醒时、梦时与深睡'),
        'ch7': ('第七章：恩典与上师', '恩典与上师 — 觉醒的外在助力'),
        'ch8': ('第八章：自我了悟', '自我了悟 — 了悟真我的本质'),
        'ch9': ('第九章：专注与念诵', '专注与念诵 — 驯服心智的方法'),
        'ch10': ('第十章：睡眠与三摩地', '睡眠与三摩地 — 无梦的状态'),
        'ch11': ('第十一章：自性', '自性 — 每一个人内在的神性'),
        'ch12': ('第十二章：无念', '无念 — 心智静止的状态'),
        'ch13': ('第十三章：解脱', '解脱 — 生命的最终目标'),
    },
}

def update_file(fp, page_title, desc):
    with open(fp, encoding='utf-8') as f:
        c = f.read()
    original = c

    full_title = page_title + SUFFIX

    # 更新 <title>
    c = re.sub(r'<title>[^<]+</title>', f'<title>{full_title}</title>', c)

    # 更新 meta description
    desc_escaped = desc.replace('"', '&quot;')
    c = re.sub(r'<meta name="description"[^>]+>', f'<meta name="description" content="{desc_escaped}">', c)

    # 更新/添加 keywords
    if '<meta name="keywords"' in c:
        c = re.sub(r'<meta name="keywords"[^>]+>', '<meta name="keywords" content="拉玛那,马哈希,灵性修行,自我了悟,阿鲁那佳拉,真我,心智,解脱">', c)
    else:
        c = re.sub(r'(<meta name="description"[^>]+>)', r'\1\n    <meta name="keywords" content="拉玛那,马哈希,灵性修行,自我了悟,阿鲁那佳拉,真我,心智,解脱">', c)

    # 更新 og:title
    c = re.sub(r'<meta property="og:title"[^>]+>', f'<meta property="og:title" content="{full_title}">', c)
    # 更新 og:description
    c = re.sub(r'<meta property="og:description"[^>]+>', f'<meta property="og:description" content="{desc_escaped}">', c)
    # 更新 og:url
    c = re.sub(r'<meta property="og:url"[^>]+>', f'<meta property="og:url" content="https://www.ramanamaharshi.space/{fp}">', c)

    # 替换面包屑里的首页标题（如果是旧的）
    c = c.replace('<title>拉玛那·马哈希知识库 - 传承自阿鲁那佳拉圣山 | 18本经典著作</title>',
                  f'<title>{full_title}</title>')

    if c != original:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(c)
        return True
    return False

# 处理普通页面
fixed = 0
for fp, (title, desc) in title_map.items():
    if update_file(fp, title, desc):
        fixed += 1
        print(f'  {fp}')

# 处理章节页
for fp in glob.glob('books/be-as-you-are-ch*.html'):
    num = re.search(r'ch(\d+)', fp).group(1)
    if num in chapter_titles['be-as-you-are']:
        title, desc = chapter_titles['be-as-you-are'][num]
        title = '📖 ' + title
        if update_file(fp, title, desc):
            fixed += 1
            print(f'  {fp}')

for fp in glob.glob('books/gems-ch*.html'):
    num = re.search(r'ch(\d+)', fp).group(1)
    if num in chapter_titles['gems']:
        title, desc = chapter_titles['gems'][num]
        title = '💎 ' + title
        if update_file(fp, title, desc):
            fixed += 1
            print(f'  {fp}')

print(f'\n共更新 {fixed} 个文件')
