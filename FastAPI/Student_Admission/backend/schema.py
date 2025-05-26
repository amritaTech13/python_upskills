from pydantic import BaseModel
from typing import Optional



class Add_Student(BaseModel):
    name: str  # Changed from name to std_name to match the model
    email: str
    age: int

class Student_response(BaseModel):
    id: int
    name: str  # This already matches the model
    email: str
    age: int
    admitted: bool
    course_id: Optional[int]  

    class Config:
        from_attributes = True  # Changed from orm_mode to from_attributes

class Add_Course(BaseModel):
    course_name: str
    total_seats: int    


class Course_response(BaseModel):
    course_id: int
    course_name: str
    total_seats: int

    class Config:
        from_attributes = True  # Changed from orm_mode to from_attributes


class Admin_create(BaseModel):
    username: str
    password: str   

class Admin_login(BaseModel):
    username: str
    password: str   