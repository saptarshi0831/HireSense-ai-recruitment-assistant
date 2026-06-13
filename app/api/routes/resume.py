from fastapi import APIRouter
from fastapi.responses import FileResponse
from pathlib import Path

router = APIRouter()

UPLOAD_DIR = Path("data/resumes")

@router.get("/resume/{filename}")
async def get_resume(filename: str):
    path = (
            UPLOAD_DIR /
            filename
        )
    
    if not path.exists():
        return {
            "error": "not found"
        }
    
    return FileResponse(path)