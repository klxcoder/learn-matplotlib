import matplotlib.pyplot as plt
import random

def generate_random_color():
    return [random.random() for _ in range(3)]  # RGB color (with scale 1, not scale 255)

def main():
    # Create a 3x3 grid of subplots
    fig, axes = plt.subplots(3, 3)

    def on_click(event): # type: ignore
        if event.inaxes:
            ax = event.inaxes
            col = ax.colNum
            row = ax.rowNum

            if 0 <= row < 3 and 0 <= col < 3:
                new_color = generate_random_color()
                ax.set_facecolor(new_color)
                fig.canvas.draw()

    # Initialize each square with a random color
    for i in range(3):
        for j in range(3):
            ax = axes[i, j]
            ax.set_xticks([])
            ax.set_yticks([])
            ax.set_facecolor(generate_random_color())
            ax.rowNum = i  # Store row index for identification
            ax.colNum = j  # Store column index for identification

    # Connect the click event to the handler function
    fig.canvas.mpl_connect('button_press_event', on_click)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()