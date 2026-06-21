from pathlib import Path

from app.services.parsers.zip_parser import extract_zip
from app.services.pipeline.resume_pipeline import ingest_resume

UPLOAD_DIR = Path("data/resumes")


def ingest_zip(zip_path):

    files = extract_zip(zip_path)

    processed = []

    for file in files:
        path = UPLOAD_DIR / file

        ingest_resume(path, file)

        processed.append(file)

    Path(zip_path).unlink()

    return {
        "processed": len(processed),
        "files": processed
    }