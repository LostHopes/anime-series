from fastapi import APIRouter, Depends
from anime.models import Anime, User
from anime.dependencies import SessionDep


router = APIRouter(
    prefix="/anime",
    tags=["anime"]
)

@router.get("/")
async def get_all():
    session: SessionDep
    return {"anime": "Jojo"}

@router.get("/{name}")
def get_item(name: str):
    session: SessionDep
    return


@router.post("/")
def add():
    return


@router.put("/{id}")
def update(id: int):
    return


