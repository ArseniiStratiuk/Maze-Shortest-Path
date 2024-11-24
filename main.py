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


def find_start(matrix: list[tuple[int, int]]) -> tuple[int, int]:
    """
    Віктор
    """
    ...


def get_shortest_path(matrix: list[tuple[int, int]],
                      start: tuple[int, int]) -> list[tuple[int, int]]:
    """
    Марта, Арсеній

    find_shortest_path(matrix: list[list[int]], start: tuple[int, int]) -> list[tuple[int, int]]

    Finds the shortest path in a maze represented as a grid, where:
    - 0 represents a passable cell (path),
    - 1 represents a wall (impassable cell),
    - 'S' is the starting point, and
    - 'F' is the ending point.

    :param: matrix, list[list[int]]
        A 2D list representing the maze grid. Each element is either 0, 1, 'S', 'F'.
        
    :param: start, tuple[int, int]
        A tuple representing the (row, column) indices of the starting position in the maze.

    :return: list[tuple[int, int]]
        A list of tuples representing the shortest path from 'S' to 'F'.
        Each tuple is a pair of indices (row, column) representing a step in the path.
        Returns -1 if no path exists.

    Example:
    --------
    >>> maze = [
    ...     [ 0 , 1 , 0 , 0 , 0 ],
    ...     [ 0 , 1 , 0 , 1 , 0 ],
    ...     [ 0 , 0 , 0 , 1 ,'F'],
    ...     ['S', 1 , 1 , 1 , 0 ],
    ...     [ 0 , 0 , 0 , 0 , 0 ],
    ... ]
    >>> start = (3, 0)
    >>> get_shortest_path(maze, start)
    [(3, 0), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (3, 4), (2, 4)]
    >>> len(get_shortest_path(maze, start)) == 8
    True
    """
    def recurtione(node):
        neighbors = get_neighbors(node[0], node[1], matrix)
        for neighbor in neighbors:
            if neighbor in visited:
                continue
            queue.append(neighbor)
            visited.add(neighbor)
            node = queue.pop(0)
            if matrix[neighbor[0]][neighbor[1]] == 'F':
                return [neighbor]
            return [neighbor] + recurtione(neighbor)

    queue = []
    visited = set()
    path = [start] + recurtione(start)
    return path


def visualize_results(shortest_path: list[tuple[int, int]],
                      matrix: list[tuple[int, int]]):
    """
    Віктор
    """
    ...
