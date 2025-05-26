# routes/course.py

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, APIKeyHeader
from sqlalchemy.orm import Session
from database import sessionLocal
from models import Course
import schema
from auth import decode_access_token

router = APIRouter()
# auth2_schema = OAuth2PasswordBearer(tokenUrl='admin/login')
auth2_schema = APIKeyHeader(name='Authorization')

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
def get_current_admin(token:str = Depends(auth2_schema)):
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail='Invalid expired token!')
    return payload['sub']

@router.post("/courses", response_model=schema.Course_response)
def create_course(course: schema.Add_Course, db: Session = Depends(get_db), admin: str = Depends(get_current_admin)):
    db_course = db.query(Course).filter(Course.course_name == course.course_name).first()
    if db_course:
        raise HTTPException(status_code=400, detail="Course already exists")
    
    new_course = Course(**course.dict())
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course


@router.get("/courses", response_model=list[schema.Course_response])
def get_courses(db: Session = Depends(get_db)):
    return db.query(Course).all()
