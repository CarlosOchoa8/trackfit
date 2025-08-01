from datetime import date, datetime
from typing import Dict, Any

from src.crud import PerformanceCalculatorBaseClase
from src.schemas import ExerciseDataBody


class WorkoutProgressionClass(PerformanceCalculatorBaseClase):
    """Calculate progression in workout."""

    def calculate_performance(self, data: ExerciseDataBody):
        """Return workout exercise perormance."""
        load_progress = self._calculate_load_progress(data=data)
        # TODO detailed more this response  if are better than above one.
        overload_progress = self._calculate_progressive_overload_index(data=data)

        print("ESTO REGRESO", {**load_progress, **overload_progress}.keys())
        return {**load_progress, **overload_progress}

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
            metric_data = []


            for index, data_key in enumerate(exercise_data_keys):
                has_next = index + 1 < exercise_data_keys_len
                # next_item = exercise_data_keys[index + 1] if has_next else None

                if next_record := exercise_data_keys[index + 1] if has_next else None:
                    data = self.__calculate_progress_between_sessions(
                        prev_session=exercise_data[data_key],
                        prev_date=data_key,
                        next_session=exercise_data[next_record],
                        next_date=next_record
                    )
                    metric_data.append(data)

            exercise_by_name[exercise_name] = metric_data

        return {"overload_progress": exercise_by_name}

    def __calculate_progress_between_sessions(
            self,
            prev_session: Dict[str, Any],
            prev_date: str | datetime,
            next_session: Dict[str, Any],
            next_date: str | datetime,
            ) -> Dict[str, str | float] | Any:
        """Calculate the difference overload and metrics on to differente day sessions for exercise.
        :param prev_session: the older session to being compared to.
        :param prev_date: older session date.
        :param next_session: next session to calculate overload.
        :param next_date: next session date.
        :return: Dict with keys from[date], to[date], metric[dict of calculated metrics between dates]."""
        metrics = {}

        # INTENSITY ABSOLUTE
        prev_abs_int = sum(serie.get("weight") for serie in prev_session) / len(prev_session)
        next_abs_int = sum(serie.get("weight") for serie in next_session) / len(next_session)
        abs_int_diff = next_abs_int - next_abs_int
        abs_int_diff_perc = ((next_abs_int - prev_abs_int) / prev_abs_int) * 100

        # INTENSITY RELATIVE SEE HOW THE INTENSITY MEASURE COMES FROM
        # prev_rel_int = sum(serie.get("intensitymeasure") for serie in prev_session) / len(prev_session)
        # next_rel_int = sum(serie.get("intensitymeasure") for serie in next_session) / len(prev_session)
        # rel_int_diff = prev_rel_int - next_rel_int
        # rel_int_diff = ((next_rel_int - next_rel_int) / prev_rel_int) * 100

        # VOLUMEN
        prev_vol = sum(serie.get("weight") * serie.get("reps") for serie in prev_session)
        next_vol = sum(serie.get("weight") * serie.get("reps") for serie in next_session)
        vol_diff = next_vol - prev_vol
        vol_diff_perc = ((next_vol - prev_vol) / prev_vol) * 100

        # MAX WEIGHT
        prev_weight = max(serie.get("weight") for serie in prev_session)
        next_weight = max(serie.get("weight") for serie in next_session)
        weight_diff = next_weight - prev_weight
        weight_diff_perc = ((next_weight - prev_weight) / prev_weight) * 100

        # SERIE DENSITY
        prev_dens = prev_vol / len(prev_session)
        next_dens = next_vol / len(next_session)
        dens_diff = next_dens - prev_dens
        dens_diff_perc = ((next_dens - prev_dens) / next_dens) * 100

        # TODO add relative intensity
        metrics = {
            "from": prev_date,
            "to": next_date,
            "metrics": {
                "absolute_intensity": {
                    "previous": prev_abs_int,
                    "next": next_abs_int,
                    "weight_diff": abs_int_diff,
                    "percentage_diff": round(abs_int_diff_perc, 2)
                },
                "volume": {
                    "previous": prev_vol,
                    "next": next_vol,
                    "weight_diff": vol_diff,
                    "percentage_diff": vol_diff_perc
                },
                # "relative_intensity" : {
                #     "previous": prev_rel_int,
                #     "next": next_rel_int,
                #     "weight_diff": rel_int_diff,
                #     "percentage_diff": round(abs_int_diff_perc, 2)
                # }
                "weight": {
                    "previous": prev_vol,
                    "next": next_vol,
                    "weight_diff": weight_diff,
                    "percentage_diff": weight_diff_perc
                },
                "density": {
                    "previous": prev_dens,
                    "next": next_dens,
                    "dens_diff": dens_diff,
                    "percentage_diff": dens_diff_perc
                }
            }
        }

        return metrics
