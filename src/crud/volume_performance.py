from typing import List, Dict 
from src.crud.performance_base_class import PerformanceCalculatorBaseClase
from src.schemas import ExerciseDataBody

class VolumePerformanceCalculator(PerformanceCalculatorBaseClase):
    """Volume Performance Calculator class."""

    def calculate_performance(self, data: ExerciseDataBody) -> Dict[str, Dict]:
        """Calculate Training Volume performance."""
        volume_total_dict = self._calculate_total_volume(data=data)
        total_session_volume_dict = self._calculate_session_volume(data=data)
        effective_volume_dict = self._calculate_effective_volume(data=data)

        return {
            "volume_performance": {**volume_total_dict, **total_session_volume_dict}
            }

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

    def _calculate_effective_volume(self, data: ExerciseDataBody) -> Dict:
        """Calculate effective volume based on level."""
        effective_series = {}
        for ex in data.exercises:
            if ex.name not in effective_series:
                effective_series[ex.name] = {}

            for data in ex.data:
                intensity_measure, value = data.intensityMeasure.split(":")
                measure_factor = self.__intensity_measure_factor(measure=intensity_measure, value=value)
                effective_series[ex.name] = (data.weight * data.reps * value) * measure_factor
                print(effective_series[ex.name])

    def __intensity_measure_factor(self, measure: str, value: float) -> float:
        """Return factor factor based con intensity measure."""
        value = float(value) // 1
        print("VALOR DE VALUR", value)
        if measure == "RIR":
            if value == 2:
                return .9
            if value == 3:
                return .7
            if value == 4:
                return .5
            if value == 5:
                return .2
            if value == 5:
                return .0
        if measure == "RPE":
            if value == 6:
                return .5
            if value == 7:
                return .7
            if value == 8:
                return .9
            if value >= 9:
                return 1