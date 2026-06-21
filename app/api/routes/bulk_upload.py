# endpoint that allows users to upload a ZIP file

from fastapi import ( UploadFile, File, APIRouter )
from pathlib import Path

from app.services.pipeline.bulk_ingest import ingest_zip

router = APIRouter()

TEMP = Path("data/temp")

TEMP.mkdir(exist_ok=True)

@router.post("/upload-resumes")
async def upload_zip(file: UploadFile = File(...)):
    path = TEMP / file.filename

    with open (path, "wb") as f:
        f.write(
            await file.read()
        )

    return ingest_zip(path)