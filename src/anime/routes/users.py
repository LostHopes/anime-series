from fastapi import APIRouter


router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/{name}",)
async def get_user(name: str):
    return


@router.post("/")
def create_user():
    return


@router.put("/")
def update_user():
    pass