"""
Combining Conditional Statements and Functions
"""


def wrapper():
    """
    label it as wrapper function to avoid renaming it
    """

    def compare_the_two(xval, yval):
        if xval > yval:
            print("Greater")
        elif xval < yval:
            print("Less")
        else:
            print("Equal")

    print(compare_the_two(10, 10))


if __name__ == "__main__":
    wrapper()
