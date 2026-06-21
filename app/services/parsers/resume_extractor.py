import re
import spacy

nlp = spacy.load("en_core_web_sm")

SECTION_HEADERS = {
    "experience": [
        "experience",
        "work experience",
        "professional experience",
        "work history",
        "career",
    ],
    "projects": [
        "projects",
        "project",
    ],
    "education": [
        "education",
        "academic background",
    ],
    "skills": [
        "skills",
        "technical skills",
        "core competencies",
    ],
    "certifications": [
        "certifications",
        "certificates",
        "licenses",
    ],
    "languages": [
        "languages",
    ],
}


def extract_section(text, headers):
    lines = text.split("\n")
    content = []
    capture = False

    for line in lines:
        lower = line.strip().lower()

        if any(lower == h or lower.startswith(h) for h in headers):
            capture = True
            continue

        if capture:
            if any(
                lower == hdr or lower.startswith(hdr)
                for section in SECTION_HEADERS.values()
                for hdr in section
            ):
                break

            content.append(line)

    return "\n".join(content).strip()


def extract_name(text):
    lines = [x.strip() for x in text.split("\n") if x.strip()]

    for line in lines[:10]:
        if (
            len(line.split()) <= 4
            and not any(c.isdigit() for c in line)
            and "@" not in line
            and len(line) < 40
        ):
            return line

    return None


def extract_skills(skills_text):
    if not skills_text:
        return []

    skills = []

    items = re.split(r"[,\n•|]", skills_text)

    BLOCK = [
        "developed",
        "built",
        "identified",
        "award",
        "recognized",
        "achieved",
        "contributed",
    ]

    for item in items:
        item = item.strip()

        if 2 <= len(item) <= 30:
            if not any(word in item.lower() for word in BLOCK):
                skills.append(item)

    return sorted(list(set(skills)))


def extract_resume_data(text):
    doc = nlp(text)

    emails = list(
        set(
            re.findall(
                r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
                text,
            )
        )
    )

    phones = list(
        set(
            re.findall(
                r"\+?\d{10,15}",
                text,
            )
        )
    )

    organizations = [
        ent.text
        for ent in doc.ents
        if ent.label_ == "ORG" and len(ent.text) < 40
    ]

    experience = extract_section(
        text,
        SECTION_HEADERS["experience"],
    )

    education = extract_section(
        text,
        SECTION_HEADERS["education"],
    )

    projects = extract_section(
        text,
        SECTION_HEADERS["projects"],
    )

    skills_section = extract_section(
        text,
        SECTION_HEADERS["skills"],
    )

    certifications = extract_section(
        text,
        SECTION_HEADERS["certifications"],
    )

    languages = extract_section(
        text,
        SECTION_HEADERS["languages"],
    )

    skills = extract_skills(skills_section)

    summary = (
        projects
        or experience
        or education
        or text
    )

    summary = " ".join(summary.split())[:300]

    return {
        "name": extract_name(text),
        "emails": emails,
        "phones": phones,
        "skills": skills,
        "organizations": list(set(organizations)),
        "experience": experience,
        "education": education,
        "projects": projects,
        "certifications": certifications,
        "languages": languages,
        "summary": summary,
        "full_text": text,
    }