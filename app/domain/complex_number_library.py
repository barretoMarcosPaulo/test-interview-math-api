from typing import List

from app.domain.interfaces import NumbersInterface, NumberInterface


class Number(NumberInterface):
    def sum(self, a: int, b: int) -> int:
        return a + b

    def divide(self, a: int, b: int) -> float:
        if b == 0:
            return b
        return round(a / b, 2)


class Numbers(NumbersInterface):
    def __init__(self):
        self.number = Number()

    def sum(self, numbers: List[int]) -> int:
        result = 0
        for num in numbers:
            result = self.number.sum(result, num)
        return result

    def average(self, numbers: List[int]) -> float:
        if len(numbers) == 0:
            return 0.0
        total = self.sum(numbers)
        return self.number.divide(total, len(numbers))
