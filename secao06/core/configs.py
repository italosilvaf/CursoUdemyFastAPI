from typing import List
from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://postgres:root@localhost:5432/db_cursofastapi'
    DBBaseModel = declarative_base()

    JWT_SECRET: str = 'cRcg132OnHyMVi0RqKgyjn3xZYH-5nZLyv5YJpPG6a0'
    """
    import secrets

    token: str = secrets.token_urlsafe(32)
    """
    ALGORITHM: str = 'HS256'
    # 60 minutos * 24 horas * 7 dias => 1 semana
    ACCESS_TOKEN_EXPIRE_MINURES = 60 * 24 * 7

    class Config:
        case_sensitive = True


settings: Settings = Settings()
