from fastapi import APIRouter, Depends


router = APIRouter(
    prefix="/anime",
    tags=["anime"]
)

@router.get("/")
async def get_all():
    return {"anime": "Jojo"}

@router.get("/{id}")
def get_item(id: int):
    return


@router.post("/")
def add():
    return


@router.put("/{id}")
def update(id: int):
    return


