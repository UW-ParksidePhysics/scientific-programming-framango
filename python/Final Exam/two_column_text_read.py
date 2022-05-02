import numpy as np


def two_column_text_read(filename):
    try:
        data = np.loadtxt(filename)
    except OSError:
        print(f'{filename} cannot be found!!')

    return data


if __name__ == '__main__':
    data_file = 'volumes_energies.dat'
    volumes_energies = two_column_text_read(data_file)
    print(volumes_energies)
