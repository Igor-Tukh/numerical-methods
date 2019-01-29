import matplotlib.pyplot as plt
import os
import numpy as np

from hw02.task01a import generate_values_table, get_max_absolute_error


def generate_interpolate_knots(N):
    """
    Generates interpolate knots as cos(Pi * (2k - 1) / ((2k - 1) * N))
    :param N: number of knots.
    :param lower: left segment border.
    :param upper: right segment border.
    :return: list of the knots.
    """

    return np.longdouble(np.array([np.cos((np.pi * (2 * k - 1)) / (2 * N)) for k in range(1, N + 1)]))


if __name__ == '__main__':
    xs = range(5, 51)
    for x0 in [0]:
        ys = []
        for N in range(5, 51):
            table = generate_values_table(x0, N, points=generate_interpolate_knots(N + 1), delta=1)
            ys.append(get_max_absolute_error(table, x0 - 1, x0 + 1, 1000))
        plt.clf()
        plt.plot(xs, ys)
        plt.ylabel('max absolute error')
        plt.xlabel('N')
        plt.title('Dependency of max absolute error, x0 = {x0}, 5 <= N <= 50'.format(x0=x0))
        plt.savefig(os.path.join('plots', 'task01c'))
