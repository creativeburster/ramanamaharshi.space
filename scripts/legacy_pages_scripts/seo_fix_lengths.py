"""
SEO Title & Description Length Fixer
- Title: 45-55 chars
- Description: 140-155 chars
"""
import glob
import re
import os

files = sorted(glob.glob('**/*.html', recursive=True))
changed = 0

SITE = '拉玛那马哈希知识库'

def pad_title(title, target_min=45, target_max=55, suffix=f' | {SITE}'):
    """确保 title 在 45-55 字符范围内，不够则扩充"""
    base = title.replace(f' | {SITE}', '').replace(f' | {SITE}', '').strip()
    with_site = f'{base}{suffix}'
    tlen = len(with_site)
    if tlen < target_min:
        # 需要扩充
        if '第' in base and ('章' in base or '节' in base):
            # 章节页，添加书名作为扩充
            expanded = f'{base}{suffix}'
        elif ' | ' in base:
            expanded = f'{base}{suffix}'
        else:
            expanded = f'{base}完整指南{suffix}'
        return expanded
    elif tlen > target_max:
        # 截断到 target_max，保持 site name 可见
        # 保留前半部分 + suffix
        avail = target_max - len(suffix)
        truncated = base[:avail].rsplit(' ', 1)[0]  # 不要截断单词
        return f'{truncated}{suffix}'
    return with_site

def fix_title_by_type(fp, current_title):
    """根据文件路径类型生成合适长度的 title"""
    fname = os.path.basename(fp).replace('.html', '')

    # 首页
    if fp == 'index.html':
        return pad_title('拉玛那马哈希知识库 | 灵性教示完整指南')

    # 知识图谱
    if fp == 'graph.html':
        return pad_title('拉玛那马哈希核心概念知识图谱 | 灵修思想可视化')

    # 网站地图
    if fp == 'sitemap.html':
        return pad_title('拉玛那马哈希知识库网站地图')

    # 书籍列表页
    if fp == 'books/index.html':
        return pad_title('拉玛那马哈希经典著作全集 | 18本灵性书籍完整目录')

    # 书籍章节页（从文件名识别）
    if 'books/' in fp:
        fname_base = fname

        # 书籍名映射
        book_map = {
            'be-as-you-are': '走向静默 如你本来',
            'gems': '宝钻集',
            'back-to-heart': '回到你心中',
            'talks': '对谈录',
            'day-by-day': '日日与彼',
            'face-to-face': '面对面',
            'search-in-secret-india': '秘密印度',
            'maharshi-gospel': '马哈希福音',
            'maha-yoga': '大瑜伽',
            'guru-vachaka-kovai': '上师言颂',
            'timeless-in-time': '时代中的永恒',
            'reflections': '反思录',
            'spiritual-stories': '灵性故事',
            'surpassing-love': '超越爱与恩典',
            'crumbs': '桌边碎语',
            'collected-works': '全集',
            'self-enquiry': '自我参究',
        }

        chapter_num_match = re.search(r'-ch(\d+)', fname_base)
        book_key = re.sub(r'-ch\d+', '', fname_base)

        book_name = book_map.get(book_key, book_key)

        if chapter_num_match:
            ch = chapter_num_match.group(1)
            return pad_title(f'{book_name} 第{ch}章 | 拉玛那马哈希教示精读')
        else:
            # 书籍详情页
            return pad_title(f'{book_name} | 拉玛那马哈希经典著作完整导读')

    # 概念页面
    if 'concepts/' in fp:
        concept_map = {
            'self-enquiry': '自我参究法',
            'awareness': '觉知与观照',
            'heart': '本心与心灵',
            'jnana': '真知之道',
            'jnani': '真知者',
            'samsara': '轮回与生死',
            'satchidananda': '存在意识喜悦',
            'bhakti': '虔诚之道',
            'japa': '念诵修持',
            'world': '世界与幻相',
            'enlightenment': '开悟与解脱',
            'sahaja': '自然安住',
            'peace': '安宁与寂静',
            'fate': '命运与业力',
            'freewill': '自由意志',
            'whoami': '我是谁',
            'mind': '心智',
            'ego': '自我与执我',
            'thoughts': '念头',
            'samskaras': '习气与种子',
            'drishti': '见与幻相',
            'maya': '摩耶幻相',
            'tat-tvam-asya': '梵我一如',
            'abidance': '安住真我',
            'silence': '静默',
            'grace': '上师恩典',
            'svasthya': '安住自性',
        }

        fname_base = fname
        cn = concept_map.get(fname_base, fname_base)
        return pad_title(f'{cn} | 拉玛那马哈希核心概念详解')

    # 问答页面
    if 'qa/qa-' in fp:
        qa_titles = {
            'qa-1': '自我参究基础问答',
            'qa-2': '心智本质与幻相',
            'qa-3': '修行方法与精进',
            'qa-4': '真我与上师',
            'qa-5': '静默与三摩地',
            'qa-6': '解脱与开悟',
            'qa-7': '虔诚与念诵',
            'qa-8': '业力与轮回',
            'qa-9': '日常修行与生活',
            'qa-10': '梦境与意识状态',
            'qa-11': '世界与存在本质',
            'qa-12': '死亡与轮回',
            'qa-13': '幸福与安宁',
            'qa-14': '经典研读与智慧',
            'qa-15': '心灵觉醒实践',
            'qa-16': '自我超越问答',
            'qa-17': '真知与迷惑',
            'qa-18': '上师与弟子',
            'qa-19': '静修与日常',
            'qa-20': '解脱与圆满',
        }
        fname_base = fname
        t = qa_titles.get(fname_base, '精选问答')
        return pad_title(f'{t} | 拉玛那马哈希150问答精编')

    if fp == 'qa/index.html':
        return pad_title('精选问答150则 | 拉玛那马哈希灵性对话精编')

    # 方法页面
    if 'methods/' in fp:
        method_map = {
            'self-enquiry': '自我参究法详解',
            'surrender': '臣服与归伏',
            'bhakti': '虔诚奉爱之道',
            'silence': '静默修行',
            'japa': '念诵修持',
            'satsang': '共修与灵性聚会',
            'discrimination': '分别与辨别',
        }
        fname_base = fname
        mn = method_map.get(fname_base, fname_base)
        return pad_title(f'{mn} | 拉玛那马哈希修行方法完整指南')

    if fp == 'methods/index.html':
        return pad_title('修行方法索引 | 拉玛那马哈希灵性修持指南')

    # 人物页面
    if 'persons/' in fp:
        persons_map = {
            'ramana': '室利·拉玛那·马哈希传记 | 印度灵性导师',
            'vallfirmalar': '室利·拉玛那·马哈希传记 | 印度灵性导师',
            'vaikom': '室利·拉玛那·马哈希传记 | 印度灵性导师',
        }
        fname_base = fname
        pn = persons_map.get(fname_base, fname_base)
        return pad_title(pn)

    if fp == 'persons/index.html':
        return pad_title('关键人物索引 | 拉玛那马哈希与其弟子')

    # 默认
    return pad_title(current_title.replace(f' | {SITE}', ''))


