import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Create a figure and an axes
fig, ax = plt.subplots()

# Set the limits for the axes
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.5, 1.5)

# Create an empty line object that will be updated in the animation
line, = ax.plot([], [], lw=2)

# Define the x-axis data (will remain constant)
x = np.linspace(0, 2 * np.pi, 100)

# The animation function: this will be called for each frame
def animate(i): # type: ignore
    # Calculate the y-data based on the frame number (i)
    y = np.sin(x + 2 * np.pi * i / 100)
    # Update the data of the line object
    line.set_data(x, y)
    # Return the updated line object
    return line,

# Create the animation object
# fig: the figure to animate
# animate: the function to call for each frame
# frames: the number of frames in the animation
# interval: delay between frames in milliseconds
# blit: optimize drawing by only redrawing what has changed
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Display the animation
plt.title("Simple Sine Wave Animation")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()

# To save the animation as a GIF (requires Pillow to be installed):
# ani.save('sine_wave.gif', writer='pillow', fps=30)

# To save as an MP4 (requires ffmpeg to be installed):
# ani.save('sine_wave.mp4', writer='ffmpeg', fps=30)