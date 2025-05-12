from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from app.api.v1.routes_auth import router as auth_router
from app.core.config import settings

app = FastAPI()

#CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://172.19.27.43:3000", settings.FRONTEND_URL, "https://nizshime-samara.github.io"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#controle de cookie state do OAuth
app.add_middleware(
    SessionMiddleware, 
    secret_key=settings.SESSION_SECRET_KEY, 
    same_site="none",         
    https_only=False   
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(auth_router, prefix="/api/v1/auth")