from pathlib import Path
from fastapi import APIRouter

from app.services.parsers.pdf_parser import (
    extract_text
)

from app.services.embeddings.embedder import (
    create_embedding
)

router = APIRouter()

UPLOAD_DIR = Path("data/resumes")

@router.get(
    "/embed/{filename}"
)
async def embed_resumes(filename: str):
    path = (UPLOAD_DIR / filename)

    if not path.exists():
        return {"error": "File Not Found"}
    
    text = extract_text(str(path))

    vector = create_embedding(text)

    return {
        "filename" : filename,
        "dimestions": len(vector),
        "preview": vector[:10] 
    }