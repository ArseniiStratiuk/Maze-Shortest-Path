# Shortest Path in a Maze

## Project Overview
This repository contains the implementation of an algorithm to find the shortest path in an n x m maze, created as part of a Discrete Math project at the Ukrainian Catholic University (Team 5).

### Input
- A matrix of size `n x m` (where `1 ≤ n, m ≤ 10^4`), provided in a `.csv` file.  
- The matrix format:
  - `0` represents walkable paths.
  - `1` represents walls.

### Output
- An array of tuples `[(a, b), ...]` representing the shortest path from the start to the endpoint.
- Returns `-1` if no path exists.

### Algorithm
The project uses the **Breadth-First Search (BFS)** algorithm for its efficiency in finding the shortest path in an unweighted graph. BFS ensures optimal performance even for large matrices.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/ArseniiStratiuk/Maze-Shortest-Path.git
   ```
