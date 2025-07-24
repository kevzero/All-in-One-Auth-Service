from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.auth.routes import auth_router
from app.admin.routes import admin_router

app = FastAPI(title='All-in-One Auth Service')

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth_router, prefix='/auth', tags=['Authentication'])
app.include_router(admin_router, prefix='/admin', tags=['Admin'])

@app.get('/')
async def root():
    return {"message": "Auth Service Running"}
