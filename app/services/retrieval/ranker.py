import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
STOPWORDS = set(stopwords.words("english"))


def extract_years(text):
    match = re.search(r"(\d+)(\+)?\s*(year|years|yr)", text.lower())

    if match:
        years = int(match.group(1))
        is_plus = match.group(2) == "+"
        return years, is_plus

    return 0, False


def preprocess_text(text):
    words = []

    for word in text.lower().split():
        cleaned = re.sub(r"[^a-z0-9+]", "", word)

        if cleaned and cleaned not in STOPWORDS:
            words.append(lemmatizer.lemmatize(cleaned))

    return words


def rank_results(query, candidates):
    ranked = []

    query_words = preprocess_text(query)
    query_exp, query_plus = extract_years(query)

    for candidate in candidates:
        score = 0

        candidate_words = preprocess_text(candidate["text"])

        # Keyword Matching (70)
        matched = 0

        for word in query_words:
            if word in candidate_words:
                matched += 1

        keyword_score = min(
            1,
            matched / max(len(query_words) * 0.4, 1)
        )

        score += keyword_score * 70

        # Experience Matching (30)
        candidate_exp, _ = extract_years(candidate["text"])

        if query_exp > 0 and candidate_exp > 0:
            if query_plus:
                if candidate_exp >= query_exp:
                    score += 30
                else:
                    score += max(
                        0,
                        30 - (query_exp - candidate_exp) * 10
                    )
            else:
                diff = abs(query_exp - candidate_exp)
                score += max(0, 30 - diff * 10)

        # Confidence level
        if score >= 80:
            confidence = "High"
        elif score >= 50:
            confidence = "Medium"
        else:
            confidence = "Low"

        ranked.append({
            "score": round(score, 2),
            "confidence": confidence,
            "text": candidate["text"],
            "filename": candidate["filename"]
        })

    ranked.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    MIN_SCORE = 20

    return [
        x
        for x in ranked
        if x["score"] >= MIN_SCORE
    ]