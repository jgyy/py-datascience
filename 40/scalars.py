"""
Scalars Vectors and Matrices
"""
from numpy import array


def wrapper():
    """
    wrapper function which description will not change
    """
    scalar = array([5])
    print(scalar)
    vector = array([5, -2, 4])
    print(vector)
    matrix = array([[5, 12, 6], [-3, 0, 14]])
    print(matrix)

    print(type(scalar))
    print(type(vector))
    print(type(matrix))
    s_array = array([5])
    print(type(s_array))

    print(matrix.shape)
    print(vector.shape)
    print(scalar.shape)
    print(s_array.shape)

    print(vector.reshape(1, 3))
    print(vector.reshape(3, 1))
    print(matrix + scalar)
    print(matrix + s_array)
    print(vector + scalar)
    print(vector)
    print(vector + s_array)
    print(matrix + vector)


if __name__ == "__main__":
    wrapper()
