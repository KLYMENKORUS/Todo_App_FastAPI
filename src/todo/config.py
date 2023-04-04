import os

from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    app_name: str = os.getenv('NAME_APP')
    db_url = os.getenv('DATABASE_URL')

    class Config:
        env_file: str = '../.env'


settings = Settings()
