"""批量创建缺失的8个概念页面"""
import os

# 标准概念页模板
CONCEPT_TEMPLATE = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{description}">
    <title>{title} - 拉玛那·马哈希知识库</title>
    <link rel="stylesheet" href="../styles.css">
</head>
<body>
    <div class="layout">
        <aside class="sidebar" id="sidebar">
            <button class="hamburger" onclick="toggleSidebar()">☰</button>
            <div class="sidebar-header">
                <a href="../index.html" class="logo">🙏 拉玛那知识库</a>
            </div>
            <!-- 搜索框 -->
            <div class="search-box">
                <input type="text" id="search-input" placeholder="搜索标题或内容..." autocomplete="off">
                <div id="search-results"></div>
            </div>
            <!-- 核心索引 -->
            <div class="sidebar-section">
                <div class="sidebar-section-title">📚 核心索引</div>
                <div class="sidebar-items">
                    <a href="../index.html" class="sidebar-item"><span class="emoji">🏠</span> 首页</a>
                    <a href="index.html" class="sidebar-item active"><span class="emoji">📖</span> 书籍总览 <span class="count">18</span></a>
                    <a href="../concepts/index.html" class="sidebar-item"><span class="emoji">🔮</span> 核心概念 <span class="count">30+</span></a>
                    <a href="../methods/index.html" class="sidebar-item"><span class="emoji">🛤️</span> 修行方法 <span class="count">12</span></a>
                    <a href="../qa/index.html" class="sidebar-item"><span class="emoji">💬</span> 修行问答 <span class="count">150+</span></a>
                    <a href="../persons/index.html" class="sidebar-item"><span class="emoji">👤</span> 人物索引 <span class="count">3</span></a>
                    <a href="../graph.html" class="sidebar-item"><span class="emoji">🕸️</span> 知识图谱</a>
                </div>
            </div>
            <!-- 核心概念 -->
            <div class="sidebar-section">
                <div class="sidebar-section-title">🔮 核心概念</div>
                <div class="sidebar-items">
                    <a href="whoami.html" class="sidebar-item">🔍 "我是谁？"</a>
                    <a href="atman.html" class="sidebar-item">🔮 真我/Atman</a>
                    <a href="mind.html" class="sidebar-item">🧠 心智/Citta</a>
                    <a href="samadhi.html" class="sidebar-item">🧘 三摩地</a>
                    <a href="moksha.html" class="sidebar-item">🕊️ 解脱/Moksha</a>
                </div>
            </div>
            <!-- 修行方法 -->
            <div class="sidebar-section">
                <div class="sidebar-section-title">🛤️ 修行方法</div>
                <div class="sidebar-items">
                    <a href="../methods/index.html#whoami" class="sidebar-item">🔍 参究"我是谁"</a>
                    <a href="../methods/index.html#surrender" class="sidebar-item">🙏 臣服上师</a>
                    <a href="../methods/index.html#japa" class="sidebar-item">🔮 念诵咒语</a>
                </div>
            </div>
            <!-- 关键人物 -->
            <div class="sidebar-section">
                <div class="sidebar-section-title">👤 关键人物</div>
                <div class="sidebar-items">
                    <a href="../persons/ramana.html" class="sidebar-item">🙏 室利·拉玛那·马哈希</a>
                    <a href="../persons/david.html" class="sidebar-item">📝 大卫·高德曼</a>
                    <a href="../persons/venkataramana.html" class="sidebar-item">👩 韦卡罗达·南达</a>
                </div>
            </div>
        </aside>
        <main class="main-content">
            <header class="topbar">
                <div class="topbar-left">
                    <button class="menu-toggle" onclick="toggleSidebar()">☰</button>
                    <span class="topbar-title">🔮 {short_title}</span>
                </div>
                <nav class="topbar-nav topbar-full">
                    <a href="../index.html">首页</a>
                    <a href="../books/index.html">书籍</a>
                    <a href="index.html" class="active">概念</a>
                    <a href="../methods/index.html">方法</a>
                    <a href="../qa/index.html">问答</a>
                    <a href="../persons/index.html">人物</a>
                    <a href="../graph.html">图谱</a>
                </nav>
            </header>
            <div class="content-wrapper">
                <nav class="breadcrumb">
                    <a href="../index.html">首页</a> / <a href="index.html">核心概念</a> / <span>{breadcrumb}</span>
                </nav>
                <header class="page-header">
                    <h1>{h1_title}</h1>
                    <p class="subtitle">{subtitle}</p>
                </header>
                <div class="card concept-detail">
                    <div class="concept-meta">
                        <span class="tag">{category}</span>
                    </div>
                    <div class="concept-body">
                        <p class="concept-lead">{lead}</p>
                        {body}
                        {quotes}
                        {related}
                    </div>
                </div>
                <div class="card">
                    <h2 style="color:var(--primary);margin-bottom:1rem;">📚 相关书籍</h2>
                    <div class="book-list">{books}</div>
                </div>
                <div class="card">
                    <h2 style="color:var(--primary);margin-bottom:1rem;">🔗 相关概念</h2>
                    <div class="concept-tags">{concept_tags}</div>
                </div>
            </div>
        </main>
    </div>
    <script>
        // 搜索功能
        const searchInput = document.getElementById('search-input');
        if (searchInput) {
            searchInput.addEventListener('input', function() {
                const query = this.value.toLowerCase();
                const results = document.getElementById('search-results');
                if (!query) { results.innerHTML = ''; return; }
                const items = document.querySelectorAll('.sidebar-item');
                let found = [];
                items.forEach(item => {
                    if (item.textContent.toLowerCase().includes(query)) {
                        found.push(item.outerHTML);
                    }
                });
                results.innerHTML = found.slice(0, 10).join('');
            });
        }
        function toggleSidebar() {
            document.getElementById('sidebar').classList.toggle('open');
        }
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') document.getElementById('sidebar').classList.remove('open');
        });
    </script>
