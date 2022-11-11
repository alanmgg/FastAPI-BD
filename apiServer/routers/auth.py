from typing import List

from fastapi import FastAPI, APIRouter, Depends, HTTPException, BackgroundTasks, Header
from sqlalchemy.orm import Session

from . import db as db_module

router = APIRouter()

# Dependency
def get_db():
    db = db_module.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/auth/{email}/{password}", tags=["Authentication"])
def auth(email: str, password: str, db: Session = Depends(get_db)):
    db_cliente = db_module.crud_cliente.get_client_by_email(db, email=email)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Client not found")
    elif db_cliente.password != password:
        raise HTTPException(status_code=404, detail="Wrong email or password")
    return db_module.crud_auth.write_token({ "email": email, "password": password })

@router.post("/verify/token/", tags=["Authentication"])
def verify_token(Authorization: str = Header(None)):
    token = Authorization.split(" ")[1]
    return db_module.crud_auth.validate_token(token, output=True)