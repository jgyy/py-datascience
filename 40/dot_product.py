"""
Dot Product
"""
from numpy import array, dot


def wrapper():
    """
    wrapper function which description will not change
    """
    x_vector = array([2, 8, -4])
    y_vector = array([1, -7, 3])
    print(dot(x_vector, y_vector))
    u_vector = array([0, 2, 5, 8])
    v_vector = array([20, 3, 4, -1])
    print(dot(u_vector, v_vector))
    print(dot(5, 6))
    print(dot(10, -2))
    print(x_vector)
    print(5 * x_vector)

    a_matrix = array([[5, 12, 6], [-3, 0, 14]])
    print(a_matrix)
    print(3 * a_matrix)
    b_matrix = array([[2, -1], [8, 0], [3, 0]])
    print(b_matrix)
    print(dot(a_matrix, b_matrix))
    c_matrix = array(
        [[-12, 5, -5, 1, 6], [6, -2, 0, 0, -3], [10, 2, 0, 8, 0], [9, -4, 8, 3, -6]]
    )
    print(c_matrix)
    d_matrix = array([[6, -1], [8, -4], [2, -2], [7, 4], [-6, -9]])
    print(dot(c_matrix, d_matrix))


if __name__ == "__main__":
    wrapper()
