"""
Structure Your Code with Indentation
"""


def wrapper():
    """
    label it as wrapper function to avoid renaming it
    """

    def ten(xval):
        xval = 10
        return xval

    print(ten(3))


if __name__ == "__main__":
    wrapper()
