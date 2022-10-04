from sqlalchemy.orm import Session

from . import models, schemas
from pprint import pprint

def get_image(db: Session, id_image: int):
    return db.query(models.Image).filter(models.Image.id_image == id_image).first()

def create_image(db: Session, image: schemas.Images):
    db_image = models.Image(**image.dict())
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image