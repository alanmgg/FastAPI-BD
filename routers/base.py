from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

router = APIRouter()

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@router.get("/", tags=["Base"])
async def read_root():
    return {"Welcome": "FastAPI Server BD"}


@router.get("/items/{item_id}", tags=["Base"])
async def read_item(item_id: int):
    return {"item_id": item_id}