from fastapi import FastAPI
from database import engin
from models import Base
from routes import student, admin, course

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engin)

app.include_router(student.router, tags=['Students'])
app.include_router(course.router, tags=['Course'])
app.include_router(admin.router, tags=['Admin'])

@app.get('/')
def welcome():
    return {'message': 'Students admission is ready now!'}