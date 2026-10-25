/**
 * 拉玛那马哈希知识库 - 优化版主脚本
 * 合并了 script.js + search.js 的功能
 * 减少HTTP请求，提升加载速度
 */

// ========== 搜索数据索引 ==========
const searchIndex = [
  // 书籍
  {type:'book',title:'走向静默，如你本来',url:'/zh-TW/books/be-as-you-are.html',excerpt:'马哈希最核心的问答精选，进入马哈希教法的最佳入门读物'},
  {type:'book',title:'宝钻集',url:'/zh-TW/books/gems.html',excerpt:'马哈希语录精华，每一则都如宝石般珍贵'},
  {type:'book',title:'对谈录',url:'/zh-TW/books/talks.html',excerpt:'与马哈希的对话记录，涵盖修行生活的方方面面'},
  {type:'book',title:'回到你心中',url:'/zh-TW/books/back-to-heart.html',excerpt:'回到真我本源的心法指引'},
  {type:'book',title:'日日与彼',url:'/zh-TW/books/day-by-day.html',excerpt:'弟子记录的马哈希每日教示'},
  {type:'book',title:'面对面',url:'/zh-TW/books/face-to-face.html',excerpt:'马哈希与求道者的对话实录'},
  {type:'book',title:'秘密印度',url:'/zh-TW/books/search-secret-india.html',excerpt:'保罗·布伦顿的朝圣记录'},
  {type:'book',title:'马哈希福音',url:'/zh-TW/books/maharshi-gospel.html',excerpt:'马哈希的灵性教导集'},
  {type:'book',title:'大瑜伽',url:'/zh-TW/books/maha-yoga.html',excerpt:'Sri Krishna Bhikshu 记录的上师教法'},
  {type:'book',title:'上师言颂',url:'/zh-TW/books/guru-vachaka-kovai.html',excerpt:'马哈希弟子编纂的精华语录'},
  {type:'book',title:'时代中的永恒',url:'/zh-TW/books/timeless.html',excerpt:'马哈希教法的现代诠释'},
  {type:'book',title:'反思录',url:'/zh-TW/books/reflections.html',excerpt:'马哈希弟子反思录'},
  {type:'book',title:'灵性故事',url:'/zh-TW/books/spiritual-stories.html',excerpt:'灵性故事的汇集'},
  {type:'book',title:'超越爱与恩典',url:'/zh-TW/books/surpassing-love.html',excerpt:'关于爱与恩典的深刻教导'},
  {type:'book',title:'桌边碎语',url:'/zh-TW/books/crumbs.html',excerpt:'静修院的日常对话'},
  {type:'book',title:'以言传意',url:'/zh-TW/books/teachings.html',excerpt:'马哈希亲口言传'},
  {type:'book',title:'全集',url:'/zh-TW/books/collected-works.html',excerpt:'马哈希全集收录'},
  // 概念
  {type:'concept',title:'真我(Atman)',url:'/zh-TW/concepts/atman.html',excerpt:'最内在的存在本质，永恒的意识'},
  {type:'concept',title:'梵(Brahman)',url:'/zh-TW/concepts/brahman.html',excerpt:'宇宙终极实相，无限的存在-意识-喜悦'},
  {type:'concept',title:'心智(Citta)',url:'/zh-TW/concepts/mind.html',excerpt:'意识的各种状态和活动'},
  {type:'concept',title:'自我/小我(Ego)',url:'/zh-TW/concepts/ego.html',excerpt:'虚假的个人身份认同'},
  {type:'concept',title:'摩耶(Maya)',url:'/zh-TW/concepts/maya.html',excerpt:'幻相的力量，创造幻象的力量'},
  {type:'concept',title:'我是谁？',url:'/zh-TW/concepts/whoami.html',excerpt:'马哈希最核心的参究法门'},
  {type:'concept',title:'解脱(Moksha)',url:'/zh-TW/concepts/moksha.html',excerpt:'从束缚中彻底觉醒'},
  {type:'concept',title:'恩典(Grace)',url:'/zh-TW/concepts/grace.html',excerpt:'上师的慈悲加持'},
  {type:'concept',title:'业力(Karma)',url:'/zh-TW/concepts/karma.html',excerpt:'行为及其因果'},
  {type:'concept',title:'三摩地(Samadhi)',url:'/zh-TW/concepts/samadhi.html',excerpt:'与真我合一的意识状态'},
  {type:'concept',title:'静默(Silence)',url:'/zh-TW/concepts/silence.html',excerpt:'马哈希的核心教法'},
  {type:'concept',title:'臣服(Surrender)',url:'/zh-TW/concepts/surrender.html',excerpt:'向真我臣服'},
  {type:'concept',title:'上师(Guru)',url:'/zh-TW/concepts/guru.html',excerpt:'灵性导师'},
  {type:'concept',title:'无我(Anatman)',url:'/zh-TW/concepts/anatma.html',excerpt:'无我/空性，与真我教义的对话'},
  {type:'concept',title:'自我参究(Atma Vichara)',url:'/zh-TW/concepts/atma-vichara.html',excerpt:'参究我是谁的核心方法'},
  {type:'concept',title:'法界(Dharmata)',url:'/zh-TW/concepts/dharmata.html',excerpt:'一切现象的究竟本性'},
  {type:'concept',title:'解脱之道(Moksha Marga)',url:'/zh-TW/concepts/moksha-path.html',excerpt:'智慧/虔诚/行动/禅定四道'},
  {type:'concept',title:'专一定住(Nishtha)',url:'/zh-TW/concepts/nishtha.html',excerpt:'对上师的坚定信靠与专注'},
  {type:'concept',title:'非二元(Advaita)',url:'/zh-TW/concepts/advaita.html',excerpt:'不二论的核心理论'},
  {type:'concept',title:'喜悦/极乐(Ananda)',url:'/zh-TW/concepts/ananda.html',excerpt:'极乐/真我的本质'},
  {type:'concept',title:'禅定(Dhyana)',url:'/zh-TW/concepts/dhyana.html',excerpt:'心意的专注与寂静'},
  {type:'concept',title:'出离(Vairagya)',url:'/zh-TW/concepts/vairagya.html',excerpt:'出离世俗欲望'},
  {type:'concept',title:'萨特-奇丹-阿南达',url:'/zh-TW/concepts/satchidananda.html',excerpt:'存在-意识-极乐三位一体'},
  // 人物
  {type:'person',title:'室利·拉玛那·马哈希',url:'/zh-TW/persons/ramana.html',excerpt:'二十世纪最重要的灵性导师之一，出生于阿鲁那佳拉山'},
  {type:'person',title:'大卫·高德曼',url:'/zh-TW/persons/david.html',excerpt:'《走向静默，如你本来》编者，拉玛那知识库创始人'},
  {type:'person',title:'阿莉伽玛（圣母）',url:'/zh-TW/persons/venkataramana.html',excerpt:'马哈希的姨妈，静修院的女瑜伽士'},
  // 方法
  {type:'method',title:'参究"我是谁"',url:'/zh-TW/methods/index.html',excerpt:'马哈希的核心修行法门'},
  {type:'method',title:'臣服上师',url:'/zh-TW/methods/index.html#surrender',excerpt:'完全向真我臣服'},
  {type:'method',title:'念诵咒语',url:'/zh-TW/methods/index.html#japa',excerpt:'持诵真我的名号'},
  {type:'method',title:'静默修行',url:'/zh-TW/methods/index.html#silence',excerpt:'体验内在的静默'},
  // 问答
  {type:'qa',title:'关于真我的问答',url:'/zh-TW/qa/index.html',excerpt:'什么是真我？如何认识真我？'},
  {type:'qa',title:'关于修行的问答',url:'/zh-TW/qa/index.html',excerpt:'如何修行？修行中的常见问题'},
  {type:'qa',title:'关于心智的问答',url:'/zh-TW/qa/index.html',excerpt:'心智是什么？如何让心智安静？'},
  {type:'qa',title:'关于解脱的问答',url:'/zh-TW/qa/index.html',excerpt:'什么是解脱？如何获得解脱？'},
  {type:'qa',title:'关于静默的问答',url:'/zh-TW/qa/index.html',excerpt:'马哈希为何保持静默？如何体验静默？'},
  {type:'qa',title:'关于幸福的问答',url:'/zh-TW/qa/index.html',excerpt:'什么是真正的幸福？幸福与快乐的区别'},
  {type:'qa',title:'关于西方修行者的问答',url:'/zh-TW/qa/index.html',excerpt:'西方人如何修行？需要改变生活方式吗？'}
];

