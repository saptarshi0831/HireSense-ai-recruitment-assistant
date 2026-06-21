from app.services.parsers.pdf_parser import (
    extract_text
)

from app.services.parsers.resume_extractor import (
    extract_resume_data
)


text = extract_text(
    "data/resumes/ResumeFull.pdf"
)

data = extract_resume_data(
    text
)

print(data)