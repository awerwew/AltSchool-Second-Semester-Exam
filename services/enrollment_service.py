from uuid import UUID, uuid4
from fastapi import HTTPException

from database import course_enrollments, users, courses
from schemas.enrollment_schema import Enrollment, EnrollmentCreate

class EnrollmentService:
     

     @staticmethod
     #this activate the check to know if a course is open.
     def is_course_open(course_id: str):
        course = courses.get(str(course_id))

        if not course:
            raise HTTPException(status_code=404, detail=f"Course with id: {course_id} does not exist.")
        return course.is_open == True

     @staticmethod
     #This activate the check to know is the user is active.
     def is_user_active(user_id: str):
        user = users.get(str(user_id))

        if not user:
            raise HTTPException(status_code=404, detail=f"User with id: {user_id} does not exist.")
        return user.is_active == True
     
     @staticmethod
     #This gets all enrollment in the program.
     def get_all_enrollment():
        enrollment_data = {}

        for enrollment in course_enrollments.values():
            user = users.get(enrollment.user_id)
            course = courses.get(enrollment.course_id)

            if not course or not user:
                continue
            if enrollment.course_id not in enrollment_data:
                enrollment_data[enrollment.course_id] = {
                   "course_id": course.id,
                   "course_title": course.title,
                   "course_description": course.description,
                   "course_is_open": course.is_open,
                   "course_enrollments":[]
                }

            enrollment_data[enrollment.course_id]["course_enrollments"].append({
                "enrollment_id": enrollment.id,
                "user_id": user.id,
                "name": user.name,
                "email": user.email,
                "user_is_active": user.is_active,
                "course_enrolled_date": enrollment.enrolled_date,
                "completed_course": enrollment.completed
            })

        return {
            "success": True,
            "message": "Data fetched successfully",
            "data": list(enrollment_data.values())
        }




     @staticmethod
     #This enrolls users in a course.
     def enroll_user_in_course(enroll_data: EnrollmentCreate):        

         #check if user is active.
         if not EnrollmentService.is_user_active(enroll_data.user_id):
            raise HTTPException(
                status_code=422,
                detail="course enrollment is only available for active users."
            )        


         # Check if course is still open.
         if not EnrollmentService.is_course_open(enroll_data.course_id):
            raise HTTPException(
                status_code=422,
                detail="The course you want to enroll for is closed"
            )
         # Check if user has already enrolled for this course before.
         for enrollment in course_enrollments.values():
            if enrollment.user_id == enroll_data.user_id and enrollment.course_id == enroll_data.course_id:
                raise HTTPException(
                    status_code=422,
                    detail="The user is already registered for the course."
                )
            
        
         enrolled = Enrollment(id=str(uuid4()), **enroll_data.model_dump())
         course_enrollments[enrolled.id] = enrolled
         return enrolled
     
     

     @staticmethod
     #Mark the completion of a course.
     def mark_course_completion(enrollment_id: UUID):
        enrollment = course_enrollments.get(str(enrollment_id))

        if not enrollment:
            raise HTTPException(status_code=404, detail=f"Course enrollment with id: {enrollment_id} does not exist.")
        enrollment.completed = True
        return enrollment
     
     
     @staticmethod
     #This gets all the enrollment of a user.
     def all_enrollments_of_user(user_id: UUID):      
      specific_user_enrollments = []

      for enrollment in course_enrollments.values():
        if enrollment.user_id == str(user_id):
            specific_user_enrollments.append(enrollment)

      return specific_user_enrollments    


       

            


enrollment_service = EnrollmentService()