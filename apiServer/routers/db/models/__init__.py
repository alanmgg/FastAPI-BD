from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from ..database import Base

class Cliente(Base):
    __tablename__ = 'cliente'

    id_cliente = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    ap_paterno = Column(String)
    ap_materno = Column(String)
    email = Column(String)
    telefono = Column(Integer)
    direccion = Column(String)
    password = Column(String)

class Autor(Base):
    __tablename__ = 'autor'

    id_autor = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    ap_paterno = Column(String)
    ap_materno = Column(String)
    pais = Column(String)