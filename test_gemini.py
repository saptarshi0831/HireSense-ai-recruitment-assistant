from app.services.llm.extractor import (
    extract_candidate
)

sample = """

John Doe

Software Engineer

Email:
john@gmail.com

Skills:
Python
FastAPI
AWS
Docker

Experience:
3 years backend

Worked on inventory system.

"""

print(

extract_candidate(
sample
)

)