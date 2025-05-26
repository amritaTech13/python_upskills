from fastapi import FastAPI, APIRouter, Depends, HTTPException
from database import sessionLocal
from sqlalchemy.orm import session
from models import Admin
import schema
import bcrypt
from auth import create_access_token

router = APIRouter()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()    

@router.post('/admin/signup')
def admin_signup(admin: schema.Admin_create, db:session = Depends(get_db)):
     db_user = db.query(Admin).filter(Admin.username == admin.username).first()
     if db_user:
          raise HTTPException(status_code=401, detail=f'{db_user} already exist ')
     hash_pass = bcrypt.hashpw(admin.password.encode(), bcrypt.gensalt()).decode()
     new_admin = Admin(username=admin.username, hashed_password=hash_pass)  # Fixed: using keyword arguments

     db.add(new_admin)
     db.commit()
     db.refresh(new_admin)
     return {'message': f'Admin {admin.username} is successfully added'}


@router.post('/admin/login')
def login(admin:schema.Admin_login, db:session= Depends(get_db)):
    db_user = db.query(Admin).filter(Admin.username == admin.username).first()
    if not db_user or not bcrypt.checkpw(admin.password.encode(), db_user.hashed_password.encode()):
        raise HTTPException(status_code=401, detail='Invalid username or password')

    token = create_access_token({'sub': db_user.username})
    return {'access_token': token, 'token_type': 'bearer'}