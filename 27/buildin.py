"""
Notable Built-In Functions in Python
"""


def wrapper():
    """
    label it as wrapper function to avoid renaming it
    """
    print(max(25, 65, 890, 15))
    print(min(25, 65, 890, 15))
    print(abs(-100))
    print(round(55.5))
    print(round(35.56789, 3))
    numbers = [1, 5, 64, 24.5]
    print(sum(numbers))
    print(pow(10, 3))
    print(len("Elephant"))

    def distance_from_zero(xval):
        if isinstance(xval, (int, float)):
            return abs(xval)
        return "Not possible"

    print(distance_from_zero(-10))
    print(distance_from_zero("cat"))


if __name__ == "__main__":
    wrapper()
