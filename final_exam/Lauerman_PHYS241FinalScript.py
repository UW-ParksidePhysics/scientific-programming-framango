from two_column_text_read import two_column_text_read
from bivariate_statistics import bivariate_statistics
from quadratic_fit import quadratic_fit
from convert_units import convert_units
from fit_curve_array import fit_curve_array
from plot_data_with_fit import plot_data_with_fit
from equations_of_state import fit_eos
from numpy import linspace
import matplotlib.pyplot as plt

display_graph = True


def parse_file_name(file_name):
    x = file_name.split(".")
    chemical_symbol = x[0]
    crystal_symmetry = x[1]
    density_functional_exchange = x[2]
    return chemical_symbol, crystal_symmetry, density_functional_exchange


file_name = "Al.Fm-3m.GGA-PBE.volumes_energies.dat"
chemical_symbol, crystal_symmetry, density_functional_exchange = parse_file_name(file_name)
array = two_column_text_read("Al.Fm-3m.GGA-PBE.volumes_energies.dat")
statistics = bivariate_statistics(array)
quadratic_coefficients = quadratic_fit(array)

min_x = statistics[2]
max_x = statistics[3]

undo_array = zip(*array)
array_2 = list(undo_array)

fit_eos_curve, fit_parameters = fit_eos(array[0], array[1], quadratic_coefficients, eos='Murnaghan',
                                        number_of_points=50)
bulk_modulus = fit_parameters[1]
equilibrium_volume = fit_parameters[3]


def annotate_graph(chemical_symbol, crystal_symmetry):
    bulk_modulus_gpa = bulk_modulus
    ax.annotate(chemical_symbol, xy=(130, 0))

    ax.annotate(r'$ {}\overline{{{}}} {}$'.format(crystal_symmetry[0:2],
                                                  crystal_symmetry[3],
                                                  crystal_symmetry[1]),
                xy=(115, 0))

    ax.annotate('K_0={:.6f}GPa'.format(bulk_modulus_gpa),
                xy=(115, -0.001))

    ax.annotate('V_0={:.3f}A^3/atom'.format(equilibrium_volume),
                xy=(115, -0.001))
    plt.axvline(equilibrium_volume - array_2[0][array_2[1].index(min(array_2[1]))] * 0.01, color="black",
                linestyle='--')

    plt.text(91, -0.0025, "created by Frank Lauerman 2022/05/11")
    plt.title("{} Equation of State for {} in DFT {}".format('Murnaghan', chemical_symbol, density_functional_exchange))
    return ax, plt


fig = plt.figure()
ax = fig.add_subplot(111)

volumes = linspace(min(array_2[0]), max(array_2[0]), len(fit_eos_curve))
line1, = ax.plot(array_2[0], array_2[1], 'o')
line2, = ax.plot(volumes, fit_eos_curve, color="black")

x_min = (min(array_2[0]) - (min(array_2[0]) * 0.10))
x_max = (max(array_2[0]) + (max(array_2[0]) * 0.10))
y_min = -537.33  # (min(array_2[1]) - (min(array_2[0]) * 0.00010))
y_max = 14.49  # (max(array_2[1]) + (max(array_2[0]) * 0.00010))

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xlabel(r'$V$ (Å$^3$/atom)')
plt.ylabel(r'$E$ (eV/atom)')
bulk_modulus_gpa = convert_units(bulk_modulus, "rb/cb")  # 7
eq_vol = array_2[0][array_2[1].index(min(array_2[1]))]
annotate_graph(chemical_symbol, crystal_symmetry)

fit_curve = fit_curve_array(quadratic_coefficients, min_x, max_x, number_of_points=100)
scatter_plot, curve_plot = plot_data_with_fit(array, fit_curve, data_format="bo", fit_format="k")

if display_graph:
    plt.show()
elif not display_graph:
    plt.savefig("Lauerman.Al.Fm-3m.GGA-PBE.MurnaghanEquationOfState.png")


print()
