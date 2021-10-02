"""
Reassignment of values
"""


def wrapper():
    """
    label it as wrapper function to avoid renaming it
    """
    pval = 14
    print(pval + 10)
    pval = 30
    print(pval + 10)


if __name__ == "__main__":
    wrapper()
