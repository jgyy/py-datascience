"""
Another Way to Define a Function
"""


def wrapper():
    """
    label it as wrapper function to avoid renaming it
    """

    def exponentiation_exp_2(xval):
        result = xval ** 2
        print (xval, "Raised to the power of 2:")
        return result

    print(exponentiation_exp_2(2))


if __name__ == "__main__":
    wrapper()
