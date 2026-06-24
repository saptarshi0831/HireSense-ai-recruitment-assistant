from app.services.retrieval.search import search_resumes
from app.services.llm.extractor import (
    client,
    extract_candidate
)


def answer_resume_question(question):
    results = search_resumes(question)

    docs = results.get(
        "documents",
        [[]]
    )[0]

    if not docs:
        return """
# No Matching Candidates

No relevant candidate profiles found.
"""

    candidates = []

    for doc in docs[:5]:
        try:
            extracted = extract_candidate(
                doc[:3000]
            )

            candidates.append({
                "name": extracted.get("name") or "Unknown",
                "skills": extracted.get("skills") or [],
                "summary": extracted.get("summary") or "No summary available",
                "experience": extracted.get("experience", 0)
            })

        except Exception as e:
            print(f"Extraction failed: {e}")

    if not candidates:
        return """
# Extraction Failed

Unable to build candidate profiles.
"""

    context = ""

    for c in candidates:
        context += f"""

Candidate:
{c['name']}

Experience:
{c['experience']} years

Skills:
{", ".join(c['skills'])}

Summary:
{c['summary']}

--------------------

"""

    prompt = f"""
You are an AI recruiter assistant.

Question:
{question}

Candidate Profiles:
{context}

Instructions:

Return MARKDOWN.

Use:

## Candidate Name

### Strengths
- point

### Skills
- point

### Projects
- point

### Recommendation

Rules:
- Mention names
- Use bullets
- Compare if needed
- Never invent experience
- Say uncertain if evidence weak
- Maximum 180 words
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config={
                "temperature": 0.2
            }
        )

        if hasattr(response, "text"):
            return response.text

    except Exception as e:
        print(f"QA failed: {e}")

    return f"""
# Resume QA Unavailable

Retrieved **{len(candidates)}** candidate profiles.

## Candidates

{
chr(10).join(
[
f"- {x['name']}"
for x
in candidates[:3]
]
)
}
"""