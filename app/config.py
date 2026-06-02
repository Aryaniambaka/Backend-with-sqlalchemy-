from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB: str 
    SECRET_KEY: str = "demo" 
    TEST_DB: str

    # Pydantic V2 Modern Configuration Syntax
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings() # type: ignore