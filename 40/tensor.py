"""
Tensors
"""
from numpy import array


def wrapper():
    """
    wrapper function which description will not change
    """
    matrix1 = array([[5, 12, 6], [-3, 0, 14]])
    print(matrix1)
    matrix2 = array([[9, 8, 7], [1, 3, -5]])
    print(matrix2)
    tensor = array([matrix1, matrix2])
    print(tensor)
    print(tensor.shape)
    t_manual = array([[[5, 12, 6], [-3, 0, 14]], [[9, 8, 7], [1, 3, -5]]])
    print(t_manual)


if __name__ == "__main__":
    wrapper()
