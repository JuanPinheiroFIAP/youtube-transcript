from pydantic import BaseModel

class TranscriptRequest(BaseModel):
    link: str
