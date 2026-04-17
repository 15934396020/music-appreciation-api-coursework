# Start Here for the Next Account

## Purpose

This file is the **single most important onboarding file** for any new account that continues this coursework project. If you are the next account, read this file first, then follow the exact reading order below. The user should not need to re-explain the project if this file and the repository are available.

## What This Project Is

This repository contains a coursework project named **Music Appreciation and Discovery API**. It is a database-backed API built for a university coursework brief (XJCO3011 — Web Services and Web Data) that requires a meaningful API project with CRUD functionality, authentication, documentation, version control, and presentation materials.

> **Current Version:** v0.3.0 — All core deliverables are complete.
> **Deadline:** 21 April 2026 via Minerva
> **Assessment:** 10-minute Oral Examination (5 min presentation + 5 min Q&A)

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
| 3 | `handover/NEXT_ACTIONS.md` | Immediate tasks to continue |
| 4 | `handover/SESSION_LOG.md` | Historical context and decisions across 3 sessions |
| 5 | `README.md` | Repository-level understanding |

## What the Next Account Should Do

All core deliverables are complete. The remaining work is:

| Priority | Task |
|---|---|
| 1 | Help user submit to Minerva (if needed) |
| 2 | Help user prepare for oral examination |
| 3 | Optional: Add pytest-cov, Docker, rate limiting for higher marks |

**DO NOT:**
- Redesign or rebuild the project
- Modify working code unless there is a specific bug
- Re-create documents that already exist

## Message Template the User Can Paste to a New Account

```
这是我们的课程项目仓库：https://github.com/15934396020/music-appreciation-api-coursework
请先阅读仓库里的 handover/FOR_NEXT_ACCOUNT.md，再查看 handover/CURRENT_STATUS.md 和 handover/NEXT_ACTIONS.md。
这个项目是 Music Appreciation and Discovery API，目前已经完成可运行原型、25个API接口、55个自动化测试、API Key认证、结构化错误处理、技术报告（PDF）、API文档（PDF）、12页PPTX演示幻灯片、GenAI对话日志、交接文档和 GitHub 同步。
请不要重做已经完成的部分，而是直接按照 NEXT_ACTIONS.md 继续推进。
本轮结束前，请同步更新交接文件，方便下一个账号继续接力。
```

## Mandatory End-of-Session Behaviour

Before any session ends, the current account must update these files:

| File | Required update |
|---|---|
| `handover/CURRENT_STATUS.md` | Real current state |
| `handover/NEXT_ACTIONS.md` | Exact next tasks |
| `handover/SESSION_LOG.md` | What was done in this session |

Then push all changes to GitHub.
