import httpx
from deepgram.utils import verboselogs
from deepgram import DeepgramClientOptions

from deepgram import (
    DeepgramClient,
    DeepgramClientOptions,
    StreamSource,
    PrerecordedOptions,
    PrerecordedResponse,
)

RATE = 48000
CHUNK_RECORDING = 1024
CHANNELS = 1
FORMAT = "linear16"

# For boosting certain words
KEYWORDS = [
    "python:2",
    "emacs:1",
    "script:1",
]
# For searching for certain phrases or words
SEARCHES = [
    "python script",
    "emacs snippet",
    "bash script",
    "shell script",
]
FIND_REPLACE = {
    "ELLM": "ellm"
}
CUSTOM_INTENTS = [
    "Generate code",
    "Refactor code",
    "Review code",
    "Get advice about code"
]
ENTITIES_TRACKED = [
    "EMAIL",
    "URL"
]

OPTIONS = PrerecordedOptions(
    model="nova-2-conversationalai",
    #detect_language=True,
    language="en",
    smart_format=True,
    keywords=KEYWORDS,
    replace=[f"{k}:{v}" for k, v in FIND_REPLACE.items()],
    # intents=True,
    # custom_intent=CUSTOM_INTENTS,
    # detect_entities=True
)


def deepgram(audio_data: bytes, *, api_key: str) -> PrerecordedResponse:
    deepgram = DeepgramClient()

    payload: StreamSource = {
        "stream": audio_data
    }
    response = deepgram.listen.prerecorded.v("1").transcribe_file(
        payload, OPTIONS, timeout=httpx.Timeout(300.0, connect=10.0)
    )
    return response
