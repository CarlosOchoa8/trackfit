from src.crud.performance_base_class import PerformanceCalculatorBaseClase
from typing import TypeVar, Type

PerformanceCalculatorBase = TypeVar("PerformanceCalculatorBase", bound=PerformanceCalculatorBaseClase)


class PerformanceCalculator:
    """Performance Calculator main class"""
    def __init__(self, data: list):
        """Init for data retrieving."""
        self.data = data

    def calculate_performance(self, performance_class: Type[PerformanceCalculatorBase]) -> dict:
        """Instaces and uses the concrete performance calculator class."""
        print("Aqui voy a partir para calcular los colores")
        perf_obj = performance_class()
        perf_res = perf_obj.calculate_performance(data=self.data)
        return perf_res
