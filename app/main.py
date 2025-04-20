from fastapi import FastAPI

from routers import user
from .database import engine, Base

# Import your models so they are registered
# from app import models

app = FastAPI()

# Create DB tables
Base.metadata.create_all(bind=engine)

# Include the user router
app.include_router(user.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to AutoSpare Hub API"}