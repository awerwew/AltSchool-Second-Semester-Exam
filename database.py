from schemas.user_schema import User
from schemas.course_schema import Course
from schemas.enrollment_schema import Enrollment

users: dict[str, User] = {}
courses: dict[str, Course] = {}
course_enrollments: dict[str, Enrollment] = {}


