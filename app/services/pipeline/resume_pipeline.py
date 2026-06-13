from app.services.parsers.pdf_parser import extract_text
from app.services.embeddings.embedder import create_embedding
from app.services.retrieval.vector_store import store_resume

def ingest_resume(file_path, filename):

    text = extract_text(file_path)

    embedding = create_embedding(text)

    store_resume(filename, text, embedding)

    return {
        "stored": True
    }