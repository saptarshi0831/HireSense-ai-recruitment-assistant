import re
from sentence_transformers import SentenceTransformer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

model = SentenceTransformer("all-MiniLM-L6-v2")

try:
    STOPWORDS = set(stopwords.words("english"))
except:
    STOPWORDS = set()

lemmatizer = WordNetLemmatizer()

def clean_text(text: str):
    text = text.lower()
    text = re.sub(r"[^a-z0-9 ]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def create_embedding(text: str):
    text = clean_text(text)

    if not text:
        return [0.0] * model.get_embedding_dimension()

    embedding = model.encode(
        text,
        normalize_embeddings=True
    )

    return embedding.tolist()