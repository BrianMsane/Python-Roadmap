""" Main script for FastAPI application
"""

from fastapi import FastAPI
from codes.fastapi_tutorial.rate_limiting import AdvancedMiddleware
from resolvers import register

app = FastAPI()
app.add_middleware(AdvancedMiddleware)
app.include_router(register.router, prefix="/api/")
