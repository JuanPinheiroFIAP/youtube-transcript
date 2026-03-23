from fastapi import APIRouter
from pydantic import BaseModel
from src.youtube_transcript.service import transcript_youtube_video
from src.youtube_transcript.schemas import TranscriptRequest


youtube_router = APIRouter(prefix="/youtube", tags=["youtube"])

@youtube_router.post("/transcript")
def fazer_transcricao_video(req: TranscriptRequest):
    saved_path = transcript_youtube_video(req.link)
    return {"saved_file": saved_path}
