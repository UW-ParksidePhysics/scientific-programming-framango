import numpy as py
import matplotlib.pyplot as plt


def plot_data_with_fit(data, fit_curve):
    scatter_plot = plt.plot(data[0, :], data[1, :])
    best_fit = plt.plot(fit_curve[0, :], fit_curve[1, :])
    plt.show()
    return scatter_plot, best_fit
