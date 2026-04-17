# Deployment Research Notes (2026-04-17)

## Repository baseline confirmed

- GitHub repository: `https://github.com/15934396020/music-appreciation-api-coursework`
- Local working copy path: `/home/ubuntu/music-appreciation-api-coursework-work`
- Handover files confirm that **external deployment is the only critical remaining task**.
- Local verification completed: `55 passed` in pytest.

## Render deployment findings

Source consulted: Render official FastAPI deployment guide (`https://render.com/docs/deploy-fastapi`).

Confirmed deployment settings:

| Setting | Value |
|---|---|
| Service type | Web Service |
| Language/runtime | Python 3 |
| Build command | `pip install -r requirements.txt` |
| Start command | `uvicorn app.main:app --host 0.0.0.0 --port $PORT` |
| Result | Service receives a public `onrender.com` URL after successful deploy |

## Working assumption

Preferred platform remains **Render.com** because it natively supports FastAPI/ASGI and avoids PythonAnywhere's ASGI beta complexity.

## PythonAnywhere deployment path selected

- User explicitly confirmed that I may use the provided PythonAnywhere account to complete deployment.
- Login page is reachable at `https://www.pythonanywhere.com/login/`.
- Visible login fields confirmed:
  - Username input
  - Password input
  - Log in button

Next step: sign in, generate API token if needed, and complete ASGI deployment using the existing `weidademiaoxiao.pythonanywhere.com` domain.

## PythonAnywhere account access confirmed

PythonAnywhere login succeeded for account `weidademiaoxiao`. The dashboard is available and shows an existing web app entry for `weidademiaoxiao.pythonanywhere.com`. This confirms that the provided credentials are valid and that deployment can proceed inside the account.

## PythonAnywhere API token status

The account settings page confirms that no PythonAnywhere API token currently exists for `weidademiaoxiao`. The API Token section provides a visible **Create a new API token** button, so the next required step is to generate a token before using the command-line deployment flow described in the official ASGI documentation.

## PythonAnywhere API token created

A new PythonAnywhere API token was successfully generated for the `weidademiaoxiao` account on 2026-04-17. This unblocks command-line/API-based ASGI deployment. The token value is intentionally not stored in repository files for security reasons, but it is available in the active browser session and can be used immediately for deployment work.

## Token extraction correction

A DOM inspection of the API token page showed that the first value previously captured from the page was actually a CSRF token, not the PythonAnywhere API token. The real API token is rendered in a separate visible text block on the page. This explains the earlier 401 authentication failure when calling the PythonAnywhere API from the local sandbox.

## Switch to in-browser console approach

After the local API upload path proved unreliable, I switched to the PythonAnywhere browser UI to use a Bash console directly for deployment. The Consoles page loaded successfully and displayed a **Bash** launch entry, but the first direct click attempt on that entry failed due to a transient element-location error. The next step is to refresh or re-read the page state and retry launching the Bash console.

## PythonAnywhere Bash console opened

The second attempt to launch a Bash console from the PythonAnywhere Consoles page succeeded. A live browser-based Bash console is now open, which should allow direct execution of the remote setup steps that were difficult to complete reliably via the external file API.

## Remote project directory existence confirmed

Inside the PythonAnywhere Bash console, attempting `git clone` returned `fatal: destination path 'music-appreciation-api-coursework' already exists and is not an empty directory.` This strongly suggests that the remote project directory was in fact created by the earlier upload attempt, even though the external API verification was inconsistent.

## Remote directory content check

A direct listing inside the PythonAnywhere Bash console showed that `~/music-appreciation-api-coursework` currently contains only a `.git` directory and not the full checked-out project files. The remote repository metadata exists, but the working tree still needs to be materialised or recloned before the app can be run.

## Fresh reclone initiated on PythonAnywhere

The incomplete remote directory was removed in the Bash console, and a fresh `git clone` from the public GitHub repository was started successfully. The console showed normal GitHub clone progress (`Enumerating objects`, `Counting objects`, `Compressing objects`, `Receiving objects`), indicating that direct cloning from GitHub works from the PythonAnywhere account.

## Default web app deleted from browser UI

The classic default web app at `weidademiaoxiao.pythonanywhere.com` was successfully deleted through the PythonAnywhere Web page and the UI now shows **You have no web apps** with only the **Add a new web app** entry remaining. This confirms that the default domain has been fully released from the classic WSGI setup.

## Browser state after web app deletion

The classic PythonAnywhere Web page now shows **You have no web apps**, confirming the deletion persisted in the browser UI. After that, the existing Bash console at `consoles/46356358/` was reopened successfully and is still available for further remote command execution if needed.

## PythonAnywhere deployment blocker confirmed

After the ASGI site itself had been created successfully, the application still returned `502` responses. The decisive blocker was not the domain binding or ASGI configuration any more, but the remote environment's inability to fetch packages from PyPI. The deployment logs showed `Network is unreachable` while trying to install runtime dependencies such as `fastapi==0.115.12`.

This meant that simply reloading the site or retrying a normal online install would not solve the issue reliably in the free environment.

## Working deployment workaround

A viable workaround was implemented by shifting dependency preparation to the local workspace and then uploading deployment assets for PythonAnywhere.

| Asset | Purpose |
|---|---|
| `requirements-deploy.txt` | Minimal runtime dependency list for deployment |
| `scripts/pythonanywhere_start.sh` | PythonAnywhere-specific startup script |
| `wheelhouse/` | Offline dependency assets prepared locally |

The startup flow was adjusted so that the PythonAnywhere app could rely on the uploaded deployment resources rather than a fresh remote package download during startup.

## Successful live outcome

The final external deployment target is now live at:

- `https://weidademiaoxiao.pythonanywhere.com`

Verified supporting endpoints:

- `https://weidademiaoxiao.pythonanywhere.com/health`
- `https://weidademiaoxiao.pythonanywhere.com/docs`
- `https://weidademiaoxiao.pythonanywhere.com/redoc`

This confirms that the project now satisfies the coursework requirement for external hosting on a publicly accessible web server.

## Follow-up actions completed locally after deployment

After the live URL was confirmed, the following repository deliverables were updated locally to reflect the deployed address:

| File | Update |
|---|---|
| `README.md` | Added live deployment links |
| `docs/TECHNICAL_REPORT.md` | Added deployment URL |
| `docs/TECHNICAL_REPORT.pdf` | Regenerated |
| `docs/API_DOCUMENTATION.md` | Updated base URL |
| `docs/API_DOCUMENTATION.pdf` | Regenerated |
| `scripts/create_pptx.py` | Updated deployment messaging |
| `docs/PRESENTATION.pptx` | Regenerated |

## Remaining operational note

At this stage the technical deployment work is complete. If anything still remains unfinished, it is repository sync (commit/push), final user-facing submission support, and oral-exam preparation — not redeployment.
