import traceback
from typing import Any, Dict, List

from fastapi import APIRouter, Depends, HTTPException, status

from src.crud import MaxRep, PerformanceCalculator, WorkoutProgressionClass
from src.crud.volume_performance import VolumePerformanceCalculator
from src.middlewares import origin_request
from src.schemas import CalculatePerformanceModel, ExerciseDataBody
from src.services.exercisedb import ExerciseRapidApiService

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
        workout_progress = perf_obj.calculate_performance(
            performance_class=WorkoutProgressionClass
        )


        return CalculatePerformanceModel(
            data={
                **volume_performance,
                "rm_performance": _1rm_theorical,
                **workout_progress,
            }
        )
    except Exception as exc:
        print("Hubo un error ==>", exc)
        traceback.print_exc()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"message": "An unexpected error has ocurred."}
        ) from exc


@router.get("/get_exercises",dependencies=[Depends(origin_request)])
def get_exercises(limit: int = 10, offset: int = 0) -> List[Dict[str, Any]]:
    """Return RapidAPIService response.\n
    :param limit: Qty of records to retrieve.\n
    :param offset: Qty of records to ignore.\n
    :return: List of Dict with data of exercises."""
    try:
        api_service = ExerciseRapidApiService()
        response = api_service.get_exercise_list(limit=limit, offset=offset)

        return response

    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"message": "An unexpected error has ocurred."}
        ) from exc


performance_router = router
