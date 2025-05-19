import secrets
import logging
from fastapi import APIRouter, Request, Depends
from fastapi.responses import JSONResponse
from starlette.responses import RedirectResponse
from authlib.integrations.base_client.errors import OAuthError

from app.adapters.google_oauth import get_google_provider
from app.adapters.jwt_service import create_access_token
from app.core.config import settings
from app.adapters.repository.user_repository import UserRepository
from app.interfaces.iuser_repository import IUserRepository
from app.domain.user import User
from app.adapters.auth_dependency import get_current_user

router = APIRouter()
logger = logging.getLogger(__name__)
user_repo: IUserRepository = UserRepository()


@router.get("/login/google")
async def login_via_google(request: Request):

    google = get_google_provider()

    redirect_uri = str(request.url_for("auth_callback"))
    # gerar um state só para registro no log (opcional):
    state = secrets.token_urlsafe(32)
    logger.info(f"🔐 State gerado: {state}")

    return await google.authorize_redirect(request, redirect_uri, state=state)


@router.get("/callback", name="auth_callback")
async def auth_callback(request: Request):

    google = get_google_provider()

    try:
        token = await google.authorize_access_token(request)
        logger.info(f"🔑 Token recebido: {token}")
    except OAuthError as e:
        logger.error(f"❌ Erro no OAuth: {e.error} - {e.description}")
        return JSONResponse(status_code=400, content={
            "error": e.error,
            "description": e.description,
        })

    try:
        user_info = await google.parse_id_token(request, token)
        logger.info("✅ Dados extraídos via id_token.")
    except Exception as e:
        logger.warning(f"⚠️ Falha no id_token ({e}) — buscando em userinfo.")
        resp = await google.get(
            "https://openidconnect.googleapis.com/v1/userinfo",
            token=token
        )
        user_info = resp.json()
        logger.info(f"✅ Dados extraídos do userinfo: {user_info}")

    user = User(
        email=user_info["email"],
        name=user_info["name"],
        picture=user_info.get("picture")
    )
    await user_repo.create_or_update(user)

    jwt_token = create_access_token({"sub": user.email, "name": user.name})

    redirect_url = f"{settings.FRONTEND_URL}/auth/callback?token={jwt_token}"
    logger.info(f"➡️ Redirecionando para o front: {redirect_url}")
    return RedirectResponse(url=redirect_url)


@router.get("/profile")
async def get_profile(current: dict = Depends(get_current_user)):
    return {"email": current["email"], "name": current["name"]}


@router.get("/users")
async def list_users():
    users = await user_repo.list_all()
    return [u.dict() for u in users]
