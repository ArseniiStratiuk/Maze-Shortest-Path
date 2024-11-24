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


def get_shortest_path(matrix: list[list[int | str]],
                      start: tuple[int, int]) -> list[tuple[int, int]] | int:
    """
    Find the shortest path in the maze, starting from the start position,
    implementing the Breadth-First Search algorithm.

    :param matrix: list[list[int | str]], The maze represented as a matrix.
        Walls are represented as 1, empty cells as 0, start position as 'S'
        and finish position as 'F'.
    :param start: tuple[int, int], The start position.
    :return list[tuple[int, int]], The shortest path from the start to the end position,
        represented as a list of coordinates of the path. If there is no path, return -1.

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
    queue = [start]
    visited = set()
    parents = {start: None}
    visited.add(start)

    while queue:
        current = queue.pop(0)

        if matrix[*current] == 'F':
            path = []
            while current:
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
