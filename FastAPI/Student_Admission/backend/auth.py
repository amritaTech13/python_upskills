from datetime import datetime, timedelta
from jose import JWTError, jwt


SECKERET_KEY = 'solvedthissecretekey'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRY = 30


def create_access_token(data: dict):
    encode_data = data.copy()
    expiry = datetime.utcnow() + (timedelta(minutes=ACCESS_TOKEN_EXPIRY)) 
    encode_data.update({"exp": expiry})
    return jwt.encode(encode_data,SECKERET_KEY,algorithm=ALGORITHM)
    
def decode_access_token(token:str):

   try:
       return jwt.encode(token, SECKERET_KEY, algorithm=ALGORITHM) 
   except JWTError:
       return None 