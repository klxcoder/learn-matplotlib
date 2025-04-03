import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Create a figure and an axes
fig, ax = plt.subplots()

# Set the limits for the axes
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Create an initial empty scatter plot
scatter = ax.scatter([], [])

# Number of points
num_points = 50

# Initialize the data arrays
x_data = np.random.rand(num_points) * 10
y_data = np.random.rand(num_points) * 10

# Update function for the animation
def update(frame): # type: ignore
    # Generate new random positions for the points
    new_x = np.random.rand(num_points) * 10
    new_y = np.random.rand(num_points) * 10

    # Update the offsets of the scatter plot
    scatter.set_offsets(np.c_[new_x, new_y])

    # You can also update other properties like color or size here if needed
    # colors = np.random.rand(num_points)
    # scatter.set_array(colors)
    # sizes = np.random.rand(num_points) * 100
    # scatter.set_sizes(sizes)

    return (scatter,)

# Create the animation object
ani = animation.FuncAnimation(fig, update, frames=100, interval=200, blit=True)

# Display the animation
plt.title("Animated Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# To save the animation (optional):
# ani.save('random_scatter.gif', writer='pillow', fps=30)
# ani.save('random_scatter.mp4', writer='ffmpeg', fps=30)