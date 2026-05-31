# from fastapi.testclient import TestClient
# from app.main import app
# import pytest
# from app.database import Base
# from datetime import datetime, timezone
# from app import schema,config
# from sqlalchemy.ext.declarative import declarative_base
# from app.config import settings
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from app.database import get_db
# SQLALCHEMY_DATABASE_URL = config.settings.test_DB
# engine= create_engine(SQLALCHEMY_DATABASE_URL) #type: ignore
# TestingSessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine) #we are overriding prev dbsession
# Base.metadata.create_all(bind=engine) 

# def override_get_db():
#     db=TestingSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# client = TestClient(app)
# now = datetime.now(timezone.utc).timestamp()

# def test_root():
#     res = client.get("post/sqlalchemy")
#     assert res.status_code == 200
# def test_login():
#     res = client.post("/user/login",json={"email":"userexample2@gmail.com","password":"string"})
#     print(res.json())
#     newuser = schema.UserResponse(**res.json()) #just check if schema is working
#     assert datetime.fromisoformat(res.json().get("created_at")).timestamp() == pytest.approx(now,abs=3)
#     assert res.status_code == 201
# app.dependency_overrides[get_db] = override_get_db