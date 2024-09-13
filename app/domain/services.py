from typing import List
from app.domain.interfaces import NumbersInterface


class MathService:
    def __init__(self, numbers_lib: NumbersInterface):
        self.numbers_lib = numbers_lib

    def sum_numbers(self, numbers: List[int]) -> int:
        return self.numbers_lib.sum(numbers)

    def average_numbers(self, numbers: List[int]) -> float:
        return self.numbers_lib.average(numbers)
