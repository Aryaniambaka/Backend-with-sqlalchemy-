from .. import models,schema,utlity
from fastapi.params import Body
from ..database import engine,SessionLocal,get_db
from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session
router = APIRouter(
    prefix="/user",
    tags=["User"]
)

@router.post("/login", status_code=status.HTTP_201_CREATED,response_model=schema.UserResponse)
def create_user(user1:schema.userinput,db:Session=Depends(get_db)):
    
    hashed_password=utlity.hash(user1.password)
    user1.password=hashed_password
    k=models.User(**user1.model_dump())
    db.add(k)
    db.commit()
    db.refresh(k)
    return k
@router.get("/user/{id}",response_model=schema.UserResponse)
def get_user(id:int,db:Session = Depends(get_db)):
    k=db.query(models.User).filter(models.User.id==id).first()
    return k