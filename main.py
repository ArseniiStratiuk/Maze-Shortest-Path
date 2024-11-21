"""
Shortest maze path.
"""


def read_file(filename: str) -> list[list[int | str]]:
    """
    Джія
    """
    ...


def get_neighbors(matrix: list[tuple[int, int]], row: int, column: int) -> list[tuple[int, int]]:
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


def get_shortest_path(matrix: list[tuple[int, int]], finish: tuple[int, int],
                      start: tuple[int, int]) -> list[tuple[int, int]] | int:
    """
    Find the shortest path in the maze, starting from the start position,
    implementing the Breadth-First Search algorithm.

    :param matrix: list[tuple[int, int]], The matrix of the maze, represented
        as a list of coordinates of the possible paths.
    :param finish: tuple[int, int], The end position.
    :param start: tuple[int, int], The start position.
    :return list[tuple[int, int]], The shortest path from the start to the end position,
        represented as a list of coordinates of the path. If there is no path, return -1.

    >>> matrix = read_file('input.csv')
    >>> start = find_start('input.csv')
    TODO: Add tests.
    """
    queue = [start]
    visited = set()
    parents = {}
    parents[start] = None
    visited.add(start)

    while queue:
        current = queue.pop(0)

        if current == finish:
            path = []
            while current is not None:
                path.append(current)
                current = parents[current]
            return path[::-1]

        for neighbor in get_neighbors(matrix, *current):
            if neighbor not in visited:
                visited.add(neighbor)
                parents[neighbor] = current
                queue.append(neighbor)

    return -1


def visualize_results(shortest_path: list[tuple[int, int]],
                      matrix: list[tuple[int, int]]):
    """
    Віктор
    """
    ...


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
