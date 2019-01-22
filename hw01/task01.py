import matplotlib.pyplot as plt
import numpy as np
import os


def save_plot(filename, x_values, y_values):
    fig = plt.figure(figsize=(8, 5))
    ax = fig.add_subplot(111)
    ax.plot(x_values, y_values)
    fig.savefig(filename, dpi=300)


def get_member(z, k):
    return 1.0 / (k ** 2 - k - z)


def get_model_member(z, k):
    return z / ((k ** 2 - k - z) * (k ** 2 - k))


def get_value(z, number_of_members=int(1e6+1)):
    return sum([get_member(z, i + 1) for i in range(number_of_members)])


def get_value_model(z, number_of_members=89):
    return get_member(z, 1) + 1 + sum([get_model_member(z, i + 2) for i in range(number_of_members - 1)])


if __name__ == '__main__':
    xs = list(np.arange(0.02, 2, 0.02))
    ys = [get_value(x) for x in xs]
    save_plot(os.path.join('plots', '2', 'A.png'), xs, ys)
    ys = [get_value_model(x) for x in xs]
    save_plot(os.path.join('plots', '2', 'B.png'), xs, ys)
    ys = [get_value(x) - get_value_model(x) for x in xs]
    save_plot(os.path.join('plots', '2', 'C.png'), xs, ys)
