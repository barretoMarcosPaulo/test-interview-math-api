from abc import ABC, abstractmethod
from typing import List


class NumberInterface(ABC):
    @abstractmethod
    def sum(self, a: int, b: int) -> int:
        pass

    @abstractmethod
    def divide(self, a: int, b: int) -> float:
        pass


class NumbersInterface(ABC):
    @abstractmethod
    def sum(self, numbers: List[int]) -> int:
        pass

    @abstractmethod
    def average(self, numbers: List[int]) -> float:
        pass
