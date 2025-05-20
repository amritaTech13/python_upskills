from pydantic import BaseModel
from db import engine
from sqlalchemy import String, Integer, Float, Boolean
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase

class Base(DeclarativeBase):
    pass

# SQLAlchemy Models
class UserDB(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_name: Mapped[str] = mapped_column(String(50), nullable=False)
    password: Mapped[str] = mapped_column(String(20), nullable=False)

class BookDB(Base):
    __tablename__ = 'books'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    book_name: Mapped[str] = mapped_column(String(50), nullable=False)
    author: Mapped[str] = mapped_column(String(50), nullable=False)
    edition: Mapped[str] = mapped_column(String(50), nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    is_available: Mapped[bool] = mapped_column(Boolean, default=True)

# Pydantic Models for API
class UserBase(BaseModel):
    user_name: str
    password: str

class User(UserBase):
    id: int
    class Config:
        orm_mode = True

class UserCreate(UserBase):
    pass

class BookBase(BaseModel):
    book_name: str
    author: str
    edition: str
    price: float
    is_available: bool = True

class Book(BookBase):
    id: int
    class Config:
        orm_mode = True

class BookCreate(BookBase):
    pass

def create_tables():
    Base.metadata.create_all(bind=engine)