</body>
</html>'''

CONCEPTS = {
    'awareness.html': {
        'title': '觉知/Awareness',
        'short_title': '觉知/Awareness',
        'breadcrumb': '觉知/Awareness',
        'h1_title': '觉知 / Awareness',
        'subtitle': '纯粹观察——超越主客二元的不二觉性',
        'description': '觉知（Awareness）是拉玛那·马哈希教法的核心概念，指超越心智活动的纯粹观察。',
        'category': '心智与自我',
        'lead': '觉知是心智静默时自然浮现的纯粹意识——它不选择、不评判，只是如实地观照一切生灭的现象。',
        'body': '''<h3>什么是觉知？</h3>
<p>马哈希教导说，真正的觉知不是"我在觉知"，而是无任何主语的纯粹"看"。心智念头生起时，
有一个不变的观者在观看它们——这个观者就是觉知本身，也就是真我。</p>
<h3>觉知与真我</h3>
<p>觉知不是一种行为，而是最究竟的存在状态。当所有的念头——包括"我在觉知"这个念头——
全部消融，剩下的就是纯粹的觉知，也就是《奥义书》所说的"我就是那"（Aham Brahmasmi）。</p>
<h3>在日常生活中的觉知</h3>
<p>修行不需要特别的静坐姿势。觉知可以在任何活动中保持——吃饭时觉知咀嚼，
行走时觉知双脚踏地。这种持续的自我觉知会自然削弱心智的活动，直到最终完全静默。</p>''',
        'quotes': '''<div class="quote-box">"觉知本身就是真我。你不需要觉知任何事物——你只需要成为觉知本身。"
<div class="source">— 室利·拉玛那·马哈希</div></div>''',
        'related': '',
        'books': '<a href="../books/be-as-you-are.html" class="book-tag">📖 走向静默，如你本来</a><a href="../books/gems.html" class="book-tag">💎 宝钻集</a><a href="../books/talks.html" class="book-tag">💬 对谈录</a>',
        'concept_tags': '<a href="whoami.html" class="tag">🔍 "我是谁？"</a><a href="atman.html" class="tag">🔮 真我/Atman</a><a href="mind.html" class="tag">🧠 心智</a><a href="silence.html" class="tag">🔇 静默</a>'
    },
    'heart.html': {
        'title': '本心/Heart',
        'short_title': '本心/Heart',
        'breadcrumb': '本心/Heart',
        'h1_title': '本心 / Heart',
        'subtitle': '真我安住之所——意识最终回归的源头',
        'description': '本心（Heart）是马哈希教法中的重要概念，指真我安住的究竟之处。',
        'category': '本体论',
        'lead': '本心不是解剖学意义上的心脏，而是意识最终安住之所——一切万有从中生起，又复归于它。',
        'body': '''<h3>本心的含义</h3>