const typeLabels = {book:'书籍',concept:'概念',qa:'问答',person:'人物',method:'方法'};
const typeColors = {book:'#3b82f6',concept:'#8b5cf6',qa:'#f59e0b',person:'#10b981',method:'#ec4899'};

// ========== 侧边栏切换 ==========
function toggleSidebar() {
  const sidebar = document.getElementById('sidebar');
  const overlay = document.getElementById('sidebarOverlay');
  if (!sidebar) return;
  const isOpen = sidebar.classList.contains('open');
  if (isOpen) {
    sidebar.classList.remove('open');
    if (overlay) overlay.classList.remove('open');
  } else {
    sidebar.classList.add('open');
    if (overlay) overlay.classList.add('open');
  }
}

// ========== 侧边栏折叠 ==========
function toggleSection(headerEl) {
  const section = headerEl.parentElement;
  const items = section.querySelector('.sidebar-items');
  if (!items) return;
  const isCollapsed = section.classList.contains('collapsed');
  if (isCollapsed) {
    section.classList.remove('collapsed');
    items.style.display = '';
  } else {
    section.classList.add('collapsed');
    items.style.display = 'none';
  }
}

// ========== 问答展开/收起 ==========
function toggleQA(element) {
  const qaItem = element.closest('.qa-item');
  if (qaItem) qaItem.classList.toggle('expanded');
}

