from fastapi import APIRouter, Depends


router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/{name}",)
async def get_user(name: str):
    return