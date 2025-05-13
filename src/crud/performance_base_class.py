from abc import ABC, abstractmethod


class PerformanceCalculator(ABC):
    """Performance base class."""

    @abstractmethod
    def calculate_performance(self) -> dict:
        """Calculate performance base."""
