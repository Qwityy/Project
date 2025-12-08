from fastapi import APIRouter
from backend.data.navigation import NAVIGATION


router = APIRouter(prefix="/navigation")


@router.get("")
async def read_navigation():
    return NAVIGATION

    