from pydantic import BaseModel
from datetime import date, time
from typing import Optional

class CalendarEvent(BaseModel):
    id: int
    event_date: date
    event_start: Optional[time] = None
    event_end: Optional[time] = None
    event_name: str
    event_desc: Optional[str] = None
    admin_id: Optional[int] = None