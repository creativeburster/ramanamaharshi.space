# -*- coding: utf-8 -*-
"""
打包 ramanamaharshi.space 完整生产代码包用于顾问审查（Argon / Code Reviewer）
特点：
1. 完整可用：包含全部生产网页(746+ HTML)、CSS、JS、知识图谱、图片、Sitemap、_headers、_redirects、zh-TW 繁体镜像等
2. 极端小巧：严格剔除历史 .git (包括 pages/ramana-kb/.git 120MB 的历史 pack)、.bak 临时备份、.py 运维脚本与构建残留，将总体积压缩至 6MB 左右
3. 顾问导读：附带 AUDIT_BRIEF.md，详细阐述架构选型、部署参数、路由、SEO、PWA 及审查建议维度
"""

import os
import zipfile

PROJECT_ROOT = r"F:\Ramana"
OUTPUT_ZIP = os.path.join(PROJECT_ROOT, "ramanamaharshi-space-audit-pack.zip")

AUDIT_BRIEF_CONTENT = """# 📋 Ramana Maharshi Knowledge Base (ramanamaharshi.space) 网站审查与顾问指引

致顾问（Argon / Website Reviewer & Consultant）：

欢迎审查 **ramanamaharshi.space** 网站代码包！
本项目是专注于印度圣哲**拉玛那·马哈希（Bhagavan Sri Ramana Maharshi）**生平、核心教导、自探法（Self-Enquiry / Vichara）及不二论（Advaita Vedanta）的现代化多语言中文数字图书馆与互动知识库。

---

## 🎯 网站技术架构概览 (Architecture Overview)

1. **部署架构**：
   - 托管平台：Cloudflare Pages 边缘网络
   - 架构模式：纯静态（Pure Static Multi-page Site, 无 SSR/Node 服务端运行时），极速边缘直出与全球 CDN 分发。
   - 生产输出目录：`pages/`（本压缩包解压后的根目录即对应线上生产站点）。
   - 边缘规则：包含 `_headers`（细粒度安全策略与强缓存策略）与 `_redirects`（规范化 canonical 301 重定向与裸域跳转）。

2. **多语言与本地化体系**：
   - 简体中文（主站）：根路径 `/`
   - 繁体中文（台湾/港澳/海外华人）：`/zh-TW/`
   - 页面间通过严格的双向 `<link rel="alternate" hreflang="..." />` 互相关联。

3. **前端技术栈与性能**：
   - 无沉重 SPA 框架（无 React/Vue 运行时开销），使用语义化 HTML5 + 原生模块化 CSS3 + 原生 JavaScript。
   - 交互功能：
     - `search.js`：轻量级前端全文检索与快速定位
     - `graph.html` + `d3.min.js`：自研知识图谱拓扑关系网络可视化
     - `sw.js` + `manifest.json`：具备 PWA 渐进式 Web 应用支持，静态资产离线缓存与秒级二访加载。

4. **SEO 与搜索引擎互联**：
   - 完整的 TDK 元数据规范（Title / Description / Keywords）。
   - OpenGraph & Twitter Card 社交分享卡片。
   - Schema.org (JSON-LD) 结构化数据（WebSite, Article, BreadcrumbList, QAPage）。
   - 模块化 XML 站点地图（`sitemap.xml` 索引包含 `sitemap-books.xml`, `sitemap-concepts.xml`, `sitemap-qa.xml`, `sitemap-zh-tw.xml`）。
   - 自动化索引推送：`.github/workflows/indexnow.yml` 支持 Bing/Yandex 的 IndexNow 协议主动收录。
   - 大模型与 AI Agent 友好：根目录提供 `llms.txt` 和 `llms-full.txt`，遵循 LLMs.txt 抓取建议标准。

---

## 📂 核心目录与文件结构说明

```text
/
├── index.html                # 网站主页（知识导航与入口）
├── graph.html                # 交互式知识图谱可视化（基于 D3.js）
├── styles.css                # 主样式表
├── styles.min.css            # 压缩版样式表
├── script.js                 # 核心通用交互逻辑
├── search.js                 # 本地全文搜索引擎
├── sw.js                     # Service Worker PWA 缓存控制
├── manifest.json             # PWA 清单
├── robots.txt                # 搜索引擎爬虫协议
├── sitemap.xml               # 站点地图入口索引
├── sitemap-*.xml             # 细分分类站点地图
├── _headers                  # Cloudflare Pages 边缘响应头（CSP, HSTS, Cache-Control）
├── _redirects                # 边缘 301 重定向规则
├── books/                    # 核心经典文献书库（原著中译、章节精读）
├── concepts/                 # 核心概念解析（真我、自探、不二论、幻力等）
├── qa/                       # 核心问答录（分类整理的大师问答与解惑）
├── methods/                  # 实修方法指南（自探实践步骤）
├── persons/                  # 门徒与相关历史人物志
├── icons/ & images/          # 网站图标、PWA 图标与社交分享头图
├── zh-TW/                    # 繁体中文完整镜像库
├── AGENTS.md                 # 仓库维护全局规范与部署指引
├── llms.txt & llms-full.txt  # LLM 结构化索引规范文件
└── .github/workflows/        # IndexNow 自动化主动推送工作流
```

---

## 💡 期待顾问审查的关键维度 (Recommended Review Dimensions)

请顾问（Argon）从以下几个关键维度对网站进行全面体检与审查，并提出专业优化建议：

1. **SEO 与搜索引擎可发现性 (SEO & Discoverability)**：
   - 标题（Title）、描述（Description）的唯一性、长度与点击率优化（CTR）。
   - 双语/繁简 `hreflang` 标签配置是否完全合规、是否存在孤岛页面或死链。
   - JSON-LD 结构化数据字段深度（是否可以丰富 FAQPage、Book、Chapter、Author 等更专一的 Schema）。
   - 内链拓扑：核心书籍章节与概念词条之间的网状内链是否足够紧密。

2. **现代前端体验与性能 (Frontend Performance & Core Web Vitals)**：
   - 关键渲染路径与 LCP / CLS / INP 指标优化建议。
   - CSS 架构与现代化重构建议（如 CSS 变量、深色模式支持、流式排版）。
   - JavaScript 脚本执行性能与 Service Worker 缓存淘汰策略。

3. **用户体验与内容排版 (UX / Typography / Accessibility)**：
   - 经文与严肃哲学阅读场景下的长文本阅读体验（字号、行距、对比度、分段留白）。
   - 移动端适配与自适应响应式细节。
   - 无障碍设计（WCAG 2.1 AA 规范、ARIA 属性、键盘导航等）。

4. **知识图谱与互动功能 (Graph & Exploration)**：
   - `graph.html` 的可视化呈现、力导向图交互流畅度与移动端友好性改进。
   - 站内检索 `search.js` 的模糊匹配、分词能力与高亮交互体验。

5. **AI 与 LLM 协同 (AI Agent Readiness)**：
   - `llms.txt` 和 `llms-full.txt` 的内容完整度与上下文利用率评估。

---

## 🚀 本地快速启动与预览方法

无需安装任何繁琐依赖，解压后在当前目录下运行任意静态 Web 服务器即可：

```bash
# Python 3
python -m http.server 8080

# 或 Node.js
npx serve .

# 或 PHP
php -S localhost:8080
```
访问 `http://localhost:8080` 即可完全体验线上站点的所有交互功能。
"""

