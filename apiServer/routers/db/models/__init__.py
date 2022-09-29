from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from ..database import Base

class Autor(Base):
    __tablename__ = 'autor'

    id_autor = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    ap_paterno = Column(String)
    ap_materno = Column(String)
    pais = Column(String)

class Categoria(Base):
    __tablename__ = 'categoria'

    id_categoria = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)

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

class Editorial(Base):
    __tablename__ = 'editorial'

    id_editorial = Column(Integer, primary_key=True, index=True)
    pais = Column(String)
    nombre = Column(String)

class Libro(Base):
    __tablename__ = 'libro'

    id_libro = Column(Integer, primary_key=True, index=True)
    num_paginas = Column(Integer)
    anio = Column(Integer)
    isbn = Column(String)
    nombre = Column(String)
    estado = Column(String)
    resenia = Column(String)
    precio = Column(Integer)
    stock = Column(Integer)
    id_autor = Column(Integer)
    id_editorial = Column(Integer)
    id_categoria = Column(Integer)