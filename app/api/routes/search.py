from fastapi import APIRouter

from app.services.retrieval.search import search_resumes
from app.services.retrieval.ranker import rank_results
from app.services.generation.candidate_card import build_candidate_card


router = APIRouter()

@router.get("/search")

async def search(query: str):
    results = search_resumes(query)

    documents = results["documents"][0]
    ids = results["ids"][0]

    ranked = rank_results(query, documents)

    cards = []

    for i, item in enumerate(ranked):

        card = build_candidate_card(
            item["text"],
            item["score"]
        )

        if i < len(ids):
            card["filename"] = ids[i]
        else:
            card["filename"] = None

        cards.append(card)

    return {
        "query": query,
        "results": cards
    }