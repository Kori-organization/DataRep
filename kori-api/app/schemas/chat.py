from pydantic import BaseModel


class StudentQuestionRequest(BaseModel):
    enrollment: int
    question: str


class ChatResponseDTO(BaseModel):
    response: str