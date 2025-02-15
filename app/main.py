from fastapi import FastAPI
from app.routes import files

# import app.logging_config

app = FastAPI(title="File Management")

# app.include_router(files.router, prefix="/files", tags=["files"])

@app.get("/")
async def root():
    return {"message": "Welcome to your customizable file management solution"}