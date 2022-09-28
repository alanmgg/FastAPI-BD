from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel

class Status(BaseModel):
    message: str

class Clientes(BaseModel):
    id_cliente: Optional[int]
    nombre: str
    ap_paterno: str
    ap_materno: str
    email: str
    telefono: int
    direccion: str
    password: str

class Autores(BaseModel):
    id_autor: Optional[int]
    nombre: str
    ap_paterno: str
    ap_materno: str
    pais: str