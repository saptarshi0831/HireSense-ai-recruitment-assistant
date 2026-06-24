from app.services.retrieval.search import search_resumes
from app.services.llm.extractor import client


def compare_candidates(query: str):
    try:
        results = search_resumes(
            query=query,
            n_results=10
        )

        docs = results.get("documents", [[]])[0]

        filtered = []
        keywords = query.lower().split()

        for doc in docs:
            lower = doc.lower()

            score = sum(
                1
                for k in keywords
                if k in lower
            )

            if score > 0:
                filtered.append(doc)

        docs = filtered[:5]

        if len(docs) < 2:
            return """
# Not Enough Candidates

At least two candidate resumes are required for comparison.
"""

        candidate_sections = []

        for idx, doc in enumerate(docs[:5]):
            candidate_sections.append(
                f"""
Candidate {idx + 1}

Resume:
{doc[:1200]}

--------------------------------------------------
"""
            )

        context = "\n".join(candidate_sections)

        prompt = f"""
You are a senior recruiter.

Question:
{query}

Candidate Resumes:
{context}

Compare only candidates relevant to the query.

Rules:
- Use only resume evidence.
- Mention names.
- Ignore unrelated resumes.
- Do not infer skills or experience.
- If missing write:
  "Not mentioned in resume"
- Return markdown.
- Keep concise.
- Prefer complete answers over short answers.
- Maximum 500 words.

Format:

# Candidate Comparison

## Overview
2-3 sentences.

## Skills
- Candidate → evidence

## Projects

For each candidate:
- Project Name
- Technologies
- Why relevant

## Strengths
- Candidate → evidence

## Recommendation
Best match and why.

Finish all sections before ending.
Do not stop after the first candidate.
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config={
                "temperature": 0.1,
                "max_output_tokens": 3000,
            },
        )

        if hasattr(response, "text") and response.text:
            return response.text

        return """
# Comparison Unavailable

The model did not return a valid response.
"""

    except Exception as e:
        print(f"Compare failed: {e}")

        if "429" in str(e):
            return """
# Comparison Temporarily Unavailable

Gemini quota exhausted.

Please try again later.
The retrieval system is functioning normally.
"""

        return f"""
# Comparison Unavailable

Error:
{str(e)}
"""


if __name__ == "__main__":
    query = "Best Python backend developer with FastAPI experience"

    result = compare_candidates(query)

    print(result)