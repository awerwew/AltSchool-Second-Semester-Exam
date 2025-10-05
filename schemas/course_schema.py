from pydantic import BaseModel
from typing import Optional


class Course(BaseModel):
    id: str
    title: str
    description: str
    is_open: bool = True

class CourseCreate(BaseModel):
    title: str
    description: str
    is_open: bool = True

class CourseUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

class Response(BaseModel):
    success: bool = True
    message: Optional[str] = None
    data: Optional[Course | list[Course]] = None