def fix_desc(desc):
    """确保 description 在 140-155 字符范围内"""
    # 清理残留的 "拉玛那马哈希Space"
    d = desc.replace('拉玛那马哈希Space', '拉玛那马哈希知识库')

    # 移除末尾可能的残留
    d = re.sub(r'拉玛那马哈希Space+', '拉玛那马哈希知识库', d)

    dlen = len(d)
    target_min = 140
    target_max = 155

    if dlen < target_min:
        # 扩充描述
        suffix = ' 拉玛那马哈希知识库 — 系统整理拉玛那马哈希教示的经典著作、核心概念、修行方法与精选问答。'
        # 检查末尾是否已有类似结尾
        if d.rstrip().endswith(('。', '？', '！')):
            suffix = ' 拉玛那马哈希知识库系统整理其经典著作、核心概念、修行方法与精选问答。'
        return d + suffix

    if dlen > target_max:
        # 截断到 155，在句号处断开
        truncated = d[:target_max]
        last_punct = max(truncated.rfind('。'), truncated.rfind('？'), truncated.rfind('！'))
        if last_punct > 120:
            return truncated[:last_punct+1]
        return truncated.rstrip() + '...'

    return d


for fp in files:
    with open(fp, encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. 修复 title
    m_title = re.search(r'<title>(.*?)</title>', content, re.DOTALL)
    if m_title:
        current_title = m_title.group(1).strip()
        new_title = fix_title_by_type(fp, current_title)

        # 额外检查：仍超长则截断
        if len(new_title) > 55:
            # 保留前52字符 + site
            avail = 55 - len(f' | {SITE}') - 1
            base = new_title.replace(f' | {SITE}', '')
            new_title = base[:avail].rstrip() + f'… | {SITE}'

        content = content.replace(
            f'<title>{m_title.group(1)}</title>',
            f'<title>{new_title}</title>'
        )

    # 2. 修复 description（清理残留 + 扩充/截断）
    m_desc = re.search(r'(<meta name=["\']description["\'] content=["\'])(.*?)(["\']\s*/?>)', content, re.DOTALL)
    if m_desc:
        current_desc = m_desc.group(2)
        new_desc = fix_desc(current_desc)
        if new_desc != current_desc:
            content = content.replace(
                m_desc.group(0),
                f'<meta name="description" content="{new_desc}">'
            )

    # 3. 同步修复 og:description 和 Twitter description
    for meta_name in ['og:description', 'twitter:description']:
        m_og = re.search(rf'(<meta (?:property|name)=["\'{meta_name}["\'][^>]+content=["\'])(.*?)(["\']\s*/?>)', content, re.DOTALL)
        if m_og:
            og_val = m_og.group(2)
            new_og = fix_desc(og_val)
            if new_og != og_val:
                content = content.replace(
                    m_og.group(0),
                    m_og.group(0).replace(og_val, new_og)
                )

    if content != original:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content)
        changed += 1

print(f'Done! Fixed {changed}/{len(files)} files')
