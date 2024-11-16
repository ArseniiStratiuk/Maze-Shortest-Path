"""
Shortest maze path.
"""


def read_file(filename: str) -> list[list[int | str]]:
    """
    Джія
    """
    ...


def get_neighbors(row: int, column: int) -> list[tuple[int, int]]:
    """
    Богдан
    """
    ...


def is_valid() -> bool:
    """
    Богдан
    """
    ...


def find_start(filename: str) -> tuple[int, int]:
    """
    Finding the start position.

    :param filename: str, The file with the matrix
    :return tuple[int, int]|None, The coordinates of the start position or 
                                None if this position doesn't exist   

    """
    matrix = read_file(filename)
    n = len(matrix)
    for i in range(n):
        m = len(matrix[i])
        for j in range(m):
            if matrix[i][j] == 'S':
                return (i, j)
    return None



def get_shortest_path(matrix: list[tuple[int, int]],
                      start: tuple[int, int]) -> list[tuple[int, int]]:
    """
    Марта, Арсеній
    """
    ...


def visualize_results(shortest_path: list[tuple[int, int]],
                      matrix: list[tuple[int, int]]):
    """
    Віктор
    """
    ...


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())