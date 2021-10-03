"""
Lists
"""


def wrapper():
    """
    label it as wrapper function to avoid renaming it
    """
    numbers = [10, 25, 40, 50]
    print(numbers[2])
    print(numbers[0])
    print(numbers[-3])
    print(numbers[-3])
    numbers[0] = 15
    print(numbers)
    del numbers[1]
    print(numbers)


if __name__ == "__main__":
    wrapper()
