import matplotlib.pyplot as plt
import numpy as np
from collections import deque

maze_str = """
###                 #########
#   ###################   # #
# ####                # # # #
# ################### # # # #
#                     # # # #
##################### # # # #
#   ##                # # # #
# # ## ### ## ######### # # #
# #    #   ##B#         # # #
# # ## ################ # # #
### ##             #### # # #
### ############## ## # # # #
###             ##    # # # #
###### ######## ####### # # #
###### ####             #   #
A      ######################
"""

maze = np.array([[1 if char == '#' else 0 for char in line] for line in maze_str.strip().split('\n')])
start = (15, 0)  # 'A'
end = (8, 13)    # 'B'

def bfs(maze, start, end):
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == end:
            return path
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < maze.shape[0] and 0 <= ny < maze.shape[1] and maze[nx, ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))
    return []

path = bfs(maze, start, end)

plt.figure(figsize=(8, 8))
plt.imshow(maze, cmap='gray_r')

if path:
    path_x, path_y = zip(*path)
    plt.plot(path_y, path_x, color='red', linewidth=3)  # Shortest path in red

plt.scatter([start[1], end[1]], [start[0], end[0]], c=['green', 'blue'], s=100)  # Start & end markers
plt.axis('off')
plt.show()
