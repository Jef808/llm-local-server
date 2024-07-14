import os
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class ServerSettings(BaseSettings):
    host_name: str = "localhost"
    port: int = 7500


class AudioSettings(BaseSettings):
    deepgram_api_key: str


class Settings(BaseSettings):
    app_name: str = "LLM-Server"
    server: ServerSettings = ServerSettings()
    audio: AudioSettings = AudioSettings(deepgram_api_key=os.environ["DEEPGRAM_API_KEY"])


@lru_cache()
def get_settings():
    return Settings()
