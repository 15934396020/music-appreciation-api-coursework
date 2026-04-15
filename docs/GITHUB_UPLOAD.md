# GitHub Upload Guide

## Purpose

This document explains how to publish the current local repository to GitHub when account access is available. The repository is already initialized locally and has a clean working tree.

## Current Local Git State

| Item | Value |
|---|---|
| Branch | `main` |
| Latest local commit | `79a2f2e` |
| Commit message | `feat: build initial music appreciation api prototype` |

## Recommended Steps

After creating an empty GitHub repository, run the following commands from the project root:

```bash
git remote add origin <YOUR_GITHUB_REPOSITORY_URL>
git push -u origin main
```

If the remote already exists, update it with:

```bash
git remote set-url origin <YOUR_GITHUB_REPOSITORY_URL>
git push -u origin main
```

## Suggested Repository Name

A suitable repository name is:

```text
music-appreciation-api-coursework
```

## Suggested GitHub Repository Description

```text
A FastAPI coursework project for music appreciation and discovery, featuring track browsing, review CRUD, tags, collections, and analytics.
```

## What to Check Before Upload

| Check | Why it matters |
|---|---|
| `.gitignore` exists | Prevents local database and cache files from being uploaded |
| `pytest -q` passes | Confirms the current version is stable |
| `README.md` is present | Makes the repository understandable to markers and collaborators |
| `handover/` files are updated | Ensures multi-session collaboration remains smooth |

## After Upload

Once the code is on GitHub, the next session should:

1. add the GitHub repository URL to `handover/CURRENT_STATUS.md`;
2. optionally create releases or milestone tags;
3. begin drafting the technical report and presentation outline based on the implemented API.
