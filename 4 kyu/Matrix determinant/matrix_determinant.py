import numpy as np


def determinant(matrix):
    matrix = np.array(matrix)

    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        matrix_determinant = 0

        for i in range(0, len(matrix)):
            matrix_minor = np.delete(matrix, 0, 0)
            matrix_minor = np.delete(matrix_minor, i, 1)

            if i % 2 == 0:
                matrix_determinant += matrix[0][i] * determinant(matrix_minor)
            else:
                matrix_determinant -= matrix[0][i] * determinant(matrix_minor)

        return matrix_determinant
    