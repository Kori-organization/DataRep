from pydantic import BaseModel
from datetime import date


class StudentBase(BaseModel):
    email: str
    name: str


class StudentCreate(StudentBase):
    password: str


class StudentResponse(StudentBase):
    enrollment: int
    issue_date: date
    serie: int
