from sqlalchemy.orm import Session

from . import models, schemas
from pprint import pprint

def get_clientes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Cliente).offset(skip).limit(limit).all()

def get_cliente(db: Session, id_cliente: int):
    return db.query(models.Cliente).filter(models.Cliente.id_cliente == id_cliente).first()

def get_client_by_email(db: Session, email: str):
    return db.query(models.Cliente).filter(models.Cliente.email == email).first()

def create_cliente(db: Session, cliente: schemas.Clientes):
    db_cliente = models.Cliente(**cliente.dict())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

def delete_cliente(db: Session, id_cliente: int):
    db.query(models.Cliente).filter(models.Cliente.id_cliente == id_cliente).delete()
    db.commit()
    return

def update_cliente(db: Session, id_cliente: int, cliente: schemas.Clientes):
    db_upd_clientes = models.Cliente(**cliente.dict())
    db_curr_cliente = db.query(models.Cliente).filter(models.Cliente.id_cliente == id_cliente).first()
    if(db_curr_cliente is not None):
        db_curr_cliente.nombre = db_upd_clientes.nombre
        db_curr_cliente.ap_paterno = db_upd_clientes.ap_paterno
        db_curr_cliente.ap_materno = db_upd_clientes.ap_materno
        db_curr_cliente.email = db_upd_clientes.email
        db_curr_cliente.telefono = db_upd_clientes.telefono
        db_curr_cliente.direccion = db_upd_clientes.direccion
        db_curr_cliente.password = db_upd_clientes.password
        db.commit()
        db.refresh(db_curr_cliente)
        return db_curr_cliente