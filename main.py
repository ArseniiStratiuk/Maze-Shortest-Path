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

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())


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
    """
    ...


def visualize_results(shortest_path: list[tuple[int, int]],
                      matrix: list[tuple[int, int]]):
    """
    Віктор
    """
    ...
