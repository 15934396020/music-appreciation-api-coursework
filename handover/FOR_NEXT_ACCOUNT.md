# Start Here for the Next Account

## Purpose

This file is the **single most important onboarding file** for any new account that continues this coursework project. If you are the next account, read this file first, then follow the exact reading order below. The user should not need to re-explain the project if this file and the repository are available.

## What This Project Is

This repository contains a coursework project named **Music Appreciation and Discovery API**. It is a database-backed API built for a university coursework brief that requires a meaningful API project with CRUD functionality, documentation, version control, and presentation materials.

The project theme has already been chosen and should not be changed unless the user explicitly requests a new direction.

> The chosen direction is a **music appreciation / music discovery API**, designed to achieve a **middle-to-upper level mark** through stability, clarity, and good presentation, rather than maximum technical complexity.

## Core Strategy That Must Remain Stable

The project should continue with the following principles.

| Area | Decision that should remain in force |
|---|---|
| Coursework goal | Aim for a solid middle-to-upper result, not an over-ambitious build |
| Theme | Music appreciation and discovery |
| Stack | FastAPI + SQLAlchemy + SQLite |
| Main CRUD focus | Reviews |
| Supporting features | Tracks, genres, user tags, collections, analytics |
| Workflow | Every session must update handover files before ending |
| Complexity control | Avoid advanced recommendation systems, authentication systems, or external API dependency in the core version |

## Current Implementation Summary

A working first milestone already exists. The repository already includes:

| Completed component | Status |
|---|---|
| Repository initialization | Done |
| Branch setup | Done, using `main` |
| FastAPI application | Done |
| Database connection | Done |
| SQLAlchemy models | Done |
| Seed dataset | Done |
| Core CRUD for reviews | Done |
| Track and genre browsing endpoints | Done |
| Tag and collection endpoints | Done |
| Analytics endpoints | Done |
| Smoke tests | Done |
| README and API planning docs | Done |
| Multi-account handover system | Done |
| Local Git commit | Done |

## Existing Endpoints

| Group | Endpoints currently available |
|---|---|
| General | `/`, `/health` |
| Tracks | `GET /tracks`, `GET /tracks/{track_id}` |
| Genres | `GET /genres` |
| Reviews | `POST /reviews`, `GET /reviews`, `GET /reviews/{review_id}`, `PUT /reviews/{review_id}`, `DELETE /reviews/{review_id}` |
| Tags | `POST /tags`, `DELETE /tags/{tag_id}` |
| Collections | `POST /collections`, `GET /collections`, `POST /collections/{collection_id}/items` |
| Analytics | `GET /analytics/top-rated-tracks`, `GET /analytics/genre-summary`, `GET /analytics/top-tags` |

## Exact Reading Order for the Next Account

Before changing any code, read these files in this exact order.

| Order | File | Why it matters |
|---|---|---|
| 1 | `handover/FOR_NEXT_ACCOUNT.md` | Quick project understanding and continuation rules |
| 2 | `handover/CURRENT_STATUS.md` | Latest real project state |
| 3 | `handover/NEXT_ACTIONS.md` | Immediate tasks to continue |
| 4 | `handover/SESSION_LOG.md` | Historical context and decisions |
| 5 | `handover/OPEN_QUESTIONS.md` | Known risks and unresolved issues |
| 6 | `README.md` | Repository-level understanding |
| 7 | `docs/API_PLAN.md` | Endpoint and data model scope |
| 8 | `docs/GITHUB_UPLOAD.md` | Remote publishing guidance |

## What the User Should Send to a New Account

If the repository has already been uploaded to GitHub, the user should preferably send **only two things**:

| Item | What to send |
|---|---|
| 1 | The GitHub repository link |
| 2 | A short instruction: “Please read `handover/FOR_NEXT_ACCOUNT.md` first and continue from `handover/NEXT_ACTIONS.md`.” |

If GitHub is not yet available, the user should send the **project zip file** and the same short instruction.

## Message Template the User Can Paste to a New Account

The user may paste the following message directly with almost no editing:

> Please continue this coursework project from the existing repository. Read `handover/FOR_NEXT_ACCOUNT.md` first, then `handover/CURRENT_STATUS.md` and `handover/NEXT_ACTIONS.md`. Do not redesign the project unless necessary. Continue from the recorded next tasks, update all handover files before stopping, and leave the repository in a clean, explainable state for the next account.

## What the Next Account Should Do First

The next account should **not** start by asking broad questions unless something critical is missing. Instead, it should first inspect the recorded state and continue practical work. The current recommended direction is:

| Priority | Task |
|---|---|
| 1 | Ensure repository remains clean and GitHub-ready |
| 2 | Add small completeness improvements if helpful |
| 3 | Prepare coursework report outline |
| 4 | Prepare presentation outline |
| 5 | Push to GitHub if credentials or access are available |

## Mandatory End-of-Session Behaviour

Before any session ends, especially when usage is low, the current account must update these files:

| File | Required update |
|---|---|
| `handover/CURRENT_STATUS.md` | Real current state |
| `handover/NEXT_ACTIONS.md` | Exact next tasks |
| `handover/SESSION_LOG.md` | What was done in this session |
| `handover/OPEN_QUESTIONS.md` | New blockers or decisions |

## Scope Reminder

This coursework does **not** need to become a commercial product. The best path is to produce a project that is coherent, testable, documented, and easy to explain in the final submission and presentation.
