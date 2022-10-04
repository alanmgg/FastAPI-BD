from typing import List

from fastapi import FastAPI, APIRouter, Depends, HTTPException, BackgroundTasks, File, UploadFile, responses
from fastapi.responses import FileResponse, JSONResponse
from sqlalchemy.orm import Session

from os import getcwd, remove
import shutil

from . import db as db_module
import env

router = APIRouter()

# Dependency
def get_db():
    db = db_module.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/upload_images", tags=["Image"], response_model=db_module.schemas.Status)
async def upload_image(image: UploadFile = File(...)):
    if getcwd()[-1] != '/':
        with open(getcwd() + env.IMAGE_DIR_WINDOWS + image.filename, "wb") as myImage:
            content = await image.read()
            myImage.write(content)
            myImage.close()
    else:
        with open(getcwd() + env.IMAGE_DIR + image.filename, "wb") as myImage:
            content = await image.read()
            myImage.write(content)
            myImage.close()

    return db_module.schemas.Status(message=f"Saved image {image.filename}")

@router.post("/images", tags=["Image"])
async def create_image(image: db_module.schemas.Images, db: Session = Depends(get_db)):
    return db_module.crud_image.create_image(db=db, image=image)

@router.get("/images/{id_image}", tags=["Image"])
def get_image(id_image: int, db: Session = Depends(get_db)):
    db_image = db_module.crud_image.get_image(db, id_image=id_image)
    if db_image is None:
        raise HTTPException(status_code=404, detail="Image not found")
    if getcwd()[-1] != '/':
        return FileResponse(getcwd() + '/' + db_image.path)
    else:
        return FileResponse(getcwd() + db_image.path)

@router.delete("/images/{name_image}", tags=["Image"], response_model=db_module.schemas.Status)
def delete_image(name_image: str):
    try:
        if getcwd()[-1] != '/':
            remove(getcwd() + env.IMAGE_DIR_WINDOWS + name_image)
            return db_module.schemas.Status(message=f"Remove image {name_image}")
        else:
            remove(getcwd() + env.IMAGE_DIR + name_image)
            return db_module.schemas.Status(message=f"Remove image {name_image}")
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Image not found")