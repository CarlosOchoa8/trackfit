from typing import Type, TypeVar

from src.crud.performance_base_class import PerformanceCalculatorBaseClase

PerformanceCalculatorBase = TypeVar("PerformanceCalculatorBase", bound=PerformanceCalculatorBaseClase)


class PerformanceCalculator:
    """Performance Calculator main class"""
    def __init__(self, data: list):
        """Init for data retrieving."""
        self.data = data

    def calculate_performance(self, performance_class: Type[PerformanceCalculatorBase]) -> dict:
        """Instaces and uses the concrete performance calculator class."""
        perf_obj = performance_class()
        perf_res = perf_obj.calculate_performance(data=self.data)
        return perf_res
