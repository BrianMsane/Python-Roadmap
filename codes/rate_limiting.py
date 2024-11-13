''' Rate limiting using the middleware and also using the slowapi module
'''


from fastapi import Response
from starlette.middleware.base import BaseHTTPMiddleware
import time
from typing import Dict
from collections import defaultdict


class AdvancedMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app=app)
        self.rate_limit_records: Dict[str, float] = defaultdict(float)

    async def log_message(self, message):
        print(message)

    async def dispatch(self, request, call_next):
        client_ip = request.client.host
        current_time = time.time()
        if current_time - self.rate_limit_records[client_ip] < 1: # 1 request per second limit
            return Response(content='Rate limit exceeded', status_code=429)
        self.rate_limit_records[client_ip] = current_time
        path = request.url.path
        await self.log_message('Request to: {url}'.format(url=path))

        # process the request
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time

        # add custom header
        custom_header = {'X-Process-Time': str(process_time)}
        for header, value in custom_header.items():
            response.headers.append(header, value)
        return response
