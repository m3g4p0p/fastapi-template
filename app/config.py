from typing import Optional

from pydantic import SecretStr
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

from .enums import Mode


class Settings(BaseSettings):

    deta_project_key: Optional[str] = None
    deta_space_app_version: Optional[str] = None
    secret_key: SecretStr = SecretStr('SECRET')
    mode: Mode = Mode.PRODUCTION

    model_config = SettingsConfigDict(
        env_file=['.env', '.env.dev', '.env.prod'],
        extra='ignore',
    )


settings = Settings()
