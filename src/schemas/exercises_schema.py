from datetime import datetime
from typing import Any, Dict, List

from pydantic import BaseModel, field_validator


class CalculatePerformanceModel(BaseModel):
    """Response data Model."""
    data: Dict
    # response: dict


class ExerciseDataModel(BaseModel):
    """Exercise info"""
    date: str | Any | datetime
    weight: str | int | float
    reps: str | int
    series: str | int
    intensityMeasure: str | int | float

    @field_validator("intensityMeasure")
    @classmethod
    def validate_intensity(cls, value: str) -> str:
        """Validate intensity measure and return type."""
        value = float(value)
        return f"RPE:{value}" if value >= 6 else f"RIR:{value}"


class ExerciseData(BaseModel):
    """Exercise info."""
    name: str
    data: List[ExerciseDataModel]


class ExerciseDataBody(BaseModel):
    """Exercise data body request."""
    exercises: List[ExerciseData]
