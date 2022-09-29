from sqlalchemy.orm import Session

from . import models, schemas
from pprint import pprint

def get_categorias(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Categoria).offset(skip).limit(limit).all()

def get_categoria(db: Session, id_categoria: int):
    return db.query(models.Categoria).filter(models.Categoria.id_categoria == id_categoria).first()

def create_categoria(db: Session, categoria: schemas.Categorias):
    db_categoria = models.Categoria(**categoria.dict())
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

def delete_categoria(db: Session, id_categoria: int):
    db.query(models.Categoria).filter(models.Categoria.id_categoria == id_categoria).delete()
    db.commit()
    return

def update_categoria(db: Session, id_categoria: int, categoria: schemas.Categorias):
    db_upd_categoria = models.Categoria(**categoria.dict())
    db_curr_categoria = db.query(models.Categoria).filter(models.Categoria.id_categoria == id_categoria).first()
    if(db_curr_categoria is not None):
        db_curr_categoria.nombre = db_upd_categoria.nombre
        db.commit()
        db.refresh(db_curr_categoria)
        return db_curr_categoria