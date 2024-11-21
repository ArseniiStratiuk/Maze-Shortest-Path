"""
Shortest maze path.
"""


# def read_file(filename: str) -> list[list[int | str]]:
#     """
#     Джія
#     """
#     ...


def get_neighbors(matrix: list[tuple[int, int]], row: str or int, column: str or int, start: str or int) \
     -> list[tuple[int, int]]:
    """
    Богдан

    >>> get_neighbors([[1, 1, 1, 1, 1], [1, 0, 0, 1, 1], [1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [1, 0, 0, 0, 1]], 1, 1, 0)
    """
    indices = [(row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1)]

    return sorted([(row, column) for row, column in indices if is_valid(matrix, row, column) and
    matrix[row][column] == start])


def is_valid(matrix, row, column) -> bool:
    """
    Богдан
    """
    return row  >= 0 and column >= 0 and row < len(matrix) and column < len(matrix[0])


# def find_start(matrix: list[tuple[int, int]]) -> tuple[int, int]:
#     """
#     Віктор
#     """
#     ...


# def get_shortest_path(matrix: list[tuple[int, int]],
#                       start: tuple[int, int]) -> list[tuple[int, int]]:
#     """
#     Марта, Арсеній
#     """
#     ...


# def visualize_results(shortest_path: list[tuple[int, int]],
#                       matrix: list[tuple[int, int]]):
#     """
#     Віктор
#     """
#     ...

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())