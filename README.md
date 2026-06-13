# AI Recruitment Assistant (RAG-Based Candidate Screening)

An end-to-end AI-powered recruitment assistant that helps recruiters search and screen candidates using semantic resume retrieval, candidate ranking, and conversational querying.

## Overview

Traditional recruitment involves manually reviewing hundreds of resumes.

This project automates candidate discovery by combining:

* Resume Parsing
* Embedding Generation
* Vector Search
* Semantic Retrieval
* Candidate Ranking
* Conversational Search
* Candidate Cards

Recruiters upload resumes and search using natural language.

Example:

> "Find Python backend developers with FastAPI experience"

The system retrieves and ranks relevant candidates.

---

## Features

### Resume Processing

* Upload PDF resumes
* Extract resume text
* Generate embeddings
* Store in vector database

### Candidate Search

* Semantic search
* Candidate ranking
* Candidate cards
* Resume viewer

### Conversational Layer

* Follow-up recruiter questions
* Requirement collection
* Query building

### Frontend

* React dashboard
* Resume upload
* Candidate search

---

## Tech Stack

### Backend

* FastAPI
* Python
* ChromaDB
* SentenceTransformers

### Frontend

* React
* Vite

### Retrieval

* Vector Embeddings
* Semantic Search

---

## System Architecture

Upload Resume

↓

Parse Resume

↓

Generate Embeddings

↓

Store in ChromaDB

↓

Recruiter Search

↓

Semantic Retrieval

↓

Ranking

↓

Candidate Cards

↓

Resume Viewer

---

## Future Improvements

* Gemini / Groq integration
* ZIP Upload
* Google Drive ingestion
* PostgreSQL + pgvector
* Hybrid Search
* Metadata filtering
* Dynamic follow-up questions
* Docker deployment

---

## Run Locally

Backend:

pip install -r requirements.txt

uvicorn main:app --reload

Frontend:

cd frontend

npm install

npm run dev

---

## Author

Built as a production-style AI Engineering learning project.