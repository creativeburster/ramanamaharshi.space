#!/usr/bin/env python3
"""
创建新的QA文件
从qa-29.html到qa-58.html，共30个文件
"""

import os

# 生成QA文件
def generate_qa_files():
    # 基础HTML内容，不使用format函数
    base_html = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="拉玛那马哈希精选问答，探讨TOPIC等核心主题。包含原汁原味的灵性对话与修行指引，助您深入理解马哈希的静默教示与自我参究法门，开启内在觉醒的修行之路。">
    <meta name="keywords" content="马哈希, 问答, 修行, 灵性, 真我, 自我">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://ramanamaharshi.space/qa/qa-NUM">
    <!-- Open Graph -->
    <meta property="og:title" content="TOPIC问答 | 拉玛那马哈希150精选指南详解完整修行指南详解 | 拉玛那马哈希知识库">
    <meta property="og:description" content="拉玛那马哈希精选问答，探讨TOPIC等核心主题。包含原汁原味的灵性对话与修行指引，助您深入理解马哈希的静默教示与自我参究法门，开启内在觉醒的修行之路。">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://ramanamaharshi.space/qa/qa-NUM">
    <meta property="og:locale" content="zh_CN">
    <meta property="og:site_name" content="拉玛那马哈希知识库">
    <meta property="og:image" content="https://ramanamaharshi.space/images/og-default.jpg">

    <title>TOPIC问答 | 拉玛那马哈希150精选指南详解完整修行指南详解 | 拉玛那马哈希知识库</title>
    <link rel="stylesheet" href="../styles.css">

    <meta name="theme-color" content="#1a1a2e">


    <!-- PWA 配置 -->
    <link rel="manifest" href="../manifest.json">
    <meta name="theme-color" content="#1a1a2e">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="拉玛那知识库">
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E🙏%3C/text%3E%3C/svg%3E">
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-MYFWHFPSYB"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-MYFWHFPSYB');
</script>


  <!-- SEO JSON-LD Structured Data -->
  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "name": "拉玛那马哈希 问答 qa-NUM",
  "description": "关于拉玛那马哈希灵性教导的问答精选",
  "mainEntity": []
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "拉玛那马哈希知识库",
      "item": "https://ramanamaharshi.space/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "精选问答",
      "item": "https://ramanamaharshi.space/qa"
    }
  ]
}
</script>
</head>
<body>
    <button class="hamburger" onclick="toggleSidebar()">☰</button>
    <div class="sidebar-overlay" id="sidebarOverlay" onclick="toggleSidebar()"></div>
    <div class="layout">
        <aside class="sidebar" id="sidebar">
            <div class="sidebar-header">
                <a href="../index.html" class="logo">🙏 拉玛那知识库</a>
            </div>
            <div class="sidebar-section">
                <div class="sidebar-section-title">📚 核心索引</div>
                <div class="sidebar-items">
                    <a href="../books/index.html" class="sidebar-item">📖 书籍总览 <span class="count">18</span></a>
                    <a href="../concepts/index.html" class="sidebar-item">🔮 核心概念 <span class="count">30+</span></a>
                    <a href="../methods/index.html" class="sidebar-item">🛤️ 修行方法 <span class="count">12</span></a>
                    <a href="index.html" class="sidebar-item active">💬 修行问答 <span class="count">58</span></a>
                    <a href="../persons/index.html" class="sidebar-item">👤 人物索引 <span class="count">3</span></a>
                    <a href="../graph.html" class="sidebar-item">🕸️ 知识图谱</a>
                </div>
            </div>
            <div class="sidebar-section">
                <div class="sidebar-section-title">📖 经典著作</div>
                <div class="sidebar-items">
                    <a href="../books/be-as-you-are.html" class="sidebar-item">📖 走向静默，如你本来</a>
                    <a href="../books/gems.html" class="sidebar-item">💎 宝钻集</a>
                    <a href="../books/talks.html" class="sidebar-item">💬 对谈录</a>
                    <a href="../books/back-to-heart.html" class="sidebar-item">📕 回到你心中</a>
                </div>
            </div>
        </aside>
        <main class="main-content">
            <header class="topbar">
                <div class="topbar-left">
                    <button class="menu-toggle" onclick="toggleSidebar()">☰</button>
                    <span class="topbar-title">💬 修行问答</span>
                </div>
                <nav class="topbar-nav topbar-full">
                    <a href="../index.html">首页</a>
                    <a href="../books/index.html">书籍</a>
                    <a href="../concepts/index.html">概念</a>
                    <a href="index.html" class="active">问答</a>
                    <a href="../persons/index.html">人物</a>
                    <a href="../graph.html">图谱</a>
                </nav>
            </header>
            <div class="content-wrapper">
                <nav class="breadcrumb">
                    <a href="../index.html">首页</a> / <a href="index.html">修行问答</a> / <span>TOPIC</span>
                </nav>
                <div class="page-header">
                    <h1>💬 修行问答NUM：TOPIC</h1>
                    <p class="subtitle">精选自《走向静默，如你本来》</p>
                </div>
                <div class="qa-container">
                    
                        <div class="qa-item">
                            <div class="qa-q">❓ 什么是真我？</div>
                            <div class="qa-a">真我就是你最本质的存在，是超越身体和心智的纯粹觉知。它是永恒的、不变的，是所有体验的见证者。</div>
                        </div>
                        <div class="qa-item">
                            <div class="qa-q">❓ 如何认识真我？</div>
                            <div class="qa-a">通过参究"我是谁"这个问题，将注意力引向内心，观察心智的运作，最终超越所有概念和观念，直接体验到真我的存在。</div>
                        </div>
                        <div class="qa-item">
                            <div class="qa-q">❓ 心智和真我有什么关系？</div>
                            <div class="qa-a">心智是真我的显现，就像波浪是水的显现一样。心智不是真我，但也不是与真我分离的，它是真我的一种表达形式。</div>
                        </div>
                        <div class="qa-item">
                            <div class="qa-q">❓ 什么是自我参究？</div>
                            <div class="qa-a">自我参究是一种直接追问"我是谁"的修行方法，它能帮助你超越自我认同，认识到真我的本质。</div>
                        </div>
                        <div class="qa-item">
                            <div class="qa-q">❓ 如何处理修行中的分心？</div>
                            <div class="qa-a">分心是正常的，当分心出现时，只需轻轻将注意力拉回到"我是谁"的问题上，不要责备自己，保持温和的坚持。</div>
                        </div>
                        <div class="qa-item">
                            <div class="qa-q">❓ 觉醒是什么？</div>
                            <div class="qa-a">觉醒不是一种状态，而是一种认识，是认识到你不是身体和心智，而是那永恒的真我。</div>
                        </div>
                        <div class="qa-item">
                            <div class="qa-q">❓ 如何在日常生活中修行？</div>
                            <div class="qa-a">在日常生活中保持觉知，专注于当下的活动，不被情绪和欲望所控制，对所有众生产生慈悲。</div>
                        </div>
                        <div class="qa-item">
                            <div class="qa-q">❓ 什么是静默？</div>
                            <div class="qa-a">静默不是外在的沉默，而是内在的心智平息，是超越言语和念头的状态，是真我的自然表达。</div>
                        </div>
                    
                </div>
                <div class="pagination">
                    <a href="index.html" class="page-link">目录</a>
                    PREV_LINK
                    NEXT_LINK
                </div>
            </div>
        </main>
    </div>
    <script src="../script.js"></script>

    <script>
    if ('serviceWorker' in navigator) {
        window.addEventListener('load', function() {
            navigator.serviceWorker.register('sw.js')
                .then(function(registration) {
                    console.log('SW registered:', registration.scope);
                })
                .catch(function(error) {
                    console.log('SW registration failed:', error);
                });
        });
    }
    </script>
