"""
Transpose of a matrix
"""
from numpy import array


def wrapper():
    """
    wrapper function which description will not change
    """
    a_matrix = array([[5, 12, 6], [-3, 0, 14]])
    print(a_matrix)
    print(a_matrix.T)
    b_matrix = array([[5, 3], [-2, 4]])
    print(b_matrix)
    print(b_matrix.T)
    c_matrix = array([[4, -5], [8, 12], [-2, -3], [19, 0]])
    print(c_matrix)
    print(c_matrix.T)

    scalar = array([5])
    print(scalar)
    print(scalar.T)
    x_vector = array([1,2,3])
    print(x_vector)
    print(x_vector.T)
    print(x_vector.shape)
    x_reshaped = x_vector.reshape(1, 3)
    print(x_reshaped.T)


if __name__ == "__main__":
    wrapper()
