from app.services.retrieval.vector_store import (
    collection
)

from app.services.embeddings.embedder import create_embedding

def search_resumes(
        query: str,
        n_results: int = 3
):
    query_embedding = create_embedding(query)
    
    results= collection.query(
        query_embeddings=[query_embedding],
        n_results= n_results
    )

    return results