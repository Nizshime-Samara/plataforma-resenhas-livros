import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    SESSION_SECRET_KEY = os.getenv("SESSION_SECRET_KEY", "default-insecure-key")
    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
    FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:3000")
    MONGO_URI = os.getenv("MONGO_URI")
    UPSTASH_REDIS_REST_URL = os.getenv("UPSTASH_REDIS_REST_URL")
    UPSTASH_REDIS_REST_TOKEN = os.getenv("UPSTASH_REDIS_REST_TOKEN")
     

settings = Settings()
