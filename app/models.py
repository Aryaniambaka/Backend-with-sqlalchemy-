from .database import Base
from sqlalchemy import Column,Integer,String,Boolean,TIMESTAMP,text,ForeignKey
from sqlalchemy.orm import relationship
class User(Base):
    __tablename__ = "user"
    email= Column(String,nullable = False,unique=True)
    password=Column(String,nullable=False)
    id=Column(Integer,primary_key=True,nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
class Post(Base):
    __tablename__= "post"
    id=Column(Integer,primary_key=True,nullable=False)
    title=Column(String,nullable=False)
    context=Column(String,nullable=False)
    published=Column(Boolean,server_default='TRUE',nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    rating=Column(Integer,nullable=True)
    owner_id=Column(Integer,ForeignKey("user.id",ondelete="CASCADE"),nullable=False) #foreign key
    is_media=Column(Boolean,nullable=True)
    owner=relationship("User")#coonect to foreign key auto




class Vote(Base):
    __tablename__ = "votes"
    user_id=Column(Integer, ForeignKey("user.id",ondelete="CASCADE"),primary_key=True)
    post_id = Column(Integer,ForeignKey("post.id",ondelete="CASCADE"),primary_key=True)