# 🤖 Ramana Maharshi Knowledge Base (ramanamaharshi.space) — Agent Guide

欢迎来到 `ramanamaharshi.space`！本文件作为所有进入本项目的 AI 编码智能体（Agent）的全局记忆与行为规范。

---

> [!NOTE]
> **🐙 官方 GitHub 仓库与账号规范 (GitHub Repository Info)**
> * 官方仓库地址：`https://github.com/creativeburster/ramanamaharshi.space`
> * 默认生产分支：`main`
> * **迁移规范**：本项目已全量迁移至新 GitHub 账号 `creativeburster`。旧账号 `gstar-byte` 已废弃，严禁在任何脚本、配置、文档或外链中引用旧账号地址。

---

> [!IMPORTANT]
> **🌟 Git 操作与推送红线 (Strict Git Push Ban)**
> 智能体**绝对不允许自主执行 `git push` 命令**！所有改动必须在本地验证无误，并在用户明确下达“push/推送”指令时方可推送。

---

## 🏗️ 架构与部署规范 (Architecture & Deployment)

* **纯静态架构**：本项目为纯静态多页面站点，核心网页与资源**全部存放在 `pages/` 目录下**（包含 `index.html`、`styles.css`、`_headers`、`_redirects`、`zh-TW/` 等）。
* **Cloudflare Pages 部署配置**：
  * Framework preset: `None`
  * Build command: 留空（无须编译）
  * Build output directory: `pages`
* **交互语言**：与用户的所有对话与汇报必须使用简体中文。
