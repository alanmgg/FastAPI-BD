from typing import List

from fastapi import FastAPI, APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session

from . import db as db_module

router = APIRouter()

# Dependency
def get_db():
    db = db_module.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/editoriales", tags=["Editorial"])
def get_editoriales(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    editoriales = db_module.crud_editorial.get_editoriales(db, skip=skip, limit=limit)
    return editoriales

@router.get("/editoriales/{id_editorial}", tags=["Editorial"])
def get_editorial(id_editorial: int, db: Session = Depends(get_db)):
    db_editorial = db_module.crud_editorial.get_editorial(db, id_editorial=id_editorial)
    if db_editorial is None:
        raise HTTPException(status_code=404, detail="Editorial not found")
    return db_editorial

@router.post("/editoriales", tags=["Editorial"])
async def create_editorial(editorial: db_module.schemas.Editoriales, db: Session = Depends(get_db)):
    return db_module.crud_editorial.create_editorial(db=db, editorial=editorial)

@router.delete("/editoriales/{id_editorial}", tags=["Editorial"], response_model=db_module.schemas.Status)
def delete_editorial(back: BackgroundTasks, id_editorial: int, db: Session = Depends(get_db)):
    db_editorial = db_module.crud_editorial.get_editorial(db, id_editorial=id_editorial)
    if db_editorial is None:
        raise HTTPException(status_code=404, detail="Editorial not found")
    db_module.crud_editorial.delete_editorial(db=db, id_editorial=id_editorial)
    return db_module.schemas.Status(message=f"Deleted editorial {id_editorial}")

@router.put("/editoriales/{id_editorial}", tags=["Editorial"], response_model=db_module.schemas.Status)
def update_editorial(id_editorial: int, editorial: db_module.schemas.Editoriales, db: Session = Depends(get_db)):
    db_editorial = db_module.crud_editorial.get_editorial(db, id_editorial=id_editorial)
    if db_editorial is None:
        raise HTTPException(status_code=404, detail="Editorial not found")
    db_module.crud_editorial.update_editorial(db, id_editorial, editorial)
    return db_module.schemas.Status(message=f"Updated editorial {id_editorial}")