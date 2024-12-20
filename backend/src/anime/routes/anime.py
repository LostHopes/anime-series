from fastapi import APIRouter


router = APIRouter(
    prefix="/anime",
    tags=["anime"]
)

@router.get("/")
async def get_all():
    return {"anime": "Jojo"}

@router.get("/{name}")
def get_item(name: str):
    return


@router.post("/")
def add():
    return


@router.put("/{id}")
def update(id: int):
    return


