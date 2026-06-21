from app.services.chat.state import conversation
from app.services.llm.extractor import extract_requirements
from app.services.retrieval.search import search_resumes
from app.services.retrieval.ranker import rank_results
from app.services.generation.candidate_card import build_candidate_card


def handle_message(message):
    extracted = extract_requirements(message)

    if extracted.get("error"):
        return {
            "reply": f"Error: {extracted['error']}"
        }

    if extracted.get("role"):
        if not conversation["role"]:
            conversation["role"] = extracted["role"]
        

    if extracted.get("experience"):
        if not conversation["experience"]:
            conversation["experience"] = str(
                extracted["experience"]
            )

    if extracted.get("skills"):
        if isinstance(extracted["skills"], list):
            conversation["skills"].extend(
                extracted["skills"]
            )

            conversation["skills"] = list(
                set(conversation["skills"])
            )

    missing = []

    if not conversation["role"]:
        missing.append("role")

    if not conversation["experience"]:
        missing.append("experience")

    if not conversation["skills"]:
        missing.append("skills")

    if missing:
        questions = {
            "role": "What role are you hiring for?",
            "experience": "Minimum experience required?",
            "skills": "Required skills?"
        }

        return {
            "reply": questions[missing[0]]
        }

    query = " ".join([
        conversation["role"],
        conversation["experience"],
        " ".join(conversation["skills"])
    ])

    results = search_resumes(query)

    if not results["documents"]:
        return {
            "reply": "No candidates found!"
            }

    docs = results["documents"][0]
    ids = results["ids"][0]

    candidates = [
        {
            "text": doc,
            "filename": file_id
        }
        for doc, file_id in zip(docs, ids)
    ]

    ranked = rank_results(
        query,
        candidates
    )

    cards = []

    for item in ranked:
        card = build_candidate_card(
            item["text"],
            item["score"]
        )

        card["filename"] = item["filename"]

        cards.append(card)

    conversation["role"] = None
    conversation["experience"] = None
    conversation["skills"] = []

    return {
        "reply": "Top Candidates",
        "results": cards[:3]
    }