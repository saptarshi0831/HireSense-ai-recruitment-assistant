import chromadb

client = chromadb.PersistentClient(
    path="data/chroma_db"
)

collection = client.get_or_create_collection(
    name="resumes"
)


def store_resume(filename, data, section_embeddings):
    combined_embedding = section_embeddings["summary"]

    collection.add(
        ids=[filename],
        documents=[data["full_text"]],
        embeddings=[combined_embedding],
        metadatas=[{
            "name": data.get("name") or "",
            "skills": ", ".join(data.get("skills", [])),
            "projects": data.get("projects", "")[:500],
            "experience": data.get("experience", "")[:500],
            "education": data.get("education", "")[:300],
            "summary": data.get("summary", "")[:300],
        }]
    )

    return True