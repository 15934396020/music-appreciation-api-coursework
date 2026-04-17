# FOR NEXT ACCOUNT

## Purpose

This file is the **single most important onboarding file** for any new account that continues this coursework project. If you are the next account, read this file first, then follow the reading order listed below. The user should not need to re-explain the project if this repository and the handover files are available.

## What This Project Is

This repository contains a coursework project named **Music Appreciation and Discovery API**. It is a database-backed RESTful API built for the XJCO3011 module and designed to satisfy the coursework requirements for CRUD functionality, authentication, documentation, presentation, and version-controlled development.

> **Current Version:** v0.3.0  
> **Deadline:** 21 April 2026 via Minerva  
> **Assessment:** 10-minute Oral Examination (5 min presentation + 5 min Q&A)

## Critical Status Update

The previously unfinished external deployment work is now **complete**.

| Item | Current status |
|---|---|
| External deployment | **DONE** |
| Live URL | `https://weidademiaoxiao.pythonanywhere.com` |
| Interactive docs | `/docs` and `/redoc` on the live site |
| Verification | Live root endpoint and `/health` have been validated during deployment work |

This means the project has now cleared the earlier 40–49 deployment ceiling and satisfies the coursework expectation of being hosted on an external web server.

## Project Completion Status

| Component | Status | Details |
|---|---|---|
| FastAPI Application | DONE | 25 endpoints, lifespan management, CORS |
| API Key Authentication | DONE | `app/auth.py` — X-API-Key header for write ops |
| Structured Error Handling | DONE | `app/errors.py` — consistent JSON errors |
| Database & Models | DONE | 6 entities, 29 seed tracks, 8 genres |
| Automated Tests | DONE | **55 tests**, 9 classes, all passing |
| External Deployment | DONE | PythonAnywhere ASGI deployment at `weidademiaoxiao.pythonanywhere.com` |
| README | DONE (updated locally) | Live deployment URL added |
| Technical Report (MD + PDF) | DONE (updated locally) | Live deployment URL added and PDF regenerated |
| API Documentation (MD + PDF) | DONE (updated locally) | Base URL updated and PDF regenerated |
| Presentation (PPTX) | DONE (updated locally) | Live deployment references refreshed and PPTX regenerated |
| GenAI Conversation Log | DONE | `docs/GENAI_CONVERSATION_LOG.pdf` |
| GitHub Push | **PENDING IN CURRENT SESSION** | Local changes still need to be committed and pushed if not already done |

## PythonAnywhere Deployment Facts

The deployed platform is **PythonAnywhere**, not Render.

| Field | Value |
|---|---|
| Username | `weidademiaoxiao` |
| Password | `0355woDE!` |
| Domain | `weidademiaoxiao.pythonanywhere.com` |
| Deployment type | PythonAnywhere **ASGI** web app |
| Important supporting files | `requirements-deploy.txt`, `scripts/pythonanywhere_start.sh`, `wheelhouse/` |
| Technical notes | `handover/deployment_research_notes_2026-04-17.md` |

The successful workaround was to avoid remote PyPI installation problems by preparing deployment dependencies locally and using uploaded offline assets for the PythonAnywhere startup flow.

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
| Risk control | Do **not** redesign finished work unless there is a verified bug |

## Exact Reading Order for the Next Account

Before changing any code, read these files in this exact order.

| Order | File | Why it matters |
|---|---|---|
| 1 | `handover/FOR_NEXT_ACCOUNT.md` | Quick project understanding and continuation rules (this file) |
| 2 | `handover/CURRENT_STATUS.md` | Latest factual project state |
| 3 | `handover/NEXT_ACTIONS.md` | Immediate remaining tasks after deployment |
| 4 | `handover/SESSION_LOG.md` | Historical context and decisions across sessions |
| 5 | `README.md` | Repository-level understanding and live URL |

## What the Next Account Should Do

If the current session stops before everything is pushed, the next account should **not** repeat deployment. It should continue from the finishing tasks below.

| Priority | Task | Status |
|---|---|---|
| **1** | **Check local changes, commit them, and push to GitHub** | Highest priority if not yet completed |
| 2 | Reconfirm live URL in README / report / API docs / PPTX | Mostly done locally; verify only |
| 3 | Help user prepare Minerva submission | Pending user-facing support |
| 4 | Help user prepare oral examination | Optional but useful |

## Do Not Do These Things

- Do **not** redeploy from scratch unless the live site is actually broken.
- Do **not** rebuild the API, tests, report, or presentation.
- Do **not** remove the PythonAnywhere deployment assets (`requirements-deploy.txt`, `scripts/pythonanywhere_start.sh`, `wheelhouse/`) unless replacing them with a verified superior deployment path.

## Message Template the User Can Paste to a New Account

```text
这是我们的课程项目仓库：https://github.com/15934396020/music-appreciation-api-coursework 。请先阅读仓库里的 handover/FOR_NEXT_ACCOUNT.md，再查看 handover/CURRENT_STATUS.md 和 handover/NEXT_ACTIONS.md。这个项目是 Music Appreciation and Discovery API，目前已经完成可运行原型、25个API接口、55个自动化测试、API Key认证、结构化错误处理、技术报告（PDF）、API文档（PDF）、12页PPTX演示幻灯片、GenAI对话日志，并且已经部署到外部平台：https://weidademiaoxiao.pythonanywhere.com 。请不要重做已经完成的部分，而是直接从交接文件记录的剩余收尾任务继续推进；本轮结束前，请同步更新交接文件。
```

## GitHub Push

The user provided a GitHub PAT in the conversation. If push still remains unfinished, use the following pattern:

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

Then push all changes to GitHub if possible.
