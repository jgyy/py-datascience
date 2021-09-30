"""
Help Yourself with Methods
"""


def wrapper():
    """
    label it as wrapper function to avoid renaming it
    """
    numbers = [15, 40, 50]
    numbers.append(100)
    print(numbers)
    numbers.extend([115, 140])
    print(numbers)
    print("The fourth element of the Numbers list is", numbers[3])
    print(len(numbers))


if __name__ == "__main__":
    wrapper()
