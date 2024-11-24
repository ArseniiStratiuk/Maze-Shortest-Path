# Shortest Path in a Maze

## Project Overview
This repository contains the implementation of an algorithm to find the shortest path in an n x m maze, created as part of a Discrete Math project at the Ukrainian Catholic University (Team 5).

### Input
- A matrix of size `n x m` (where `1 ≤ n, m ≤ 10^4`), provided in a `.csv` file.
- The matrix format:
  - `0` represents walkable paths.
  - `1` represents walls.
  - `S` represents the start position.
  - `E` represents the end position.

### Output
- An array of tuples `[(a, b), ...]` representing the shortest path from the start to the endpoint.
- Returns `-1` if no path exists.

### Algorithm
The project uses the **Breadth-First Search (BFS)** algorithm for its efficiency in finding the shortest path in an unweighted graph. BFS ensures optimal performance even for large matrices.

---

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/ArseniiStratiuk/Maze-Shortest-Path.git
   ```

---

## Code Architecture

### Modules and Functions

#### `read_file(filename: str) -> list[list[int | str]]`
- Reads and parses the `.csv` input file, returning a 2D list representation of the maze.
- **To-Do:** Add help messages for argparse commands.

#### `find_start(filename: str) -> tuple[int, int]`
- Identifies the start position (`S`) in the maze.

#### `get_neighbors(matrix: list[tuple[int, int]], row: int, column: int) -> list[tuple[int, int]]`
- Returns valid neighboring cells for a given cell in the maze.

#### `is_valid() -> bool`
- Validates maze cell.

#### `get_shortest_path(matrix: list[tuple[int, int]], finish: tuple[int, int], start: tuple[int, int]) -> list[tuple[int, int]] | int`
- Implements the **BFS** algorithm to find the shortest path.
- **To-Do:** Add tests, optimize.

#### `visualize_results(shortest_path: list[tuple[int, int]], matrix: list[tuple[int, int]])`
- Visualizes the shortest path on the maze.
- **To-Do:** Develop visualization logic using ASCII art or libraries like `matplotlib`.

---

## To-Do List

1. **Performance Optimization:**
   - Investigate the use of deque for BFS to optimize queue operations.

2. **Visualization:**
   - Implement the `visualize_results` function to understand the output path better.

3. **Documentation:**
   - Add detailed docstrings for all functions.
   - Include a diagram or flowchart for the BFS algorithm.
