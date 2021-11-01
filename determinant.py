# test
def _get_list_of_slices(matrix: list[list[int]]) -> list[list[list[int]]]:
    """Returns a list of slices of a matrix. Used to find the determinant."""
    matrix = matrix[1:]
    slice_list = []

    # the outer loop adds each 2D array to a list of all the slices
    for col in range(len(matrix[0])):
        matrix_slice = []
        # the inner loop creates a new 2D array, which includes everything
        # in the input matrix except the first row and the column col
        for row in range(len(matrix)):
            matrix_slice.append(matrix[row][0:col] + matrix[row][col + 1:])
        slice_list.append(matrix_slice)

    return slice_list


def determinant(matrix: list[list[int]]) -> int:
    """Given a 2D array representing a matrix, returns the determinant.
    Assumes the matrix is square.
    """
    # base case: determinant([[a]]) = a
    if len(matrix) == 1:
        return matrix[0][0]

    # doing this is much faster than using the next bit for 2x2 matrices
    if len(matrix) == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

    slice_list = _get_list_of_slices(matrix)
    det = 0
    # even terms in the determinant are positive, odd terms are negative
    for i in range(len(slice_list)):
        if i % 2 == 0:
            det += matrix[0][i] * determinant(slice_list[i])
        else:
            det -= matrix[0][i] * determinant(slice_list[i])

    return det
