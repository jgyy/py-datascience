"""
Dictionaries
"""


def wrapper():
    """
    label it as wrapper function to avoid renaming it
    """
    menu = {
        "meal_1": "Spaghetti",
        "meal_2": "Fries",
        "meal_3": "Hamburger",
        "meal_4": "Lasagna",
    }
    print(menu["meal_2"])
    menu["meal_5"] = "Soup"
    print(menu)
    menu["meal_3"] = "Cheesburger"
    print(menu)
    dessert = ["Pancakes", "Ice-cream", "Tiramisu"]
    menu["meal_6"] = dessert
    print(menu)
    price_list = {}
    price_list["Spaghetti"] = 10
    price_list["Fries"] = 5
    price_list["Cheesburger"] = 8
    price_list["Lasagna"] = 12
    price_list["Soup"] = 5
    print(price_list)
    price_list = {}
    price_list[menu["meal_1"]] = 10
    price_list[menu["meal_2"]] = 5
    price_list[menu["meal_3"]] = 8
    price_list[menu["meal_4"]] = 12
    price_list[menu["meal_5"]] = 5
    print(price_list)
    print(price_list.get("Spaghetti"))
    print(price_list.get(menu["meal_1"]))


if __name__ == "__main__":
    wrapper()
