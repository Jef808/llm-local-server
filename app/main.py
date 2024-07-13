from typing import Annotated
from dataclasses import dataclass
from fastapi import FastAPI, File


app = FastAPI()


@dataclass
class TranscriptionResult:
    timestamp: str
    model: str
    audio_duration: float
    confidence: float
    text: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/transcribe/",
          response_model=TranscriptionResult,
          tags=["audio"])
def transcribe(data: Annotated[bytes, File()]):
    """Transcribe audio data into text.

    The payload should be a WAV file.
    """
    response = request_transcription(data)

    return TranscriptionResult(
        timestamp=response.metadata.created,
        model=response.metadata.model_info[response.metadata.models[0]]['name'],
        audio_duration=response.metadata.duration,
        confidence=response.results.channels[0].alternatives[0].confidence,
        text=response.results.channels[0].alternatives[0].paragraphs.transcript,
    )