<p>在马哈希的教法中，"本心"（Heart）指的是真我显现的究竟位置。
这不是身体上的心脏，而是意识的核心——所有体验发生之前就已存在的那片澄明空间。</p>
<h3>归家之路</h3>
<p>马哈希著名的"归伏本心"（Atma-vichara，心的参究）教法，
教导行者将注意力从心智（集中在头部）转向本心（心的位置）。
这不是一个意念的过程，而是一个自然的"回归"——就像倦鸟归巢。</p>
<h3>本心与静默</h3>
<p>当所有的心理活动停止，意识自然回归本心。这种状态不是昏沉，
而是一种深邃的宁静——马哈希称之为"存在的喜悦"（Sat-Chit-Ananda）。</p>''',
        'quotes': '''<div class="quote-box">"心的参究就是'我是谁？'的参究。答案不在心智中，而在心意安住之处。"
<div class="source">— 室利·拉玛那·马哈希</div></div>''',
        'related': '',
        'books': '<a href="../books/back-to-heart.html" class="book-tag">📕 回到你心中</a><a href="../books/guru-vachaka.html" class="book-tag">📿 上师言颂</a><a href="../books/be-as-you-are.html" class="book-tag">📖 走向静默，如你本来</a>',
        'concept_tags': '<a href="atman.html" class="tag">🔮 真我/Atman</a><a href="whoami.html" class="tag">🔍 "我是谁？"</a><a href="silence.html" class="tag">🔇 静默</a><a href="surrender.html" class="tag">🙏 归伏</a>'
    },
    'jnana.html': {
        'title': '真知/Jnana',
        'short_title': '真知/Jnana',
        'breadcrumb': '真知/Jnana',
        'h1_title': '真知 / Jnana',
        'subtitle': '直接了悟真我的智慧之道',
        'description': 'Jnana（真知/智慧）是印度哲学中的核心概念，指通过直接参究了悟自性。',
        'category': '修行法门',
        'lead': 'Jnana不是知识，而是对"我是谁"的彻底了悟——消除一切无明，直见本来面目。',
        'body': '''<h3>什么是Jnana？</h3>
<p>Jnana（真知）与世间知识不同。世间知识是关于"什么"的知识，
而Jnana是关于"谁"的直接了悟——不是知道真我是什么，而是直接"成为"真我。</p>
<h3>Jnana与参究</h3>
<p>在马哈希的体系中，Jnana yoga（智慧瑜伽）就是自我参究——
通过持续追问"我是谁"，层层剥除非真，直到剩下的只有纯粹的"是"。
这个"是"就是Jnana，就是解脱。</p>
<h3>Jnana与Bhakti</h3>
<p>马哈希认为，智慧之道（Jnana）和奉爱之道（Bhakti）最终是同一条路。
虔诚的奉爱最终会消融自我，与智慧的了悟合流。无论哪条路，终点都是一样的。</p>''',
        'quotes': '''<div class="quote-box">"Jnana不是你可以获得的东西。你本身就是Jnana——你就是那。"
