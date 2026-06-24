from fastapi import APIRouter

from app.services.qa.resume_qa import answer_resume_question

router = APIRouter()

@router.get("/resume-qa")
async def resume_qa(query: str):
    return{
        "answer" : answer_resume_question(query)
    }