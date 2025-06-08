from datetime import datetime, date
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
        exercise_by_date = {}

        for ex in data.exercises:
            if exercise_by_date.get(ex.name) is None:
                exercise_by_date[ex.name] = {}
                for a in ex.data:
                    if a.date not in exercise_by_date[ex.name]:
                        exercise_by_date[ex.name][a.date] = a.weight
                    if a.weight > exercise_by_date[ex.name][a.date]:
                        exercise_by_date[ex.name][a.date] = a.weight
            else:
                print(".")

        for name, data in exercise_by_date.items():
            ordered_dates = sorted(data, reverse=False)
            ordered_data = {date: data[date] for date in ordered_dates}
            exercise_by_date[name].clear()
            exercise_by_date[name].update(ordered_data)

        print("Progresiones =>")
        for name, data in exercise_by_date.items():
            init_weight = list(data.values())[0]
            init_date = list(data.keys())[0]
            final_weight = list(data.values())[-1]
            final_date = list(data.keys())[-1]
            exercise_by_date[name] = {
                "start_date": init_date, 
                "end_date": final_date,
                "progress": {
                    "start_weight": init_weight,
                    "end_weight": final_weight,
                    "weight_diff": final_weight - init_weight,
                    "percentage_progression": f"{round((final_weight - init_weight) / init_weight * 100, 2)}%"
                }
            }

        print("data =>", exercise_by_date)
        return {"Data": "Here"}
