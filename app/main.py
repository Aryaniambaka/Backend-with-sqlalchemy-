from app.Router import post,user,auth,vote
from fastapi import FastAPI,Response,status,HTTPException,Depends
from fastapi.params import Body
from passlib.context import CryptContext
from pydantic import BaseModel
from typing import Optional,List
from random import randrange
import psycopg2
from . import models,schema,utlity,config
from sqlalchemy.orm import Session
from .database import engine,SessionLocal,get_db
from fastapi.middleware.cors import CORSMiddleware



#models.Base.metadata.create_all(bind=engine) 
#it stops auto creation
app=FastAPI()
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
origins=["https://www.google.com"]#["*"] public api
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)






