from functools import lru_cache
from typing import Annotated
from dataclasses import dataclass
from fastapi import FastAPI, File

from .config import get_settings
from .routers import audio


app = FastAPI()

app.include_router(
    audio.router
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == '__main__':
    import uvicorn
    settings = get_settings()
    uvicorn.run(app, host="0.0.0.0", port=settings.server.port)
