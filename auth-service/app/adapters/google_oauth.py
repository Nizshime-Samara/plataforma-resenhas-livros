from authlib.integrations.starlette_client import OAuth
from app.core.config import settings

oauth = OAuth()

userinfo_endpoint = "https://openidconnect.googleapis.com/v1/userinfo"

oauth.register(
    name="google",
    client_id=settings.GOOGLE_CLIENT_ID,
    client_secret=settings.GOOGLE_CLIENT_SECRET,
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile", "response_type": "code id_token", "response_mode": "query",},
    
    
    userinfo_endpoint=userinfo_endpoint  # <- se seu client suportar
)

def get_google_provider():
    return oauth.create_client('google') 
