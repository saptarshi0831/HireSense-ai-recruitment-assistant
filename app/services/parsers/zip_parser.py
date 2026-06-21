# zip upload feature

import zipfile

from pathlib import Path

UPLOAD_DIR = Path("data/resumes")

def extract_zip(zip_path):
    extracted = []

    with zipfile.ZipFile(zip_path, "r") as z:
        z.extractall(UPLOAD_DIR)

        for file in z.namelist():
            if file.endswith(".pdf"):
                extracted.append(file)

    return extracted