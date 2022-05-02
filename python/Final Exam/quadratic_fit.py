import numpy as np


def quadratic_fit(data):
    x = data[:, 0]
    y = data[:, 1]
    quadratic_coefficients = np.polyfit(x, y, 2)

    return quadratic_coefficients


if __name__ == '__main__':
    data = np.array([[2, 7], [0, 1], [-1, 1]])
    coefficients = quadratic_fit(data)
    print(coefficients)
