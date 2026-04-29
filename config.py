from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str

    REDIS_HOST: str
    REDIS_PORT: int

    CLOUDINARY_NAME: str
    CLOUDINARY_API_KEY: str
    CLOUDINARY_API_SECRET: str

    EMAIL_USER: str
    EMAIL_PASSWORD: str

    class Config:
        env_file = ".env"

settings = Settings()
