import matplotlib.pyplot as plt
import os
import numpy as np

from hw02.task01a import get_max_absolute_error, generate_values_table, generate_knots, get_function_value, \
    get_lagrange_polynomial_value


def build_all_errors_plot(x0, ns, filename='task01b_40', points_number=1000):
    plot_name = 'Lagrange polynomial error (x0 = {x0}, N = 40)'.format(x0=x0)
    xs = generate_knots(x0 - 5, x0 + 5, points_number)
    plt.clf()
    for N in ns:
        points = generate_knots(x0 - 5, x0 + 5, N + 1)
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
        ys = []
        for N in range(5, 51):
            table = generate_values_table(x0, N)
            ys.append(np.log10(get_max_absolute_error(table, x0 - 5, x0 + 5, 10000)))
        plt.clf()
        plt.plot(xs, ys)
        plt.ylabel('log(max absolute error)')
        plt.xlabel('N')
        plt.title('Dependency of max absolute error, x0 = {x0}, 5 <= N <= 50'.format(x0=x0))
        plt.savefig(os.path.join('plots', 'task01b'))

        build_all_errors_plot(x0, [40])
