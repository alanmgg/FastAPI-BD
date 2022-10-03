from sqlalchemy.orm import Session

from . import models, schemas
from pprint import pprint

def get_tarjetas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tarjeta).offset(skip).limit(limit).all()

def get_tarjeta(db: Session, id_tarjeta: int):
    return db.query(models.Tarjeta).filter(models.Tarjeta.id_tarjeta == id_tarjeta).first()

def create_tarjeta(db: Session, tarjeta: schemas.Tarjetas):
    db_tarjeta = models.Tarjeta(**tarjeta.dict())
    db.add(db_tarjeta)
    db.commit()
    db.refresh(db_tarjeta)
    return db_tarjeta

def delete_tarjeta(db: Session, id_tarjeta: int):
    db.query(models.Tarjeta).filter(models.Tarjeta.id_tarjeta == id_tarjeta).delete()
    db.commit()
    return

def update_tarjeta(db: Session, id_tarjeta: int, tarjeta: schemas.Tarjetas):
    db_upd_tarjeta = models.Tarjeta(**tarjeta.dict())
    db_curr_tarjeta = db.query(models.Tarjeta).filter(models.Tarjeta.id_tarjeta == id_tarjeta).first()
    if(db_curr_tarjeta is not None):
        db_curr_tarjeta.num_tarjeta = db_upd_tarjeta.num_tarjeta
        db_curr_tarjeta.anio = db_upd_tarjeta.anio
        db_curr_tarjeta.mes = db_upd_tarjeta.mes
        db_curr_tarjeta.nombre = db_upd_tarjeta.nombre
        db_curr_tarjeta.id_cliente = db_upd_tarjeta.id_cliente
        db.commit()
        db.refresh(db_curr_tarjeta)
        return db_curr_tarjeta