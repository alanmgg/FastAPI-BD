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

@router.get("/autores", tags=["Autor"])
def get_autores(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    autores = db_module.crud_autor.get_autores(db, skip=skip, limit=limit)
    return autores

@router.get("/autores/{id_autor}", tags=["Autor"])
def get_autor(id_autor: int, db: Session = Depends(get_db)):
    db_autor = db_module.crud_autor.get_autor(db, id_autor=id_autor)
    if db_autor is None:
        raise HTTPException(status_code=404, detail="Autor not found")
    return db_autor

@router.post("/autores", tags=["Autor"])
async def create_autor(autor: db_module.schemas.Autores, db: Session = Depends(get_db)):
    return db_module.crud_autor.create_autor(db=db, autor=autor)

@router.delete("/autores/{id_autor}", tags=["Autor"], response_model=db_module.schemas.Status)
def delete_autor(back: BackgroundTasks, id_autor: int, db: Session = Depends(get_db)):
    db_autor = db_module.crud_autor.get_autor(db, id_autor=id_autor)
    if db_autor is None:
        raise HTTPException(status_code=404, detail="Autor not found")
    db_module.crud_autor.delete_autor(db=db, id_autor=id_autor)
    return db_module.schemas.Status(message=f"Deleted autor {id_autor}")

@router.put("/autores/{id_autor}", tags=["Autor"], response_model=db_module.schemas.Status)
def update_autor(id_autor: int, autor: db_module.schemas.Autores, db: Session = Depends(get_db)):
    db_autor = db_module.crud_autor.get_autor(db, id_autor=id_autor)
    if db_autor is None:
        raise HTTPException(status_code=404, detail="Autor not found")
    db_module.crud_autor.update_autor(db, id_autor, autor)
    return db_module.schemas.Status(message=f"Updated autor {id_autor}")