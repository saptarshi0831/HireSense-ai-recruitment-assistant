from app.services.chat.state import conversation
from app.services.retrieval.search import search_resumes
from app.services.retrieval.ranker import rank_results
from app.services.generation.candidate_card import build_candidate_card

def handle_message(message):

    if(conversation["role"] is None):

        conversation["role"] = message

        return {
            "reply":

            "Minimum experience?"
        }
    
    if(conversation["experience"] is None):
        
        conversation["experience"] = message

        return {
            "reply":

            "Required skills?"
        }
    
    conversation["skills"].append(message)

    query = " ".join([conversation["role"],
                      
                      conversation["experience"],
                      
                      " ".join(conversation["skills"]
                           )
                    ])
    

    results = search_resumes(query)

    docs = results["documents"][0]

    ranked = rank_results(query, docs)

    cards = []

    for item in ranked:
        cards.append(
            build_candidate_card(
                item["text"],
                item["score"]
            )
        )

    conversation["role"] = None

    conversation["experience"] = None

    conversation["skills"] = []

    return {
        "reply": "Top Candidates",
        "results": cards[:3]
    }