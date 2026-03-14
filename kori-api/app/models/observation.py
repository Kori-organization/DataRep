from pydantic import BaseModel

class Observation(BaseModel):
    id: int
    student_id: int
    observation: str