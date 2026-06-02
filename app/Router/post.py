from .. import models,schema,utlity,OAuth2
from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from fastapi.params import Body
from sqlalchemy.orm import Session
from ..database import engine,SessionLocal,get_db
from typing import Optional,List
from sqlalchemy import func
router = APIRouter(
    prefix="/post",
    tags=['Post']
)
@router.get("/mypost",response_model=List[schema.PostResponse])
def my_post(db: Session=Depends(get_db),get_current_user: int = Depends(OAuth2.get_current_user),Limit: int = 100,skip: int = 0,search : Optional[str] =""):
    k=db.query(models.Post).filter(models.Post.owner_id == get_current_user.id)#type: ignore
    print(Limit)
    return k.filter(models.Post.title.contains(search)).limit(Limit).offset(skip).all()
@router.get("/sqlalchemy",response_model=List[schema.VOTEOUT])
def test_posts(db: Session=Depends(get_db)):
    k=db.query(models.Post).all()
    results=db.query(models.Post,func.count(models.Vote.post_id).label("vote")).join(models.Vote,models.Vote.post_id == models.Post.id,isouter=True).group_by(models.Post.id).all()
    
    return results
@router.post("/new")
def add_posts(post:schema.Postss,db: Session=Depends(get_db),get_current_user: int = Depends(OAuth2.get_current_user)):
    k=models.Post(owner_id=get_current_user.id,**post.model_dump()) #type: ignore
    print(post.model_dump())
    print(get_current_user.id)#type: ignore
    # k=models.Post(title=post.title,published=post.published,context=post.context)
    db.add(k)
    db.commit()
    db.refresh(k)
    return k
@router.get("/lol/{id}",response_model=schema.UserResponse)
def find_post(id:int,db: Session=Depends(get_db)):
    k=db.query(models.Post).filter(models.Post.id == id).first()
    return k
@router.delete("/delete/{id}")
def delete_post(id:int,db: Session=Depends(get_db ),get_current_user: int = Depends(OAuth2.get_current_user)):
    k=db.query(models.Post).filter(models.Post.id == id)
   
   
    if k.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="post do not exits")
    if not k.first().owner_id == get_current_user.id:#type: ignore
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="you cant delete this")
    k.delete(synchronize_session=False)
    db.commit()
    return "done"
@router.put("/update/{id}",status_code=status.HTTP_201_CREATED,response_model=schema.PostResponse)
def update_post(id: int ,post:schema.Postupdate ,db: Session= Depends(get_db),get_current_user: int = Depends(OAuth2.get_current_user)):
    k=db.query(models.Post).filter(models.Post.id == id)
    if not k.first().owner_id == get_current_user.id:#type: ignore
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="you cant delete this")
    k.update(post.model_dump(),synchronize_session=False) #type: ignore
    db.commit()
    return k.first()