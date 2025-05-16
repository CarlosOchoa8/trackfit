from abc import ABC, abstractmethod


class PerformanceCalculatorBaseClase(ABC):
    """Performance base class."""

    @abstractmethod
    def calculate_performance(self, data: list) -> dict:
        """Calculate performance base."""
