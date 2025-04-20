from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: str
    role: Optional[str] = 'staff'  # Default role is 'staff'

class UserCreate(UserBase):
    password: str  # Password to create the user

class UserOut(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True  # Tells Pydantic to treat ORM models like dicts

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    role: Optional[str] = None