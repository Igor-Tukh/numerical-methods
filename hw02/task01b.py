import matplotlib.pyplot as plt
import os

from hw02.task01a import get_max_absolute_error, generate_values_table


if __name__ == '__main__':
    xs = range(5, 51)
    for x0 in [100]:
        ys = []
        for N in range(5, 51):
            table = generate_values_table(x0, N)
            ys.append(get_max_absolute_error(table, x0 - 5, x0 + 5, 1000))
        plt.clf()
        plt.plot(xs, ys)
        plt.ylabel('max absolute error')
        plt.xlabel('N')
        plt.title('Dependency of max absolute error, x0 = {x0}, 5 <= N <= 50'.format(x0=x0))
        plt.savefig(os.path.join('plots', 'task01b'))

        ys = []
        for N in range(5, 41):
            table = generate_values_table(x0, N)
            ys.append(get_max_absolute_error(table, x0 - 5, x0 + 5, 1000))
        plt.clf()
        plt.plot(range(5, 41), ys)
        plt.ylabel('max absolute error')
        plt.xlabel('N')
        plt.title('Dependency of max absolute error, x0 = {x0}, 5 <= N <= 50'.format(x0=x0))
        plt.savefig(os.path.join('plots', 'task01b_cut'))

