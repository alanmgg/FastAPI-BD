from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from ..database import Base

class Prueba(Base):
    __tablename__ = 'prueba'

    prueba_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)