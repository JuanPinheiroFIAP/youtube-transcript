from fastapi import FastAPI
from src.youtube_transcript.api import youtube_router

app = FastAPI()

app.include_router(youtube_router)