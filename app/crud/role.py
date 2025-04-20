from sqlalchemy.orm import Session
from app.models import Role
from app.schemas import RoleCreate, RoleUpdate

def create_role(db: Session, role: RoleCreate):
    db_role = Role(name=role.name)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

def get_roles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Role).offset(skip).limit(limit).all()

def get_role_by_id(db: Session, role_id: int):
    return db.query(Role).filter(Role.id == role_id).first()

def get_role_by_name(db: Session, role_name: str):
    return db.query(Role).filter(Role.name == role_name).first()

def update_role(db: Session, role_id: int, role: RoleUpdate):
    db_role = db.query(Role).filter(Role.id == role_id).first()
    if db_role:
        db_role.name = role.name
        db.commit()
        db.refresh(db_role)
    return db_role

def delete_role(db: Session, role_id: int):
    db_role = db.query(Role).filter(Role.id == role_id).first()
    if db_role:
        db.delete(db_role)
        db.commit()
    return db_role