// ========== 搜索高亮 ==========
function highlightMatch(text, query) {
  if (!query) return text;
  const regex = new RegExp(`(${query.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')})`, 'gi');
  return text.replace(regex, '<strong style="color:#fbbf24;">$1</strong>');
}

// ========== 初始化搜索 ==========
function initSearch() {
  const searchInput = document.getElementById('search-input');
  const searchResults = document.getElementById('search-results');
  if (!searchInput || !searchResults) return;

  let debounceTimer;
  searchInput.addEventListener('input', function() {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(() => {
      const q = this.value.trim().toLowerCase();
      if (!q) {
        searchResults.innerHTML = '';
        searchResults.style.display = 'none';
        return;
      }

      const matches = searchIndex.filter(item =>
        item.title.toLowerCase().includes(q) ||
        item.excerpt.toLowerCase().includes(q)
      );

      if (matches.length === 0) {
        searchResults.innerHTML = '<div style="padding:16px;color:#64748b;text-align:center;">未找到结果</div>';
      } else {
        searchResults.innerHTML = matches.slice(0, 8).map(item => `
          <a href="${item.url}" style="display:block;padding:12px 16px;border-bottom:1px solid rgba(255,255,255,0.05);text-decoration:none;color:#e2e8f0;">
            <div style="display:flex;align-items:center;gap:8px;margin-bottom:4px;">
              <span style="background:${typeColors[item.type] || '#666'};padding:2px 8px;border-radius:4px;font-size:11px;">${typeLabels[item.type] || item.type}</span>
              <span style="font-weight:500;">${highlightMatch(item.title, q)}</span>
            </div>
            <div style="font-size:12px;color:#94a3b8;">${highlightMatch(item.excerpt, q)}</div>
          </a>
        `).join('');
      }
      searchResults.style.display = 'block';
    }, 150); // 防抖 150ms
  });

  searchInput.addEventListener('blur', function() {
    setTimeout(() => { searchResults.style.display = 'none'; }, 200);
  });

  searchInput.addEventListener('focus', function() {
    if (this.value.trim()) searchResults.style.display = 'block';
  });
}

// ========== DOM 加载完成后初始化 ==========
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initApp);
} else {
  initApp();
}

function initApp() {
  // 初始化搜索
  initSearch();

  // 侧边栏折叠功能
  document.querySelectorAll('.sidebar-section-title').forEach(function(title) {
    title.style.cursor = 'pointer';
    title.addEventListener('click', function() { toggleSection(this); });
  });

  // 遮罩层点击关闭
  const overlay = document.getElementById('sidebarOverlay');
  if (overlay) overlay.addEventListener('click', toggleSidebar);

  // 动画延迟（使用 requestAnimationFrame 优化）
  requestAnimationFrame(() => {
    document.querySelectorAll('.stat-card, .quick-entry a, .card').forEach((el, i) => {
      el.style.animationDelay = (i * 0.08) + 's';
    });
  });
}
