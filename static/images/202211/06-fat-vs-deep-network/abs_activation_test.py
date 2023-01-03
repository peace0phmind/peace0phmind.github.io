import numpy as np
import matplotlib.pyplot as plt


def relu(x):
    return (np.maximum(0, x))


def abs_activation(x):
    y1 = relu(x * 1 - 0.5)
    y2 = relu(x * -1 + 0.5)

    return (y1 + y2) * 2 + 0


if __name__ == '__main__':
    layer_number = 4
    x = np.linspace(start=0, stop=1, num=1001)
    y = x
    for _ in range(layer_number):
        y = abs_activation(y)
    plt.plot(x, y)
    plt.show()
