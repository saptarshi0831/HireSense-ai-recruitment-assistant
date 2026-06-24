from fastapi import FastAPI
from app.api.routes.upload import router as upload_router
from app.api.routes.parser import router as parser_router
from app.api.routes.embed import router as embed_router
from app.api.routes.store import router as store_router
from app.api.routes.search import router as search_router
from app.api.routes.rag import router as rag_router
from app.api.routes.extract import router as extract_router
from app.api.routes.profile import router as profile_router
from app.api.routes.chat import router as chat_router
from app.api.routes.resume import router as resume_router
from app.api.routes.bulk_upload import router as bulk_router
from app.api.routes.qa import router as qa_router
from app.api.routes.compare import router as compare_router

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Resume Screening RAG"
)

app.add_middleware(CORSMiddleware,
                   allow_origins=["http://localhost:5173"],
                   allow_methods=["*"],
                   allow_headers=["*"]
                )

app.include_router(upload_router)
app.include_router(parser_router)
app.include_router(embed_router)
app.include_router(store_router)
app.include_router(search_router)
app.include_router(rag_router)
app.include_router(extract_router)
app.include_router(profile_router)
app.include_router(chat_router)
app.include_router(resume_router)
app.include_router(bulk_router)
app.include_router(qa_router)
app.include_router(compare_router)

@app.get("/")
async def root():
    return {
        "message": "Resume Screening RAG Running"
    }