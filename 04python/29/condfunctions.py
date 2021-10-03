"""
All in - Conditional Statements, Functions, and Loops
"""


def wrapper():
    """
    label it as wrapper function to avoid renaming it
    """
    nums = [1, 35, 12, 24, 31, 51, 70, 100]

    def count(numbers):
        numbers = sorted(numbers)
        tot = 0
        while numbers[tot] < 20:
            tot += 1
        return tot

    print(count(nums))


if __name__ == "__main__":
    wrapper()
