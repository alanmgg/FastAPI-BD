from sqlalchemy.orm import Session

from . import models, schemas
from pprint import pprint

def get_pruebas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Prueba).offset(skip).limit(limit).all()

def get_prueba(db: Session, prueba_id: int):
    return db.query(models.Prueba).filter(models.Prueba.prueba_id == prueba_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.name == username).first()

def create_prueba(db: Session, prueba: schemas.Pruebas):
    db_prueba = models.Prueba(**prueba.dict())
    db.add(db_prueba)
    db.commit()
    db.refresh(db_prueba)
    return db_prueba

def delete_prueba(db: Session, prueba_id: int):
    db.query(models.Prueba).filter(models.Prueba.prueba_id == prueba_id).delete()
    db.commit()
    return

def update_prueba(db: Session, prueba_id: int, prueba: schemas.Pruebas):
    db_upd_pruebas = models.Prueba(**prueba.dict())
    db_curr_prueba = db.query(models.Prueba).filter(models.Prueba.prueba_id == prueba_id).first()
    if(db_curr_prueba is not None):
        db_curr_prueba.name = db_upd_pruebas.name
        db_curr_prueba.description = db_upd_pruebas.description
        db.commit()
        db.refresh(db_curr_prueba)
        return db_curr_prueba