from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.auth.jwt_handler import create_access_token, create_refresh_token
from app.auth.oauth import google_login, github_login

router = APIRouter()

class UserLogin(BaseModel):
    username: str
    password: str

fake_users = {"admin": {"password": "admin123", "role": "admin"}}

@router.post('/login')
async def login(user: UserLogin):
    if user.username in fake_users and fake_users[user.username]['password'] == user.password:
        return {
            "access_token": create_access_token({"sub": user.username, "role": fake_users[user.username]['role']}),
            "refresh_token": create_refresh_token({"sub": user.username})
        }
    raise HTTPException(status_code=401, detail='Invalid credentials')

@router.get('/oauth/google')
async def oauth_google():
    return google_login()

@router.get('/oauth/github')
async def oauth_github():
    return github_login()
