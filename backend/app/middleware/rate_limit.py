import time
from fastapi import Request, HTTPException, status
from starlette.middleware.base import BaseHTTPMiddleware

class RateLimitMiddleware(BaseHTTPMiddleware):
    """
    Simple in-memory rate limiting middleware.
    Limits requests per IP to X per window (sliding).
    """

    def __init__(self, app, max_requests: int = 100, window_seconds: int = 60):
        super().__init__(app)
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = {}  # {ip: [timestamps]}

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        now = time.time()
        window_start = now - self.window_seconds

        # Clean old requests
        timestamps = [ts for ts in self.requests.get(client_ip, []) if ts > window_start]
        timestamps.append(now)
        self.requests[client_ip] = timestamps

        if len(timestamps) > self.max_requests:
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Rate limit exceeded. Try again later."
            )

        response = await call_next(request)
        return response
