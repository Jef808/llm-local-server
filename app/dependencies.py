from functools import lru_cache
from deepgram import DeepgramClient
from .config import Settings


@lru_cache
def get_settings():
    return Settings()
