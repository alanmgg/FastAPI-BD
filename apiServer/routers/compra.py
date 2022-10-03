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

@router.get("/compras", tags=["Compra"])
def get_compras(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    compras = db_module.crud_compra.get_compras(db, skip=skip, limit=limit)
    return compras

@router.get("/compras/{id_compra}", tags=["Compra"])
def get_compra(id_compra: int, db: Session = Depends(get_db)):
    db_compra = db_module.crud_compra.get_compra(db, id_compra=id_compra)
    if db_compra is None:
        raise HTTPException(status_code=404, detail="Compra not found")
    return db_compra

@router.post("/compras", tags=["Compra"])
async def create_compra(compra: db_module.schemas.Compras, db: Session = Depends(get_db)):
    return db_module.crud_compra.create_compra(db=db, compra=compra)

@router.delete("/compras/{id_compra}", tags=["Compra"], response_model=db_module.schemas.Status)
def delete_compra(back: BackgroundTasks, id_compra: int, db: Session = Depends(get_db)):
    db_compra = db_module.crud_compra.get_compra(db, id_compra=id_compra)
    if db_compra is None:
        raise HTTPException(status_code=404, detail="Compra not found")
    db_module.crud_compra.delete_compra(db=db, id_compra=id_compra)
    return db_module.schemas.Status(message=f"Deleted compra {id_compra}")

@router.put("/compras/{id_compra}", tags=["Compra"], response_model=db_module.schemas.Status)
def update_compra(id_compra: int, compra: db_module.schemas.Compras, db: Session = Depends(get_db)):
    db_compra = db_module.crud_compra.get_compra(db, id_compra=id_compra)
    if db_compra is None:
        raise HTTPException(status_code=404, detail="Compra not found")
    db_module.crud_compra.update_compra(db, id_compra, compra)
    return db_module.schemas.Status(message=f"Updated compra {id_compra}")