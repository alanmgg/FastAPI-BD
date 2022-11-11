from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel, EmailStr

class Status(BaseModel):
    message: str

class Autores(BaseModel):
    id_autor: Optional[int]
    nombre: str
    ap_paterno: str
    ap_materno: Optional[str]
    pais: str

class Categorias(BaseModel):
    id_categoria: Optional[int]
    nombre: str

class Clientes(BaseModel):
    id_cliente: Optional[int]
    nombre: str
    ap_paterno: str
    ap_materno: str
    email: str
    telefono: int
    direccion: str
    password: str
    role: str
    id_image: int

class Auth(BaseModel):
    email: str
    password: str

class Compras(BaseModel):
    id_compra: Optional[int]
    fecha: datetime
    precio: int
    cantidad: int
    id_libro: int
    id_cliente: int

class Editoriales(BaseModel):
    id_editorial: Optional[int]
    pais: str
    nombre: str

class Images(BaseModel):
    id_image: Optional[int]
    path: str

class Libros(BaseModel):
    id_libro: Optional[int]
    num_paginas: int
    anio: int
    isbn_10: int
    isbn_13: int
    nombre: str
    estado: str
    resenia: str
    precio: int
    stock: int
    id_autor: int
    id_editorial: int
    id_categoria: int
    id_image: int

class Tarjetas(BaseModel):
    id_tarjeta: Optional[int]
    num_tarjeta: int
    anio: int
    mes: int
    nombre: str
    id_cliente: int