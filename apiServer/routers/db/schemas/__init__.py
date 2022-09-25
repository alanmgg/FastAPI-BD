from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel

class Status(BaseModel):
    message: str

class Pruebas(BaseModel):
    prueba_id: Optional[int]
    name: str
    description: str