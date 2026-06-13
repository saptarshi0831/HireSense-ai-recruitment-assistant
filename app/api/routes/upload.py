from pathlib import Path

from fastapi import APIRouter
from fastapi import File
from fastapi import UploadFile

router = APIRouter()

UPLOAD_DIR = Path("data/resumes")

UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True
)

@router.post("/upload-resume")
async def upload_resume(
    file: UploadFile = File(...)
):
    file_path = (
        UPLOAD_DIR /
        file.filename
    )

    content = await file.read()

    with open(
        file_path,
        "wb"
    ) as f:
        f.write(content)

    return {
        "filename": file.filename,
        "status": "uploaded"
    }