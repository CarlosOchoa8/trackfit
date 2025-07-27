from datetime import date, datetime
from typing import Dict, Any

from src.crud import PerformanceCalculatorBaseClase
from src.schemas import ExerciseDataBody


class WorkoutProgressionClass(PerformanceCalculatorBaseClase):
    """Calculate progression in workout."""

    def calculate_performance(self, data: ExerciseDataBody):
        """Return workout exercise perormance."""
        load_progress = self._calculate_load_progress(data=data)
        self._calculate_progressive_overload_index(data=data)

        return load_progress
    def _calculate_load_progress(self, data: ExerciseDataBody) -> Dict:
        """Return dict of progress in load by exercise."""
        ex_load_progress = {}

        for ex in data.exercises:
            if ex_load_progress.get(ex.name) is None:
                ex_load_progress[ex.name] = {}
                for a in ex.data:
                    if a.date not in ex_load_progress[ex.name]:
                        ex_load_progress[ex.name][a.date] = a.weight
                    if a.weight > ex_load_progress[ex.name][a.date]:
                        ex_load_progress[ex.name][a.date] = a.weight
            else:
                print(".")

        for name, data in ex_load_progress.items():
            ordered_dates = sorted(data, reverse=False)
            ordered_data = {date: data[date] for date in ordered_dates}
            ex_load_progress[name].clear()
            ex_load_progress[name].update(ordered_data)

        for name, data in ex_load_progress.items():
            init_weight = list(data.values())[0]
            init_date = list(data.keys())[0]
            final_weight = list(data.values())[-1]
            final_date = list(data.keys())[-1]
            ex_load_progress[name] = {
                "start_date": init_date, 
                "end_date": final_date,
                "progress": {
                    "start_weight": init_weight,
                    "end_weight": final_weight,
                    "weight_diff": final_weight - init_weight,
                    "percentage_progression": f"{round((final_weight - init_weight) / init_weight * 100, 2)}%"
                }
            }

        return {"load_progress": ex_load_progress}

# TODO find the way on how to separate the date between data exercises
    def _calculate_progressive_overload_index(self, data: ExerciseDataBody) -> Dict[str, Any]:
        """Calculate over the time how the overload is.
        :param data: body of data ExerciseDataBody.
        :return: Dictionary with progress over the time."""
        print("Data que estoy recibiendo =>")

        for data in data.exercises:
            print("DATA DE EJERCICIOS =>", data)
