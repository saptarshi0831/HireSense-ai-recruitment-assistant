import chromadb

client = chromadb.PersistentClient(
    path= "data/chroma_db"
)

collection= client.get_or_create_collection(
    name= "resumes"
)

def store_resume(filename: str, text: str, embedding: list):
    collection.add(
        documents=[text],
        embeddings=[embedding],
        ids=[filename]
    )

    return True