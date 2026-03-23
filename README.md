# Youtube Transcript

Projeto FastAPI para baixar e salvar transcrição de vídeo YouTube em arquivo `.txt`.

- link de entrada (URL YouTube)
- captura transcrição (`youtube-transcript-api`)
- normaliza (suporta `FetchedTranscript(...)` + lista de dics `{ text, start, duration }`)
- salva `VIDEO_ID.txt`
- endpoint: `POST /youtube/transcript`

---

## 🧩 Requisitos

- Python 3.12, 3.13 ou 3.14 (`>=3.12,<3.15`)
- Poetry 1.7+ (ou compatível)

---

## ⚙️ Instalação (Poetry)

```bash
# dentro do diretório do projeto
cd c:\programação\youtube-transcript

# instalar dependências (pode criar virtualenv própria)
poetry install
```

Se não tiver o `poetry`:

```bash
pip install poetry
```

---

## ▶️ Executar

```bash
poetry run uvicorn src.youtube_transcript.main:app --reload --host 0.0.0.0 --port 8000
```

A API ficará disponível em:

- `http://127.0.0.1:8000`
- docs automáticos: `http://127.0.0.1:8000/docs`

---

## 🛠️ Como usar

### Endpoint

`POST /youtube/transcript`

Corpo JSON:

```json
{
  "link": "https://www.youtube.com/watch?v=12345ABCDEf"
}
```

Resposta esperada:

```json
{
  "saved_file": "12345ABCDEf.txt"
}
```

---

## 🔧 Estrutura atual

- pyproject.toml – dependencies + settings
- main.py – FastAPI app
- youtube.py – router + endpoint
- youtube_schema.py – schema Pydantic
- trascript_youtube.py – lógica de transcrição: `YouTubeTranscriptApi`, normalize + save TXT

---

## 🧾 Lógica de transcrição

Função principal:
- `transcript_youtube_video(link)`
- extrai `video_id` via regex
- chama `YouTubeTranscriptApi.fetch(video_id, languages=["pt-BR","en","pt"])`
- se `is_generated=True` devolve `None` (com hook para Whisper no futuro)
- salva transcrição em `VIDEO_ID.txt` via `save_transcript_to_txt(...)`

Normalização:
- aceita:
  - objeto com `snippets` (formato antigo, `FetchedTranscript`)
  - lista de dics (novo formato)
- extrai apenas `text` não-vazios

---