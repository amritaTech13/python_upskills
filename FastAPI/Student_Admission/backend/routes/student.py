from fastapi import FastAPI,APIRouter, Depends, HTTPException
from sqlalchemy.orm import session
from database import sessionLocal , Base
from  models import Student, Course
# from schema import Add_Student, Add_Course, Student_response, course_response
import schema

router = APIRouter()

def get_db():
    db = sessionLocal()
    try:
        yield db   
    finally:
        db.close()


@router.post('/Students', response_model= schema.Student_response)
def create_student(student: schema.Add_Student, db : session = Depends(get_db)):
    std_email = db.query(Student).filter(Student.email == student.email).first()

    if std_email:
        raise HTTPException(status_code=401, detail='Students already enrolled')
    
    new_Student = Student(**student.dict())
    db.add(new_Student)
    db.commit()
    db.refresh(new_Student)
    return new_Student

@router.get('/All_Students', response_model=list[schema.Student_response])
def all_students(db:session = Depends(get_db)):
    return db.query(Student).all()