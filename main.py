"""
Shortest maze path.
"""


def read_file(filename: str) -> list[list[int | str]]:
    """
    Reads the matrix from a .csv file and returns a list of rows.
    Converts '1' and '0' to integers, keeps 'S' and 'F' as strings, 
    and returns 'incorrect matrix' for invalid inputs.
    Args:
        file_name (str): .csv file with the matrix.
    Returns:
        list[list[int | str]]: list of rows or 'Incorrect matrix' if invalid inputs are found.
    >>> with open("matrix1.csv", "w", encoding="utf-8") as f:
    ...    _ = f.write("S,0,0,0\\n1,1,0,F\\n0,0,0,0\\n")
    >>> read_file('matrix1.csv')
    [['S', 0, 0, 0], [1, 1, 0, 'F'], [0, 0, 0, 0]]
    >>> with open("matrix2.csv", "w", encoding="utf-8") as f:
    ...    _ = f.write("0,0,0,0\\n1,1,0,F\\n0,0,0,0\\n")
    >>> read_file('matrix2.csv')
    'Incorrect matrix'
    """
    matrix=[]
    start_found = False
    finish_found = False
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            row=line.strip().split(',')
            processed_row = []
            for part in row:
                if part == '1':
                    processed_row.append(1)
                elif part == '0':
                    processed_row.append(0)
                elif part in {'S', 'F'}:
                    processed_row.append(part)
                else:
                    return 'Incorrect matrix'
            if 'S' in processed_row:
                start_found = True
            if 'F' in processed_row:
                finish_found = True
            matrix.append(processed_row)
    if not start_found or not finish_found:
        return 'Incorrect matrix'
    return matrix


def get_neighbors(matrix: list[tuple[int, int]], row: int, column: int) \
     -> list[tuple[int, int]]:
    """
    >>> get_neighbors([[1, 1, 1, 1, 1], [1, 0, 0, 1, 1], [1, 0, 1, 0, 1], \
[1, 1, 1, 1, 1], [1, 0, 0, 0, 1]], 1, 1)
    [(2, 1), (1, 2)]
    """
    indices = [(row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1)]

    return ([(row, column) for row, column in indices if is_valid(matrix, row, column) and
    matrix[row][column] in [0, 'F']])


def is_valid(matrix, row, column) -> bool:
    """
    """
    return row  >= 0 and column >= 0 and row < len(matrix) and column < len(matrix[0])


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

        if matrix[current[0]][current[1]] == 'F':
            path = []
            while current:
                path.append(current)
                current = parents[current]
            return path[::-1]

        for neighbor in get_neighbors(matrix, current[0], current[1]):
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


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
