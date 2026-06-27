# HireSense - AI Resume Screening Platform

An end-to-end AI-powered recruitment assistant that enables recruiters to efficiently search, compare, and evaluate candidates using semantic resume retrieval, Retrieval-Augmented Generation (RAG), and Large Language Models.

---

## Demo

🎥 **Project Demo:**

```
https://youtu.be/your-demo-link
```

---

## Overview

HireSense automates the resume screening process by combining vector search, semantic retrieval, and AI-powered reasoning. Recruiters can upload resumes, search candidates using natural language, compare applicants, and ask follow-up questions without manually reviewing every resume.

Example recruiter queries:

* "Find Python backend developers with FastAPI experience."
* "Compare Python and Golang candidates."
* "Who worked on RAG?"
* "Which candidate has the strongest backend project?"

---

# Features

## Resume Processing

* Bulk ZIP resume upload
* PDF parsing and text extraction
* Structured candidate profile extraction using Gemini
* Automatic resume summarization

## Semantic Candidate Search

* Semantic search using Sentence Transformers
* Candidate ranking with custom scoring
* Match score and confidence estimation
* Resume preview and download

## AI Recruiter Assistant

* Natural language recruiter Q&A
* Candidate comparison
* Resume-based recommendations
* Evidence-based responses using RAG

## Frontend

* Modern React dashboard
* Resume upload interface
* Candidate search
* Candidate comparison
* Recruiter AI Assistant

---

# Tech Stack

### Backend

* Python
* FastAPI
* ChromaDB
* Sentence Transformers
* Gemini 2.5 Flash
* NLTK

### Frontend

* React
* Vite
* CSS

### AI & Retrieval

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Vector Embeddings
* Custom Candidate Ranking

---

# System Architecture

```
Resume Upload (ZIP/PDF)
        │
        ▼
 Resume Parsing
        │
        ▼
 Candidate Profile Extraction (Gemini)
        │
        ▼
 Embedding Generation
        │
        ▼
 Store Embeddings (ChromaDB)
        │
        ▼
 Natural Language Search
        │
        ▼
 Semantic Retrieval
        │
        ▼
 Candidate Ranking
        │
        ├──────────────┐
        ▼              ▼
 Candidate Cards   Recruiter AI Assistant
                        │
                        ▼
             Candidate Comparison & Q&A
```

---

# Run Locally

## Backend

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Frontend

```bash
cd frontend
npm install
npm run dev
```

---

# Future Improvements

* Recruiter authentication
* Candidate analytics dashboard
* Hybrid Search (BM25 + Vector Search)
* PostgreSQL + pgvector
* Cloud storage integration
* Docker deployment
* CI/CD pipeline
* Production deployment

---

# Author

**Saptarshi Das**

Built as a full-stack AI engineering project demonstrating Retrieval-Augmented Generation (RAG), semantic search, vector databases, and LLM-powered recruiter assistance.
