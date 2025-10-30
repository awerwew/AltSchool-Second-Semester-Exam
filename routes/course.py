from fastapi import APIRouter, HTTPException
from schemas.course_schema import CourseCreate, CourseUpdate, Response
from services.course_service import course_service
from uuid import UUID




course_router = APIRouter()


@course_router.get("/")
def get_all_courses():
    courses = course_service.get_all_courses()
    return Response(message="Success", data= courses)


@course_router.get("/{course_id}", status_code= 200, summary="Get course by course_id")
def get_course_by_id(course_id: UUID):
    course = course_service.get_course_by_id(course_id) 
    if not course:
        raise HTTPException(status_code=404, detail=f"Course with id: {course_id} not found")
    return Response(message="Successful", data= course)


@course_router.post("/create", summary="This endpoint creates course")
def create_course(course_data: CourseCreate):
    course = course_service.create_course(course_data)
    return Response(message="Course was created successfully", data=course)

@course_router.put("/updates/{course_id}")
def course_update(course_id: UUID, course_data:CourseUpdate):
    course = course_service.course_update(course_id, course_data)
    if not course:
        raise HTTPException(status_code=404, detail=f"For this id: {course_id}, no data was found")
    return Response(message="Course updated successful", data=course)


@course_router.delete("/deletes/{course_id}")
def delete_course(course_id: UUID):
    is_deleted= course_service.delete_course(course_id)
    if not is_deleted:
        raise HTTPException(status_code=404, detail=f"Course with id: {course_id} not found")
    return Response(message="Course deleted successfully", data=None)


@course_router.patch("/close-enrollment/{course_id}", summary="This endpoint is used to close course enrollment")
def close_enrollment(course_id: UUID):
    closed_enrollment = course_service.close_enrollment(course_id)
    if not closed_enrollment:
        raise HTTPException(status_code= 404, detail=f"Course with id: {course_id} not found")
    return Response(message="Enrollment closed successfully", data= None)


@course_router.patch("/reopen-enrollment/{course_id}", summary="This endpoint is used to reopen course enrollment")
def reopen_enrollment(course_id: UUID):
    opened_enrollment = course_service.reopen_enrollment(course_id)
    if not opened_enrollment:
        raise HTTPException(status_code= 404, detail=f"Course with id: {course_id} not found")
    return Response(message="Enrollment reopened successfully", data= None)



@course_router.get("/courses/{course_id}/enrolled-users", summary="To retrieve users in a paticular course")
def retrieve_enrolled_users(course_id:UUID):
    popular_course = course_service.retrieve_enrolled_users(course_id)
    return {"Message": "Popular course retrieved successfully", "data":popular_course}     

         
 

    






    