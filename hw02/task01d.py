import matplotlib.pyplot as plt
import os
import numpy as np

from hw02.task01a import generate_values_table, get_max_absolute_error
from hw02.task01c import generate_interpolate_knots


def get_function_value(x):
    return np.abs(np.longdouble(x) - 1)


if __name__ == '__main__':
    xs = range(5, 51)
    for x0 in [1]:
        ys = []
        for N in range(5, 51):
            table = generate_values_table(x0, N, func=get_function_value, delta=1)
            ys.append(get_max_absolute_error(table, x0 - 1, x0 + 1, 1000))
        plt.clf()
        plt.plot(xs, ys)
        plt.ylabel('max absolute error')
        plt.xlabel('N')
        plt.title('Dependency of max absolute error, x0 = {x0}, 5 <= N <= 50'.format(x0=x0))
        plt.savefig(os.path.join('plots', 'task01d(b)'))

    for x0 in [1]:
        ys = []
        for N in range(5, 51):
            table = generate_values_table(x0, N, func=get_function_value, delta=1, points=generate_interpolate_knots(N))
            ys.append(get_max_absolute_error(table, x0 - 1, x0 + 1, 1000))
        plt.clf()
        plt.plot(xs, ys)
        plt.ylabel('max absolute error')
        plt.xlabel('N')
        plt.title('Dependency of max absolute error, x0 = {x0}, 5 <= N <= 50'.format(x0=x0))
        plt.savefig(os.path.join('plots', 'task01d(c)'))

