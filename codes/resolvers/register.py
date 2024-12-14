""" Registration API Endpoints
"""

import os
from pydantic import BaseModel
from pymongo import MongoClient
from fastapi import APIRouter, Depends, Request


def get_db():
    client = MongoClient(os.getenv("CONNECTION"))
    db = client[os.getenv("DATABASE")]
    return db


class AuthRes(BaseModel):
    authenticate: bool


router = APIRouter()


@router.post("/authenticate", response_model=AuthRes)
def authenticate(req: Request, db: MongoClient = Depends(get_db)) -> AuthRes:
    collection = db["mycollection"]
    result = collection.find_one({"username": req.body.username})
    if result:
        return {"authenticated": True}
    return {"authenticated": False}
