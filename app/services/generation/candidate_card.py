from app.services.parsers.resume_extractor import extract_resume_data

def build_candidate_card(text, score):

    data = extract_resume_data(text)

    return {
        "candidate": data["name"],
        "skills": data["skills"],
        "emails": data["emails"],
        "match_score": score,
        "summary": "Candidate appears relevant based on extracted skills"
    }