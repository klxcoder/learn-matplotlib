import matplotlib.pyplot as plt
import numpy as np

# Create a simple maze grid (1 = wall, 0 = path)
maze = np.array([
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1]
])

plt.imshow(maze, cmap='gray_r')  # 'gray_r' for white path & black walls
plt.axis('off')  # Optional: removes axis ticks
plt.show()
