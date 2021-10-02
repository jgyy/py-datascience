"""
Iterating over Dictionaries
"""


def wrapper():
    """
    label it as wrapper function to avoid renaming it
    """
    prices = {"box_of_spaghetti": 4, "lasagna": 5, "hamburger": 2}
    quantity = {"box_of_spaghetti": 6, "lasagna": 10, "hamburger": 0}
    money_spent = 0
    for i, j in quantity.items():
        if prices[i] >= 5:
            money_spent += prices[i] * j
    print(money_spent)
    prices = {"box_of_spaghetti": 4, "lasagna": 5, "hamburger": 2}
    quantity = {"box_of_spaghetti": 6, "lasagna": 10, "hamburger": 0}
    money_spent = 0
    for i, j in quantity.items():
        if prices[i] < 5:
            money_spent += prices[i] * j
    print(money_spent)


if __name__ == "__main__":
    wrapper()
