from fastapi import FastAPI

from app.routers import user
from app.routers import role
from .database import engine, Base


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(role.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to AutoSpare Hub API"}