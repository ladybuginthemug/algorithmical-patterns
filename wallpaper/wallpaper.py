import matplotlib.pyplot as plt
import random

x_values = []
y_values = []

def wallpaper(corna,cornb,side):
    for i in range(1, 100):
        for j in range(1, 100):
            x = corna + i * side / 100
            y = cornb + j * side / 100
            c = int(x ** 2 + y ** 2)

            if c % 2 == 0:
                x_values.append(x)
                y_values.append(y)



wallpaper(70,80,random.randrange(1,100))

plt.plot(x_values, y_values, 'ks' , marker='s',markersize=1)
plt.axis('off')
plt.tight_layout()
plt.show()
