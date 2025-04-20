from pydantic import BaseModel
from enum import Enum

class RoleEnum(str, Enum):
    admin = "admin"
    staff = "staff"
    customer = "customer"

class RoleCreate(BaseModel):
    name: RoleEnum

class RoleUpdate(BaseModel):
    name: RoleEnum

class RoleBase(BaseModel):
    id: int
    name: RoleEnum

    class Config:
        orm_mode = True
