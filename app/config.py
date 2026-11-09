from pydantic_settings import BaseSettings, SettingsConfigDict
#from dotenv import find_dotenv, load_dotenv
import os



env_path = os.path.join(os.path.dirname(__file__), ".env")
#load_dotenv(find_dotenv(".env"))



class Settings(BaseSettings):
    database_hostname: str
    database_port: int
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expires_minutes: int

    model_config = SettingsConfigDict(env_file=env_path)
    #model_config = SettingsConfigDict()


settings = Settings()
