from pydantic import BaseModel
from typing import List


class CalculatePerformanceModel(BaseModel):
    response: dict


class ExerciseDataModel(BaseModel):
    data: List[dict | str]
