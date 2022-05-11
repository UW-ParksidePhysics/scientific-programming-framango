from two_column_text_read import two_column_text_read
from bivariate_statistics import bivariate_statistics
from quadratic_fit import quadratic_fit
from fit_curve_array import fit_curve_array
from plot_data_with_fit import plot_data_with_fit
from equations_of_state import fit_eos
from numpy import linspace
import matplotlib.pyplot as plt


def parse_file_name(file_name):
    x = file_name.split(".")
    symbol = x[0]
    structure = x[1]
    acronym = x[2]
    return symbol, structure, acronym


file_name = "Al.Fm-3m.GGA-PBE.volumes_energies.dat"
symbol, structure, acronym = parse_file_name(file_name)
array = two_column_text_read("Al.Fm-3m.GGA-PBE.volumes_energies.dat")
statistics = bivariate_statistics(array)
quadratic_coefficients = quadratic_fit(array)
print(quadratic_coefficients)
