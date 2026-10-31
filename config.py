#конфиг настроек 
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Game Stats Tracker API"
    database_url: str = "gamestats.db"

# указываем Pydantic, откуда брать файл с переменными окружения
model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
    