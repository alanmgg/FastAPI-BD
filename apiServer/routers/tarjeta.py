from typing import List

from fastapi import FastAPI, APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session

from . import db as db_module

router = APIRouter(route_class=db_module.middleware.VerifyToken)

# Dependency
def get_db():
    db = db_module.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/tarjetas", tags=["Tarjeta"])
def get_tarjetas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tarjetas = db_module.crud_tarjeta.get_tarjetas(db, skip=skip, limit=limit)
    return tarjetas

@router.get("/tarjetas/{id_tarjeta}", tags=["Tarjeta"])
def get_tarjeta(id_tarjeta: int, db: Session = Depends(get_db)):
    db_tarjeta = db_module.crud_tarjeta.get_tarjeta(db, id_tarjeta=id_tarjeta)
    if db_tarjeta is None:
        raise HTTPException(status_code=404, detail="Tarjeta not found")
    return db_tarjeta

@router.post("/tarjetas", tags=["Tarjeta"])
async def create_tarjeta(tarjeta: db_module.schemas.Tarjetas, db: Session = Depends(get_db)):
    return db_module.crud_tarjeta.create_tarjeta(db=db, tarjeta=tarjeta)

@router.delete("/tarjetas/{id_tarjeta}", tags=["Tarjeta"], response_model=db_module.schemas.Status)
def delete_tarjeta(back: BackgroundTasks, id_tarjeta: int, db: Session = Depends(get_db)):
    db_tarjeta = db_module.crud_tarjeta.get_tarjeta(db, id_tarjeta=id_tarjeta)
    if db_tarjeta is None:
        raise HTTPException(status_code=404, detail="Tarjeta not found")
    db_module.crud_tarjeta.delete_tarjeta(db=db, id_tarjeta=id_tarjeta)
    return db_module.schemas.Status(message=f"Deleted tarjeta {id_tarjeta}")

@router.put("/tarjetas/{id_tarjeta}", tags=["Tarjeta"], response_model=db_module.schemas.Status)
def update_tarjeta(id_tarjeta: int, tarjeta: db_module.schemas.Tarjetas, db: Session = Depends(get_db)):
    db_tarjeta = db_module.crud_tarjeta.get_tarjeta(db, id_tarjeta=id_tarjeta)
    if db_tarjeta is None:
        raise HTTPException(status_code=404, detail="Tarjeta not found")
    db_module.crud_tarjeta.update_tarjeta(db, id_tarjeta, tarjeta)
    return db_module.schemas.Status(message=f"Updated tarjeta {id_tarjeta}")