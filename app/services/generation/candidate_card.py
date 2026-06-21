from app.services.parsers.resume_extractor import (
    extract_resume_data
)
from app.services.llm.extractor import (
    extract_candidate
)

def generate_summary(text):
    words = (
        text
        .replace("\n", " ")
        .split()
    )

    summary = " ".join(words[:50])

    if len(words) > 50:
        summary += "..."

    return summary


def build_candidate_card(text, score):
    # Gemini -> fallback -> Regex
    try:
        data = extract_candidate(text)

        if data.get("error"):
            data = extract_resume_data(text)

    except Exception:
        data = extract_resume_data(text)

    summary = (
        data.get("summary")
        or generate_summary(text)
    )

    return {
        "candidate": data.get("name", "") or "Unknown Candidate",
        "skills": data.get("skills", []),
        "email": data.get("email", ""),
        "match_score": score,
        "summary": summary 
    }