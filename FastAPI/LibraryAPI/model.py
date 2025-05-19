from pydantic import BaseModel
from typing import List

class BookBase(BaseModel):
    book_name: str
    author: str
    edition: str 
    price: float

class Book_name(BaseModel):
    book_name: str
class Book(BookBase):
    is_available: bool = False

class EBook(BookBase):
    download_link: str

class BookRequest(BookBase):
    pass

class BookResponse(BookBase):
    is_available: bool = False

class BookReturn(Book_name):
     is_available: bool = False 