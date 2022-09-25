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

@router.get("/pruebas", tags=["Prueba"])
def get_pruebas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pruebas = db_module.crud_prueba.get_pruebas(db, skip=skip, limit=limit)
    return pruebas

@router.get("/pruebas/{prueba_id}", tags=["Prueba"])
def get_prueba(prueba_id: int, db: Session = Depends(get_db)):
    db_prueba = db_module.crud_prueba.get_prueba(db, prueba_id=prueba_id)
    if db_prueba is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_prueba

@router.post("/pruebas", tags=["Prueba"])
async def create_prueba(prueba: db_module.schemas.Pruebas, db: Session = Depends(get_db)):
    return db_module.crud_prueba.create_prueba(db=db, prueba=prueba)

@router.delete("/pruebas/{prueba_id}", tags=["Prueba"], response_model=db_module.schemas.Status)
def delete_prueba(back: BackgroundTasks, prueba_id: int, db: Session = Depends(get_db)):
    db_prueba = db_module.crud_prueba.get_prueba(db, prueba_id=prueba_id)
    if db_prueba is None:
        raise HTTPException(status_code=404, detail="Prueba not found")
    db_module.crud_prueba.delete_prueba(db=db, prueba_id=prueba_id)
    return db_module.schemas.Status(message=f"Deleted prueba {prueba_id}")

@router.put("/pruebas/{prueba_id}", tags=["Prueba"], response_model=db_module.schemas.Status)
def update_prueba(prueba_id: int, prueba: db_module.schemas.Pruebas, db: Session = Depends(get_db)):
    db_prueba = db_module.crud_prueba.get_prueba(db, prueba_id=prueba_id)
    if db_prueba is None:
        raise HTTPException(status_code=404, detail="Prueba not found")
    db_module.crud_prueba.update_prueba(db, prueba_id, prueba)
    return db_module.schemas.Status(message=f"Updated prueba {prueba_id}")