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

        exercise_by_name = {}
        exercise_by_date = {}
        for ex_data in data.exercises:
            exercise_by_name |= {ex_data.name: ex_data.data}

        for ex_name, ex_data in exercise_by_name.items():
            for data in ex_data:

                if exercise_by_date.get(ex_name) is None:
                    exercise_by_date[ex_name] = {data.date: []}

                if data.date not in exercise_by_date.get(ex_name):
                    exercise_by_date[ex_name][data.date] = []

                exercise_by_date[ex_name][data.date].append({
                    "series": data.series,
                    "weight": data.weight,
                    "reps": data.reps,
                    "intensity_measure": data.intensityMeasure,
                    })

        print("KEYS DE MI DICCIONARIO POR FECHA")
        # print(exercise_by_date)

        # Order exercises data by date
        for ex_name in exercise_by_date:
            data_ordered = sorted(exercise_by_date[ex_name].items(),
                             key=lambda x: datetime.strptime(x[0], "%Y-%m-%d"))
            exercise_by_date[ex_name].clear()
            exercise_by_date[ex_name].update(data_ordered)  #type: ignore

        # Iterate from last to new one exercise.
        for exercise_name, exercise_data in exercise_by_date.items():
            exercise_data_keys = list(exercise_data.keys())
            exercise_data_keys_len = len(exercise_data_keys)


            for index, data_key in enumerate(exercise_data_keys):
                has_next = index + 1 < exercise_data_keys_len
                # next_item = exercise_data_keys[index + 1] if has_next else None

                if next_record := exercise_data_keys[index + 1] if has_next else None:
                    data = self.__calculate_progress_between_sessions(
                        prev_session=exercise_data[data_key],
                        next_session=exercise_data[next_record]
                    )

    def __calculate_progress_between_sessions(
            self,
            prev_session: Dict[str, Any],
            next_session: Dict[str, Any]
            ) -> Dict[str, str | float] | Any:
        """Calculate the difference overload on to differente day sessions for exercise."""
        metrics = {}

        # INTENSITY ABSOLUTE
        prev_abs_int = sum(serie.get("weight") for serie in prev_session) / len(prev_session)
        next_abs_int = sum(serie.get("weight") for serie in next_session) / len(next_session)

        # INTENSITY RELATIVE SEE HOW THE INTENSITY MEASURE COMES FROM
        # prev_rel_int = sum(serie.get("intensitymeasure") for serie in prev_session) / len(prev_session)
        # next_rel_int = sum(serie.get("intensitymeasure") for serie in next_session) / len(prev_session)

        # VOLUMEN
        prev_rel_vol = sum(serie.get("weight") * serie.get("reps") for serie in prev_session)
        next_rel_vol = sum(serie.get("weight") * serie.get("reps") for serie in next_session)

        # MAX WEIGHT
        prev_rel_weight = max(serie.get("weight") for serie in prev_session)
        next_rel_weight = max(serie.get("weight") for serie in next_session)

        # SERIE DENSITY
        prev_dens_ser = prev_rel_vol / len(prev_session)
        next_dens_ser = next_rel_vol / len(next_session)

        return {"msg": "ok"}