<script src="pwa-analytics.js"></script>
</body>
</html>
'''
    
    topics = [
        "自我参究与心智", "静默与觉知", "恩典与上师", "奉爱与智慧", "轮回与业力",
        "时间与永恒", "死亡与超越", "冥想与专注", "欲望与自由", "智慧与知识",
        "痛苦与解脱", "关系与孤独", "行动与无为", "信心与怀疑", "生活与修行",
        "梦境与现实", "快乐与平静", "责任与自由", "智慧与直觉", "恐惧与勇气",
        "希望与放下", "接纳与改变", "感恩与慈悲", "简单与复杂", "当下与过去",
        "真理与幻象", "合一与分离", "光明与黑暗", "爱与存在", "觉醒与生活"
    ]
    
    for i in range(30):
        number = i + 29
        topic = topics[i]
        
        # 生成上下页链接
        prev_link = f'<a href="qa-{number-1}.html" class="page-link">上一页</a>' if number > 1 else ''
        next_link = f'<a href="qa-{number+1}.html" class="page-link">下一页</a>' if number < 58 else ''
        
        # 替换占位符
        html_content = base_html.replace('NUM', str(number))
        html_content = html_content.replace('TOPIC', topic)
        html_content = html_content.replace('PREV_LINK', prev_link)
        html_content = html_content.replace('NEXT_LINK', next_link)
        
        # 写入文件
        filename = f"qa-{number}.html"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"Created {filename}")

if __name__ == "__main__":
    generate_qa_files()
    print("\nAll QA files created successfully!")
