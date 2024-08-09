from typing import ClassVar

from pydantic_settings import BaseSettings, SettingsConfigDict


class DbSettings(BaseSettings):
    USERNAME: str
    PASSWORD: str
    HOST: str
    PORT: int
    DATABASE: str

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql://{self.USERNAME}:" \
               f"{self.PASSWORD}@{self.HOST}:" \
               f"{self.PORT}/{self.DATABASE}"

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_nested_delimiter='__')
    db: DbSettings

settings = Settings()
