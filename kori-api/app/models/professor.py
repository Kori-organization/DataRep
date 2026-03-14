from pydantic import BaseModel

class ProfessorBase(BaseModel):
    username: str
    name: str

class ProfessorCreate(ProfessorBase):
    password_hash: str

class ProfessorResponse(ProfessorBase):
    id : int
    subject_id: int