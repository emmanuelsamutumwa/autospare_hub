from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from app.database import Base
import enum

# Enum definition for roles
class RoleEnum(enum.Enum):
    admin = "admin"
    staff = "staff"
    customer = "customer"

# Role model
class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Enum(RoleEnum), unique=True, nullable=False)

    def __repr__(self):
        return f"<Role(id={self.id}, name={self.name})>"
