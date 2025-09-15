from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    APP_NAME: str = "FavFlix"
    API_PREFIX: str = "/api/v1"
    APP_ENV: str = Field("development", env="APP_ENV")

    # Database
    DATABASE_URL: str = Field(..., env="DATABASE_URL")

    # JWT
    JWT_SECRET_KEY: str = Field(..., env="JWT_SECRET_KEY")
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRES_MINUTES: int = 60

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
