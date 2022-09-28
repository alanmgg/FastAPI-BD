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

@router.get("/clientes", tags=["Cliente"])
def get_clientes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    clientes = db_module.crud_cliente.get_clientes(db, skip=skip, limit=limit)
    return clientes

@router.get("/clientes/{id_cliente}", tags=["Cliente"])
def get_cliente(id_cliente: int, db: Session = Depends(get_db)):
    db_cliente = db_module.crud_cliente.get_cliente(db, id_cliente=id_cliente)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente not found")
    return db_cliente

@router.post("/clientes", tags=["Cliente"])
async def create_cliente(cliente: db_module.schemas.Clientes, db: Session = Depends(get_db)):
    return db_module.crud_cliente.create_cliente(db=db, cliente=cliente)

@router.delete("/clientes/{id_cliente}", tags=["Cliente"], response_model=db_module.schemas.Status)
def delete_cliente(back: BackgroundTasks, id_cliente: int, db: Session = Depends(get_db)):
    db_cliente = db_module.crud_cliente.get_cliente(db, id_cliente=id_cliente)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente not found")
    db_module.crud_cliente.delete_cliente(db=db, id_cliente=id_cliente)
    return db_module.schemas.Status(message=f"Deleted cliente {id_cliente}")

@router.put("/clientes/{id_cliente}", tags=["Cliente"], response_model=db_module.schemas.Status)
def update_cliente(id_cliente: int, cliente: db_module.schemas.Clientes, db: Session = Depends(get_db)):
    db_cliente = db_module.crud_cliente.get_cliente(db, id_cliente=id_cliente)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente not found")
    db_module.crud_cliente.update_cliente(db, id_cliente, cliente)
    return db_module.schemas.Status(message=f"Updated cliente {id_cliente}")