from fastapi import HTTPException
from schemas.course_schema import Course, CourseCreate, CourseUpdate
from database import courses, course_enrollments, users
from uuid import UUID, uuid4
from typing import Dict


class CourseService:

    @staticmethod
    #This return of gets all course created.
    def get_all_courses():
        return list(courses.values())
    
    @staticmethod
    def get_course_by_id(course_id):
        course = courses.get(str(course_id))
        if not course:
            return None
        return course

    

    @staticmethod
    #This returns all create new course.
    def create_course(course_data: CourseCreate):
        for course in courses.values():
            if course.title == course_data.title:
                raise HTTPException(status_code=422, detail="A course with this title already exists.")

        new_course = Course(id=str(uuid4()), **course_data.model_dump())
        courses[new_course.id] = new_course
        return new_course
    

    @staticmethod
    #This updates the course created.
    def course_update(course_id: UUID, course_data:CourseUpdate):
        course = courses.get(str(course_id))
        if not course:
            return None
        

        course.title = course_data.title
        course.description = course_data.description
        return course
    
    @staticmethod
    #This deletes course
    def delete_course(course_id: UUID):
        course = courses.get(str(course_id))
        if not course:
            return None
        
        del courses[course.id]   
        return True 
    
    @staticmethod
    #This terminates or close enrollments
    def close_enrollment(course_id):
        course = courses.get(str(course_id))
        if not course:
            return None
                    
        course.is_open = False
        return course
    
    @staticmethod
    #This reopens terminated of closed enrollments
    def reopen_enrollment(course_id):
        course = courses.get(str(course_id))
        if not course:
            return None
                    
        course.is_open = True
        return course
    
    @staticmethod
    #This returns or gets enrolled users to a particular course by course_id
    def retrieve_enrolled_users(course_id: UUID) -> Dict:
        enrolled_users = []

        for enrollment in course_enrollments.values():
            if enrollment.course_id == str(course_id): 
                user = users.get(enrollment.user_id)
                if user:
                    enrolled_users.append(user.model_dump())
    
        if not enrolled_users:
            raise HTTPException(status_code=404, detail=f"Course with id: {course_id} not found")        
                                               
        return {
            "course_id": str(course_id),
            "enrolled_users":(enrolled_users) 
        }

    

    
        

   


course_service = CourseService()