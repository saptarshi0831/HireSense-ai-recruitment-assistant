import re
import spacy


nlp = spacy.load("en_core_web_sm")

KNOWN_SKILLS = [
    "python",
    "fastapi",
    "aws",
    "sql",
    "postgresql"

    "docker",

    "machine_learning",

    "tensorflow",

    "pytorch",

    "java",

    "react",

    "llm",
    "rag"
]

def extract_resume_data(text: str):

    doc = nlp(text)

    names = [
        ent.text

        for ent in doc.ents

        if ent.label_ == "PERSON"
    ]

    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+", text)
    
    lower = text.lower()
    
    found = []

    for skill in KNOWN_SKILLS:
        if skill in lower:
            found.append(skill)


    return {
        "name": names[0]
                if names
                else "Unknown",
        
        "emails": list(set(emails)),

        "skills": sorted(found)
    }