from pydantic import BaseModel
from typing import Optional

class ReportCard(BaseModel):
    final_situation: str

class ReportCardResponse(ReportCard):
    id: int
    student_id: int