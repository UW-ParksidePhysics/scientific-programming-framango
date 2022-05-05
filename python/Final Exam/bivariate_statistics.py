import numpy as np
from scipy import stats


def bivariate_statistics(data):
    if len(data) != 2 or len(data[0]) <= 1:
        raise IndexError
    stat = stats.describe(data)
    mean_of_y = stat.minmax[0][1]
    standard_deviation_of_y = np.sqrt(stat.variance[1])
    minimum_x_value = stat.minmax[0][0]
    maximum_x_value = stat.minmax[0][1]
    minimum_y_value = stat.minmax[1][0]
    maximum_y_value = stat.minmax[1][1]

    statistics = np.array(
        [mean_of_y, standard_deviation_of_y, minimum_x_value, maximum_x_value, minimum_y_value, maximum_y_value])

    return statistics


if __name__ == __'main'__:
    x = [2, 5, 4]
    y = [5, 3, 2]
    data = np.array([x, y])
    print(bivariate_statistics(data))
