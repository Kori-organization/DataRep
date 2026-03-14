from fastapi import APIRouter
from app.services.student_service import AlunoService

router = APIRouter(prefix="/students", tags=["Students"])


@router.get("/{enrollment}")
async def get_student_report(enrollment: int):
    return await AlunoService.get_student_report(enrollment)


@router.get("/{enrollment}/observations")
async def get_observations(enrollment: int):
    return await AlunoService.get_student_observations(enrollment)


@router.get("/calendar/events")
async def get_calendar():
    return await AlunoService.get_calendar_events()