from pathlib import Path
from fastapi import APIRouter
from app.services.parsers.pdf_parser import (
    extract_text
)

router = APIRouter()

UPLOAD_DIR = Path(
    "data/resumes"
)

@router.get(
    "/parse/{filename}"
)
async def parse_resume(filename: str):
    path = (
        UPLOAD_DIR /
        filename
    )

    if not path.exists():
        return {
            "error": "File Not Found"
        }
    
    text = extract_text(str(path))

    return {
        "filename": filename,
        "preview": text[:2000]
    }