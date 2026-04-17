# Current Status

> **Last updated: 2026-04-17 (Session 3)**

## Project Identity

| Item | Value |
|---|---|
| Project name | **Music Appreciation and Discovery API** |
| GitHub repository | `https://github.com/15934396020/music-appreciation-api-coursework` |
| Stack | **FastAPI 0.115.12 + SQLAlchemy 2.0.40 + Pydantic 2.11.3 + SQLite** |
| API version | **v0.3.0** (added authentication and structured error handling) |
| Coursework target | **middle-to-upper performance** (70-79 band) |
| Deadline | **21 April 2026** via Minerva |
| Assessment | **10-minute Oral Examination** (5 min presentation + 5 min Q&A) |

## First File to Read

Any new account must start with:

> `handover/FOR_NEXT_ACCOUNT.md`

## Completion Summary

| Area | Status | Details |
|---|---|---|
| FastAPI Application | DONE | `app/main.py` with lifespan, CORS, structured error handling |
| Authentication Module | DONE | `app/auth.py` — API key via X-API-Key header for write ops |
| Error Handling Module | DONE | `app/errors.py` — consistent JSON error responses |
| Database & Models | DONE | 6 entities: Genre, Track, Review, UserTag, Collection, CollectionItem |
| Pydantic Schemas | DONE | Request/response validation with strict constraints |
| Seed Data | DONE | 29 tracks across 8 genres in `app/seed.py` |
| API Endpoints | DONE | 25 endpoints across 7 groups |
| Automated Tests | DONE | **55 tests** across **9 test classes** — all passing |
| README.md | DONE | Full project documentation with auth examples |
| API Documentation (MD + PDF) | DONE | `docs/API_DOCUMENTATION.md` and `.pdf` |
| Technical Report (MD + PDF) | DONE | `docs/TECHNICAL_REPORT.md` and `.pdf` |
| Technical Report (LaTeX) | DONE | `docs/TECHNICAL_REPORT.tex` (from Session 2) |
| Presentation (PPTX) | DONE | `docs/PRESENTATION.pptx` — 12 professional slides |
| Presentation (HTML) | DONE | `docs/presentation/` — 10 slides (from Session 2) |
| GenAI Conversation Log | DONE | `docs/GENAI_CONVERSATION_LOG.md` and `.pdf` |
| GitHub Sync | DONE | All Session 3 changes pushed to main branch (commit `b02e6f6`) |
| Handover Documents | DONE | Updated for next session |
| **External Deployment** | **NOT DONE** | PythonAnywhere 不原生支持 ASGI/FastAPI，需要用 API 方式部署（见下方说明） |

## CRITICAL: Deployment Issue Discovered

**PythonAnywhere 不原生支持 FastAPI（ASGI 框架）。** 在 Session 3 尝试部署时发现：

1. PythonAnywhere 的标准 Web 界面只支持 WSGI 框架（Django, Flask 等）
2. FastAPI 是 ASGI 框架，需要通过 PythonAnywhere 的 **ASGI beta API** 部署
3. 官方文档：https://help.pythonanywhere.com/pages/ASGICommandLine/
4. 已在 PythonAnywhere 创建了账号并创建了 web app（手动配置模式），但尚未完成 ASGI 配置

**PythonAnywhere 账号信息：**
- 用户名：`weidademiaoxiao`
- 密码：`0355woDE!`
- 域名：`weidademiaoxiao.pythonanywhere.com`
- 状态：已创建 web app（Manual Configuration, Python 3.10），但 WSGI 文件需要改为 ASGI 配置

**部署方案选择（下一个账号需要决定）：**

| 方案 | 平台 | 难度 | 说明 |
|---|---|---|---|
| A | PythonAnywhere ASGI beta | 中 | 需要通过 API token + 命令行配置，参考官方文档 |
| B | Render.com | 低 | 免费，原生支持 FastAPI，自动从 GitHub 部署 |
| C | Railway.app | 低 | 免费额度，原生支持 FastAPI |
| D | Koyeb | 低 | 免费，原生支持 FastAPI |

**推荐方案 B（Render.com）**，因为课程要求只说"hosted on an external web server, e.g. PythonAnywhere"，并非必须用 PythonAnywhere。

## Session 3 Changes

### New Files
- `app/auth.py` — API key authentication module
- `app/errors.py` — Structured error handling module
- `docs/PRESENTATION.pptx` — 12-slide PowerPoint presentation
- `docs/GENAI_CONVERSATION_LOG.md` — GenAI usage documentation
- `docs/GENAI_CONVERSATION_LOG.pdf` — GenAI log PDF
- `scripts/create_pptx.py` — PPTX generation script

### Modified Files
- `app/main.py` — Integrated error handlers, updated version to 0.3.0
- `app/routers/api.py` — Added `require_api_key` dependency to all write endpoints
- `tests/conftest.py` — Added `auth_headers` fixture
- `tests/test_api.py` — 48 → 55 tests (added TestAuthentication class, auth headers)
- `docs/TECHNICAL_REPORT.md` + `.pdf` — Updated with auth section, fixed track count
- `docs/API_DOCUMENTATION.md` + `.pdf` — Added auth docs, error format, protected endpoints
- `README.md` — Added auth section, test count update, new files in structure

## Test Status

> **55 passed** in 0.48s (pytest -v)

Test classes:
1. TestGeneralEndpoints (2 tests)
2. TestGenreEndpoints (3 tests)
3. TestTrackEndpoints (8 tests)
4. TestReviewCRUD (9 tests)
5. TestTagEndpoints (7 tests)
6. TestCollectionEndpoints (9 tests)
7. TestAnalyticsEndpoints (5 tests)
8. TestAuthentication (6 tests) — NEW in Session 3
9. TestValidation (6 tests)

## Authentication Details

- **Scheme:** API Key via `X-API-Key` header
- **Demo Key:** `music-api-demo-key-2026`
- **Protected:** All POST, PUT, DELETE endpoints
- **Public:** All GET endpoints (including analytics)
- **Error codes:** 401 (missing key), 403 (invalid key)

## Remaining Work

| Priority | Task | Status |
|---|---|---|
| **1** | **部署到外部平台（50+ 分必需）** | **NOT DONE — 最高优先级** |
| 2 | 准备 Minerva 提交材料 | Pending |
| 3 | 准备口头答辩 | Pending |
