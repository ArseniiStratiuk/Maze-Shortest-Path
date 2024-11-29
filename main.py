"""
Shortest maze path.
"""
import os


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


def get_neighbors(matrix: list[list[int | str]],
                  row: int, column: int) -> list[tuple[int, int]]:
    """
    Get the neighbors of the given row and column in the matrix.

    Returns:
        list[tuple[int, int]]: The neighbors of the given row and column.

    >>> get_neighbors([[1, 1, 1, 1, 1], [1, 0, 0, 1, 1], [1, 0, 1, 0, 1], \
[1, 1, 1, 1, 1], [1, 0, 0, 0, 1]], 1, 1)
    [(2, 1), (1, 2)]
    """
    indices = [(row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1)]

    return ([(row, column) for row, column in indices
             if is_valid(matrix, row, column) and matrix[row][column] in [0, 'F']])


def is_valid(matrix: list[list[int | str]], row: int, column: int) -> bool:
    """
    Check if the given row and column are valid in the matrix.

    Returns:
        bool: True if the row and column are valid, False otherwise.

    >>> is_valid([[1, 1, 1, 1, 1], [1, 0, 0, 1, 1], [1, 0, 1, 0, 1], \
[1, 1, 1, 1, 1], [1, 0, 0, 0, 1]], 1, 1)
    True
    """
    return 0 <= row < len(matrix) and 0 <= column < len(matrix[0])


def find_start(matrix: list[list[int | str]]) -> tuple[int, int]:
    """
    Find the start position in the maze.

    Args:
        matrix (list[list[int | str]]): The maze represented as a matrix.

    Returns:
        tuple[int, int]: The start position.

    >>> maze = [
    ...     [ 0 , 1 , 0 , 0 , 0 ],
    ...     [ 0 , 1 , 0 , 1 , 0 ],
    ...     [ 0 , 0 , 0 , 1 ,'F'],
    ...     ['S', 1 , 1 , 1 , 0 ],
    ...     [ 0 , 0 , 0 , 0 , 0 ],
    ... ]
    >>> find_start(maze)
    (3, 0)
    """
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

    Args:
        matrix (list[list[int | str]]): The maze represented as a matrix.
        start (tuple[int, int]): The start position.

    Returns:
        list[tuple[int, int]]|int: The shortest path in the maze or -1 if
        there is no path.

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
                      matrix: list[list[int | str]]) -> str | None:
    """
    Visualize the results of the shortest path in the maze. Using ascii art
    for the matrices no bigger than 20x20. For the bigger one, just write the
    visualization to a file located in "Visualization" folder within the
    working directory.

    Different colors are used for the path, start, finish, and obstacles.

    Args:
        shortest_path (list[tuple[int, int]]): The shortest path in the maze.
        matrix (list[list[int | str]]): The maze represented as a matrix.

    Returns:
        str|None: The visualization in a string format of the maze with the
        shortest path or None if written to a file.

    >>> maze = [
    ...     [ 0 , 1 , 0 , 0 , 0 ],
    ...     [ 0 , 1 , 0 , 1 , 0 ],
    ...     [ 0 , 0 , 0 , 1 ,'F'],
    ...     ['S', 1 , 1 , 1 , 0 ],
    ...     [ 0 , 0 , 0 , 0 , 0 ],
    ... ]
    >>> start = find_start(maze)
    >>> shortest_path = get_shortest_path(maze, start)
    >>> visualize_results(shortest_path, maze)
    '+---+---+---+---+---+\\n|   | \\x1b[91m#\\x1b[0m |   |   |   |\\n+---+---+---+---+---+\\n\
|   | \\x1b[91m#\\x1b[0m |   | \\x1b[91m#\\x1b[0m |   |\\n+---+---+---+---+---+\\n|   |   |   | \
\\x1b[91m#\\x1b[0m | \\x1b[94mF\\x1b[0m |\\n+---+---+---+---+---+\\n| \\x1b[94mS\\x1b[0m | \
\\x1b[91m#\\x1b[0m | \\x1b[91m#\\x1b[0m | \\x1b[91m#\\x1b[0m | \\x1b[92mX\\x1b[0m |\\n+---+--\
-+---+---+---+\\n| \\x1b[92mX\\x1b[0m | \\x1b[92mX\\x1b[0m | \\x1b[92mX\\x1b[0m | \\x1b[92mX\\\
x1b[0m | \\x1b[92mX\\x1b[0m |\\n+---+---+---+---+---+'
    """
    rows = len(matrix)
    columns = len(matrix[0])
    visualizing_data = []

    for i in range(rows):
        visualizing_data.append('+---' * columns + '+')
        row = []
        for j in range(columns):
            if (i, j) in shortest_path:
                row.append('| X ' if matrix[i][j] == 0 else f'| {matrix[i][j]} ')
            else:
                row.append('|   ' if matrix[i][j] != 1 else '| # ')
        row.append('|')
        visualizing_data.append(''.join(row))
    visualizing_data.append('+---' * columns + '+')

    result = '\n'.join(visualizing_data)

    # Color the path in green; start, finish in blue; obstacles in red.
    result = result.replace('X', '\033[92mX\033[0m')
    result = result.replace('S', '\033[94mS\033[0m')
    result = result.replace('F', '\033[94mF\033[0m')
    result = result.replace('#', '\033[91m#\033[0m')

    if rows <= 20 and columns <= 20:
        return result

    filename = f'{len(shortest_path)}_steps_{rows}x{columns}_matrix.txt'
    if not os.path.exists('Visualization'):
        os.makedirs('Visualization')
    with open(f'Visualization/{filename}', 'w', encoding='utf-8') as file:
        file.write(result)

    return None


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
