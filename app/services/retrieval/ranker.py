def rank_results(query, documents):
    ranked = []

    query_words = query.lower().split()

    for doc in documents:
        lower = doc.lower()
        score = 0

        for word in query_words:
            if word in lower:
                score += 20

        ranked.append({
            "score": score,
            "text": doc
        })

    ranked.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return ranked