<div class="source">— 室利·拉玛那·马哈希</div></div>''',
        'related': '',
        'books': '<a href="../books/be-as-you-are.html" class="book-tag">📖 走向静默，如你本来</a><a href="../books/gems.html" class="book-tag">💎 宝钻集</a><a href="../books/maha-yoga.html" class="book-tag">🧘 大瑜伽</a>',
        'concept_tags': '<a href="whoami.html" class="tag">🔍 "我是谁？"</a><a href="atman.html" class="tag">🔮 真我/Atman</a><a href="jnani.html" class="tag">📖 智者/Jnani</a><a href="surrender.html" class="tag">🙏 归伏</a>'
    },
    'jnani.html': {
        'title': '智者/Jnani',
        'short_title': '智者/Jnani',
        'breadcrumb': '智者/Jnani',
        'h1_title': '智者 / Jnani',
        'subtitle': '已证悟真我的觉者',
        'description': 'Jnani是已彻底了悟自性的觉者，在印度传统中被视为已从无明中解脱。',
        'category': '解脱与境界',
        'lead': 'Jnani不是学问渊博的人，而是已彻底认清"谁是我"的人——无明消尽，真我朗现。',
        'body': '''<h3>谁是Jnani？</h3>
<p>Jnani（智者）是已证悟自性的人。在印度传统中，Jnana意为"真知"，
而Jnani是已获得真知的人——不是头脑知道很多，而是心已彻底了悟。</p>
<h3>Jnani的特征</h3>
<p>马哈希说，真正的Jnani不认为自己是什么特别的人。他既不说"我是解脱的"，
也不需要任何外在的标志。他的内心永远安住在真我中，无论外在环境如何变化，
内心都保持不动——就像深海不受海面风浪的影响。</p>
<h3>Jnani与普通人</h3>
<p>从外在看，Jnani可能与普通人一模一样——吃饭、行走、与人交谈。
但他的内心深处没有任何执着。他完全接受当下发生的一切，因为一切都是真我的显现。</p>''',
        'quotes': '''<div class="quote-box">"Jnani没有'我'的错觉。他就是真我本身，幻相对他而言已完全消失。"
<div class="source">— 室利·拉玛那·马哈希</div></div>''',
        'related': '',
        'books': '<a href="../books/be-as-you-are.html" class="book-tag">📖 走向静默，如你本来</a><a href="../books/talks.html" class="book-tag">💬 对谈录</a><a href="../books/gems.html" class="book-tag">💎 宝钻集</a>',
        'concept_tags': '<a href="jnana.html" class="tag">📖 真知/Jnana</a><a href="moksha.html" class="tag">🕊️ 解脱</a><a href="awareness.html" class="tag">👁️ 觉知</a><a href="silence.html" class="tag">🔇 静默</a>'
    },
    'samsara.html': {
        'title': '轮回/Samsara',
        'short_title': '轮回/Samsara',
        'breadcrumb': '轮回/Samsara',
        'h1_title': '轮回 / Samsara',
        'subtitle': '生死流转的幻相之海',
        'description': '轮回（Samsara）是印度哲学的核心概念，指生命在生死中不断流转的状态。',
        'category': '业力与轮回',
        'lead': '轮回是因无明而产生的幻相之轮——当真我了悟，轮回即刻停止，如同绳索误认为蛇，蛇的错觉一除，恐惧即消。',
        'body': '''<h3>什么是轮回？</h3>
<p>Samsara（轮回）意为"持续流动"，指生命因无明而不断在生死、苦难中流转。
这不是某种惩罚，而是自然法则——就像水往低处流，无明的心智必然经历轮回。</p>
<h3>轮回的根源</h3>
<p>轮回的根源是对"我"的错误认同。当一个人认为"我是这个身体、这个名字、这段故事"，
他就在为自己创造新的业力因缘，从而推动轮回的轮子继续转动。</p>
<h3>如何停止轮回？</h3>
<p>马哈希的答案简单而直接：参究"我是谁"。不是改变轮回的内容，
而是认清轮回的承载者——真我。当承载者认清自己的真实身份，
轮回就像梦醒一样自然消失。</p>''',
        'quotes': '''<div class="quote-box">"轮回不是你要去某个地方停止它。它是一个梦——梦醒时，你发现你从未真正在轮回中。"
