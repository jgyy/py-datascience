"""
While Loops and Incrementing
"""


def wrapper():
    """
    label it as wrapper function to avoid renaming it
    """
    xval = 1
    while xval <= 30:
        print (xval, end=" ")
        xval += 2


if __name__ == "__main__":
    wrapper()
