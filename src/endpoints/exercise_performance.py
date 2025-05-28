import traceback

from fastapi import APIRouter, HTTPException, status

from src.crud import MaxRep, PerformanceCalculator
from src.crud.volume_performance import VolumePerformanceCalculator
from src.schemas import (CalculatePerformanceModel, ExerciseData,
                         ExerciseDataBody, ExerciseDataModel)

router = APIRouter(prefix="/performance")


@router.post("/calculate", response_model=CalculatePerformanceModel)
def calculate(exercise_data: ExerciseDataBody) -> CalculatePerformanceModel:
    """Principal calculator endpoint."""
    try:
        perf_obj = PerformanceCalculator(data=exercise_data)
        volume_performance = perf_obj.calculate_performance(
            performance_class=VolumePerformanceCalculator
            )
        _1rm_theorical = perf_obj.calculate_performance(
            performance_class=MaxRep
        )

        return CalculatePerformanceModel(
            data={
                **volume_performance,
                "1rm_performance": _1rm_theorical
            }
        )
    except Exception as exc:
        print("Hubo un error =>", exc)
        traceback.print_exc()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"message": "An unexpected error has ocurred."}
        ) from exc



performance_router = router
