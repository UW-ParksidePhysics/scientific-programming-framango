__author__ = 'Adrian Sanchez'
import numpy as np


def lowest_eigenvectors(square_matrix, number_of_eigenvectors=3):
    m, n = square_matrix.shape
    if m != n:
        raise IndexError('not square')
    values, vectors = np.linalg.eig(square_matrix)
    values_sorted = np.sort(values)
    vector_sorted = vectors[:, values.argsort()]
    return values_sorted[:number_of_eigenvectors], vector_sorted.transpose()[:number_of_eigenvectors]
