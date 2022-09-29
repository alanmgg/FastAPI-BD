from sqlalchemy.orm import Session

from . import models, schemas
from pprint import pprint

def get_libros(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Libro).offset(skip).limit(limit).all()

def get_libro(db: Session, id_libro: int):
    return db.query(models.Libro).filter(models.Libro.id_libro == id_libro).first()

def create_libro(db: Session, libro: schemas.Libros):
    db_libro = models.Libro(**libro.dict())
    db.add(db_libro)
    db.commit()
    db.refresh(db_libro)
    return db_libro

def delete_libro(db: Session, id_libro: int):
    db.query(models.Libro).filter(models.Libro.id_libro == id_libro).delete()
    db.commit()
    return

def update_libro(db: Session, id_libro: int, libro: schemas.Libros):
    db_upd_libro = models.Libro(**libro.dict())
    db_curr_libro = db.query(models.Libro).filter(models.Libro.id_libro == id_libro).first()
    if(db_curr_libro is not None):
        db_curr_libro.num_paginas = db_upd_libro.num_paginas
        db_curr_libro.anio = db_upd_libro.anio
        db_curr_libro.isbn = db_upd_libro.isbn
        db_curr_libro.nombre = db_upd_libro.nombre
        db_curr_libro.estado = db_upd_libro.estado
        db_curr_libro.resenia = db_upd_libro.resenia
        db_curr_libro.precio = db_upd_libro.precio
        db_curr_libro.id_autor = db_upd_libro.id_autor
        db_curr_libro.id_editorial = db_upd_libro.id_editorial
        db_curr_libro.id_categoria = db_upd_libro.id_categoria
        db_curr_libro.stock = db_upd_libro.stock
        db.commit()
        db.refresh(db_curr_libro)
        return db_curr_libro