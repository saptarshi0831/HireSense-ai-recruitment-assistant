from pathlib import Path

from fastapi import APIRouter

from app.services.parsers.pdf_parser import extract_text
from app.services.parsers.resume_extractor import extract_resume_data

router = APIRouter()

UPLOAD_DIR = Path(
    "data/resumes"
)

@router.get("/extract/{filename}")

async def extract(filename: str):
    path = (
            UPLOAD_DIR /
            filename
            )
    
    if not path.exists():
        return {
            "error": "missing"
        }
    
    text = extract_text(str(path))

    data = extract_resume_data(text)

    return data