"""
List Slicing
"""


def wrapper():
    """
    label it as wrapper function to avoid renaming it
    """
    numbers = [15, 40, 50, 100, 115, 140]
    print(numbers[3:5])
    print(numbers[:4])
    print(numbers[3:])
    print(numbers[-4:])
    print(numbers.index(15))
    two_numbers = [1, 2]
    all_numbers = [two_numbers, numbers]
    print(all_numbers)
    numbers.sort(reverse=True)
    print(numbers)


if __name__ == "__main__":
    wrapper()
