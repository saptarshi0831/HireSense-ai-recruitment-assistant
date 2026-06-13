from sentence_transformers import ( SentenceTransformer )

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_embedding(text: str):
    # embedding-vector dimension 384
    embedding = model.encode(text)

    return embedding.tolist()