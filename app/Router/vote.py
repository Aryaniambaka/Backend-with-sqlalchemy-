from .. import models,schema,utlity,OAuth2
from fastapi.params import Body
from ..database import engine,SessionLocal,get_db
from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session
router=APIRouter(
    prefix="/vote",
    tags=["vote"]
)

@router.post("/",status_code=status.HTTP_201_CREATED)
def vote(vote: schema.Vote,db: Session = Depends(get_db),get_current_user: int = Depends(OAuth2.get_current_user)):
    do_exists=db.query(models.Post).filter(models.Post.id==vote.post_id).first()
    vote_query=db.query(models.Vote).filter(models.Vote.post_id==vote.post_id).filter(models.Vote.user_id==get_current_user.id) #type: ignore
    found_vote=vote_query.first()
    if do_exists == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="no post with that id")
    if(vote.dir == 1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="already voted")
        new_vote=models.Vote(post_id=vote.post_id,user_id=get_current_user.id)#type: ignore
        db.add(new_vote)
        db.commit()
        return {"message":"voted successfully"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="vote do not exits")
        vote_query.delete(synchronize_session=False)
        db.commit()
        return{"message":"vote deleted"}
    #sql command to join vote and user then get votes in single tab le select post.*,count(votes.post_id) as Vote_Count from post left join votes on post.id  = votes.post_id where post.id = 31 group by post.id