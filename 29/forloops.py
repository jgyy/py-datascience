"""
For Loops
"""


def wrapper():
    """
    label it as wrapper function to avoid renaming it
    """
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for digit in digits:
        print(digit)
    for digit in digits:
        print (digit, end=" ")


if __name__ == "__main__":
    wrapper()
