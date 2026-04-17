# Start Here for the Next Account

## Purpose

This file is the **single most important onboarding file** for any new account that continues this coursework project. If you are the next account, read this file first, then follow the exact reading order below. The user should not need to re-explain the project if this file and the repository are available.

## What This Project Is

This repository contains a coursework project named **Music Appreciation and Discovery API**. It is a database-backed API built for a university coursework brief (XJCO3011 — Web Services and Web Data) that requires a meaningful API project with CRUD functionality, authentication, documentation, version control, and presentation materials.

> **Current Version:** v0.3.0 — All core deliverables are complete.
> **Deadline:** 21 April 2026 via Minerva
> **Assessment:** 10-minute Oral Examination (5 min presentation + 5 min Q&A)

## ⚠️ CRITICAL: 唯一剩余的关键工作 — 部署到外部平台

**不部署 = 最多只能拿 Pass 分数（40-49）。部署是拿 50+ 分的硬性要求。**

课程评分标准明确规定：
- 40-49 (Pass): "server-side code **not deployed** on an external platform"
- 50-59 (Satisfactory): "Hosted on an external web server, e.g. PythonAnywhere"
- 70-79 (Very Good): "Professional deployment"

**推荐使用 Render.com**（免费，原生支持 FastAPI/ASGI），而非 PythonAnywhere（不原生支持 ASGI）。

详细部署步骤见 `handover/NEXT_ACTIONS.md` 的 "Priority 1" 部分。

## Project Completion Status

| Component | Status | Details |
|---|---|---|
| FastAPI Application | DONE | 25 endpoints, lifespan management, CORS |
| API Key Authentication | DONE | `app/auth.py` — X-API-Key header for write ops |
| Structured Error Handling | DONE | `app/errors.py` — consistent JSON errors |
| Database & Models | DONE | 6 entities, 29 seed tracks, 8 genres |
| Automated Tests | DONE | **55 tests**, 9 classes, all passing |
| Technical Report (PDF) | DONE | `docs/TECHNICAL_REPORT.pdf` |
| API Documentation (PDF) | DONE | `docs/API_DOCUMENTATION.pdf` |
| Presentation (PPTX) | DONE | `docs/PRESENTATION.pptx` (12 slides) |
| GenAI Conversation Log | DONE | `docs/GENAI_CONVERSATION_LOG.pdf` |
| GitHub Repository | DONE | All code pushed to main branch |
| **External Deployment** | **NOT DONE** | **最高优先级 — 推荐 Render.com** |

## PythonAnywhere Account (Created but Incomplete)

Session 3 已创建 PythonAnywhere 账号，但发现其不原生支持 FastAPI：
- 用户名：`weidademiaoxiao`
- 密码：`0355woDE!`
- 域名：`weidademiaoxiao.pythonanywhere.com`
- 状态：已创建 web app（Manual Config, Python 3.10），需要 ASGI beta API 配置
- 如果要用 PythonAnywhere，参考：https://help.pythonanywhere.com/pages/ASGICommandLine/

## Core Strategy That Must Remain Stable

| Area | Decision that should remain in force |
|---|---|
| Coursework goal | Aim for a solid middle-to-upper result (70-79 band) |
| Theme | Music appreciation and discovery |
| Stack | FastAPI + SQLAlchemy + SQLite |
| Main CRUD focus | Reviews (full lifecycle with auth) |
| Supporting features | Tracks, genres, user tags, collections, analytics |
| Authentication | API key via X-API-Key header (demo key: `music-api-demo-key-2026`) |
| Workflow | Every session must update handover files before ending |

## Exact Reading Order for the Next Account

Before changing any code, read these files in this exact order.

| Order | File | Why it matters |
|---|---|---|
| 1 | `handover/FOR_NEXT_ACCOUNT.md` | Quick project understanding and continuation rules (this file) |
| 2 | `handover/CURRENT_STATUS.md` | Latest real project state with all changes |
| 3 | `handover/NEXT_ACTIONS.md` | Immediate tasks to continue (deployment instructions!) |
| 4 | `handover/SESSION_LOG.md` | Historical context and decisions across 3 sessions |
| 5 | `README.md` | Repository-level understanding |

## What the Next Account Should Do

| Priority | Task | Status |
|---|---|---|
| **1** | **部署到外部平台（Render.com 推荐）** | **NOT DONE — 最高优先级** |
| 2 | 部署后更新文档中的 URL | Pending |
| 3 | 推送更新到 GitHub | Pending |
| 4 | 帮用户准备 Minerva 提交 | Pending |
| 5 | 帮用户准备口头答辩 | Optional |

**DO NOT:**
- Redesign or rebuild the project
- Modify working code unless there is a specific bug
- Re-create documents that already exist

## Message Template the User Can Paste to a New Account

```
这是我们的课程项目仓库：https://github.com/15934396020/music-appreciation-api-coursework  。请先阅读仓库里的 handover/FOR_NEXT_ACCOUNT.md，再查看 handover/CURRENT_STATUS.md 和 handover/NEXT_ACTIONS.md。这个项目是 Music Appreciation and Discovery API，目前已经完成可运行原型、25个API接口、55个自动化测试、API Key认证、结构化错误处理、技术报告（PDF）、API文档（PDF）、12页PPTX演示幻灯片、GenAI对话日志、交接文档和 GitHub 同步。**唯一剩余的关键工作是：部署到外部平台（不部署只能拿 Pass 分数 40-49）。** 请不要重做已经完成的部分，而是直接按照 NEXT_ACTIONS.md 继续推进；本轮结束前，请同步更新交接文件，方便下一个账号继续接力。
```

附件说明：
- `handover-for-next-account.zip` — 完整项目代码（含 .git 历史和所有交接文档），解压后可直接运行和开发
- `coursework-submission.zip` — 当前已完成的作业提交材料（技术报告 PDF、API文档 PDF、演示幻灯片），请在此基础上继续完善，不要重做
- `XJCO3011_Coursework1_Brief__2025_2026(1).pdf` — 课程要求原文，请仔细对照 deadline（4月21日）和评分标准来推进剩余工作

## GitHub Push

GitHub PAT 需要用户提供。推送命令：
```bash
git remote set-url origin https://<PAT>@github.com/15934396020/music-appreciation-api-coursework.git
git push origin main
git remote set-url origin https://github.com/15934396020/music-appreciation-api-coursework.git
```

## Mandatory End-of-Session Behaviour

Before any session ends, the current account must update these files:

| File | Required update |
|---|---|
| `handover/CURRENT_STATUS.md` | Real current state |
| `handover/NEXT_ACTIONS.md` | Exact next tasks |
| `handover/SESSION_LOG.md` | What was done in this session |

Then push all changes to GitHub.
