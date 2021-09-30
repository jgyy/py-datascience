"""
Using a Function in Another Function
"""


def wrapper():
    """
    label it as wrapper function to avoid renaming it
    """

    def plus_five(xval):
        return xval + 5

    def m_by_3(xval):
        return plus_five(xval) * 3

    print(m_by_3(5))


if __name__ == "__main__":
    wrapper()
