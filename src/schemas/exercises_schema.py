from datetime import datetime
from typing import Any, List

from pydantic import BaseModel


class CalculatePerformanceModel(BaseModel):
    """Response data Model."""
    response: dict


class ExerciseDataModel(BaseModel):
    """Exercise info"""
    date: str | Any | datetime
    weight: str | int
    reps: str | int
    series: str | int
    intensityMeasure: str


class ExerciseData(BaseModel):
    """Exercise info."""
    name: str
    data: List[ExerciseDataModel]


class ExerciseDataBody(BaseModel):
    """Exercise data body request."""
    exercises: List[ExerciseData]
