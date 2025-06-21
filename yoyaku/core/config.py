import os

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

class Settings(BaseSettings):
    db_name: str
    db_user: str
    db_password: str
    db_host: str = "localhost"
    db_port: int = 5432

    model_config = SettingsConfigDict(
        env_file=os.path.join(BASE_DIR, ".env")
    )

settings = Settings()
