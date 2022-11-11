from fastapi import FastAPI, Depends, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from . import routers
from . routers import db
import env

db.database.Base.metadata.create_all(bind=db.engine)

description = """
The Bookbay API helps you do things for the proper functioning of a page in the book operation. She will be in charge of running the website [www.bookbay.store](https://www.bookbay.store) 🚀

## Base
We will be able to know if the API is in operation or is stopped through various methods. If so, please contact alanfmorag@gmail.com 📧

## Authentication
With the following routes you can:  
☑️ Generate a **token**.  
☑️ Validate a **token**.

## Autor
With the following routes you can:  
☑️ Insert data from **autor**.  
☑️ Get data from **autor**.  
☑️ Get a single data from **autor**.  
☑️ Update a single data of **autor**.  
☑️ Delete a single data from **autor**.  

## Categoria
With the following routes you can:  
☑️ Insert data from **categoria**.  
☑️ Get data from **categoria**.  
☑️ Get a single data from **categoria**.  
☑️ Update a single data of **categoria**.  
☑️ Delete a single data from **categoria**.  

## Cliente
With the following routes you can:  
☑️ Insert data from **cliente**.  
☑️ Get data from **cliente**.  
☑️ Get a single data from **cliente**.  
☑️ Update a single data of **cliente**.  
☑️ Delete a single data from **cliente**.  

## Compra
With the following routes you can:  
☑️ Insert data from **compra**.  
☑️ Get data from **compra**.  
☑️ Get a single data from **compra**.  
☑️ Update a single data of **compra**.  
☑️ Delete a single data from **compra**.  

## Editorial
With the following routes you can:  
☑️ Insert data from **editorial**.  
☑️ Get data from **editorial**.  
☑️ Get a single data from **editorial**.  
☑️ Update a single data of **editorial**.  
☑️ Delete a single data from **editorial**.  

## Image
With the following routes you can:  
☑️ Upload **profile picture**.  
☑️ Upload **book photo**.  
☑️ Insert data from **image**.  
☑️ Get a single data from **image**.  
☑️ Delete a single data from **image**.  

## Libro
With the following routes you can:  
☑️ Insert data from **libro**.  
☑️ Get data from **libro**.  
☑️ Get a single data from **libro**.  
☑️ Update a single data of **libro**.  
☑️ Delete a single data from **libro**.  

## Tarjeta
With the following routes you can:  
☑️ Insert data from **tarjeta**.  
☑️ Get data from **tarjeta**.  
☑️ Get a single data from **tarjeta**.  
☑️ Update a single data of **tarjeta**.  
☑️ Delete a single data from **tarjeta**.  
"""

openapi_tags = [
    {
        "name": "Base",
        "description": "Routes to know if the API is active"
    },
    {
        "name": "Authentication",
        "description": "Routes containing user authentication"
    },
    {
        "name": "Autor",
        "description": "Routes containing the methods to enter authors to the database"
    },
    {
        "name": "Categoria",
        "description": "Routes containing the methods to enter categories into the database"
    },
    {
        "name": "Cliente",
        "description": "Routes containing the methods to enter clients into the database"
    },
    {
        "name": "Compra",
        "description": "Routes containing the methods to enter purchases into the database"
    },
    {
        "name": "Editorial",
        "description": "Routes containing the methods to enter publishers into the database"
    },
    {
        "name": "Image",
        "description": "Routes containing the methods to upload images to the server"
    },
    {
        "name": "Libro",
        "description": "Routes containing the methods to enter books into the database"
    },
    {
        "name": "Tarjeta",
        "description": "Routes containing the methods to enter cards into the database"
    }
]

app = FastAPI(
    title="Bookbay API",
    root_path="/api/v1",
    description=description,
    version="1.0.1",
    openapi_tags=openapi_tags,
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "AFMG",
        "url": "https://alanmg.me/",
        "email": "alanfmorag@gmail.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://raw.githubusercontent.com/alanmgg/FastAPI-BD/main/LICENSE",
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routers.base.router)
app.include_router(routers.auth.router)
app.include_router(routers.autor.router)
app.include_router(routers.categoria.router)
app.include_router(routers.cliente.router)
app.include_router(routers.compra.router)
app.include_router(routers.editorial.router)
app.include_router(routers.image.router)
app.include_router(routers.libro.router)
app.include_router(routers.tarjeta.router)

app.mount("/app", StaticFiles(directory=env.APP_DIR_WINDOWS, html=True), name="static")
