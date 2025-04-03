import matplotlib.pyplot as plt
import random

fig, ax = plt.subplots()
ax.set_title('Click to Add Points')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# You can plot some initial data if you like
ax.plot([1, 2, 3], [4, 5, 6])

# Create an empty list to store the clicked points
points = []

marker_styles = ['o', '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd', 'D', 'p', 'h', 'H', '*', '8']
colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']  # red, green, blue, cyan, magenta, yellow, black

def onclick(event): # type: ignore
    if event.inaxes == ax:  # Check if the click occurred within the axes
        x, y = event.xdata, event.ydata
        points.append((x, y))

        # Randomly choose a marker style and color
        marker = random.choice(marker_styles)
        color = random.choice(colors)
        style = color + marker  # Combine color and marker
        print(style, x, y)
        ax.plot(x, y, style)

        fig.canvas.draw()  # Redraw the canvas to show the new point

fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()