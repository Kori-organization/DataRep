from typing import Optional, List
from pydantic import BaseModel, Field
from datetime import date
from app.models.reportCard import ReportCardResponse


class StudentGradeDTO(BaseModel):
    subject_id: int
    subject_name: str
    grade1: Optional[float] = None
    grade2: Optional[float] = None
    rec: Optional[float] = None


class StudentReportDTO(BaseModel):
    enrollment: int
    name: str
    serie: int
    issue_date: date
    report_card: Optional[ReportCardResponse]
    grades: List[StudentGradeDTO] = Field(default_factory=list)