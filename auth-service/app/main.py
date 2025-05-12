from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from app.api.v1.routes_auth import router as auth_router
from app.core.config import settings

app = FastAPI()
#CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://172.19.27.43:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(SessionMiddleware, secret_key=settings.SESSION_SECRET_KEY)
app.add_middleware(SessionMiddleware, secret_key=settings.JWT_SECRET_KEY)

@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(auth_router, prefix="/api/v1/auth")