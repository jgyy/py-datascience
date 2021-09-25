"""
A Practical Example of Probability Distributions
"""
from os.path import dirname, realpath
from pandas import DataFrame, read_excel
from matplotlib.pyplot import figure, show, xlabel, ylabel, scatter

PATH = dirname(realpath(__file__))


def customers():
    """
    wrapper function
    """
    data = DataFrame(read_excel(f"{PATH}/customers_membership_post.xlsx"))
    print(data)
    xaxis = data["Customer Age"]
    yaxis = data["Membership Status"]

    figure("Subscription")
    scatter(xaxis, yaxis)
    ylabel("Membership Status")
    xlabel("Customer Age")


if __name__ == "__main__":
    customers()
    show()
