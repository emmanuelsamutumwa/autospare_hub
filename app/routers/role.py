from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, dependencies

router = APIRouter()

@router.post("/roles/", response_model=schemas.RoleBase)
def create_role(role: schemas.RoleCreate, db: Session = Depends(dependencies.get_db)):
    return crud.create_role(db=db, role=role)

@router.get("/roles/", response_model=list[schemas.RoleBase])
def get_roles(skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db)):
    return crud.get_roles(db=db, skip=skip, limit=limit)

@router.get("/roles/{role_id}", response_model=schemas.RoleBase)
def get_role(role_id: int, db: Session = Depends(dependencies.get_db)):
    db_role = crud.get_role_by_id(db=db, role_id=role_id)
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role

@router.put("/roles/{role_id}", response_model=schemas.RoleBase)
def update_role(role_id: int, role: schemas.RoleUpdate, db: Session = Depends(dependencies.get_db)):
    db_role = crud.update_role(db=db, role_id=role_id, role=role)
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role

@router.delete("/roles/{role_id}", response_model=schemas.RoleBase)
def delete_role(role_id: int, db: Session = Depends(dependencies.get_db)):
    db_role = crud.delete_role(db=db, role_id=role_id)
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role