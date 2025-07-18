import os
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent
env_path = Path(os.getenv("ENV_FILE", BASE_DIR / ".env.local"))


class Settings(BaseSettings):
    db_name: str
    db_user: str
    db_password: str
    db_host: str = Field("localhost", env="DB_HOST")
    db_port: int = Field(5432, env="DB_PORT")

    model_config = SettingsConfigDict(
        env_file=env_path,
        env_prefix="DB_",
        case_sensitive=False,
        extra="ignore",
    )

    def __init__(self, **values):
        super().__init__(**values)
        # Если db_host из env равен "db" но мы НЕ в докере - меняем на localhost
        if self.db_host == "db" and not os.getenv("IN_DOCKER"):
            self.db_host = "localhost"


class SecretSettings(BaseSettings):
    django_secret_key: str = Field(..., alias="DJANGO_SECRET_KEY")

    model_config = SettingsConfigDict(
        env_file=env_path,
        case_sensitive=False,
        extra="ignore",
    )


settings = Settings()
secrets = SecretSettings()
