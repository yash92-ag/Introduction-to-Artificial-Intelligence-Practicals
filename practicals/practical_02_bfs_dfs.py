"""
Practical 2: Implementing BFS and DFS

Aim:
    To represent a graph in Python and implement Breadth-First Search (BFS)
    and Depth-First Search (DFS) traversal algorithms.

How to run:
    python practicals/practical_02_bfs_dfs.py
"""

from collections import deque

# ---------------------------------------------------------------
# STEP 1: Represent the city map as a graph (adjacency list)
# Each key is a place, and its value is the list of places next to it.
# ---------------------------------------------------------------
graph = {
    "Central": ["North", "West"],
    "North": ["Central", "NorthEast", "East"],
    "West": ["Central", "SouthWest"],
    "NorthEast": ["North"],
    "East": ["North", "SouthEast"],
    "SouthWest": ["West"],
    "SouthEast": ["East"]
}

# STEP 2: Print every node with its neighbours
for node, neighbors in graph.items():
    print(f"{node} -> {neighbors}")


# ---------------------------------------------------------------
# STEP 3: Breadth-First Search (BFS)
# Visits nodes level by level using a FIFO queue.
# ---------------------------------------------------------------
def bfs(graph, start):
    visited = set([start])      # nodes we have already seen
    queue = deque([start])      # nodes waiting to be visited
    order = []                  # the order in which we visit nodes

    while queue:
        node = queue.popleft()  # take the first node in the queue
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order


bfs_order = bfs(graph, "Central")
print("BFS traversal order:", bfs_order)


# ---------------------------------------------------------------
# STEP 4: Depth-First Search (DFS) using recursion
# Goes as deep as possible along one branch before backtracking.
# ---------------------------------------------------------------
def dfs(graph, start, visited=None, order=None):
    if visited is None:
        visited = set()
    if order is None:
        order = []

    visited.add(start)
    order.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, order)
    return order


dfs_order = dfs(graph, "Central")
print("DFS traversal order:", dfs_order)


# ---------------------------------------------------------------
# STEP 5: BFS path finding (shortest route between two nodes)
# The queue stores whole paths instead of single nodes.
# ---------------------------------------------------------------
def bfs_path(graph, start, goal):
    queue = deque([[start]])
    visited = set([start])

    while queue:
        path = queue.popleft()
        node = path[-1]             # last node of the current path
        if node == goal:
            return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    return None                     # no path exists


path = bfs_path(graph, "Central", "SouthEast")
print("Path from Central to SouthEast:", " -> ".join(path))

# ---------------------------------------------------------------
# STEP 6: Comparison of BFS vs DFS
# ---------------------------------------------------------------
# | Aspect          | BFS                          | DFS                          |
# |-----------------|------------------------------|------------------------------|
# | Traversal style | Level by level               | Deep along one branch first  |
# | Data structure  | FIFO queue (deque)           | Stack / recursion            |
# | Shortest path   | Guarantees fewest edges      | Does not guarantee           |
# | Memory          | O(b^d)                       | O(b * m)                     |
