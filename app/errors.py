"""Structured error handling for the Music Appreciation and Discovery API.

Provides custom exception handlers that return consistent JSON error
responses with ``error``, ``message``, and ``detail`` fields.  This
improves the developer experience by making error payloads predictable
across all endpoints.
"""

from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException


def register_error_handlers(app: FastAPI) -> None:
    """Attach custom exception handlers to the FastAPI application."""

    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(
        request: Request, exc: StarletteHTTPException
    ) -> JSONResponse:
        """Return a structured JSON body for all HTTP exceptions."""
        # If the detail is already a dict (e.g. from auth module), use it.
        if isinstance(exc.detail, dict):
            body = exc.detail
        else:
            body = {
                "error": _status_to_error_code(exc.status_code),
                "message": str(exc.detail),
            }
        return JSONResponse(status_code=exc.status_code, content=body)

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request, exc: RequestValidationError
    ) -> JSONResponse:
        """Return a structured JSON body for Pydantic validation errors."""
        errors = []
        for err in exc.errors():
            errors.append(
                {
                    "field": " -> ".join(str(loc) for loc in err["loc"]),
                    "message": err["msg"],
                    "type": err["type"],
                }
            )
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={
                "error": "validation_error",
                "message": "Request validation failed. Check the 'details' field for specifics.",
                "details": errors,
            },
        )


def _status_to_error_code(status_code: int) -> str:
    """Map an HTTP status code to a short snake_case error identifier."""
    mapping = {
        400: "bad_request",
        401: "authentication_required",
        403: "forbidden",
        404: "not_found",
        405: "method_not_allowed",
        409: "conflict",
        422: "validation_error",
        429: "rate_limit_exceeded",
        500: "internal_server_error",
    }
    return mapping.get(status_code, f"http_{status_code}")
