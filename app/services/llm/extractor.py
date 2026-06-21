from dotenv import load_dotenv
from google import genai
import os
import json

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found. Please add it to your .env file."
    )

client = genai.Client(api_key=api_key)


def extract_requirements(message):
    prompt = f"""
Extract recruiter requirements.

Return ONLY valid JSON in this format:

{{
    "role": "",
    "experience": 0,
    "skills": []
}}

Message: {message}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "temperature": 0.1,
            }
        )

        return json.loads(response.text)

    except Exception:
        return {
            "role": "",
            "experience": 0,
            "skills": []
        }


def extract_candidate(text):
    prompt = f"""
Extract candidate information from the resume.

Return ONLY valid JSON in this format:

{{
    "name": "",
    "email": "",
    "skills": [],
    "experience": 0,
    "summary": ""
}}

For "summary":
- Write a professional 2-3 sentence summary.
- Mention primary skills.
- Mention experience level.
- Mention domain expertise.
- Keep under 50 words.

Resume: {text}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "temperature": 0.1,
            }
        )

        return json.loads(response.text)

    except Exception as e:
         return {
            "name": None,
            "skills": [],
            "emails": [],
            "summary": ""
        }


if __name__ == "__main__":

    recruiter_message = """
    Looking for a Python Backend Developer
    with 3+ years of experience in FastAPI,
    PostgreSQL, Docker, and AWS.
    """

    requirements = extract_requirements(
        recruiter_message
    )

    print("\nRequirements:")
    print(json.dumps(requirements, indent=2))

    resume_text = """
    John Doe
    john.doe@email.com

    Skills:
    Python, Django, FastAPI, PostgreSQL, Docker

    Experience:
    Software Engineer with 3 years of experience
    building web applications and backend systems.
    """

    candidate = extract_candidate(
        resume_text
    )