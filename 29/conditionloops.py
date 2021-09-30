"""
Use Conditional Statements and Loops Together
"""


def wrapper():
    """
    label it as wrapper function to avoid renaming it
    """
    for num in range(1, 11):
        print(num * 2)
    for xval in range(1, 31):
        if xval % 2 == 1:
            print(xval, end=" ")
        else:
            print("Even", end=" ")
    numbers = [1, 2, 3, 4, 5, 6]
    for item in numbers:
        print(item * 10, end=" ")
    for i, _ in enumerate(numbers):
        print(numbers[i] * 10, end=" ")


if __name__ == "__main__":
    wrapper()
