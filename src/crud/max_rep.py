import math
from typing import Dict

from src.crud.performance_base_class import PerformanceCalculatorBaseClase
from src.schemas import ExerciseDataBody


class MaxRep(PerformanceCalculatorBaseClase):
    """Calculate theorical max 1RM"""
    def calculate_performance(self, data: ExerciseDataBody):
        print("=============================== CALCULANDO 1RM ===============================")
        epley_1rm = self._calculate_1rm_epley(data=data)
        brzycki_1rm = self._calculate_1rm_brzycki(data=data)
        lombardi_1rm = self._calculate_1rm_lombardi(data=data)

    def _calculate_1rm_epley(self, data: ExerciseDataBody) -> Dict:
        """Estimate 1RM based on Epley formula."""
        filtered_data = self._get_filtered_data(data=data)
        epley_1rm = {
            ex: round(data.weight * (1 + data.reps / 30), 2) for ex, data in filtered_data.items()
        }

        return {"epley1rm": epley_1rm}

    def _calculate_1rm_brzycki(self, data: ExerciseDataBody) -> Dict:
        """Estimate 1RM based on Brzycki formula."""
        filtered_data = self._get_filtered_data(data=data)
        brzycki_1rm  = {
            ex: round(data.weight * (36 / (37 - data.reps)), 2) for ex, data in filtered_data.items()
        }

        return {"brzycki1rm": brzycki_1rm}

    def _calculate_1rm_lombardi(self, data: ExerciseDataBody) -> Dict:
        """Estimate 1RM based on Lombardi formula."""
        filtered_data = self._get_filtered_data(data=data)
        lombardi_1rm  = {
            ex: round(data.weight * math.pow(data.reps, .10), 2) for ex, data in filtered_data.items()
        }

        return {"1RM": lombardi_1rm}

    def _get_filtered_data(self, data: ExerciseDataBody) -> Dict[str, int | float]:
        """Return dict of exercises and his max weight lifted data."""
        filtered_data = {}

        for exercise in data.exercises:
            if exercise.name not in filtered_data:
                tmp = None
                for record in exercise.data:
                    if tmp is None:
                        tmp = record
                    if record.weight > tmp.weight and record.date > tmp.date:
                        tmp = record

                filtered_data[exercise.name] = tmp

        return filtered_data
