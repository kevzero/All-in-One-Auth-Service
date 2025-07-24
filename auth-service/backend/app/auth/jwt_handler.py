import jwt, datetime
from fastapi import HTTPException

SECRET_KEY = 'SECRET'
ALGORITHM = 'HS256'

def create_access_token(data: dict):
    payload = data.copy()
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def create_refresh_token(data: dict):
    payload = data.copy()
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(days=7)
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
