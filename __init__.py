from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from . import routers
import env

app = FastAPI()
app = FastAPI(dependencies=[])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routers.base.router)

app.mount("/app", StaticFiles(directory=env.APP_DIR, html=True), name="static")