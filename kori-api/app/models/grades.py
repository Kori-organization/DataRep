from pydantic import BaseModel
from typing import Optional

class Grades(BaseModel):
    id: int
    grade1: Optional[float] = None
    grade2: Optional[float] = None
    rec: Optional[float] = None

class GradesResponse(BaseModel):
    subject_id: int
    grade1: Optional[float] = None
    grade2: Optional[float] = None
    rec: Optional[float] = None