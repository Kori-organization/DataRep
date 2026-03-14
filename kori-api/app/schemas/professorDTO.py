from pydantic import BaseModel
from typing import Optional


class ProfessorStudentGradesDTO(BaseModel):
    enrollment: int
    name: str
    serie: int
    grade1: Optional[float] = None
    grade2: Optional[float] = None
    rec: Optional[float] = None


class StudentRankingDTO(BaseModel):
    enrollment: int
    name: str
    serie: int
    average: Optional[float] = None