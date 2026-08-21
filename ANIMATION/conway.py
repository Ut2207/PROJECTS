import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# note this isnt mine but a reference code for mistakes i might make
# in the git commit specifically mention this

# Grid size
N = 80

# Random initial state (0 = dead, 1 = alive)
grid = np.random.choice([0, 1], size=(N, N), p=[0.85, 0.15])

fig, ax = plt.subplots()
img = ax.imshow(grid, cmap="binary", interpolation="nearest")
ax.set_title("Conway's Game of Life")
ax.axis("off")


def update(frame):
    global grid

    # Count neighbors using np.roll
    neighbors = (
        np.roll(grid, 1, 0)
        + np.roll(grid, -1, 0)
        + np.roll(grid, 1, 1)
        + np.roll(grid, -1, 1)
        + np.roll(np.roll(grid, 1, 0), 1, 1)
        + np.roll(np.roll(grid, 1, 0), -1, 1)
        + np.roll(np.roll(grid, -1, 0), 1, 1)
        + np.roll(np.roll(grid, -1, 0), -1, 1)
    )

    # Apply Conway rules
    new_grid = ((grid == 1) & ((neighbors == 2) | (neighbors == 3))) | (
        (grid == 0) & (neighbors == 3)
    )

    grid = new_grid.astype(int)
    img.set_data(grid)
    return [img]


ani = FuncAnimation(fig, update, interval=100, blit=True)
plt.show()
