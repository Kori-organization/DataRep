from fastapi import APIRouter
from app.services.professor_service import ProfessorService

router = APIRouter(prefix="/professors", tags=["Professors"])


@router.get("/{professor_id}/students")
async def get_students_grades(professor_id: int):
    return await ProfessorService.get_students_grades(professor_id)


@router.get("/{professor_id}/ranking")
async def get_ranking(professor_id: int):
    return await ProfessorService.get_ranking(professor_id)