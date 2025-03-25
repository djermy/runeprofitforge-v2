from fastapi import APIRouter
from sqlmodel import Session, select

router = APIRouter(
    prefix="/alchemiser_mk2",
    tags=["alchemiser_mk2"],
)

@router.get("/")
async def root():
    return store.grand_exchange_store.get_all()

@router.get("/{item_id}")
async def get_item_by_id(id: int):
    return store.grand_exchange_store.get(id)