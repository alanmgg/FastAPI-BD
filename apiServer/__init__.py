from fastapi import FastAPI, Depends, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from . import routers
from . routers import db
import env

db.database.Base.metadata.create_all(bind=db.engine)

description = """
The Books API helps you do things for the proper functioning of a page in books operation 🚀

## Base
You can **know if the API is active**.

## Autor
You will be able to:
* Insert data from **autor** (_implemented_).
* Get data from **autor** (_implemented_).
* Get a single data from **autor** (_implemented_).
* Update a single data of **autor** (_implemented_).
* Delete a single data from **autor** (_implemented_).

## Categoria
You will be able to:
* Insert data from **categoria** (_implemented_).
* Get data from **categoria** (_implemented_).
* Get a single data from **categoria** (_implemented_).
* Update a single data of **categoria** (_implemented_).
* Delete a single data from **categoria** (_implemented_).

## Cliente
You will be able to:
* Insert data from **cliente** (_implemented_).
* Get data from **cliente** (_implemented_).
* Get a single data from **cliente** (_implemented_).
* Update a single data of **cliente** (_implemented_).
* Delete a single data from **cliente** (_implemented_).

## Compra
You will be able to:
* Insert data from **compra** (_implemented_).
* Get data from **compra** (_implemented_).
* Get a single data from **compra** (_implemented_).
* Update a single data of **compra** (_implemented_).
* Delete a single data from **compra** (_implemented_).

## Editorial
You will be able to:
* Insert data from **editorial** (_implemented_).
* Get data from **editorial** (_implemented_).
* Get a single data from **editorial** (_implemented_).
* Update a single data of **editorial** (_implemented_).
* Delete a single data from **editorial** (_implemented_).

## Libro
You will be able to:
* Insert data from **libro** (_implemented_).
* Get data from **libro** (_implemented_).
* Get a single data from **libro** (_implemented_).
* Update a single data of **libro** (_implemented_).
* Delete a single data from **libro** (_implemented_).

## Tarjeta
You will be able to:
* Insert data from **tarjeta** (_implemented_).
* Get data from **tarjeta** (_implemented_).
* Get a single data from **tarjeta** (_implemented_).
* Update a single data of **tarjeta** (_implemented_).
* Delete a single data from **tarjeta** (_implemented_).
"""

app = FastAPI(
    title="Books API",
    description=description,
    version="1.0.0",
    openapi_tags=[
    {
        "name": "Base",
        "description": "Routes to know if the API is active"
    },
    {
        "name": "Autor",
        "description": "Routes to know if the API is active"
    },
    {
        "name": "Categoria",
        "description": "Routes to know if the API is active"
    },
    {
        "name": "Cliente",
        "description": "Routes to know if the API is active"
    },
    {
        "name": "Compra",
        "description": "Routes to know if the API is active"
    },
    {
        "name": "Editorial",
        "description": "Routes to know if the API is active"
    },
    {
        "name": "Libro",
        "description": "Routes to know if the API is active"
    },
    {
        "name": "Tarjeta",
        "description": "Routes to know if the API is active"
    }],
    contact={
        "name": "AFMG",
        "url": "http://alanmg.me/",
        "email": "alanfmorag@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
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
app.include_router(routers.autor.router)
app.include_router(routers.categoria.router)
app.include_router(routers.cliente.router)
app.include_router(routers.compra.router)
app.include_router(routers.editorial.router)
app.include_router(routers.libro.router)
app.include_router(routers.tarjeta.router)

app.mount("/app", StaticFiles(directory=env.APP_DIR, html=True), name="static")