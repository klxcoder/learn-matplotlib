import matplotlib.pyplot as plt

def main():
    # Set up the plot
    _, ax = plt.subplots()
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

    plt.title("Tic-Tac-Toe Board")
    plt.show()

if __name__ == "__main__":
    main()