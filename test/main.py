from fastapi import FastAPI

app = FastAPI()

#----------------------------------IN MEMORY MOCK DATA-------------------------------------------
#COURSE DATA
fake_courses = [
     {"course_id": 1, "title":"Python Basics", "description":"Learn Python", "is_open": True},
     {"course_id": 2, "title":"Functions", "description":"Learn Functions", "is_open": True}
]

#THE USER DATA
fake_users = [
    {"name":"user1", "user_id": 1, "email": "user1@example.com", "is_active": True},
    {"name":"user2", "user_id": 2, "email": "user2@example.com", "is_active": True}
]

users = [{"user_id": 1, "name": "Alice"}, {"user_id": 2, "name": "Bob"}]
courses = [{"course_id": 1, "title": "Math"}, {"course_id": 2, "title": "Science"}]
enrollments =[{"user_id":1, "course_id": 1, "enrollment_id": 1},{"user_id":2, "course_id": 2, "enrollment_id": 2}]

#-------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------
#THE COURSE ENDPOINTS 
#-------------------------------------------------------------------------------------------

@app.get("/courses/all", status_code=200)
def get_all_courses():
    return {"message": "Success", "data": fake_courses}

@app.get("/courses/details/{course_id}", status_code=200)
def get_course_by_id(course_id: int):
     for course in fake_courses:
        if course["course_id"] == course_id:
             return {"message": "Success", "data": course}
     return ("Course not found")    

@app.post("/courses/create", status_code=201)
def create_course(course: dict):
    fake_courses.append(course)
    return {"message": "Course was created successfully", "data":course}

@app.put("/courses/update/{course_id}", status_code=200)
def update_course(course_id: int, title:str):
    existing_course = next((c for c in fake_courses if c["course_id"] == course_id), None)

    if existing_course is None:
        return ("Course not found")

    existing_course["title"] = title
    return {"message": "Course was updated successfully", "data": existing_course}



@app.patch("/courses/close/{course_id}", status_code=200)
def close_enrollment(course_id: int):
    for course in fake_courses:
        if not course:
          return ("Course not found")
    course["is_open"] = False
    return {"message": "Course deactivated successfully", "data": course}
    

@app.delete("/courses/delete/{course_id}", status_code=200)
def delete_course(course_id: int):
    existing_course = next((c for c in fake_courses if c["course_id"] == course_id), None)

    if existing_course is None:
        return ("Course not found")
    
    fake_courses.remove(existing_course)
    return {"message": "Course deleted successfully", "data": None}



@app.patch("/courses/reopen/{course_id}", status_code=200)
def reopen_enrollment(course_id: int):
    for course in fake_courses:
         if not course:
           return ("Course not found")
    course["is_open"] = True
    return {"message": "Course reactivated successfully", "data": course}

#-------------------------------------------------------------------------------------------
#THE USER ENDPOINT
#-------------------------------------------------------------------------------------------

@app.get("/users/all", status_code=200)
def get_all_users():
    return {"message": "Success", "data": fake_users}

@app.get("/users/details/{user_id}", status_code=200)
def get_user_by_id(user_id: int):
     for user in fake_users:
        if user["user_id"] == user_id:
             return {"message": "Success", "data": user}
     return ("User not found")    

@app.post("/users/create", status_code=201)
def create_user(user: dict):
    fake_users.append(user)
    return {"message": "User was created successfully", "data":user}

@app.put("/users/update/{user_id}", status_code=200)
def update_user(user_id: int, name:str):
    existing_user = next((u for u in fake_users if u["user_id"] == user_id), None)

    if existing_user is None:
        return ("User not found")

    existing_user["name"] = name
    return {"message": "User was updated successfully", "data": existing_user}



@app.patch("/users/deactivate/{user_id}", status_code=200)
def deactivate_user(user_id: int):
    for user in fake_users:
        if not user:
          return ("User not found")
    user["is_active"] = False
    return {"message": "User deactivated successfully", "data": user}
    

@app.delete("/users/delete/{user_id}", status_code=200)
def delete_user(user_id: int):
    existing_user = next((u for u in fake_users if u["user_id"] == user_id), None)

    if existing_user is None:
        return ("User not found")
    
    fake_users.remove(existing_user)
    return {"message": "User deleted successfully", "data": None}



@app.patch("/users/reactivate/{user_id}", status_code=200)
def reactivate_user(user_id: int):
    for user in fake_users:
         if not user:
           return ("User not found")
    user["is_active"] = True
    return {"message": "User reactivated successfully", "data": user}


#----------------------------------------------------------------------------------------
#THE ENROLLMENT ENDPOINT
#----------------------------------------------------------------------------------------
@app.get("/enrollments/" )
def get_all_enrollments():
    return enrollments


@app.patch("/enrollments/mark-completion/{enrollment_id}", status_code=201)
def mark_course_completion(enrollment_id: int):
    for enrollment in enrollments:
        if enrollment["enrollment_id"] == enrollment_id:
            enrollment["completed"] = True
            return {
                "message": "Course completion marked successful",
                "data": enrollment
            }
    return ("Course enrollment with id not found")



@app.get("/enrollments/user-enrollments/{user_id}")
def get_enrollments_of_user(user_id: int):
    user_enrollments = [e for e in enrollments if str(e["user_id"]) == str(user_id)]

    if not user_enrollments:
        return ("User with id not found")

    return {
        "message": "User enrollments retrieved successfully",
        "data": user_enrollments
    }