# Multi-Account Handover Protocol

## Purpose

This project is designed to be continued by multiple accounts in separate working sessions. The goal of this protocol is to ensure that any new session can understand the project state within a few minutes, continue implementation without repeating work, and leave behind a clear record for the next session.

## Mandatory Workflow for Every New Session

When a new account starts working on this project, it must read the following files in order before changing code:

| Order | File | Purpose |
|---|---|---|
| 1 | `handover/CURRENT_STATUS.md` | Understand the latest build status, completed work, blockers, and immediate priorities |
| 2 | `handover/NEXT_ACTIONS.md` | See the exact next implementation tasks to continue |
| 3 | `handover/SESSION_LOG.md` | Review recent work history and decisions made in previous sessions |
| 4 | `README.md` | Understand the project purpose, setup steps, and architecture summary |
| 5 | `docs/API_PLAN.md` | Understand data model, endpoint design, and scope |

Only after reading these files should the next account begin coding.

## Mandatory Handover Before a Session Ends

Before the current account stops, especially when time or usage is running low, it must update all of the following:

| File | What must be updated |
|---|---|
| `handover/CURRENT_STATUS.md` | Current implementation state, what works now, what is unfinished, whether the app runs |
| `handover/NEXT_ACTIONS.md` | The next 3 to 7 concrete tasks in order |
| `handover/SESSION_LOG.md` | A dated summary of what was completed in the session |
| `handover/OPEN_QUESTIONS.md` | Any unresolved design decisions, bugs, or risks |

## Decision-Making Rules

All sessions should follow the same project strategy unless the user explicitly changes it.

> The project target is **middle-to-upper performance**, not maximum complexity.

That means every account should prefer:

- stable and explainable implementation;
- clean CRUD and analytics endpoints;
- solid documentation and Git history;
- low-risk technical choices;
- incremental progress that is easy to present in the coursework oral exam.

Every session should avoid unnecessary complexity such as advanced recommendation engines, heavy audio processing, or large-scale infrastructure changes unless the user specifically requests them.

## Branching and Commit Guidance

This local repository is prepared for GitHub upload. Each session should make small logical commits after meaningful milestones. Suggested commit style:

| Type | Example |
|---|---|
| setup | `setup: initialize FastAPI project structure` |
| feat | `feat: add review CRUD endpoints` |
| docs | `docs: update handover and API plan` |
| fix | `fix: correct review validation and status codes` |
| test | `test: add API smoke tests for tracks and reviews` |

## Session Exit Checklist

Before ending a session, confirm the following:

| Check | Requirement |
|---|---|
| Code state recorded | `CURRENT_STATUS.md` updated |
| Next work clear | `NEXT_ACTIONS.md` updated |
| Work history preserved | `SESSION_LOG.md` updated |
| Known risks preserved | `OPEN_QUESTIONS.md` updated |
| Setup still reproducible | `README.md` reflects current state |

## Current Project Direction

The current project is a **Music Appreciation and Discovery API** for coursework. It uses a local SQL database and focuses on:

- track browsing;
- genre browsing;
- review CRUD;
- user tags;
- collections;
- simple analytics endpoints.

The project is intended to be implemented with **FastAPI + SQLAlchemy + SQLite**, then uploaded to GitHub for submission preparation.
