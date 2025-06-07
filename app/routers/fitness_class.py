from fastapi import APIRouter
router = APIRouter()

@router.get("/items/")
async def read_items():
    return [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 32.0},
    ]
