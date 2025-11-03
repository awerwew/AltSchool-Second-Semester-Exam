from fastapi import FastAPI
from routes.course import course_router
from routes.enrollment import enrollment_router
from routes.user import user_router


app = FastAPI()



app.include_router(course_router, prefix="/courses", tags=["Courses"])
app.include_router(enrollment_router, prefix="/course-enrollments", tags=["Course Enrollments"])
app.include_router(user_router, prefix="/users", tags=["Users"])


@app.get("/", tags=["Home"], status_code= 200)
def home():
    return {"Message": "Welcome to EduTrack Lite API"}
