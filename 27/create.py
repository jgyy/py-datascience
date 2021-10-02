"""
Creating a Function with a Parameter
"""


def wrapper():
    """
    label it as wrapper function to avoid renaming it
    """

    def multiplication_by_2(xval):
        return xval * 2

    def division_by_2(xval):
        return float(xval) / 2

    def divisin_by_2(xval):
        return xval / 2.0

    print(multiplication_by_2(2))
    print(division_by_2(2))
    print(divisin_by_2(2))


if __name__ == "__main__":
    wrapper()
