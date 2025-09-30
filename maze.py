import random

"""
There are 5 different preconfigured mazes in this file and one random maze.
Each maze will get progressively more difficult.
0's represent empty space.
1's represent walls or barriers.
-1 represents the start of the maze.
2 represents the end of the maze.

Your task for this project: 
    Use one of the search algorithms we learned about to find the shortest possible path through the maze.
    Algorithms should always start with the node of -1 and end with node of 2.

You should have two outputs:
    1. The number of tiles of the shortest path (if there isn't a path return None)
    2. The actual path of the shortest path through the maze
"""

# The first maze configuration for you to get through
maze = [
    [0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, -1, 0, 0, 0, 0, 0, 0, 0, 0],
]

maze1 = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, -1, 1, 1, 1, 2, 1],
]

maze2 = [
    [1, 1, 1, 1, 1, 1, -1, 1],
    [1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [1, 2, 1, 0, 0, 0, 0, 1],
]

maze3 = [
    [1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [1, 2, 1, 0, 0, 0, -1, 1],
]

maze4 = [
    [1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [-1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# For this random maze, only return if there is a possible path through it
# Start and endpoints are made by you
SIDE_LEN = 30 # CONSTANT NUMBER DO NOT CHANGE

maze5 = [
    [random.randint(0, 1) for j in range(SIDE_LEN)] 
    for i in range(SIDE_LEN) 
]

# Shows maze 5 in output log
for i in maze5:
    for j in i:
        print(j, end = " ")
    print()
