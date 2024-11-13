''' Main script for FastAPI application
'''

from fastapi import FastAPI
from rate_limiting import AdvancedMiddleware


app = FastAPI()
app.add_middleware(AdvancedMiddleware)
