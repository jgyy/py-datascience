"""
Logical and Identity Operators
"""


def wrapper():
    """
    label it as wrapper function to avoid renaming it
    """
    print(False or not True and not False)
    print(True and not False and True or not False)
    print(True or False and False)
    print(False and True or False)
    print(10 is not 12)
    print(50 is 50)


if __name__ == "__main__":
    wrapper()
