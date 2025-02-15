from pydantic import BaseSettings
class Settings(BaseSettings):
    # Choose Storage backend

    STORAGE_BACKEND: str = "local"

    # local storage settings
    LOCAL_STORAGE_DIR: str = "/tmp/files"

    # AWS S3 Settings 
    S3_BUCKET: str = ''
    AWS_ACCESS_KEY: str = ""
    AWS_SECRET_KEY: str = ""
    
    class Config:
        env_file = ".env"

settings = Settings()
