from fastapi import APIRouter
from app.schemas.chat import StudentQuestionRequest, ProfessorQuestionRequest, ChatResponseDTO
from app.services.chat_service import ChatService

router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("/student", response_model=ChatResponseDTO)
async def ask_student_question(payload: StudentQuestionRequest):
    return await ChatService.ask_student_question(
        enrollment=payload.enrollment,
        question=payload.question
    )


@router.post("/professor", response_model=ChatResponseDTO)
async def ask_professor_question(payload: ProfessorQuestionRequest):
    return await ChatService.ask_professor_question(
        professor_id=payload.professor_id,
        question=payload.question
    )