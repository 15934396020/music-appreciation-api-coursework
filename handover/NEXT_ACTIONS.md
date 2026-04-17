# NEXT ACTIONS

> **Last updated: 2026-04-17 (Session 4 — deployment completed, final wrap-up pending)**  
> **Deadline: 21 April 2026 (via Minerva)**  
> **Assessment: 10-minute Oral Examination (5 min presentation + 5 min Q&A)**

---

## Immediate Situation

The previous highest-risk task has been completed: the API is now externally deployed at:

> `https://weidademiaoxiao.pythonanywhere.com`

The repository has also been updated locally so that the live deployment URL appears in the key deliverables:

| Deliverable | Local update status |
|---|---|
| `README.md` | Updated |
| `docs/TECHNICAL_REPORT.md` | Updated |
| `docs/TECHNICAL_REPORT.pdf` | Regenerated |
| `docs/API_DOCUMENTATION.md` | Updated |
| `docs/API_DOCUMENTATION.pdf` | Regenerated |
| `docs/PRESENTATION.pptx` | Regenerated |
| `scripts/create_pptx.py` | Updated source for PPTX regeneration |

That means the **main remaining work is now repository sync and submission support**, not redeployment.

---

## Priority 1 — Commit and Push the Current Changes to GitHub

If the current session ends before pushing, the next account should continue from this exact point.

| Step | Action |
|---|---|
| 1 | Run `git status` and review modified files |
| 2 | Confirm that deployment-support assets are intentionally included: `requirements-deploy.txt`, `scripts/pythonanywhere_start.sh`, and `wheelhouse/` |
| 3 | Commit the changes with a clear message mentioning deployment completion and document refresh |
| 4 | Push to `main` using the user-provided PAT if necessary |
| 5 | Revert remote URL back to the clean GitHub URL after push |

Suggested command pattern:

```bash
git status
git add README.md docs/TECHNICAL_REPORT.md docs/TECHNICAL_REPORT.pdf docs/API_DOCUMENTATION.md docs/API_DOCUMENTATION.pdf docs/PRESENTATION.pptx scripts/create_pptx.py handover/FOR_NEXT_ACCOUNT.md handover/CURRENT_STATUS.md handover/NEXT_ACTIONS.md handover/SESSION_LOG.md handover/deployment_research_notes_2026-04-17.md requirements-deploy.txt scripts/pythonanywhere_start.sh wheelhouse/
git commit -m "Complete PythonAnywhere deployment and refresh deliverables"
git remote set-url origin https://<PAT>@github.com/15934396020/music-appreciation-api-coursework.git
git push origin main
git remote set-url origin https://github.com/15934396020/music-appreciation-api-coursework.git
```

---

## Priority 2 — Final Deployment Verification

Deployment is already working, but before ending the task or handing off, run one quick final verification.

| Check | Expected result |
|---|---|
| `GET /` | 200 OK with API welcome payload |
| `GET /health` | 200 OK with `{"status": "ok"}` |
| `/docs` | Swagger UI loads |
| `/redoc` | ReDoc loads |

Reference URLs:

- `https://weidademiaoxiao.pythonanywhere.com`
- `https://weidademiaoxiao.pythonanywhere.com/health`
- `https://weidademiaoxiao.pythonanywhere.com/docs`
- `https://weidademiaoxiao.pythonanywhere.com/redoc`

---

## Priority 3 — Ensure Handover Files Match the Live Reality

If more work is done, update the following files again before stopping.

| File | Required update |
|---|---|
| `handover/FOR_NEXT_ACCOUNT.md` | Keep the top-level message aligned with the current true state |
| `handover/CURRENT_STATUS.md` | Reflect the latest deployment / push / submission state |
| `handover/NEXT_ACTIONS.md` | Keep only the actually remaining tasks |
| `handover/SESSION_LOG.md` | Append what happened in this session |
| `handover/deployment_research_notes_2026-04-17.md` | Preserve the final technical deployment trail |

---

## Priority 4 — Help the User Prepare the Coursework Submission

The user ultimately needs submission-ready deliverables rather than more engineering work.

| Submission item | Current state |
|---|---|
| Technical Report (PDF) | Ready after updated regeneration |
| Presentation Slides (PPTX) | Ready after regeneration |
| API Documentation (PDF) | Ready after updated regeneration |
| GitHub Repository Link | Ready once final push completes |
| GenAI evidence | Already available in repository |

Practical support that may still be needed:

1. Confirm the final GitHub commit is visible online.
2. Confirm the technical report and API documentation PDFs in the repository are the refreshed versions.
3. Help the user identify exactly which files to upload to Minerva.

---

## Priority 5 — Oral Examination Preparation

If the user asks for help after the repo is synced, shift focus to presentation and Q&A preparation.

| Topic | Key angle |
|---|---|
| Problem framing | Music appreciation metadata API with realistic coursework scope |
| Stack choice | FastAPI + SQLAlchemy + SQLite for clarity, speed, and explainability |
| Security | API key authentication for write operations |
| Reliability | Structured error handling and 55 automated tests |
| Added value | 5 analytics endpoints beyond basic CRUD |
| Deployment | Live external hosting on PythonAnywhere |

---

## Important Do-Not-Repeat Guidance

- Do **not** redo the deployment unless the live service is actually broken.
- Do **not** rebuild documents that already exist.
- Do **not** remove deployment support files just to make the repo look smaller.
- Do **not** spend time switching to Render unless PythonAnywhere fails again and there is strong evidence that the live deployment is no longer usable.

---

## Completed Tasks (Do Not Repeat)

| Session | Already completed |
|---|---|
| Session 1 | Core FastAPI app, models, seed data, initial endpoints |
| Session 2 | Lifespan refactor, 48 tests, PDF documents, HTML slides, GitHub push |
| Session 3 | API key auth, structured errors, 55 tests, PPTX deck, GenAI log, updated docs, initial deployment research |
| Session 4 | PythonAnywhere ASGI deployment completed, key deliverables updated with live URL, PDFs regenerated, PPTX regenerated |

---

## Useful Commands

```bash
# Run tests locally
pytest -v

# Run the API locally
uvicorn app.main:app --reload

# Regenerate PDFs
manus-md-to-pdf docs/TECHNICAL_REPORT.md docs/TECHNICAL_REPORT.pdf
manus-md-to-pdf docs/API_DOCUMENTATION.md docs/API_DOCUMENTATION.pdf

# Regenerate PPTX
python3.11 scripts/create_pptx.py
```
