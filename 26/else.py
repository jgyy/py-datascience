"""
Add an ELSE Statement
"""


def wrapper():
    """
    label it as wrapper function to avoid renaming it
    """
    xval = 102
    if xval > 100:
        print ("A busy day")
    else:
        print ("A calm day")


if __name__ == "__main__":
    wrapper()
