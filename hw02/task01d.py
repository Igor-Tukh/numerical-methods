import matplotlib.pyplot as plt
import os
import numpy as np

from hw02.task01a import generate_values_table, get_max_absolute_error, generate_knots, get_function_value, \
    get_lagrange_polynomial_value
from hw02.task01c import generate_interpolate_knots


def get_abs_function_value(x):
    return np.abs(np.longdouble(x) - 1)


def build_all_errors_plot(x0, ns, filename='task01d_40_un', points_number=1000):
    plot_name = 'Lagrange polynomial error (x0 = {x0}, N = 40)'.format(x0=x0)
    xs = generate_knots(x0 - 1, x0 + 1, points_number)
    plt.clf()
    for N in ns:
        points = generate_interpolate_knots(N + 1, x0 - 1, x0 + 1)
        table = [(point, get_abs_function_value(point)) for point in points]
        ys = [np.abs(get_lagrange_polynomial_value(table, x) - get_abs_function_value(x)) for x in xs]
        plt.plot(xs, ys)
    plt.xlabel('x')
    plt.ylabel('absolute error')
    plt.title(plot_name)
    plt.savefig(os.path.join('plots', filename))


if __name__ == '__main__':
    xs = range(5, 51)
    for x0 in [1]:
        # build_all_errors_plot(x0, [40])
        # ys = []
        # for N in range(5, 51):
        #     table = generate_values_table(x0, N, func=get_abs_function_value, delta=1)
        #     ys.append(np.log10(get_max_absolute_error(table, x0 - 1, x0 + 1, 1000, func=get_abs_function_value)))
        # plt.clf()
        # plt.plot(xs, ys)
        # plt.ylabel('log(max absolute error)')
        # plt.xlabel('N')
        # plt.title('Dependency of max absolute error, x0 = {x0}, 5 <= N <= 50'.format(x0=x0))
        # plt.savefig(os.path.join('plots', 'task01d(b)'))
        #
        # ys = []
        # for N in range(5, 51):
        #     table = generate_values_table(x0, N, points=generate_interpolate_knots(N + 1, x0 - 1, x0 + 1), delta=1,
        #                                   func=get_abs_function_value)
        #     ys.append(np.log(get_max_absolute_error(table, x0 - 1, x0 + 1, 1000, func=get_abs_function_value)))
        # plt.clf()
        # plt.plot(np.log(xs), ys)
        # plt.ylabel('log(max absolute error)')
        # plt.xlabel('N')
        # plt.title('Dependency of max absolute error, x0 = {x0}, 5 <= N <= 50'.format(x0=x0))
        # plt.savefig(os.path.join('plots', 'task01d(c)'))
        #
        plt.clf()
        ys = []
        for N in range(5, 51):
            table = generate_values_table(x0, N, func=get_abs_function_value, delta=1)
            ys.append(np.log10(get_max_absolute_error(table, x0 - 1, x0 + 1, 1000, func=get_abs_function_value)))
        plt.plot(xs, ys)
        ys = []
        for N in range(5, 51):
            table = generate_values_table(x0, N, points=generate_interpolate_knots(N + 1, x0 - 1, x0 + 1), delta=1,
                                          func=get_abs_function_value)
            ys.append(np.log10(get_max_absolute_error(table, x0 - 1, x0 + 1, 1000, func=get_abs_function_value)))
        plt.plot(xs, ys)
        ys = []
        for N in range(5, 51):
            table = generate_values_table(100, N, points=generate_interpolate_knots(N + 1, 100 - 5, 100 + 5), delta=5)
            ys.append(np.log10(get_max_absolute_error(table, 100 - 5, 100 + 5, 1000)))
        plt.plot(xs, ys)
        ys = []
        for N in range(5, 51):
            table = generate_values_table(100, N)
            ys.append(np.log10(get_max_absolute_error(table, 100 - 5, 100 + 5, 1000)))
        plt.plot(xs, ys)
        plt.ylabel('log(max absolute error)')
        plt.xlabel('N')
        plt.title('Dependency of max absolute error, 5 <= N <= 50'.format(x0=x0))
        plt.savefig(os.path.join('plots', 'task01d(all)'))
