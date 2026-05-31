from pydantic import BaseModel,EmailStr,Field
from typing import Optional,List
from datetime import datetime

class UserResponse(BaseModel):
    id:int
    created_at: datetime
    
    
    
    
    class Config:
        from_attributes=True


class Postss(BaseModel):
    title: str
    context: str
   
    published: bool = True
    rating: Optional[int] = None
class Postupdate(Postss):
    pass
class PostResponse(BaseModel):
    title: str
    context: str
    created_at: datetime
    owner_id:int
    id:int
    owner:UserResponse
    class Config:
        from_attributes=True

class userinput(BaseModel):
    email:EmailStr
    password:str
class Tokenreturn(BaseModel):
    access_token: str
    token_type: str
class Tokenpayload(BaseModel):
    id: Optional[int]=None
class Vote(BaseModel):
    post_id : int
    dir:int = Field(ge=0,le=1)
class VOTEOUT(BaseModel):      
    Post: PostResponse         
    vote: int

    class Config:
        from_attributes = True
    