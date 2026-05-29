from pydantic_settings import BaseSettings# use to set data type of enviromnet variable
class Settings(BaseSettings):
    DB: str #also case insensetive
    SECRET_KEY: str = "demo" #use as default if cant fetch
settings = Settings()#type: ignore
class Config:
    env_file= ".env"