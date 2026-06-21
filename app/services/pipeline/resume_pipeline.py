from app.services.parsers.pdf_parser import extract_text
from app.services.parsers.resume_extractor import extract_resume_data
from app.services.embeddings.embedder import create_embedding
from app.services.retrieval.vector_store import store_resume


def ingest_resume(file_path, filename):
    text = extract_text(file_path)

    data = extract_resume_data(text)

    section_embeddings = {
        "skills": create_embedding(
            " ".join(data.get("skills", []))
        ),
        "projects": create_embedding(
            data.get("projects", "")
        ),
        "experience": create_embedding(
            data.get("experience", "")
        ),
        "summary": create_embedding(
            data.get("summary", "")
        ),
    }

    store_resume(
        filename,
        data,
        section_embeddings,
    )

    return {"stored": True}