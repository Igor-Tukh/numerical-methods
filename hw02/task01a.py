import numpy as np
import matplotlib.pyplot as plt
import os


def get_lagrange_polynomial_basis(points, substitution_point):
    """
    Function which calculates Lagrange basis polynomials value in a given point.
    :param points: list of unique points in which interpolation will be performed.
    :param substitution_point: point for substitute in the polynomials.
    :return: substitution result list.
    """

    points = np.longdouble(points)
    substitution_point = np.longdouble(substitution_point)
    coefficients = np.longdouble([])

    for first_ind, first_point in enumerate(points):
        denominator = np.longdouble(1)
        numerator = np.longdouble(1)
        for second_ind, second_point in enumerate(points):
            if second_ind == first_ind:
                continue
            denominator *= (first_point - second_point)
            numerator *= (substitution_point - second_point)
        coefficients = np.append(coefficients, numerator / denominator)

    return coefficients


def get_lagrange_polynomial_value(table, substitution_point):
    """
    Function which calculates Lagrange polynomial value in the given point.
    :param table: list of pairs (point, value) to perform the interpolation. All the points must be different.
    :param substitution_point: point to in the polynomial.
    :return: substitution result.
    """

    coeffs = get_lagrange_polynomial_basis([point for point, _ in table], substitution_point)
    result = np.longdouble(0)
    for ind, (_, value) in enumerate(table):
        result += np.longdouble(value) * coeffs[ind]
    return result


def generate_uniform_distribution(lower, upper, number_of_values):
    """
    Function which generates several uniform distributed values.
    :param lower: the smallest value which could be generated.
    :param upper: the greatest value value which could be generated.
    :param number_of_values: number of values to generate
    :return: np.array of generated values.
    """

    return np.longdouble(np.array(list(np.random.uniform(lower, upper, number_of_values))))


def generate_knots(lower, upper, number_of_values):
    """
    Function which generates several values with equal distance between neighbours.
    :param lower: the smallest value which could be generated.
    :param upper: the greatest value value which could be generated.
    :param number_of_values: number of values to generate
    :return: np.array of generated values.
    """
    return np.longdouble(np.array([lower + k * (1.0 * (upper - lower)) / (number_of_values - 1)
                                   for k in range(number_of_values)]))


def get_function_value(x):
    """
    Function which calculates the value of the x sin(2x) function.
    :param x: point to substitute in the function.
    :return: substitution result.
    """
    x = np.longdouble(x)
    return x * (np.sin(2 * x))


def get_max_absolute_error(table, lower, upper, number_of_points=100000, func=get_function_value):
    """
    Function which calculates the largest absolute error i.e. abs(Lagrange polynomial - function value)
    :param table: list of pairs (point, value) to perform the interpolation. All the points must be different.
    :param lower: the smallest value of the research segment.
    :param upper: the greatest value of the research segment.
    :param number_of_points: number of points to get values.
    :return: the greatest absolute error of the research segment.
    """

    points = generate_knots(lower, upper, number_of_points)
    max_error = -1
    for point in points:
        max_error = max(max_error, np.abs(get_lagrange_polynomial_value(table, point) - func(point)))
    return max_error


def generate_values_table(x0, N, func=get_function_value, points=None, delta=5):
    """
    Generates list of pairs (point, value) to perform the interpolation. All the points must be different.
    :param func: base function.
    :param x0: knot center.
    :param N: polynomial degree.
    :return: list of pairs (point, value).
    """

    if points is None:
        points = generate_knots(x0 - delta, x0 + delta, N + 1)
    return [(point, func(point)) for point in points]


def build_error_plot(x0, N, plot_name=None, filename=None, points_number=1000):
    """
    Builds absolute error plot (abs(Lagrange polynomial value - function value)).
    :param x0: knot center.
    :param N: polynomial degree.
    :param plot_name: name of plot.
    :param filename: filename to save plot.
    :param points_number: number of points to build.
    :return: nothing.
    """

    if plot_name is None:
        plot_name = 'Lagrange polynomial error (x0 = {x0}, N = {N})'.format(x0=x0, N=N)
    if filename is None:
        filename = 'lagrange_polynomial_error_plot_{x0}_{N}'.format(x0=x0, N=N)
    points = generate_knots(x0 - 5, x0 + 5, N + 1)
    table = [(point, get_function_value(point)) for point in points]
    xs = generate_knots(x0 - 5, x0 + 5, points_number)
    ys = [np.abs(get_lagrange_polynomial_value(table, x) - get_function_value(x)) for x in xs]

    plt.clf()
    plt.plot(xs, ys)
    plt.xlabel('x')
    plt.ylabel('absolute error')
    plt.title(plot_name)
    plt.savefig(os.path.join('plots', filename))

    print('N = {N}, x0 = {x0}, max error = {error}'.format(N=N,
                                                           x0=x0,
                                                           error=get_max_absolute_error(table, x0 - 5, x0 + 5)))


def build_all_errors_plot(x0, ns, filename='task01a', points_number=1000):
    plot_name = 'Lagrange polynomial error (x0 = {x0}, N = 5, 10, 15)'.format(x0=x0)
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
    for x0 in [100]:
        for N in [5, 10, 15]:
            build_error_plot(x0, N)
        build_all_errors_plot(x0, [5, 10, 15])
