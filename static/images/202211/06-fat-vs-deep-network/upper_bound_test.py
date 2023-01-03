import numpy as np
import matplotlib.pyplot as plt


def relu(x):
    return (np.maximum(0, x))


def upper_bound_test(x):
    y1 = relu(x * 1 + 1)
    y2 = relu(x * 1 - 1)
    y3 = relu(x * 1 + 0)

    return (y1 + y2 + y3) * 1 + 0


if __name__ == '__main__':
    x = np.linspace(start=-2, stop=2, num=41)
    y = upper_bound_test(x)
    plt.plot(x, y)
    plt.show()
