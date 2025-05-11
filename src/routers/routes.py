from fastapi import APIRouter
from src.endpoints import exercise_router

router = APIRouter()

router.include_router(exercise_router)
