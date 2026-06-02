import os#nano ~/.bashrc source ~/.bashrc (here doing by using inbuilt device env variable)
from jose import JWTError,jwt

from datetime import datetime,timedelta,timezone
from fastapi import Depends,status,HTTPException
from fastapi.security import OAuth2PasswordBearer
from . import schema
from .Router import post,user,auth
from fastapi import FastAPI,Response,status,HTTPException,Depends
from fastapi.params import Body
from passlib.context import CryptContext
from pydantic import BaseModel
from typing import Optional,List
from random import randrange
import psycopg2
from . import models,schema,utlity,database
from app.config import settings
from sqlalchemy.orm import Session
from .database import engine,SessionLocal,get_db
#Secret_key,algoritm,expiration time 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/jwt/login')

SECRET_KEY = settings.SECRET_KEY
#SECRET_KEY = os.environ.get("SECRET_KEY") #always string
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES=30
def create_access_token(data: dict):
    to_encode = data.copy()
    expire= datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)#type:ignore
    return encoded_jwt
def verify_access_token(token:str,credential_exception):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])#type:ignore
        id = payload.get("user_id") 
        if id is None:
            raise credential_exception
        token_data = schema.Tokenpayload(id=id)
    except JWTError:
        raise credential_exception
    return token_data
def get_current_user(token: str=Depends(oauth2_scheme),db: Session= Depends(get_db)):
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="could not validate",headers={"WWW-Authenticate":"Bearer"})
    tokenn = verify_access_token(token , credential_exception)
    user = db.query(models.User).filter(models.User.id == tokenn.id).first()
    return user #type: ignore
    