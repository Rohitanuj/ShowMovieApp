from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import IntegrityError

from app.core.config import settings
from app.core.logging import init_logging
from app.middleware.error_handlers import validation_exception_handler, integrity_error_handler
from app.middleware.rate_limit import RateLimitMiddleware

# Routers
from app.api.v1 import auth, entries, admin

# Initialize logging
logger = init_logging("DEBUG" if settings.APP_ENV == "development" else "INFO")

# FastAPI app
app = FastAPI(title=settings.APP_NAME)

# Middleware
app.add_middleware(RateLimitMiddleware, max_requests=100, window_seconds=60)

# Exception handlers
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(IntegrityError, integrity_error_handler)

# Routers
app.include_router(auth.router, prefix=settings.API_PREFIX)
app.include_router(entries.router, prefix=settings.API_PREFIX)
app.include_router(admin.router, prefix=settings.API_PREFIX)

@app.on_event("startup")
def on_startup():
    logger.info("🚀 Application startup complete")

@app.on_event("shutdown")
def on_shutdown():
    logger.info("🛑 Application shutdown complete")

@app.get("/")
def root():
    return {"message": f"Welcome to {settings.APP_NAME}"}
