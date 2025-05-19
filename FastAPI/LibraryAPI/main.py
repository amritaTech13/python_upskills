from fastapi import FastAPI , Depends, HTTPException
from library import Library, Book
from model import BookRequest, BookResponse,EBook, BookReturn
from pydantic import BaseModel
from typing import Optional
import jwt as PyJWT
from datetime import datetime, timedelta

app = FastAPI()
lib = Library()

#JWT configration
SECURITY_KEY = 'mysecretkey'
ALOGRITHM = 'HS256'

user_DB = {
    'Admin':{
        'user_name': 'Admin',
        'password': 'Admin123'
    }    
}

book_DB = [
            {'book_name': 'JavaScript','author': 'Brendan','edition': '2nd Edition','price': 500, 'is_available': True },
            {'book_name': 'Python','author': 'Guido van Rossum','edition': '3rd Edition','price': 200, 'is_available': True },
            {'book_name': 'React','author': 'Jordan Walke','edition': '1st Edition','price': 800, 'is_available': True }
        ]

class User(BaseModel):
    user_name: str
    password: str

class Book(BaseModel):
    book_name: str
    author: str
    edition: str
    price: float
    is_available: bool


def create_jwt_token(data:dict, expiry: Optional[timedelta] = None ):
    encode_data = data.copy()
    expire = datetime.utcnow() + (expiry or timedelta(hours=1))
    encode_data.update({'exp': expire})
    encrypted_data = PyJWT.encode(encode_data, SECURITY_KEY, algorithm=ALOGRITHM)
    return encrypted_data

def decode_jwt_token(token: str):
    try:
        decoded_data = PyJWT.decode(token, SECURITY_KEY, algorithms=[ALOGRITHM])
        return decoded_data if decoded_data['exp'] >= datetime.utcnow().timestamp() else None
    except PyJWT.PyJWTError:
        return None    


def get_userName(token):
    user_data = decode_jwt_token(token)
    if not user_data:
        raise HTTPException(status_code=401, detail='Invalid or Expired time!')
    return user_data['sub']

@app.post('/signup', tags=['Signup'])
def signup(users: User):
        if users.user_name in user_DB :
            raise HTTPException(status_code=401, detail='Username already exist')
        user_DB['user_name'] = {'user_name':users.user_name, 'password': users.password}
        return {'message': f'User: {users.user_name} signed up successfully'}

@app.post('/login', tags=['Login'])
def login(users: User):
        user_get = user_DB.get(users.user_name)
        if not user_get or user_get['password'] != users.password:
            raise HTTPException(status_code=401, detail='Invalid credentials')
        token = create_jwt_token(data={'sub':users.user_name})
        return {'access_token':token, 'token_type':'bearer'}

@app.post('/borrow', tags=['Borrow Books'])
def borrow_books(book_name:str, token:str):
     get_user = get_userName(token)
     for book in book_DB:
          if book['book_name'] == book_name: 
            if book['is_available']:
               book['is_available'] = False
               return {'message': f'{get_user} borrowed {book_name} book'}
          else:
               return{'message': f'{book_name} is not available'}     
     raise HTTPException(status_code=401, detail=f'{book_name} not found')  

@app.post('/return', tags=['Return Books'])
def return_books(book_name:str, token):
     get_userName = get_userName(token)
     for book in book_DB:
          if book['book_name'] == book_name and not book['is_available']:
                  book['is_available'] = True
                  return {'message':f'{get_userName} return {book_name} book'}
          
@app.get('/getBook', tags=['Show Books'])
def get_books():
    return book_DB


