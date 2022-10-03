from sqlalchemy.orm import Session

from . import models, schemas
from pprint import pprint

def get_compras(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Compra).offset(skip).limit(limit).all()

def get_compra(db: Session, id_compra: int):
    return db.query(models.Compra).filter(models.Compra.id_compra == id_compra).first()

def create_compra(db: Session, compra: schemas.Compras):
    db_compra = models.Compra(**compra.dict())
    db.add(db_compra)
    db.commit()
    db.refresh(db_compra)
    return db_compra

def delete_compra(db: Session, id_compra: int):
    db.query(models.Compra).filter(models.Compra.id_compra == id_compra).delete()
    db.commit()
    return

def update_compra(db: Session, id_compra: int, compra: schemas.Compras):
    db_upd_compra = models.Compra(**compra.dict())
    db_curr_compra = db.query(models.Compra).filter(models.Compra.id_compra == id_compra).first()
    if(db_curr_compra is not None):
        db_curr_compra.fecha = db_upd_compra.fecha
        db_curr_compra.precio = db_upd_compra.precio
        db_curr_compra.cantidad = db_upd_compra.cantidad
        db_curr_compra.id_libro = db_upd_compra.id_libro
        db_curr_compra.id_cliente = db_upd_compra.id_cliente
        db.commit()
        db.refresh(db_curr_compra)
        return db_curr_compra