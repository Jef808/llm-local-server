from functools import lru_cache
from typing import Annotated
from dataclasses import dataclass
from fastapi import FastAPI, File

from .routers import audio


app = FastAPI()

app.include_router(
    audio.router
)


@app.get("/")
async def root():
    return {"message": "Hello World"}
