from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import IntegrityError
import logging

logger = logging.getLogger("app.middleware")

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """
    Handles Pydantic validation errors → returns 422 JSON.
    """
    logger.warning(f"Validation error at {request.url}: {exc.errors()}")
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": exc.errors()},
    )

async def integrity_error_handler(request: Request, exc: IntegrityError):
    """
    Handles DB unique constraint violations, etc.
    """
    logger.error(f"Integrity error at {request.url}: {exc.orig}")
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": "Database integrity error"},
    )
