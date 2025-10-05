from datetime import datetime
from pydantic import BaseModel
from typing import Optional



class Enrollment(BaseModel):
    id: str
    user_id: str
    course_id: str
    enrolled_date: datetime
    completed: bool = False

class EnrollmentCreate(BaseModel):
    user_id: str
    course_id: str
    enrolled_date: datetime
    completed: bool = False

class Response(BaseModel):
    success: bool = True
    message: Optional[str] = None
    data: Optional[Enrollment | list[Enrollment]] = None