import math
from typing import List, Tuple, Callable
from collections import Counter


class CentralTendecies:
    def __init__(self, *args):
        self._args: Tuple = args

    def mean(self) -> float:
        return sum(*self._args) / len(*self._args)

    def median(self) -> float | int:
        if len(self._args) % 2 != 0:
            return sorted(self._args[0])[len(*self._args) // 2]
        return sorted(self._args[0])[len(*self._args) // 2] + self._args[0][len(*self._args) // 2 + 1] / 2

    def mode(self) -> List | int:
        return Counter(*self._args).most_common(1)


class Dispersion:
    """How much data are distance from other"""
    def __init__(self, *args):
        self._args = args

    def amplitude(self) -> int:
        return sorted(*self._args)[-1] - sorted(*self._args)[0]

    def variance(self, mean: Callable) -> float:
        return sum(list(map(lambda x: (x - mean()) ** 2 / (len(*self._args) - 1), *self._args)))

    def standard_deviation(self, mean: Callable) -> float:
        return math.sqrt(self.variance(mean))

    def covariance(self, list_a: List, list_b: List, mean: Callable) -> float:
        """allows you to measure the dispersion of the mean based on two variables"""
        return sum(list(map(lambda x, y: (x - mean()) * (y - mean()), list_a, list_b))) / (len(list_a) - 1)


if __name__ == '__main__':
    # basic description of data
    values = [1, 2, 3, 4, 6, 4, 3, 1, 2]
    valuesB = sorted([1, 2, 3, 4, 6, 4, 3, 1, 2], reverse=True)
    print(len(values))
    print(max(values))
    print(min(values))
    print(sorted(values))

    central_tendencies: CentralTendecies = CentralTendecies(values)
    print(central_tendencies.mean())
    print(central_tendencies.median())
    print(central_tendencies.mode())

    dispersion: Dispersion = Dispersion(values)
    print(dispersion.amplitude())
    print(dispersion.variance(central_tendencies.mean))
    print(dispersion.standard_deviation(central_tendencies.mean))
    print(dispersion.covariance(values, valuesB, central_tendencies.mean))
