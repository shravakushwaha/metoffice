from functools import lru_cache
from pydantic import BaseSettings
from enum import Enum


class Profile(str, Enum):
    DEV = "dev"
    STAGING = "staging"
    PROD = "production"


class ProfileSetting(BaseSettings):
    profile: Profile

    def get_settings(self):
        return Settings(_env_file="app/environments/.env" + "." + self.profile.lower())

    class Config:
        # env_file = "../.env"
        env_file = "app/environments/.env"
        env_file_encoding = "utf-8"


class Settings(BaseSettings):
    APP_NAME: str
    DB_URL: str
    AUTH_URL: str
    SENDGRID_API_KEY: str

    class Config:
        case_sensitive = True
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings():
    profile = ProfileSetting()
    return profile.get_settings()
