from fastapi import APIRouter

from app.services.chat.recruiter_chat import handle_message

router = APIRouter()

@router.get("/chat")
async def chat(message: str):

    return (
        handle_message(message)
    )