def build_package():
    print("Starting build of audit package...")
    
    EXCLUDE_DIRS = {'.git', '__pycache__', 'node_modules', '.wrangler', '.astro', '.windsurf', '.workbuddy', 'dist'}
    EXCLUDE_EXTS = {'.bak', '.backup', '.py', '.pyc', '.tmp', '.old'}
    
    if os.path.exists(OUTPUT_ZIP):
        os.remove(OUTPUT_ZIP)
        
    file_count = 0
    total_uncompressed = 0
    added_names = set()
    
    with zipfile.ZipFile(OUTPUT_ZIP, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        # 1. 写入顾问说明文档
        zf.writestr("AUDIT_BRIEF.md", AUDIT_BRIEF_CONTENT.encode('utf-8'))
        added_names.add("AUDIT_BRIEF.md")
        file_count += 1
        
        # 2. 写入根目录特有规范与索引文档
        for root_file in ["AGENTS.md", "llms.txt", "llms-full.txt", ".gitignore"]:
            fp = os.path.join(PROJECT_ROOT, root_file)
            if os.path.exists(fp) and root_file not in added_names:
                zf.write(fp, root_file)
                added_names.add(root_file)
                file_count += 1
                total_uncompressed += os.path.getsize(fp)
                
        # 3. 写入 GitHub Actions (IndexNow)
        workflow_fp = os.path.join(PROJECT_ROOT, ".github", "workflows", "indexnow.yml")
        if os.path.exists(workflow_fp):
            zf.write(workflow_fp, ".github/workflows/indexnow.yml")
            added_names.add(".github/workflows/indexnow.yml")
            file_count += 1
            total_uncompressed += os.path.getsize(workflow_fp)

        # 4. 写入 pages/ 下所有核心生产网站文件
        pages_root = os.path.join(PROJECT_ROOT, "pages")
        for root, dirs, files in os.walk(pages_root):
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
            
            for f in files:
                ext = os.path.splitext(f)[1].lower()
                if ext in EXCLUDE_EXTS:
                    continue
                full_path = os.path.join(root, f)
                rel_path = os.path.relpath(full_path, pages_root)
                rel_archive_path = rel_path.replace("\\", "/")
                
                if rel_archive_path in added_names:
                    continue
                zf.write(full_path, rel_archive_path)
                added_names.add(rel_archive_path)
                file_count += 1
                total_uncompressed += os.path.getsize(full_path)

    zip_size = os.path.getsize(OUTPUT_ZIP)
    print("=" * 60)
    print("Build package successfully!")
    print(f"Archive path: {OUTPUT_ZIP}")
    print(f"Total files: {file_count}")
    print(f"Uncompressed size: {total_uncompressed / 1024 / 1024:.2f} MB")
    print(f"Compressed size: {zip_size / 1024 / 1024:.2f} MB ({zip_size} bytes)")
    print("=" * 60)

if __name__ == "__main__":
    build_package()
