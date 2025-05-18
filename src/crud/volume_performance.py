from typing import List, Dict 
from src.crud.performance_base_class import PerformanceCalculatorBaseClase
from src.schemas import ExerciseDataBody

class VolumePerformanceCalculator(PerformanceCalculatorBaseClase):
    """Volume Performance Calculator class."""

    def calculate_performance(self, data: ExerciseDataBody):
        """Calculate Training Volume performance."""
        volume_total_dict = self._calculate_total_volume(data=data)
        total_session_volume_dict = self._calculate_session_volume(data=data)
        return "Volume Performance"

    def _calculate_total_volume(self, data: List) -> Dict[str, Dict]:
        """Calculate Total Training Volume."""
        print("calcular volumen total.")
        # print(data)
        total_volume_data = {}

        for exercise in data.exercises:
            total_weight = sum(item.weight for item in exercise.data)
            total_reps = sum(item.reps for item in exercise.data)
            total_series = len(exercise.data)

            total_volume_data[exercise.name] = total_weight * total_reps * total_series

        return {
            "total_volume": total_volume_data
            }

    def _calculate_session_volume(self, data: ExerciseDataBody) -> Dict[str, int | Dict]:
        """Return volume calculated and detailed per training session [date]."""
        sessions_volume = {}
        sessions_series = {}
        sessions_exercises_count = {}

        for exercise_data in data.exercises:
            exercise_by_date = {}

            for serie in exercise_data.data:
                date = serie.date
                reps = serie.reps
                weight = serie.weight

                exercise_by_date[date] = True

                serie_volume = weight * reps
                if date in sessions_volume:
                    sessions_volume[date] += serie_volume
                    sessions_series[date] += 1
                else:
                    sessions_volume[date] = serie_volume
                    sessions_series[date] = 1
                    sessions_exercises_count[date] = 0


            for date in exercise_by_date:
                if date in sessions_exercises_count:
                    sessions_exercises_count[date] += 1
        result = {
            "total_sessions_volume": sessions_volume,
            "total_sessions": len(sessions_volume),
            "session_detail": {}
        }

        for date, volume in sessions_volume.items():
            result["session_detail"][date] = {
                "volume": volume,
                "exercises_qty": sessions_exercises_count.get(date),
                "series_count": sessions_series.get(date),
                "average_serie_volume": volume / sessions_series.get(date) if sessions_series.get(date) > 0 else 0
            }

        return {
            "total_session_volume": sessions_volume
        }
