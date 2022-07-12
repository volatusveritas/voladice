from __future__ import annotations
import random


class Result:
    def __init__(self, rolls:list[int]=[]) -> None:
        self._rolls: list[int] = rolls

    def __int__(self) -> int:
        return self.get_total()

    def __add__(self, other: Result) -> Result:
        return Result(self._rolls + other._rolls)

    def get_rolls(self) -> list[int]:
        return self._rolls

    def add_rolls(self, rolls:list[int]) -> None:
        self._rolls.extend(rolls)

    def get_total(self) -> int:
        return sum(self._rolls)

    def filter(self) -> None:
        ...


class Dice:
    def __init__(self, lower_limit: int, upper_limit: int) -> None:
        self._lower_limit: int = lower_limit
        self._upper_limit: int = upper_limit

    def _get_single_roll(self) -> int:
        return random.randint(self._lower_limit, self._upper_limit)

    def roll(self) -> Result:
        return Result([self._get_single_roll()])

    def rollmany(self, amount: int) -> Result:
        return Result([self._get_single_roll() for _ in range(amount)])


D4 = Dice(1, 4)
D6 = Dice(1, 6)
D8 = Dice(1, 8)
D10 = Dice(1, 10)
D12 = Dice(1, 12)
D20 = Dice(1, 20)
D100 = Dice(1, 100)
