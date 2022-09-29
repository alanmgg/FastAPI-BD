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

@router.get("/categorias", tags=["Categoria"])
def get_categorias(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categorias = db_module.crud_categoria.get_categorias(db, skip=skip, limit=limit)
    return categorias

@router.get("/categorias/{id_categoria}", tags=["Categoria"])
def get_categoria(id_categoria: int, db: Session = Depends(get_db)):
    db_categoria = db_module.crud_categoria.get_categoria(db, id_categoria=id_categoria)
    if db_categoria is None:
        raise HTTPException(status_code=404, detail="Categoria not found")
    return db_categoria

@router.post("/categorias", tags=["Categoria"])
async def create_categoria(categoria: db_module.schemas.Categorias, db: Session = Depends(get_db)):
    return db_module.crud_categoria.create_categoria(db=db, categoria=categoria)

@router.delete("/categorias/{id_categoria}", tags=["Categoria"], response_model=db_module.schemas.Status)
def delete_categoria(back: BackgroundTasks, id_categoria: int, db: Session = Depends(get_db)):
    db_categoria = db_module.crud_categoria.get_categoria(db, id_categoria=id_categoria)
    if db_categoria is None:
        raise HTTPException(status_code=404, detail="Categoria not found")
    db_module.crud_categoria.delete_categoria(db=db, id_categoria=id_categoria)
    return db_module.schemas.Status(message=f"Deleted categoria {id_categoria}")

@router.put("/categorias/{id_categoria}", tags=["Categoria"], response_model=db_module.schemas.Status)
def update_categoria(id_categoria: int, categoria: db_module.schemas.Categorias, db: Session = Depends(get_db)):
    db_categoria = db_module.crud_categoria.get_categoria(db, id_categoria=id_categoria)
    if db_categoria is None:
        raise HTTPException(status_code=404, detail="Categoria not found")
    db_module.crud_categoria.update_categoria(db, id_categoria, categoria)
    return db_module.schemas.Status(message=f"Updated categoria {id_categoria}")