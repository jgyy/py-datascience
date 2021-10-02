"""
Tuples
"""


def wrapper():
    """
    label it as wrapper function to avoid renaming it
    """
    cars = "BMW", "Dodge", "Ford"
    print(cars)
    print(cars[1])
    name, age = "Peter,24".split(",")
    print(name)
    print(age)

    def rectangle_info(xval, yval):
        area = xval * yval
        perimeter = 2 * (xval + yval)
        print("Area and Parameter:")
        return area, perimeter

    print(rectangle_info(2, 10))


if __name__ == "__main__":
    wrapper()
