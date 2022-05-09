from two_column_text_read import two_column_text_read

filename = 'Al.Fm-3m.GGA-PBE.volumes_energies.dat'


def parse_file_name(filename):
    x = filename.split(".")
    chemical_symbol = x[0]
    crystal_symmetry_symbol = x[1]
    density_functional_exchange = x[2]
    return chemical_symbol, crystal_symmetry_symbol, density_functional_exchange



