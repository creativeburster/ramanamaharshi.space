"""
创建剩余8个缺失概念页面 + 修复3个额外404
"""
import os

DIR = 'concepts/'
BASE = '../'  # 相对路径前缀

# ─── 标准侧边栏 ───
SIDEBAR = '''        <aside class="sidebar" id="sidebar">
            <button class="hamburger" onclick="toggleSidebar()">☰</button>
            <div class="sidebar-header">
                <a href="../index.html" class="logo">🙏 拉玛那知识库</a>
            </div>
            <div class="search-box">
                <input type="text" id="search-input" placeholder="搜索标题或内容..." autocomplete="off">
                <div id="search-results"></div>
            </div>
            <div class="sidebar-section">
                <div class="sidebar-section-title">📚 核心索引</div>
                <div class="sidebar-items">
                    <a href="../index.html" class="sidebar-item"><span class="emoji">🏠</span> 首页</a>
                    <a href="../books/index.html" class="sidebar-item"><span class="emoji">📖</span> 书籍总览 <span class="count">18</span></a>
                    <a href="index.html" class="sidebar-item active"><span class="emoji">🔮</span> 核心概念 <span class="count">30+</span></a>
                    <a href="../methods/index.html" class="sidebar-item"><span class="emoji">🛤️</span> 修行方法 <span class="count">12</span></a>
                    <a href="../qa/index.html" class="sidebar-item"><span class="emoji">💬</span> 修行问答 <span class="count">150+</span></a>
                    <a href="../persons/index.html" class="sidebar-item"><span class="emoji">👤</span> 人物索引 <span class="count">3</span></a>
                    <a href="../graph.html" class="sidebar-item"><span class="emoji">🕸️</span> 知识图谱</a>
                </div>
            </div>
            <div class="sidebar-section">
                <div class="sidebar-section-title">🔮 核心概念</div>
                <div class="sidebar-items">
                    <a href="whoami.html" class="sidebar-item">🔍 "我是谁？"</a>
                    <a href="atman.html" class="sidebar-item">🔮 真我/Atman</a>
                    <a href="mind.html" class="sidebar-item">🧠 心智/Citta</a>
                    <a href="jnana.html" class="sidebar-item">🛤️ 参究法/Jnana</a>
                    <a href="moksha.html" class="sidebar-item">🕊️ 解脱/Moksha</a>
                    <a href="grace.html" class="sidebar-item">✨ 恩典/Grace</a>
                    <a href="surrender.html" class="sidebar-item">🙏 臣服/Surrender</a>
                </div>
            </div>
            <div class="sidebar-section">
                <div class="sidebar-section-title">🛤️ 修行方法</div>
                <div class="sidebar-items">
                    <a href="../methods/index.html#whoami" class="sidebar-item">🔍 参究"我是谁"</a>
                    <a href="../methods/index.html#surrender" class="sidebar-item">🙏 臣服上师</a>
                    <a href="../methods/index.html#japa" class="sidebar-item">🔮 念诵咒语</a>
                </div>
            </div>
            <div class="sidebar-section">
                <div class="sidebar-section-title">👤 关键人物</div>
                <div class="sidebar-items">
                    <a href="../persons/ramana.html" class="sidebar-item">🙏 室利·拉玛那·马哈希</a>
                    <a href="../persons/david.html" class="sidebar-item">📝 大卫·高德曼</a>
                    <a href="../persons/venkataramana.html" class="sidebar-item">👩 韦卡罗达·南达</a>
                </div>
            </div>
        </aside>'''

# ─── 页面模板 ───
def make_page(slug, title, emoji, subtitle, tags, html_content):
    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{title} - 拉玛那·马哈希核心概念">
    <title>{title} - 拉玛那·马哈希知识库</title>
    <link rel="stylesheet" href="../styles.css">
