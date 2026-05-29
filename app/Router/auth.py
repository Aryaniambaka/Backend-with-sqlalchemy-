from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from fastapi.params import Body
from passlib.context import CryptContext
from pydantic import BaseModel
from typing import Optional,List
from random import randrange
import psycopg2
from .. import models,schema,utlity,database,OAuth2
from sqlalchemy.orm import Session
from ..database import engine,SessionLocal,get_db
router=APIRouter(
    prefix="/jwt",
    tags=['auth']
)
@router.post('/login',response_model=schema.Tokenreturn)
#to get normal input uc:userinput normal json input 
def login(u_c:OAuth2PasswordRequestForm=Depends() ,db:Session=Depends(database.get_db)):
    #only username,password
    user1=db.query(models.User).filter(models.User.email==u_c.username).first()
    if not user1:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credential")
    if not utlity.verify(u_c.password,user1.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credential")
    access_token = OAuth2.create_access_token(data={"user_id":user1.id})
    return {"access_token" : access_token, "token_type":"bearer"}


