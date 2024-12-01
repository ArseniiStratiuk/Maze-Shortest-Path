"""
Shortest maze path.
"""


import argparse

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
    ...    _ = f.write("0,1,0,0,0\\n0,1,0,1,0\\n0,0,0,1,F\\nS,1,1,1,0\\n0,0,0,0,0\\n")
    >>> read_file('matrix1.csv')
    [[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 'F'], ['S', 1, 1, 1, 0], [0, 0, 0, 0, 0]]
    >>> with open("matrix2.csv", "w", encoding="utf-8") as f:
    ...    _ = f.write("0,S,0,0\\n1,1,0,F\\n0,S,0,0\\n")
    >>> read_file('matrix2.csv')
    'Incorrect maze'
    """
    matrix=[]
    found_s_f = False
    count_s_f=0
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
                    count_s_f+=1
                    processed_row.append(part)
                else:
                    return 'Incorrect maze'
            if 'S' in processed_row and 'F' in processed_row:
                found_s_f = True
            matrix.append(processed_row)
    if not found_s_f and count_s_f!=2:
        return 'Incorrect maze'
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

parser = argparse.ArgumentParser(description="Maze shortest path finder.")
parser.add_argument("input_file", help="Path to the .csv file containing the maze.")
args = parser.parse_args()
matrix_maze = read_file(args.input_file)
if matrix_maze == 'Incorrect maze':
    print("Error: Incorrect maze format.")
else:
    start_maze = find_start(matrix_maze)
    shortest_path_maze = get_shortest_path(matrix_maze, start_maze)
    if shortest_path_maze == -1:
        print("There is no path :(")
    else:
        print(f"Shortest path in the maze: {shortest_path_maze}")
        visualization = visualize_results(shortest_path_maze, matrix_maze)
        if visualization:
            print(visualization)
        else:
            print("Maze is to large to visualize. It is saved to 'Visualization' folder.")
