# Generative AI Conversation Log

**Project:** Music Appreciation and Discovery API  
**Module:** XJCO3011 - Web Services and Web Data  
**AI Tool Used:** Manus AI (LLM-based autonomous agent)

---

## Overview

This document provides a summary of the key interactions with Generative AI throughout the development of this coursework project. In accordance with the module's GREEN GenAI policy, all AI usage is declared here with purposes, outcomes, and representative examples.

The project was developed across multiple AI sessions using a structured handover protocol. Each session's work was recorded in `handover/SESSION_LOG.md` and the AI was given full context of previous sessions through handover documents.

---

## Session 1: Project Initialisation and Core Implementation

**Date:** 2026-04-15  
**Duration:** Full session  
**AI Tool:** Manus AI

### Conversation Summary

**User Request:** "Create a coursework project for XJCO3011 — a Music Appreciation and Discovery API."

**AI Actions:**
1. Analysed the coursework brief to understand requirements and marking criteria.
2. Proposed FastAPI + SQLAlchemy + SQLite as the technology stack, justifying each choice.
3. Designed the six-entity data model (Genre, Track, Review, UserTag, Collection, CollectionItem).
4. Generated seed data with 29 curated music tracks across 8 genres.
5. Implemented all core endpoints (CRUD for reviews, browsing for tracks/genres, tag management, collection management).
6. Created the initial test suite with smoke tests.
7. Established the multi-account handover protocol.

**Key Design Decision Explored with AI:**
> "Should we use Flask or FastAPI for this project?"  
> AI recommended FastAPI for its automatic OpenAPI documentation, type validation via Pydantic, and modern async support. Flask was considered but rejected because it would require additional libraries (Flask-RESTful, Marshmallow) to achieve the same functionality.

**Outcome:** Working API prototype with 25 endpoints, seed data, and basic tests.

---

## Session 2: Documentation, Testing, and Deliverables

**Date:** 2026-04-15  
**Duration:** Full session  
**AI Tool:** Manus AI

### Conversation Summary

**User Request:** "Continue from the handover documents. Complete tests, documentation, and presentation materials."

**AI Actions:**
1. Expanded the test suite from 4 smoke tests to 48 comprehensive tests across 8 test classes.
2. Migrated `main.py` from deprecated `on_event("startup")` to modern `lifespan` context manager.
3. Created `TECHNICAL_REPORT.tex` with professional LaTeX formatting (coloured section headers, framed GenAI declaration box).
4. Created `API_DOCUMENTATION.tex` with HTTP method colour-coded labels and table of contents.
5. Compiled both LaTeX documents to PDF.
6. Generated 10 HTML presentation slides covering all coursework deliverables.
7. Pushed all code and documentation to the GitHub repository.
8. Updated all handover documents for the next session.

**Key Refactoring Explored with AI:**
> "The startup event pattern `@app.on_event('startup')` is deprecated in newer FastAPI versions. How should we handle this?"  
> AI implemented the `@asynccontextmanager` lifespan pattern, which is the recommended modern approach. This also required updating the test fixture to use `with TestClient(app) as c:` to properly trigger the lifespan.

**Outcome:** Complete submission materials (report PDF, API docs PDF, slides), 48 passing tests, GitHub repository fully synchronised.

---

## Session 3: Authentication, Error Handling, and Final Polish

**Date:** 2026-04-17  
**Duration:** Full session  
**AI Tool:** Manus AI

### Conversation Summary

**User Request:** "Continue from NEXT_ACTIONS.md. Don't redo completed work."

**AI Actions:**
1. Analysed the coursework marking rubric to identify gaps (authentication required for 50+ band).
2. Implemented API key authentication module (`app/auth.py`) using FastAPI's dependency injection.
3. Created structured error handling module (`app/errors.py`) for consistent JSON error responses.
4. Added authentication to all write operations while keeping read operations public.
5. Expanded test suite to 55 tests across 9 classes (added `TestAuthentication` class).
6. Updated technical report to reflect authentication and error handling additions.
7. Created this GenAI conversation log.
8. Created PPTX presentation from existing HTML slide content.
9. Updated all documentation (README, API docs, handover files).
10. Pushed all changes to GitHub.

**Key Architecture Decision Explored with AI:**
> "The marking rubric requires 'Basic authentication present' for the 50-59 band and 'Well-documented API with authentication' for 60-69. Should we add OAuth2 or a simpler scheme?"  
> AI recommended API key authentication via the `X-API-Key` header as the optimal balance between meeting the rubric requirement and maintaining simplicity. OAuth2/JWT was considered but deemed over-engineered for a coursework prototype where the primary goal is demonstrating understanding of authentication concepts.

**Error Handling Design:**
> "How should we standardise error responses across the API?"  
> AI designed a structured error response format with `error` (machine-readable code), `message` (human-readable description), and `details` (validation-specific field errors). This was implemented via custom FastAPI exception handlers that intercept both HTTP exceptions and Pydantic validation errors.

**Outcome:** Authentication system, structured error handling, 55 passing tests, updated documentation, PPTX presentation.

---

## Summary of GenAI Usage Across All Sessions

| Session | Primary AI Usage | Outcome |
|---|---|---|
| 1 | Architecture design, code generation, data modelling | Working API prototype |
| 2 | Test expansion, LaTeX documentation, presentation creation | Complete submission materials |
| 3 | Authentication design, error handling, rubric analysis | Production-quality API |

## AI Usage Categories

| Category | Examples |
|---|---|
| **Code Generation** | FastAPI endpoints, SQLAlchemy models, Pydantic schemas, authentication module |
| **Refactoring** | Lifespan migration, structured error handling |
| **Testing** | Test suite design, edge case identification, fixture configuration |
| **Documentation** | Technical report, API documentation, presentation slides, this conversation log |
| **Design Decisions** | Stack selection, authentication approach, error response format, scope control |
| **Project Management** | Handover protocol, session logging, priority analysis |

## Declaration

All code generated by AI was reviewed, tested, and refined before inclusion in the project. The AI served as a productivity tool and design partner, while all final decisions on architecture, scope, and implementation were made with the coursework requirements and marking criteria in mind.
