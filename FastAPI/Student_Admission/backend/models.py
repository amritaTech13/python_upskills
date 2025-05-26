from sqlalchemy import Integer , Column, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base


class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String, unique=True, nullable=False)
    admitted = Column(Boolean,default=False)
    course_id = Column(Integer, ForeignKey('courses.id')) #courses name  of tablename
    course = relationship('Course', back_populates='students' )

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    course_name = Column(String, unique=True, index=True)
    total_seats = Column(Integer)

    students = relationship('Student', back_populates='course')

class Admin(Base):
    __tablename__ = 'admins'
    id= Column(Integer, primary_key=True, index=True)    
    username= Column(String, unique=True, nullable=False)
    hashed_password= Column(String(50), nullable=False)