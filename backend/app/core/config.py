from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    # App
    APP_NAME: str = "FavFlix"
    API_PREFIX: str = "/api/v1"
    APP_ENV: str = Field("development", env="APP_ENV")

    # Database
    DATABASE_URL: str = Field(..., env="DATABASE_URL")

    # JWT
    JWT_SECRET_KEY: str = Field(..., env="JWT_SECRET_KEY")
    JWT_ALGORITHM: str = Field("HS256", env="JWT_ALGORITHM")
    JWT_ACCESS_TOKEN_EXPIRES_MINUTES: int = Field(60, env="JWT_ACCESS_TOKEN_EXPIRES_MINUTES")

    # S3 / MinIO
    AWS_ACCESS_KEY_ID: str = Field(..., env="AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY: str = Field(..., env="AWS_SECRET_ACCESS_KEY")
    S3_BUCKET: str = Field(..., env="S3_BUCKET")
    S3_REGION: str = Field("us-east-1", env="S3_REGION")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
