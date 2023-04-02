#  linear algebra
import math
from typing import List, Tuple


def sub(array: List) -> List:
    return [p - n for p, n in array]


def scalar_multiply(scallar: int, vector: List) -> List:
    return [scallar * v for v in vector]


def dot_product(vector: List) -> int:
    """scallar product"""
    return sum([x * y for x, y in vector])


def distance(vectorA: List, vectorB: List) -> float:
    return sum([(x - y) ** 2 for x, y in zip(vectorA, vectorB)])


def magnitude(vector: List) -> float:
    """Distance w to v"""
    return math.sqrt(sum([x ** 2 for x in vector]))


def read_shape(matrix: List[List]) -> Tuple[int, int]:
    """Read a matrix B and returns number of lines and number of columns"""
    return len(matrix), len(matrix[0]) if matrix else 0


def make_matrix(num_rows: int, num_cols: int) -> List[List]:
    return [[0 for column in range(num_cols)] for row in range(num_cols)]


def identity_matrix(num_rows: int, num_cols: int) -> List[List]:
    return [[0 if line != column else 1 for column in range(num_cols)] for line in range(num_rows)]


if __name__ == '__main__':
    vectorA = [1, 3]
    vectorB = [3, 1]

    # vectorA + vectorB
    print(list(map(sum, zip(vectorA, vectorB))))

    # vectorA - vectorB
    print(sub(list(zip(vectorA, vectorB))))

    print(scalar_multiply(2, vectorB))

    # scallar product (measures the distance that the vector A extends to B)
    print(dot_product(list(zip(vectorA, vectorB))))

    # magnitude
    print(magnitude(vectorA))
    print(magnitude(vectorB))

    # distance
    print(distance(vectorA, vectorB))

    # matrix 2x2
    B = [
        [1, 2],
        [3, 4]
    ]
    print(read_shape(B))
    print(make_matrix(*read_shape(B)))  # 2x2

    # identity matrix
    print(identity_matrix(*read_shape(B)))
