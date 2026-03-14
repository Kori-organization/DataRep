from pydantic import BaseModel
from typing import Optional
from datetime import date
from app.models.reportCard import ReportCardResponse
from app.models.grades import GradesResponse

class StudentReportDTO(BaseModel):
    enrollment: int
    name: str
    serie: int
    issue_date: date
    report_card: Optional[ReportCardResponse]
    grades: Optional[GradesResponse]