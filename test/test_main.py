
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

#------------------------------------IN MEMORY MOCK DATA------------------------------------------------------------
fake_courses = [
     {"course_id": 1, "title":"Python Basics", "description":"Learn Python", "is_open": True},
     {"course_id": 2, "title":"Functions", "description":"Learn Functions", "is_open": True}
]

fake_users = [
    {"name":"user1", "user_id": 1, "email": "user1@example.com", "is_active": True},
    {"name":"user2", "user_id": 2, "email": "user2@example.com", "is_active": True}
]

users = [{"user_id": 1, "name": "Alice"}, {"user_id": 2, "name": "Bob"}]
courses = [{"course_id": 1, "title": "Math"}, {"course_id": 2, "title": "Science"}]
enrollments =[{"user_id":1, "course_id": 1, "enrollment_id": 1},{"user_id":2, "course_id": 2, "enrollment_id": 2}]
#------------------------------------------------------------------------------------------------------------------

#-------------------
#THE TEST FOR COURSE
#--------------------

def test_get_all_courses():
    response = client.get("/courses/all")
    assert response.status_code == 200
    assert response.json()["message"] == "Success"

def test_get_course_by_id():
    course_id = 1
    response = client.get(f"/courses/details/{course_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Success"

def test_create_course():
    course = fake_courses[0]
    response = client.post("/courses/create", json=course)
    assert response.status_code == 201
    assert response.json()["message"] == "Course was created successfully"

def test_update_course():
    course_id = 2
    title = "Updated Title"
    response = client.put(f"/courses/update/{course_id}?title={title}")
    assert response.status_code == 200
    assert response.json()["message"] == "Course was updated successfully"
    assert response.json()["data"]["title"] == title

def test_close_enrollment():
    course_id = 1
    response = client.patch(f"/courses/close/{course_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Course deactivated successfully"

def test_delete_course():
    course_id = 2
    response = client.delete(f"/courses/delete/{course_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Course deleted successfully"

def test_reopen_enrollment():
    course_id = 1
    response = client.patch(f"/courses/reopen/{course_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Course reactivated successfully"


#-------------------
#THE TEST FOR USER
#-------------------

def test_get_all_users():
    response = client.get("/users/all")
    assert response.status_code == 200
    assert response.json()["message"] == "Success"

def test_get_user_by_id():
    user_id = 1
    response = client.get(f"/users/details/{user_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Success"

def test_create_user():
    user = fake_users[0]
    response = client.post("/users/create", json=user)
    assert response.status_code == 201
    assert response.json()["message"] == "User was created successfully"

def test_update_user():
    user_id = 2
    name = "Updated Name"
    response = client.put(f"/users/update/{user_id}?name={name}")
    assert response.status_code == 200
    assert response.json()["message"] == "User was updated successfully"
    assert response.json()["data"]["name"] == name

def test_deactivate_user():
    user_id = 1
    response = client.patch(f"/users/deactivate/{user_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "User deactivated successfully"

def test_delete_user():
    user_id = 2
    response = client.delete(f"/users/delete/{user_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "User deleted successfully"

def test_reactivate_user():
    user_id = 1
    response = client.patch(f"/users/reactivate/{user_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "User reactivated successfully"



#------------------------  
# THE TEST FOR ENROLLMENT
#------------------------
def test_get_all_enrollment():
    response = client.get("/enrollments/")
    assert response.status_code == 200


def test_mark_course_completion():
    enrollment_id = 1
    response = client.patch(f"/enrollments/mark-completion/{enrollment_id}")
    assert response.status_code == 201
    assert response.json()["message"] == "Course completion marked successful"


def test_all_enrollments_of_user():
    user_id = 1
    response = client.get(f"/enrollments/user-enrollments/{user_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "User enrollments retrieved successfully"