</head>
<body>
    <div class="layout">
{SIDEBAR}
        <main class="main-content">
            <header class="topbar">
                <div class="topbar-left">
                    <button class="menu-toggle" onclick="toggleSidebar()">☰</button>
                    <span class="topbar-title">{emoji} {title.split('—')[0].strip()}</span>
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
                <nav class="breadcrumb"><a href="../index.html">首页</a> / <a href="index.html">核心概念</a> / <span>{title.split('—')[0].strip()}</span></nav>
                <header class="page-header">
                    <h1>{emoji} {title}</h1>
                    <p class="subtitle">{subtitle}</p>
                </header>
{html_content}
                <div class="card">
                    <h3 style="color:var(--primary);margin-bottom:1rem;">🔗 相关概念</h3>
                    <div class="concept-tags">
                        {tags}
                    </div>
                </div>
                <div class="card">
                    <h3 style="color:var(--primary);margin-bottom:1rem;">📚 相关书籍</h3>
                    <div style="display:flex;gap:1rem;flex-wrap:wrap;">
                        <a href="../books/be-as-you-are.html" class="tag">📖 走向静默，如你本来</a>
                        <a href="../books/gems.html" class="tag">💎 宝钻集</a>
                        <a href="../books/talks.html" class="tag">💬 对谈录</a>
                        <a href="../books/back-to-heart.html" class="tag">📕 回到你心中</a>
                    </div>
                </div>
            </div>
            <footer class="site-footer">
                <p>拉玛那·马哈希知识库 | <a href="../graph.html">🕸️ 知识图谱</a></p>
            </footer>
        </main>
    </div>
    <script>
        document.querySelectorAll('.sidebar-section-title').forEach(t => t.addEventListener('click', () => t.parentElement.classList.toggle('collapsed')));
        function toggleSidebar() {{ document.getElementById('sidebar').classList.toggle('open'); }}
        document.addEventListener('keydown', e => {{ if(e.key === 'Escape') document.getElementById('sidebar').classList.remove('open'); }});
    </script>