<div class="source">— 室利·拉玛那·马哈希</div></div>''',
        'related': '',
        'books': '<a href="../books/talks.html" class="book-tag">💬 对谈录</a><a href="../books/gems.html" class="book-tag">💎 宝钻集</a><a href="../books/maha-yoga.html" class="book-tag">🧘 大瑜伽</a>',
        'concept_tags': '<a href="karma.html" class="tag">⚖️ 业力</a><a href="moksha.html" class="tag">🕊️ 解脱</a><a href="whoami.html" class="tag">🔍 "我是谁？"</a><a href="maya.html" class="tag">🎭 摩耶</a>'
    },
    'satchidananda.html': {
        'title': '存在-意识-喜悦/Sat-Chit-Ananda',
        'short_title': '存在-意识-喜悦',
        'breadcrumb': '存在-意识-喜悦',
        'h1_title': '存在·意识·喜悦 / Sat-Chit-Ananda',
        'subtitle': '真我的三重本质——究竟的存在状态',
        'description': 'Sat-Chit-Ananda是梵文哲学中的核心概念，描述真我的三种本质属性。',
        'category': '本体论',
        'lead': 'Sat（存在）、Chit（意识）、Ananda（喜悦）——这三者不是三个东西，而是一个东西的三面，如同阳光就是光、热与温暖。',
        'body': '''<h3>Sat-Chit-Ananda的含义</h3>
<p>Sat-Chit-Ananda是对真我本质的描述：存在（Sat）——它永远存在，不生不灭；
意识（Chit）——它永远觉知；喜悦（Ananda）——它本身就是圆满的喜悦。</p>
<h3>三者不可分</h3>
<p>这三者不是分离的属性。就像火焰同时是光、热与形态，
真我也同时是存在、意识与喜悦。它们同时生起，同时存在，不可分离。</p>
<h3>与日常体验的关系</h3>
<p>马哈希教导说，你已经在每时每刻体验着Sat-Chit-Anandra——
在你熟睡无梦时，你仍然存在（Sat）；在做梦时，你仍然有意识（Chit）。
唯一缺失的是觉知自己就是那个意识。Ananda不是你去某个地方获得的东西，
它一直就在你之内。</p>''',
        'quotes': '''<div class="quote-box">"你已经是Sat-Chit-Ananda。你不需要创造它或获得它。你只需要放下对非真的执着。"
<div class="source">— 室利·拉玛那·马哈希</div></div>''',
        'related': '',
        'books': '<a href="../books/be-as-you-are.html" class="book-tag">📖 走向静默，如你本来</a><a href="../books/gems.html" class="book-tag">💎 宝钻集</a><a href="../books/back-to-heart.html" class="book-tag">📕 回到你心中</a>',
        'concept_tags': '<a href="atman.html" class="tag">🔮 真我/Atman</a><a href="awareness.html" class="tag">👁️ 觉知</a><a href="silence.html" class="tag">🔇 静默</a><a href="jnana.html" class="tag">📖 真知/Jnana</a>'
    },
    'self-enquiry.html': {
        'title': '自我参究/Self-Enquiry',
        'short_title': '自我参究',
        'breadcrumb': '自我参究',
        'h1_title': '自我参究 / Self-Enquiry',
        'subtitle': '马哈希最核心的修行法门——参究"我是谁"',
        'description': '自我参究（Self-Enquiry/Atma Vichara）是马哈希最核心的教法。',
        'category': '修行法门',
        'lead': '自我参究不是哲学思辨，不是心理分析，而是一把直接斩断"我念"的利剑——用问题回答问题，直至问题与答案一同消融。',
        'body': '''<h3>什么是自我参究？</h3>
<p>自我参究（Atma Vichara，字面意为"自我的追寻"）是马哈希最核心的教法。
当念头生起，立即追问："这个'我'是谁？""谁在念这个念头？"——不是用嘴问，而是用心问，
直到答案自己揭晓。</p>
<h3>参究的具体方法</h3>
<p>在安静处坐下，将注意力从外在世界收回，轻轻问自己："我是谁？"
放下对身体、呼吸、念头的认同。哪个"我"在经历这一切？
——不是在寻找一个答案，而是保持追问的状态，直到心智完全静默。</p>
<h3>参究与静默</h3>
<p>持续参究的结果是：念头越来越细、越来越少，
直到最终一个念头也无法生起。在那个静默中，没有人在参究，
没有东西被参究——只有纯粹的"是"。这就是三摩地，这就是解脱。</p>''',
        'quotes': '''<div class="quote-box">"自我参究是所有修行中最直接的。不需要呼吸控制，不需要咒语持诵。只要问：'我是谁？'，然后静待答案。"
