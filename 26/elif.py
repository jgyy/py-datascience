"""
Add an ELSE Statement
"""


def wrapper():
    """
    label it as wrapper function to avoid renaming it
    """
    xval = 200
    if xval > 200:
        print("Big")
    elif 100 < xval <= 200:
        print("Average")
    elif 0 <= xval <= 100:
        print("Small")
    else:
        print("Negative")


if __name__ == "__main__":
    wrapper()
