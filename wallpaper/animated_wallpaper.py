import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import numpy as np

def colorWallpaper(canvas, a, b, side, points=200):
    image = np.zeros((points, points, 3), dtype=np.uint8)

    for i in range(points):
        for j in range(points):
            x = a + i * (side / points)
            y = b + j * (side / points)
            c = int(x ** 2 + y ** 2)
            color = [255, 0, 0] \
                if c % 4 == 0 \
                else [0, 255, 0] \
                if c % 4 == 1 \
                else [0, 0, 255] \
                if c % 4 == 2 \
                else [255, 255, 255]
            image[i, j] = color

    canvas.imshow(image)

# Function to update the plot in each animation frame
def update(frame, canvas, side):
    canvas.clear()
    colorWallpaper(canvas, 5, 5, side[frame])
    plt.axis('off')

fig, ax = plt.subplots()
# Adjust the range and step as needed
side_values = np.arange(0, 50, 0.5)

# Create the animation
animation = FuncAnimation(fig, update, frames=len(side_values), fargs=(ax, side_values), interval=500)
animation.save('color_wallpaper_animation.gif', writer=PillowWriter())

plt.axis('off')
plt.show()
