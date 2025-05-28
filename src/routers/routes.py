from fastapi import APIRouter
from src.endpoints import performance_router

router = APIRouter()

router.include_router(performance_router)
