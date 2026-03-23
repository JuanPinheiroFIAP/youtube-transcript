from youtube_transcript_api import YouTubeTranscriptApi
import re


def _normalize_transcript_data(transcript):
    if isinstance(transcript, dict) and "snippets" in transcript:
        transcript = transcript["snippets"]

    normalized = []
    for item in transcript:
        if isinstance(item, dict):
            text = item.get("text", "").strip()
        else:
            text = getattr(item, "text", "").strip()
        if text:
            normalized.append(text)

    return normalized

def save_transcript_to_txt(transcript, output_file):
    lines = _normalize_transcript_data(transcript)
    with open(output_file, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

    return output_file

def transcript_youtube_video(link):
    yyt_api = YouTubeTranscriptApi()

    try:
        video_id = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", link).group(1)
    except Exception:
        raise ValueError("Formato de link invalido")
    
    try:
        transcript = yyt_api.fetch(video_id, languages=["pt-BR", "en", "pt"])

        if transcript.is_generated:
            print("Transcrição gerada por IA → indo para Whisper")
            return None
        
        print("Transcrição encontrada")
        output_file = f"{video_id}.txt"

        save_transcript_to_txt(transcript, output_file)

        print(f"Transcrição baixada e salva em: {output_file}")

        return output_file

    except Exception as e:
        print("Sem transcrição disponível")
        print("Indo para Whisper...")
