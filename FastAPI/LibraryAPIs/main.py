from fastapi import FastAPI, Depends, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from db import engine, sessionLocal
from model import UserDB, BookDB, User, Book, UserCreate, BookCreate, create_tables
from typing import Optional, List
import jwt as PyJWT  # Import as PyJWT to be explicit
from datetime import datetime, timedelta

app = FastAPI()

# JWT configuration
SECURITY_KEY = 'mysecretkey'
ALGORITHM = 'HS256'

oauth_scheme = OAuth2PasswordBearer(tokenUrl='login')

# Dependency to get DB session
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_jwt_token(data: dict, expiry: Optional[timedelta] = None):
    encode_data = data.copy()
    expire = datetime.utcnow() + (expiry or timedelta(hours=1))
    encode_data.update({'exp': expire})
    return PyJWT.encode(encode_data, SECURITY_KEY, algorithm=ALGORITHM)

def decode_jwt_token(token: str):
    try:
        decoded_data = PyJWT.decode(token, SECURITY_KEY, algorithms=[ALGORITHM])
        return decoded_data if decoded_data['exp'] >= datetime.utcnow().timestamp() else None
    except PyJWT.InvalidTokenError:  # Changed to more specific error
        return None    

def get_user_name(token: str = Depends(oauth_scheme), db: Session = Depends(get_db)):
    user_data = decode_jwt_token(token)
    if not user_data:
        raise HTTPException(status_code=401, detail='Invalid or Expired token!')
    user = db.query(UserDB).filter(UserDB.user_name == user_data['sub']).first()
    if not user:
        raise HTTPException(status_code=401, detail='User not found!')
    return user_data['sub']

@app.post('/signup', tags=['Signup'])
def signup(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(UserDB).filter(UserDB.user_name == user.user_name).first()
    if db_user:
        raise HTTPException(status_code=400, detail='Username already exists')
    new_user = UserDB(user_name=user.user_name, password=user.password, email= user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {'message': f'User: {user.user_name} signed up successfully'}

@app.post('/login', tags=['Login'])
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(UserDB).filter(UserDB.user_name == user.user_name).first()
    if not db_user or db_user.password != user.password:
        raise HTTPException(status_code=401, detail='Invalid credentials')
    token = create_jwt_token(data={'sub': user.user_name})
    return {'access_token': token, 'token_type': 'bearer'}

@app.post('/books', tags=['Books'], response_model=Book)
def add_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = BookDB(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.get('/books', tags=['Books'], response_model=List[Book])
def list_books(db: Session = Depends(get_db)):
    return db.query(BookDB).all()

@app.put('/books/{book_name}/borrow', tags=['Books'])
def borrow_book(book_name: str, token: str, db: Session = Depends(get_db)):
    user_name = get_user_name(token, db)
    book = db.query(BookDB).filter(BookDB.book_name == book_name).first()
    if not book:
        raise HTTPException(status_code=404, detail='Book not found')
    if not book.is_available:
        raise HTTPException(status_code=400, detail='Book is not available')
    book.is_available = False
    db.commit()
    return {'message': f'{user_name} borrowed {book_name} book'}

@app.post('/books/{book_name}/return', tags=['Books'])
def return_book(book_name: str, token: str, db: Session = Depends(get_db)):
    user_name = get_user_name(token, db)
    book = db.query(BookDB).filter(BookDB.book_name == book_name).first()
    if not book:
        raise HTTPException(status_code=404, detail='Book not found')
    if book.is_available:
        raise HTTPException(status_code=400, detail='Book is already returned')
    book.is_available = True
    db.commit()
    return {'message': f'{user_name} returned the {book_name} book'}

@app.delete('/delete/{book_name}', tags=['Books'])
def delete_book(book_name: str, token: str, db: Session = Depends(get_db)):
    user_name = get_user_name(token, db)
    found_book = db.query(BookDB).filter(BookDB.book_name == book_name).first() 
    if not found_book:
        raise HTTPException(status_code=404, detail=f'This {book_name} is found in library')
    else:
        db.delete(found_book)
        db.commit()
        return {'message': f'user {user_name} deleted {book_name} book successfully'}
           
# Create database tables
create_tables()
