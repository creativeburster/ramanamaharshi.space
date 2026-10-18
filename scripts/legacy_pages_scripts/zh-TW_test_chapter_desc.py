import re, sys
sys.path.insert(0, '.')

# 测试 make_chapter_desc
def make_chapter_desc(book_key, ch_num):
    book_names = {
        'be-as-you-are': '《走向静默，如你本来》',
        'gems': '《宝钻集》',
        'back-to-heart': '《回到你心中》',
        'talks': '《对谈录》',
        'crumbs': '《桌边碎语》',
        'reflections': '《反思录》',
    }
    book = book_names.get(book_key, '该书')

    desc_templates = {
        'be-as-you-are': f'{book}第{ch_num}章完整内容与修行要点，包含原文精要、核心段落解读及概念交叉引用。{book}为拉玛那马哈希教示的核心著作，研读本章有助深入理解自我参究、静默与解脱的内在智慧。',
        'gems': f'{book}第{ch_num}章完整内容与修行要点，涵盖该章核心主题与修行洞见。{book}汇集马哈希教示精华，共13章，研读本章有助深入理解真我参究，心智本质与解脱之道。',
        'back-to-heart': f'{book}第{ch_num}章完整内容与修行要点，收录马哈希与弟子间的深情对话。{book}展现慈悲教示与日常生活中的修行指引，研读本章有助回归本心、体验内在觉醒的智慧。',
        'talks': f'{book}第{ch_num}章完整内容，涵盖自我参究、业力、解脱等核心主题的精彩对话。{book}是研究马哈希教示的重要文献，研读本章有助深入理解其静默智慧与修行指引。',
        'crumbs': f'{book}第{ch_num}章完整内容，以短文形式呈现马哈希的日常教示。{book}涵盖真我、静默与修行智慧，适合碎片化阅读与日常反思，研读本章有助将灵性智慧融入生活。',
        'reflections': f'{book}第{ch_num}章完整内容，汇集马哈希的灵性反思与修行洞见。{book}提供深入理解内在智慧的修行指引，研读本章有助深化自我参究、提升灵性觉醒的层次。',
    }
    t = desc_templates.get(book_key, f'{book}第{ch_num}章完整内容，研读本章有助深入理解拉玛那马哈希的教示精华与修行智慧。')
    if len(t) > 155:
        for sep in '。！？':
            pos = t.rfind(sep)
            if pos > 135:
                return t[:pos+1]
        return t[:154] + '…'
    return t

# 测试
for book_key in ['be-as-you-are', 'gems', 'back-to-heart', 'talks', 'crumbs', 'reflections']:
    for ch in [1, 5]:
        desc = make_chapter_desc(book_key, ch)
        print(f'[{len(desc):3d}] {book_key} ch{ch}: {desc[:60]}...')