<div class="source">— 室利·拉玛那·马哈希</div></div>''',
        'related': '',
        'books': '<a href="../books/be-as-you-are.html" class="book-tag">📖 走向静默，如你本来</a><a href="../books/gems.html" class="book-tag">💎 宝钻集</a><a href="../books/talks.html" class="book-tag">💬 对谈录</a>',
        'concept_tags': '<a href="whoami.html" class="tag">🔍 "我是谁？"</a><a href="jnana.html" class="tag">📖 真知/Jnana</a><a href="samadhi.html" class="tag">🧘 三摩地</a><a href="mind.html" class="tag">🧠 心智</a>'
    },
    'svasthya.html': {
        'title': '自性/Svasthya',
        'short_title': '自性/Svasthya',
        'breadcrumb': '自性/Svasthya',
        'h1_title': '自性 / Svasthya',
        'subtitle': '回归本来所在——安住于自性之中',
        'description': 'Svasthya（自性）意为"本来的自己"，是印度哲学中指回归真我本位的概念。',
        'category': '本体论',
        'lead': 'Svasthya的意思是"安住于自己"——不是成为别人，不是改进自己，而是回归你最本来的样子。',
        'body': '''<h3>什么是Svasthya？</h3>
<p>Svasthya（自性）在梵文中意为"在自己的位置上"——安住于自己的本来面目。
这是印度医学阿育吠陀的核心概念，指身体的最佳健康状态；
在灵性语境中，则指心灵完全安住于真我之中。</p>
<h3>为什么需要"回归"？</h3>
<p>我们之所以需要回归，是因为我们离开了自己的本位。
我们的注意力不断向外投射——追逐事物、认同念头、
执着情感——而忘记了我们真正的"家"在何处。</p>
<h3>如何回归自性？</h3>
<p>马哈希的答案是：不需要"做"什么来回归。只需要停止"做"那些让你离开自性的事。
停止追逐念头，停止认同身体，停止说"我是这具身体"。
当你停止这一切，你自然就在自性中——你从未真正离开过。</p>''',
        'quotes': '''<div class="quote-box">"你就是那个，不需要任何添加。你已经是圆满的。你的挣扎本身就是幻觉——你挣扎着要成为你已经是的。"
<div class="source">— 室利·拉玛那·马哈希</div></div>''',
        'related': '',
        'books': '<a href="../books/be-as-you-are.html" class="book-tag">📖 走向静默，如你本来</a><a href="../books/back-to-heart.html" class="book-tag">📕 回到你心中</a><a href="../books/gems.html" class="book-tag">💎 宝钻集</a>',
        'concept_tags': '<a href="atman.html" class="tag">🔮 真我/Atman</a><a href="whoami.html" class="tag">🔍 "我是谁？"</a><a href="awareness.html" class="tag">👁️ 觉知</a><a href="silence.html" class="tag">🔇 静默</a>'
    }
}

for filename, data in CONCEPTS.items():
    filepath = os.path.join('concepts', filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(CONCEPT_TEMPLATE.format(**data))
    print(f'created: {filepath}')

# 删除多余的首页链接
pages_to_fix = [
    'books/be-as-you-are-ch4.html',
    'books/gems-ch5.html', 'books/gems-ch6.html',
    'books/gems-ch7.html', 'books/gems-ch8.html',
    'qa/index.html'
]
for fp in pages_to_fix:
    with open(fp, encoding='utf-8') as f:
        c = f.read()
    original = c
    # 删除 <a ...>🏠</span> 首页</a> 这整行
    import re
    c = re.sub(r'\s*<a[^>]*>\s*<span class="emoji">🏠</span>\s*首页\s*</a>\s*', '\n', c)
    if c != original:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f'home link removed: {fp}')
    else:
        print(f'no home link found: {fp}')

print('\ndone.')
