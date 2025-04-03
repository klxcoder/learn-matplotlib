import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import math

def main():
    # Set up the plot
    fig, ax = plt.subplots()


    def onclick(event): # type: ignore
        if event.inaxes == ax:  # Check if the click occurred within the axes
            x, y = event.xdata, event.ydata
            x = math.floor(x)
            y = math.floor(y)

            # Remove all existing text objects in the clicked cell
            for text in ax.texts:
                if math.floor(text.get_position()[0]) == x and math.floor(text.get_position()[1]) == y:
                    text.set_text("O" if text.get_text() == "X" else "X")

            # Get the background color of the figure
            background_color = fig.get_facecolor()

            # Create a new rectangle with the background color to cover the area
            clear_rect = Rectangle((x, y), 1, 1, facecolor=background_color, edgecolor=background_color)

            # Add the clearing rectangle to the axes
            ax.add_patch(clear_rect)

            fig.canvas.draw()  # Redraw the canvas to show the new point

    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3)
    ax.set_aspect('equal')  # Make sure the grid is square
    ax.axis('off')  # Turn off the axis numbers and ticks

    # Draw the horizontal lines
    ax.plot([0, 3], [1, 1], 'k-', linewidth=2)
    ax.plot([0, 3], [2, 2], 'k-', linewidth=2)

    # Draw the vertical lines
    ax.plot([1, 1], [0, 3], 'k-', linewidth=2)
    ax.plot([2, 2], [0, 3], 'k-', linewidth=2)

    # Optional: Add numbers to the cells for reference
    for i in range(3):
        for j in range(3):
            ax.text(i + 0.5, j + 0.5, "X" if (j * 3 + i + 1) % 2 else "O", ha='center', va='center', fontsize=30)

    fig.canvas.mpl_connect('button_press_event', onclick)

    plt.title("Tic-Tac-Toe Board")
    plt.show()

if __name__ == "__main__":
    main()