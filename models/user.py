from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
from sqlalchemy.sql import func

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String, default='staff')  # 'staff' or 'admin'
    created_at = Column(DateTime, server_default=func.now())

    # You can link to Sales or other tables if you want
    sales = relationship("Sale", back_populates="user")  # Example relationship

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"