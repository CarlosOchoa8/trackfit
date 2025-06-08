from typing import Dict
from src.crud import PerformanceCalculatorBaseClase
from src.schemas import ExerciseDataBody


class WorkoutProgressionClass(PerformanceCalculatorBaseClase):
    """Calculate progression in workout."""
    def calculate_performance(self, data: ExerciseDataBody):
        """Return workout exercise perormance."""
        load_progress = self._calculate_load_progress(data=data)

        return "Hola"
    def _calculate_load_progress(self, data: ExerciseDataBody) -> Dict:
        """Return dict of progress in load by exercise."""
        print("calculando progreso en cargas")
        exercise_by_date = {
            
        }

        for ex in data.exercises:
            print("====================")
            if exercise_by_date.get(ex.name) is None:
                # exercise_by_date[ex.name] = ex
                print("Lo voy agregar", ex)
            else:
                exercise_by_date[ex.name] = {
                    ""
                }
        return {"Data": "Here"}
