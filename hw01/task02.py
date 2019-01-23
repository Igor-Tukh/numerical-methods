import matplotlib.pyplot as plt
import numpy as np
import os


def save_plot(filename, x_values, y_values):
    fig = plt.figure(figsize=(8, 5))
    ax = fig.add_subplot(111)
    ax.plot(x_values, y_values)
    fig.savefig(filename, dpi=300)


def get_member(k, z):
    return (z ** k) / (2 * k - 1)


def get_aitken_values(z, values):
    first, second, third = values[0], values[1], values[2]
    divider = first + third - 2 * second
    if divider == 0:
        return None
    result = [(third * first - second * second) / divider]
    for k in range(3, len(values)):
        first, second, third = second, third, values[k]
        divider = first + third - 2 * second
        if divider == 0:
            return None
        result.append((third * first - second * second) / divider)
    return result


def get_aitken_value_iterative(z, start_number):
    current_sum = 0
    values = []
    for k in range(1, start_number + 1):
        current_sum += get_member(k, z)
        values.append(current_sum)

    last_value = 0
    while values is not None and len(values) >= 3:
        last_value = values[-1]
        values = get_aitken_values(z, values)
    return last_value


if __name__ == '__main__':
    xs = range(1000, 10001, 1000)
    for z in [-0.9, -1, (-1 + 1j) / np.sqrt(2), 1j]:
        ys = [get_aitken_value_iterative(z, x) for x in xs]
        print(ys[-1])
        if z.imag != 0:
            ys = [abs(y) for y in ys]
        save_plot(os.path.join('plots', '3', 'plot_' + str(z) + '.png'), xs, ys)

    xs = np.arange(0, 2 * np.pi, np.pi / 8)
    ys = []
    for angle in xs:
        value = np.cos(angle) + 1j * np.sin(angle)
        ys.append(abs(get_aitken_value_iterative(value, 10000) - get_aitken_value_iterative(value, 1000)))
    save_plot(os.path.join('plots', '3', 'diff.png'), xs, ys)
    print(xs)
    print(ys)
