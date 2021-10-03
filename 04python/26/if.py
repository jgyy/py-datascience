"""
Introduction to the IF statement
"""


def wrapper():
    """
    label it as wrapper function to avoid renaming it
    """
    if 5 > 2:
        print ("The condition has been satisfied")
    xval = 10
    yval = 25

    if xval > 3 and yval > 13:
        print ('Both conditions are correct')
    if xval <= 3 or yval <= 13:
        print ('At least one of the conditions is false')


if __name__ == "__main__":
    wrapper()
