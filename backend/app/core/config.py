from pydantic import BaseSettings, AnyHttpUrl
from typing import List


class Settings(BaseSettings):
    PROJECT_NAME: str = "IA Site"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "change-me"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    ALGORITHM: str = "HS256"
    DATABASE_URL: str = "sqlite:///./app.db"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    FRONTEND_URL: str = "http://localhost:5173"
    RATE_LIMIT_LOGIN: str = "5/minute"
    UPLOAD_DIR: str = "./uploads"
    AI_PROVIDER: str = "local"
    AI_MODEL: str = "gpt-4o-mini"
    OPENAI_API_KEY: str = ""
    GENERATED_DIR: str = "./generated"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
