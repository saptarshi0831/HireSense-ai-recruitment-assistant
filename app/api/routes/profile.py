from pathlib import Path

from fastapi import APIRouter

from app.services.parsers.pdf_parser import extract_text
from app.services.parsers.resume_extractor import extract_resume_data
from app.services.retrieval.candidate_store import save_candidate

router = APIRouter()

UPLOAD_DIR = Path("data/resumes")

@router.post("/profile/{filename}")
async def profile(filename: str):
    
    path = UPLOAD_DIR / filename

    text = extract_text(str(path))

    data = extract_resume_data(text)

    save_candidate(data)

    return data