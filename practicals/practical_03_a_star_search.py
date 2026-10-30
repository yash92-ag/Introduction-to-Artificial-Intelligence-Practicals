"""
Practical 3: Implementing A* Search

Aim:
    To implement the A* search algorithm using a heuristic function to find
    the optimal path on a grid.

How to run:
    python practicals/practical_03_a_star_search.py
"""

import heapq

# ---------------------------------------------------------------
# STEP 1: Warehouse floor as a 2D grid
# 0 = open cell, 1 = shelving obstacle
# ---------------------------------------------------------------
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

# STEP 2: Start and goal positions (row, column)
start = (0, 0)   # Charging dock
goal = (4, 4)    # Target picking location
print("Start:", start, "| Goal:", goal)
print(f"Grid dimensions: {len(grid)} rows x {len(grid[0])} columns initialized.\n")


# ---------------------------------------------------------------
# STEP 3: Heuristic h(n) = Manhattan distance
# An estimate of how far a cell is from the goal.
# ---------------------------------------------------------------
def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


h_estimate = manhattan(start, goal)
print("Heuristic estimate from start to goal:", h_estimate)


# ---------------------------------------------------------------
# STEP 4: A* search
# f(n) = g(n) + h(n)
#   g(n) = steps taken so far, h(n) = estimated steps remaining
# heapq always gives us the cell with the smallest f(n) first.
# ---------------------------------------------------------------
def a_star(grid, start, goal):
    rows, cols = len(grid), len(grid[0])

    # Each item: (f_score, g_score, current_cell, path_taken)
    open_set = [(manhattan(start, goal), 0, start, [start])]
    visited = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)

        if current == goal:
            return path, g          # goal reached

        if current in visited:
            continue
        visited.add(current)

        r, c = current
        # Move up, down, left, right
        neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for nr, nc in neighbors:
            # Stay inside the grid and avoid obstacles
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                if (nr, nc) not in visited:
                    new_g = g + 1
                    new_f = new_g + manhattan((nr, nc), goal)
                    heapq.heappush(open_set,
                                   (new_f, new_g, (nr, nc), path + [(nr, nc)]))

    return None, float("inf")       # no path found


# STEP 5: Run the search
path, cost = a_star(grid, start, goal)
print("Optimal path:", path)
print("Path cost:", cost)


# ---------------------------------------------------------------
# STEP 6: Display the grid with the path marked
# S = start, G = goal, * = path
# ---------------------------------------------------------------
def print_grid_with_path(grid, path):
    display = [[str(cell) for cell in row] for row in grid]
    for r, c in path:
        if (r, c) == start:
            display[r][c] = "S"
        elif (r, c) == goal:
            display[r][c] = "G"
        else:
            display[r][c] = "*"
    for row in display:
        print(" ".join(row))


print(f"Optimal path found with cost = {cost} steps:\n")
print_grid_with_path(grid, path)
