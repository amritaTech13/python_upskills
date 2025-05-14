
from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def index():
    return {'Name':'Amrita', 'lName': 'Rajbhar'}

# path parameter
Students = {
        1: {
        'name':'Amrita',
         'age': 27,
         'degree': 'M.Tech'
    }
}
class Student(BaseModel):
    name:str
    age:int
    degree:str

class Update_Student(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    degree: Optional[str] = None

@app.get('/get_Students/{students_id}') 
def get_Students(students_id:int):
    return Students[students_id]

#query parameter
@app.get('/get_student_by_name')
def get_Students(name:Optional[str]=None):
    for id in Students:
        if Students[id]['name'] == name:
            return  Students[id]
    return {"Data": "Not found"}

#combine Path and query parameter
@app.get('/get_student_by_name/{students_id}')
def get_Students(*,id:int, name:Optional[str]=None, test:int):
    for id in Students:
        if Students[id]['name'] == name:
            return  Students[id]
    return {"Data": "Not found"}

#post methods
@app.post('/create_student/{students_id}')
def create_student(students_id:int, student: Student):
    if students_id in Students:
        return {'Error':'This students is already exist'}
    Students[students_id] = student
    return Students[students_id]

#put methods
@app.put('/update_student/{students_id}')   
def update_student(students_id: int, student:Update_Student):
    if students_id not in Students:
        return {"Error": "Student does not exist"}
    if student.name != None:
        Students[students_id].name = student.name
    if student.age != None:
        Students[students_id].age = student.age
    if student.degree != None:
        Students[students_id].degree = student.degree        

    return Students[students_id]  

#delet method
@app.delete('/delete-student/{students_id}')
def delete_students(students_id:int): 
    if students_id not in Students:
        return {"Error":"Student does not found"}
    del Students[students_id]
    return {"Message":"Student deleted successfully!"}