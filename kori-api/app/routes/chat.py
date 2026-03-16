from fastapi import APIRouter
from app.schemas.chat import StudentQuestionRequest, ChatResponseDTO
from app.services.chat_service import ChatService

router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("/student", response_model=ChatResponseDTO)
async def ask_student_question(payload: StudentQuestionRequest):
    return await ChatService.ask_student_question(
        enrollment=payload.enrollment,
        question=payload.question
    )