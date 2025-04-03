import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_title('Click to Add Points')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# You can plot some initial data if you like
ax.plot([1, 2, 3], [4, 5, 6])

# Create an empty list to store the clicked points
points = []

def onclick(event): # type: ignore
    if event.inaxes == ax:  # Check if the click occurred within the axes
        x, y = event.xdata, event.ydata
        points.append((x, y))
        ax.plot(x, y, 'ro')  # 'ro' means red circle marker
        fig.canvas.draw()  # Redraw the canvas to show the new point

fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()