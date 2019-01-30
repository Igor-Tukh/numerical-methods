import matplotlib.pyplot as plt
import os
import numpy as np

from hw02.task01a import generate_values_table, get_max_absolute_error, generate_knots, \
    get_lagrange_polynomial_value, get_function_value


def generate_interpolate_knots(N, lower, upper):
    """
    Generates interpolate knots as cos(Pi * (2k - 1) / ((2k - 1) * N))
    :param N: number of knots.
    :param lower: left segment border.
    :param upper: right segment border.
    :return: list of the knots.
    """

    knots = np.longdouble(np.array([np.cos((np.pi * (2 * k - 1)) / (2 * N)) for k in range(1, N + 1)]))
    return [np.longdouble(lower + upper) / 2 + (upper - lower) * knot / 2 for knot in knots]


def build_all_errors_plot(x0, ns, filename='task01c_40', points_number=1000):
    plot_name = 'Lagrange polynomial error (x0 = {x0}, N = 40)'.format(x0=x0)
    xs = generate_knots(x0 - 5, x0 + 5, points_number)
    plt.clf()
    for N in ns:
        points = generate_interpolate_knots(N + 1, x0 - 5, x0 + 5)
        table = [(point, get_function_value(point)) for point in points]
        ys = [np.abs(get_lagrange_polynomial_value(table, x) - get_function_value(x)) for x in xs]
        plt.plot(xs, ys)
    plt.xlabel('x')
    plt.ylabel('absolute error')
    plt.title(plot_name)
    plt.savefig(os.path.join('plots', filename))


if __name__ == '__main__':
    xs = range(5, 51)
    for x0 in [100]:
        build_all_errors_plot(x0, [40])
        ys = []
        for N in range(5, 51):
            table = generate_values_table(x0, N, points=generate_interpolate_knots(N + 1, x0 - 5, x0 + 5), delta=5)
            ys.append(np.log10(get_max_absolute_error(table, x0 - 5, x0 + 5, 1000)))
        plt.clf()
        plt.plot(xs, ys)
        ys = []
        for N in range(5, 51):
            table = generate_values_table(x0, N)
            ys.append(np.log10(get_max_absolute_error(table, x0 - 5, x0 + 5, 1000)))
        plt.plot(xs, ys)
        plt.ylabel('log(max absolute error)')
        plt.xlabel('N')
        plt.title('Dependency of max absolute error, x0 = {x0}, 5 <= N <= 50'.format(x0=x0))
        plt.savefig(os.path.join('plots', 'task01c(all)'))
