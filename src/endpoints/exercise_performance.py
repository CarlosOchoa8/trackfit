from fastapi import APIRouter
from src.schemas.exercises_schema import CalculatePerformanceModel, ExerciseDataModel

router = APIRouter()


@router.post("/calculate", response_model=CalculatePerformanceModel)
def calculate(exercise_data: ExerciseDataModel) -> CalculatePerformanceModel:
    """Principal calculator endpint."""

    data = [
    {
        "exercise": {
            "name": "assisted chest dip (kneeling)",
            "data": [
                {
                    "date": "",
                    "weight": "123123",
                    "reps": "12123",
                    "series": "123123",
                    "intensityMeasure": "@5"
                },
                {
                    "date": "",
                    "weight": "123123",
                    "reps": "12123",
                    "series": "123123",
                    "intensityMeasure": "@5"
                },
                {
                    "date": "",
                    "weight": "123123",
                    "reps": "12123",
                    "series": "123123",
                    "intensityMeasure": "@5"
                },
                {
                    "date": "",
                    "weight": "123123",
                    "reps": "12123",
                    "series": "123123",
                    "intensityMeasure": "@5"
                },
                {
                    "date": "",
                    "weight": "123123",
                    "reps": "12123",
                    "series": "123123",
                    "intensityMeasure": "@5"
                }
            ]
        }
    },
    {
        "exercise": {
            "name": "45° side bend",
            "data": [
                {
                    "date": "",
                    "weight": "12",
                    "reps": "888",
                    "series": "888",
                    "intensityMeasure": "@55"
                },
                {
                    "date": "",
                    "weight": "12",
                    "reps": "888",
                    "series": "888",
                    "intensityMeasure": "@55"
                },
                {
                    "date": "",
                    "weight": "12",
                    "reps": "888",
                    "series": "888",
                    "intensityMeasure": "@55"
                }
            ]
        }
    }
]
    print("DATA QUE RECIBO", exercise_data.data)
    # exercise_data = {
    #     item.get("exercise").get("name"): item.get("exercise").get("data") for item in data
    # }

    for i in exercise_data:
        print("I ->", i)

    return CalculatePerformanceModel(
        response={
            "Mensaje": "Texto"
        }
    )


exercise_router = router
