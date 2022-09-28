from sqlalchemy.orm import Session

from . import models, schemas
from pprint import pprint

def get_autores(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Autor).offset(skip).limit(limit).all()

def get_autor(db: Session, id_autor: int):
    return db.query(models.Autor).filter(models.Autor.id_autor == id_autor).first()

def create_autor(db: Session, autor: schemas.Autores):
    db_autor = models.Autor(**autor.dict())
    db.add(db_autor)
    db.commit()
    db.refresh(db_autor)
    return db_autor

def delete_autor(db: Session, id_autor: int):
    db.query(models.Autor).filter(models.Autor.id_autor == id_autor).delete()
    db.commit()
    return

def update_autor(db: Session, id_autor: int, autor: schemas.Autores):
    db_upd_autor = models.Autor(**autor.dict())
    db_curr_autor = db.query(models.Autor).filter(models.Autor.id_autor == id_autor).first()
    if(db_curr_autor is not None):
        db_curr_autor.nombre = db_upd_autor.nombre
        db_curr_autor.ap_paterno = db_upd_autor.ap_paterno
        db_curr_autor.ap_materno = db_upd_autor.ap_materno
        db_curr_autor.pais = db_upd_autor.pais
        db.commit()
        db.refresh(db_curr_autor)
        return db_curr_autor