from fastapi import APIRouter,HTTPException
from schemas.enrollment_schema import EnrollmentCreate, Response
from uuid import UUID
from services.enrollment_service import enrollment_service


enrollment_router = APIRouter()


@enrollment_router.get("/")
def get_all_enrollment():    
    return enrollment_service.get_all_enrollment()



@enrollment_router.post("/",status_code=201, summary="Enroll a user to a course")
def enroll_user_in_course(enroll_data: EnrollmentCreate): 
    enrolled = enrollment_service.enroll_user_in_course(enroll_data)
    return Response(message="User enrolled course successfully", data=enrolled)


post_summary ="Marks the completion of a course enrolled by a user"
@enrollment_router.patch("/mark-completion/{enrollment_id}", status_code=201,summary=post_summary, response_model=Response)
def mark_course_completion(enrollment_id: UUID):
    try:
        completion_marked = enrollment_service.mark_course_completion(enrollment_id)
        if not completion_marked:
           raise HTTPException(status_code= 404, detail="Course enrollment with id not found")
        return Response(message="Course completion marked successful", data=completion_marked)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
    

@enrollment_router.get("/user-enrollments/{user_id}", response_model=Response, status_code=200)
def all_enrollments_of_user(user_id: UUID):
    user_enrollments = enrollment_service.all_enrollments_of_user(user_id)

    if not user_enrollments:
        raise HTTPException(status_code=404, detail="User with this id not found")

    return Response(
        success=True,
        message="User enrollments retrieved successfully",
        data=user_enrollments
    )

  