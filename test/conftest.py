from fastapi.testclient import TestClient
from app.main import app
import pytest
from app.database import Base
from datetime import datetime, timezone
from app import schema,config
from sqlalchemy.ext.declarative import declarative_base
from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import get_db
from alembic import command
import pytest
import os
from jose import jwt
from app import schema,config
from .db import client,session
from datetime import datetime, timezone
import pytest
from app.config import settings
SECRET_KEY = settings.SECRET_KEY
now = datetime.now(timezone.utc).timestamp()
#SECRET_KEY = os.environ.get("SECRET_KEY") #always string #use config file as it is reloded
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES=30
@pytest.fixture
def fixture_user(client):
    lol={"email":"userexample222@gmail.com","password":"string"}
    res = client.post("/user/login",json=lol)
    user=res.json()
    user["password"]=lol["password"]
    user["email"]=lol["email"]

    newuser = schema.UserResponse(**res.json()) #just check if schema is working
    assert datetime.fromisoformat(res.json().get("created_at")).timestamp() == pytest.approx(now,abs=3)
    assert res.status_code == 201
    print(res.json())
    return user

   
@pytest.fixture()#scope="module" in all fixture so that they run once
def session():
     #return TestClient(app) its adv version is yield
    #run code before our test
    Base.metadata.drop_all(bind=engine) #first delte prev then new
    Base.metadata.create_all(bind=engine) 

    #yield TestClient(app)
    #run code after our test 
    #Base.metadata.drop_all(bind=engine) 
    db=TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture()
def client(session):
    def override_get_db():
    
        
            yield session
        
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()
    
SQLALCHEMY_DATABASE_URL = config.settings.TEST_DB
engine= create_engine(SQLALCHEMY_DATABASE_URL) #type: ignore
TestingSessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine) #we are overriding prev dbsession


# def override_get_db():
#     db=TestingSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

#client = TestClient(app)
