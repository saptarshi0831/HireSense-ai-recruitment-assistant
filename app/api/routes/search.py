from fastapi import APIRouter

from app.services.retrieval.search import search_resumes
from app.services.retrieval.ranker import rank_results
from app.services.generation.candidate_card import build_candidate_card

router = APIRouter()

TOP_K = 5


@router.get("/search")
async def search(query: str):
    results = search_resumes(query)

    if not results["documents"]:
        return {
            "query": query,
            "results": []
        }

    documents = results["documents"][0]
    ids = results["ids"][0]

    candidates = [
        {
            "text": doc,
            "filename": file_id
        }
        for doc, file_id in zip(documents, ids)
    ]

    ranked = rank_results(query, candidates)

    cards = []

    for item in ranked:
        card = build_candidate_card(
            item["text"],
            item["score"]
        )

        card["filename"] = item["filename"]
        card["confidence"] = item["confidence"]

        cards.append(card)

    return {
        "query": query,
        "results": cards[:TOP_K]
    }