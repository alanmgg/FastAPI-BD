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

@router.get("/libros", tags=["Libro"])
def get_libros(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    libros = db_module.crud_libro.get_libros(db, skip=skip, limit=limit)
    return libros

@router.get("/libros/{id_libro}", tags=["Libro"])
def get_libro(id_libro: int, db: Session = Depends(get_db)):
    db_libro = db_module.crud_libro.get_libro(db, id_libro=id_libro)
    if db_libro is None:
        raise HTTPException(status_code=404, detail="Libro not found")
    return db_libro

@router.post("/libros", tags=["Libro"])
async def create_libro(libro: db_module.schemas.Libros, db: Session = Depends(get_db)):
    return db_module.crud_libro.create_libro(db=db, libro=libro)

@router.delete("/libros/{id_libro}", tags=["Libro"], response_model=db_module.schemas.Status)
def delete_autor(back: BackgroundTasks, id_libro: int, db: Session = Depends(get_db)):
    db_libro = db_module.crud_libro.get_libro(db, id_libro=id_libro)
    if db_libro is None:
        raise HTTPException(status_code=404, detail="Libro not found")
    db_module.crud_libro.delete_libro(db=db, id_libro=id_libro)
    return db_module.schemas.Status(message=f"Deleted libro {id_libro}")

@router.put("/libros/{id_libro}", tags=["Libro"], response_model=db_module.schemas.Status)
def update_libro(id_libro: int, libro: db_module.schemas.Libros, db: Session = Depends(get_db)):
    db_libro = db_module.crud_libro.get_libro(db, id_libro=id_libro)
    if db_libro is None:
        raise HTTPException(status_code=404, detail="Libro not found")
    db_module.crud_libro.update_libro(db, id_libro, libro)
    return db_module.schemas.Status(message=f"Updated libro {id_libro}")