from sqlalchemy.orm import Session

from . import models, schemas
from pprint import pprint

def get_editoriales(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Editorial).offset(skip).limit(limit).all()

def get_editorial(db: Session, id_editorial: int):
    return db.query(models.Editorial).filter(models.Editorial.id_editorial == id_editorial).first()

def create_editorial(db: Session, editorial: schemas.Editoriales):
    db_editorial = models.Editorial(**editorial.dict())
    db.add(db_editorial)
    db.commit()
    db.refresh(db_editorial)
    return db_editorial

def delete_editorial(db: Session, id_editorial: int):
    db.query(models.Editorial).filter(models.Editorial.id_editorial == id_editorial).delete()
    db.commit()
    return

def update_editorial(db: Session, id_editorial: int, editorial: schemas.Editoriales):
    db_upd_editorial = models.Editorial(**editorial.dict())
    db_curr_editorial = db.query(models.Editorial).filter(models.Editorial.id_editorial == id_editorial).first()
    if(db_curr_editorial is not None):
        db_curr_editorial.nombre = db_upd_editorial.nombre
        db_curr_editorial.pais = db_upd_editorial.pais
        db.commit()
        db.refresh(db_curr_editorial)
        return db_curr_editorial