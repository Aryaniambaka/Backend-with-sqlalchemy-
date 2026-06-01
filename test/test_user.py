import pytest
import os
from jose import jwt
from app import schema,config
from .db import client,session
from datetime import datetime, timezone
import pytest
from app.config import settings
SECRET_KEY = settings.SECRET_KEY
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES=30
now = datetime.now(timezone.utc).timestamp()

def test_root(client): #now if i give access to the session i can access db 
    res = client.get("post/sqlalchemy")
    assert res.status_code == 200
def test_login(client):
    res = client.post("/user/login",json={"email":"userexample222@gmail.com","password":"string"})
    print(res.json())
    newuser = schema.UserResponse(**res.json()) #just check if schema is working
    assert datetime.fromisoformat(res.json().get("created_at")).timestamp() == pytest.approx(now,abs=3)
    assert res.status_code == 201
#app.dependency_overrides[get_db] = override_get_db
def test_login_user(client,fixture_user):#btw client alrady in fixture
    res=client.post("/jwt/login/",data={"username":fixture_user['email'],"password": fixture_user['password']})
    login_res=schema.Tokenreturn(**res.json())
    payload = jwt.decode(login_res.access_token,SECRET_KEY,algorithms=[ALGORITHM])#type:ignore
    id = payload.get("user_id")
    print("LOGIN:", res.status_code, res.json())
    assert id == fixture_user['id']
    assert login_res.token_type == "bearer"
    assert res.status_code == 200