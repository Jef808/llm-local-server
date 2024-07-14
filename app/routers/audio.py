from typing import Annotated
from functools import lru_cache
from dataclasses import dataclass
from fastapi import APIRouter, Depends, File
from ..internal import transcribe
from ..config import get_settings, Settings


router = APIRouter(
    tags=["audio"],
    prefix="/audio"
)


@dataclass
class TranscriptionResponse:
    timestamp: str
    model: str
    audio_duration: float
    confidence: float
    text: str


@router.post("/transcribe/", response_model=TranscriptionResponse)
def handle_transcribe(data: Annotated[bytes, File()], settings: Annotated[Settings, Depends(get_settings)]):
    """Transcribe audio data into text.

    The payload should be a WAV file.
    """
    api_key = settings.audio.deepgram_api_key
    response = transcribe.deepgram(data, api_key=api_key)

    return TranscriptionResponse(
        timestamp=response.metadata.created,
        model=response.metadata.model_info[response.metadata.models[0]]['name'],
        audio_duration=response.metadata.duration,
        confidence=response.results.channels[0].alternatives[0].confidence,
        text=response.results.channels[0].alternatives[0].paragraphs.transcript,
    )
