''' Registration API Endpoints
'''


from pymongo import MongoClient
from fastapi import APIRouter, Depends, Request

def get_db():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["database_name"]
    return db


router = APIRouter()

@router.post("/authenticate")
def authenticate(req: Request, db: MongoClient = Depends(get_db)):
    collection = db['mycollection']
    result = collection.find_one({"username": req.body.usename})
    if result:
        return {True}
    return {False}
