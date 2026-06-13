from fastapi import APIRouter

from app.services.retrieval.search import search_resumes
from app.services.generation.generator import summarize_resume

router = APIRouter()

@router.get("/rag")
async def rag(query: str):

    results = (
        search_resumes(query)
    )

    documents= (results["documents"][0])

    summaries = []

    for doc in documents:

        summaries.append(
            summarize_resume(doc)
        )

        return {
            "query": query,
            "results": summaries
        }