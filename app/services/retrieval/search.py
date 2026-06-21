from app.services.retrieval.vector_store import collection
from app.services.embeddings.embedder import create_embedding


def extract_keywords(query):
    return [
        word.lower()
        for word in query.split()
        if len(word) > 2
    ]


def search_resumes(query: str, n_results: int = 20):
    query_embedding = create_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results,
        include=["documents", "metadatas"],
    )

    keywords = extract_keywords(query)

    filtered_docs = []
    filtered_ids = []

    for doc, file_id, meta in zip(
        results["documents"][0],
        results["ids"][0],
        results["metadatas"][0],
    ):
        searchable = " ".join(
            str(v)
            for v in meta.values()
            if v
        ).lower()

        if any(keyword in searchable for keyword in keywords):
            filtered_docs.append(doc)
            filtered_ids.append(file_id)

    # Fallback to semantic search results
    if not filtered_docs:
        return {
            "documents": results["documents"],
            "ids": results["ids"],
        }

    return {
        "documents": [filtered_docs],
        "ids": [filtered_ids],
    }