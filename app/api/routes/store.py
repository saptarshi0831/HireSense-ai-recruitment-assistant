from pathlib import Path

from fastapi import APIRouter

from app.services.parsers.pdf_parser import extract_text

from app.services.embeddings.embedder import create_embedding

from app.services.retrieval.vector_store import store_resume

router = APIRouter()

UPLOAD_DIR= Path(
    "data/resumes"
)

@router.post("/store/{filename}")

async def store(filename: str):
    path= (
        UPLOAD_DIR /
        filename
    )

    text= extract_text(str(path))

    embedding= create_embedding(text)

    store_resume(
        filename,
        text,
        embedding
    )

    return {
        "stored": filename
    }