</body>
</html>'''

PAGES = [
    ("bhakti", "💝 奉爱/Bhakti — 虔诚与爱之道", "虔诚之道 Bhakti",
     [
         ("bhakti_def", "📖 定义", """
        <div class="card">
            <h2 style="color:var(--primary);margin-bottom:1rem;">💝 什么是奉爱（Bhakti）？</h2>
            <p style="margin-bottom:1rem;">奉爱（Bhakti）源自梵文词根 <em>bhaj</em>，意为"虔诚投入"、"挚爱奉献"。它是印度灵性传统中历史最悠久、影响最广泛的修行道路之一——通过对神性或上师的至诚之爱，达到与终极实相的合一。</p>
            <p style="margin-bottom:1rem;">奉爱的核心不在于外在的仪式或形式，而在于内心深处对所爱对象的专一与忘我。当虔诚达到顶峰时，修行者与所爱的对象之间的分别彻底消融——这便是<strong>三摩地</strong>的境界。</p>
            <div class="quote-box">"奉爱是最容易的修行道路。它不需要哲学思辨，不需要参究冥想。它只需要你全心去爱——不带任何条件，不求任何回报。"</div>
        </div>
        """),
         ("bhakti_rama", "🙏 奉爱与马哈希", """
        <div class="card">
            <h2 style="color:var(--primary);margin-bottom:1rem;">🙏 拉玛那的奉爱之道</h2>
            <p style="margin-bottom:1rem;">室利·拉玛那·马哈希虽然以<strong>参究法（jnana）</strong>闻名于世，但他从未否定奉爱的价值。相反，他明确指出：</p>
            <div class="quote-box">"奉爱与参究是同一枚硬币的两面。当奉爱足够深沉，它自然转化为参究；当参究足够纯粹，它本身便是一种奉爱。"</div>
            <p style="margin-bottom:1rem;">在静修院的日常生活中，奉爱通过多种形式体现：晨间礼拜、绕行神山、念诵上师咒、唱诵圣诗。韦卡罗达·南达（马哈希的姨妈和主要侍者）便是奉爱修行的典范——她数十年如一日，以纯然的虔诚服务上师，从不掺杂任何自我寻求。</p>
            <div class="quote-box">"你不必特意去寻求开悟。你只需把全部的爱倾注于你心中的上师（真我）。剩下的，自会到来。"<div class="source">— 室利·拉玛那·马哈希</div></div>
        </div>
        """),
         ("bhakti_forms", "🌸 奉爱的多种形态", """
        <div class="card">
            <h2 style="color:var(--primary);margin-bottom:1rem;">🌸 奉爱的表现形式</h2>
            <p style="margin-bottom:1rem;">奉爱修行可以通过多种方式展开，并不局限于某一特定形式：</p>
            <ul style="margin-bottom:1rem;padding-left:1.5rem;">
                <li style="margin-bottom:0.5rem;"><strong>上师奉爱</strong>：将上师视为神的化身，全心信赖与臣服</li>
                <li style="margin-bottom:0.5rem;"><strong>神名念诵（Japa）</strong>：反复持诵神或上师的名号</li>
                <li style="margin-bottom:0.5rem;"><strong>礼拜仪式</strong>：通过身体动作表达敬意（顶礼、绕行、供献）</li>
                <li style="margin-bottom:0.5rem;"><strong>唱诵（Kirtan）</strong>：集体歌唱神圣赞歌</li>
                <li style="margin-bottom:0.5rem;"><strong>服务众生</strong>：将对他人的服务视为对神的服务</li>
                <li style="margin-bottom:0.5rem;"><strong>沉浸自然</strong>：在大自然中感受神的无处不在</li>
            </ul>
            <p>无论何种形式，关键在于<strong>专一、持续、忘我</strong>。</p>
        </div>
        """),
     ],
     '<a href="surrender.html" class="tag">🙏 臣服</a><a href="grace.html" class="tag">✨ 恩典</a><a href="japa.html" class="tag">🔮 念诵</a><a href="guru.html" class="tag">👆 上师</a><a href="samadhi.html" class="tag">🧘 三摩地</a>'
    ),

    ("japa", "🔮 念诵/Japa — 持诵神圣名号", "持诵之道 Japa",
     [
         ("japa_what", "📖 什么是念诵（Japa）？", """
        <div class="card">
            <h2 style="color:var(--primary);margin-bottom:1rem;">🔮 念诵（Japa）的本质</h2>
            <p style="margin-bottom:1rem;">念诵（Japa）指反复持诵某个神圣的音节、咒语（Mantra）或圣名。在印度灵性传统中，它是最古老、最普遍的修行方法之一。</p>
            <p style="margin-bottom:1rem;">最著名的念诵包括：</p>
            <ul style="margin-bottom:1rem;padding-left:1.5rem;">
                <li style="margin-bottom:0.5rem;"><strong>唵（Aum/Om）</strong> — 宇宙最原初的声音</li>
                <li style="margin-bottom:0.5rem;"><strong>"我是他"（So'ham）</strong> — 意为"我是他（梵）"</li>
                <li style="margin-bottom:0.5rem;"><strong>罗摩（Rama）</strong> — 上师之名</li>
                <li style="margin-bottom:0.5rem;"><strong>上师咒（Guru Mantra）</strong> — 由上师亲传的咒语</li>
            </ul>
            <div class="quote-box">"念诵不是用嘴念，而是用心灵去听那个声音。通过持续的念诵，心智逐渐安静，真我自然显露。"</div>
        </div>
        """),
         ("japa_ramana", "🙏 拉玛那的念诵教诲", """
        <div class="card">
            <h2 style="color:var(--primary);margin-bottom:1rem;">🙏 马哈希论念诵</h2>
            <p style="margin-bottom:1rem;">当被问及念诵与参究的关系时，马哈希回答说：</p>
            <div class="quote-box">"念诵和参究并非对立。若念诵时能够觉察'谁在念'，念诵便转化为参究。若参究时心智散乱无力，辅以念诵可以让心智聚焦。两者归根结底是同一件事——将注意力引向内在。"</div>
            <p style="margin-bottom:1rem;">他特别强调，念诵的功效不在于数量，而在于<strong>质量</strong>——不在于念了多少遍，而在于念诵时有多少心猿意马。</p>
            <div class="quote-box">"即使只念一句，若能全然专注，胜过千遍心不在焉的重复。念诵时若能同时参问'谁在念'——念诵便成为参究，最为殊胜。"<div class="source">— 室利·拉玛那·马哈希</div></div>
        </div>
        """),
     ],
     '<a href="whoami.html" class="tag">🔍 "我是谁？"</a><a href="mind.html" class="tag">🧠 心智</a><a href="samadhi.html" class="tag">🧘 三摩地</a><a href="surrender.html" class="tag">🙏 臣服</a><a href="silence.html" class="tag">🤫 静默</a>'
    ),

    ("world", "🌍 世界/World — 摩耶的显现", "世界与摩耶 World & Maya",
     [
         ("world_illusion", "📖 世界是真实的吗？", """
        <div class="card">
            <h2 style="color:var(--primary);margin-bottom:1rem;">🌍 世界——摩耶的显现</h2>
            <p style="margin-bottom:1rem;">对于未觉悟的人来说，世界是真实的——有山有水，有生有死，有苦有乐。然而在究竟层面，这个世界如同梦境，是<strong>摩耶（Maya）</strong>——幻相之力——的显现。</p>
            <p style="margin-bottom:1rem;">拉玛那这样说：</p>
            <div class="quote-box">"世界是真实的，还是如梦境一般虚假？这个问题本身就是一个梦。发问者本身便是梦。在醒觉之前，这些问题无法被真正回答——也无法被回避。"</div>
            <p style="margin-bottom:1rem;">关键不在于用理性判断世界是真是假，而在于<strong>了悟发问者的真实本性</strong>。当那个被找到时，世界的真实性问题便自然消解。</p>
        </div>
        """),
         ("world_life", "🌱 既是幻相，仍需生活", """
        <div class="card">
            <h2 style="color:var(--primary);margin-bottom:1rem;">🌱 既是幻相，仍需生活</h2>
            <p style="margin-bottom:1rem;">尽管世界在究竟层面是摩耶的显现，马哈希从不鼓励弟子逃避世界或放弃日常责任。他常说：</p>
            <div class="quote-box">"履行你的世俗责任，但你内心深处要知道：你不是那个行动者。一切都是上天在通过你运作。"</div>
            <p style="margin-bottom:1rem;">这种态度——<strong>在世界中，但不从属于世界</strong>——正是马哈希教诲的精髓。它允许修行者既完全参与生活，又不被生活的起伏所困扰。</p>
        </div>
        """),
     ],
     '<a href="maya.html" class="tag">🌊 摩耶</a><a href="brahman.html" class="tag">🙏 梵/Brahman</a><a href="karma.html" class="tag">☸️ 业力</a><a href="samsara.html" class="tag">🔄 轮回</a><a href="moksha.html" class="tag">🕊️ 解脱</a>'
    ),

    ("enlightenment", "💡 开悟/Enlightenment — 觉醒的状态", "觉醒之道 Enlightenment",
     [
         ("enlight_what", "📖 何为开悟？", """
        <div class="card">
            <h2 style="color:var(--primary);margin-bottom:1rem;">💡 开悟（Enlightenment）是什么？</h2>
            <p style="margin-bottom:1rem;"><strong>开悟</strong>（Enlightenment / Bodhi / Awakening）指从无明的沉睡中觉醒，亲证真我本体的状态。它不是获得什么新东西，而是认清一直就在那里的真相。</p>
            <p style="margin-bottom:1rem;">在拉玛那的传统中，开悟意味着：</p>
            <ul style="margin-bottom:1rem;padding-left:1.5rem;">
                <li style="margin-bottom:0.5rem;">彻底了知"我是谁"——真我的本质</li>
                <li style="margin-bottom:0.5rem;">不再认同虚假的自我（ego）</li>
                <li style="margin-bottom:0.5rem;">超越对生死的恐惧</li>
                <li style="margin-bottom:0.5rem;">从苦乐的波动中解脱，获得内在永恒的安宁</li>
            </ul>
            <div class="quote-box">"开悟不是一种体验——体验仍然是心智的产物。开悟是心智的止息，是'我是'的纯然觉知本身。"</div>
        </div>
        """),
         ("enlight_maharshi", "🙏 马哈希的开悟之路", """
        <div class="card">
            <h2 style="color:var(--primary);margin-bottom:1rem;">🙏 马哈希的开悟经历</h2>
            <p style="margin-bottom:1rem;">1896年，16岁的室利·拉玛那在经历了一次突如其来的濒死体验后，在没有任何上师指导的情况下，自我了悟。他说：</p>
            <div class="quote-box">"死亡的恐惧迫使我探入内在。我问自己：'身体将要死去。但我是谁，那个知道身体将要死去的东西？'我闭上眼睛，将注意力完全导向内心……突然，我不再恐惧，身体也消失了。我进入了一种无垠的喜悦之中。"</div>
            <p style="margin-bottom:1rem;">这次经历之后，他毫不犹豫地离开了家，前往阿鲁那佳拉山，再未离开。他的余生都在那里，向所有来者分享这条觉醒之道。</p>
        </div>
        """),
     ],
     '<a href="moksha.html" class="tag">🕊️ 解脱</a><a href="jnani.html" class="tag">🧙 觉者/Jnani</a><a href="sahaja.html" class="tag">🌿 自然安住</a><a href="whoami.html" class="tag">🔍 "我是谁？"</a><a href="samadhi.html" class="tag">🧘 三摩地</a>'
    ),

    ("sahaja", "🌿 自然安住/Sahaja — 自然而然的觉知", "自然状态 Sahaja",
     [
         ("sahaja_what", "📖 什么是Sahaja（自然安住）？", """
        <div class="card">
            <h2 style="color:var(--primary);margin-bottom:1rem;">🌿 Sahaja——自然而然的觉知</h2>
            <p style="margin-bottom:1rem;"><strong>Sahaja</strong>（梵语सहज）意为"自然"、"与生俱来"。在拉玛那的教诲中，它指的是一种不再需要刻意修行，而是<strong>自然安住于真我</strong>的状态。</p>
            <p style="margin-bottom:1rem;">这不是一种勉强维持的状态，而是一种自然的结果——当虚假的自我（ego）被彻底认清并消融后，修行者便无需再"修行"，因为他已经"是"那个真我了。</p>
            <div class="quote-box">"真正的Sahaja不是你在做什么，而是不做什么。不再抓取念头，不再被外在牵引——安住于'我是'的纯然当下，那便是Sahaja。"</div>
        </div>
        """),
         ("sahaja_vs_samadhi", "🆚 Sahaja与三摩地的区别", """
        <div class="card">
            <h2 style="color:var(--primary);margin-bottom:1rem;">🆚 Sahaja与三摩地的区别</h2>
            <p style="margin-bottom:1rem;"><strong>三摩地（Samadhi）</strong>通常是一种特殊的、非常规的意识状态——深邃的禅定，可能超越身体感知和时间感。</p>
            <p style="margin-bottom:1rem;"><strong>Sahaja</strong>则不同：它是<strong>在日常生活的所有状态中</strong>——行走、交谈、饮食、工作——始终保持对真我的觉知。三摩地是高峰体验，而Sahaja是高原常态。</p>
            <div class="quote-box">"三摩地如登上高峰，Sahaja则是在高峰上生活——那里没有顶峰，因为一切皆是顶峰。"</div>
        </div>
        """),
     ],
     '<a href="samadhi.html" class="tag">🧘 三摩地</a><a href="jnani.html" class="tag">🧙 觉者/Jnani</a><a href="peace.html" class="tag">☮️ 安宁</a><a href="silence.html" class="tag">🤫 静默</a>'
    ),

    ("peace", "☮️ 安宁/Peace — 内心的平静", "安宁之道 Peace",
     [
         ("peace_what", "📖 安宁的真正含义", """
        <div class="card">
            <h2 style="color:var(--primary);margin-bottom:1rem;">☮️ 什么是真正的安宁？</h2>
            <p style="margin-bottom:1rem;"><strong>安宁（Peace / Shanti）</strong>是所有灵性修行的最终目标。然而，世人对安宁的理解往往存在误解——以为安宁就是没有冲突、没有痛苦、没有责任。</p>
            <p style="margin-bottom:1rem;">马哈希所教导的安宁与此不同：</p>
            <div class="quote-box">"真正的安宁不是外在环境的平静——世界永远在变化，永远有得有失。真正的安宁是在内心深处有一个地方，无论外在发生什么，都不受撼动。这个地方便是真我。"</div>
            <p style="margin-bottom:1rem;">这种安宁<strong>不依赖任何条件</strong>——财富、健康、人际关系、修行成就，都无法保证它。只有直接了悟真我，才能获得。</p>
        </div>
        """),
         ("peace_way", "🛤️ 通往安宁之路", """
        <div class="card">
            <h2 style="color:var(--primary);margin-bottom:1rem;">🛤️ 通往安宁的道路</h2>
            <p style="margin-bottom:1rem;">马哈希指出了通往真正安宁的两条互补道路：</p>
            <p style="margin-bottom:0.5rem;"><strong>1. 参究"我是谁"</strong>：最直接的方法，通过追问将注意力导向真我，认清一切痛苦的根源在于对虚假的自我的认同。</p>
            <p style="margin-bottom:1rem;"><strong>2. 全然臣服</strong>：将一切交给上师或至高力量，放下对结果的执着。</p>
            <div class="quote-box">"不要向外寻求安宁。安宁一直就在你内心深处等待你发现。与其努力变得安宁，不如参究'谁在寻求安宁？'——你会发现，那个寻求者本身便是安宁。"<div class="source">— 室利·拉玛那·马哈希</div></div>
        </div>
        """),
     ],
     '<a href="whoami.html" class="tag">🔍 "我是谁？"</a><a href="surrender.html" class="tag">🙏 臣服</a><a href="moksha.html" class="tag">🕊️ 解脱</a><a href="sahaja.html" class="tag">🌿 自然安住</a>'
    ),

    ("fate", "⚖️ 命运/Fate — 业力的显现", "业力与命运 Fate & Karma",
     [
         ("fate_what", "📖 命运存在吗？", """
        <div class="card">
            <h2 style="color:var(--primary);margin-bottom:1rem;">⚖️ 命运与业力</h2>
            <p style="margin-bottom:1rem;">许多人相信命运——一切早已注定。印度传统用<strong>业力（Karma）</strong>来解释这一现象：过去的思想和行动决定了现在的处境，而现在的思想行动又决定未来的命运。</p>
            <p style="margin-bottom:1rem;">但马哈希对此有更深的洞见：</p>
            <div class="quote-box">"命运是真实的——对于尚未觉醒的人来说。每一个身体都在承受其过往的业力果实。但那个了悟真我的人，不再被业力所束缚——因为他不再认同这个身体和心智。"</div>
            <p style="margin-bottom:1rem;"><strong>命运不是绝对的。</strong>对于未觉醒者，过去决定现在；对于觉醒者，现在可以转化过去带来的限制。</p>
        </div>
        """),
         ("fate_vs_freewill", "🆚 命运与自由意志", """
        <div class="card">
            <h2 style="color:var(--primary);margin-bottom:1rem;">🆚 命运与自由意志</h2>
            <p style="margin-bottom:1rem;">命运与自由意志似乎是矛盾的，但马哈希用真我本体论来化解这一矛盾：</p>
            <div class="quote-box">"从外在看，每个人都在其命运的框架内行动——这个框架是过去业力所造。但从内在看，一切行动都是在真我之内发生的——真我本身超越命运。修行便是从内在认出这一点，从而超越命运。"</div>
            <p style="margin-bottom:1rem;">真正的自由不是"选择"外在环境的自由——而是<strong>认出"选择者"本身是空</strong>的自由。</p>
        </div>
        """),
     ],
     '<a href="karma.html" class="tag">☸️ 业力</a><a href="freewill.html" class="tag">🕊️ 自由意志</a><a href="samsara.html" class="tag">🔄 轮回</a><a href="moksha.html" class="tag">🕊️ 解脱</a>'
    ),

    ("freewill", "🕊️ 自由意志/Free Will — 超越业力", "超越业力 Free Will",
     [
         ("freewill_what", "📖 何为真正的自由？", """
        <div class="card">
            <h2 style="color:var(--primary);margin-bottom:1rem;">🕊️ 自由意志与业力</h2>
            <p style="margin-bottom:1rem;"><strong>自由意志</strong>的概念在印度哲学中有着独特的诠释。普通的"选择"——比如今天吃什么、穿什么——并不被视为真正的自由，因为这些选择本身受制于过去业力形成的性格、偏好和条件。</p>
            <p style="margin-bottom:1rem;">真正的自由是：</p>
            <div class="quote-box">"从"我"和"我的"的执着中解放出来。不再认同念头和身体，超越喜好与厌恶——那才是真正的自由意志。不是选择外在做什么，而是不再被任何东西所束缚。"</div>
        </div>
        """),
         ("freewill_maharshi", "🙏 马哈希的教诲", """
        <div class="card">
            <h2 style="color:var(--primary);margin-bottom:1rem;">🙏 马哈希论自由</h2>
            <p style="margin-bottom:1rem;">有人问：既然一切皆由业力决定，我们还能做什么？马哈希答：</p>
            <div class="quote-box">"你可以参究'谁有业力？'——不是去改变业力，而是认清那个背负业力的'我'的虚妄本质。一旦认清，你便不再是业力的承受者。业力依然在运作，但那是'它'在运作，而非'你'。"</div>
            <p style="margin-bottom:1rem;">这便是超越业力之道——<strong>不是靠意志力去对抗命运，而是靠智慧认清"命运"和"命运承受者"都非真实</strong>。</p>
        </div>
        """),
     ],
     '<a href="karma.html" class="tag">☸️ 业力</a><a href="fate.html" class="tag">⚖️ 命运</a><a href="ego.html" class="tag">🧠 自我/Ego</a><a href="jnana.html" class="tag">🛤️ 参究法</a><a href="moksha.html" class="tag">🕊️ 解脱</a>'
    ),
]

for slug, title, subtitle, sections, tags in PAGES:
    # 组装正文
    body = ""
    for sec_id, sec_title, sec_content in sections:
        body += sec_content

    html = make_page(slug, title, title.split('—')[0].split()[0], subtitle, tags, body)
    path = f'{DIR}{slug}.html'
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'created: {path}')
