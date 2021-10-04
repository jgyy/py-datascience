"""
Errors when adding scalars vectors and matrices
"""
from numpy import array


def wrapper():
    """
    wrapper function which description will not change
    """
    print(5 + 5)
    print(10 - 4)
    matrix1 = array([[5, 12, 6], [-3, 0, 14]])
    print(matrix1)
    matrix2 = array([[9, 8, 7], [1, 3, -5]])
    print(matrix2)
    print(matrix1 + matrix2)

    matrix3 = array([[5, 3], [-2, 4]])
    print(matrix3)
    matrix4 = array([[7, -5], [3, 8]])
    print(matrix4)
    print(matrix3 - matrix4)

    matrix5 = array([[22.33, -4.73], [-203.14, 1200.02], [4.22, 234.1]])
    print(matrix5)
    matrix6 = array([[131.13, 448.29], [-340.21, 1.06], [30.41, 424.99]])
    print(matrix6)
    print(matrix5 - matrix6)
    vector1 = array([1, 2, 3, 4, 5])
    print(vector1)
    vector2 = array([5, 4, 3, 2, 1])
    print(vector2)
    print(vector1 + vector2)
    print(vector1 - vector2)

    print(matrix1 + 1)
    print(vector1 + 1)
    print(matrix1 + array([1]))
    print(vector1 + array([1]))


if __name__ == "__main__":
    wrapper()
