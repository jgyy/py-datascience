"""
A Practical Example of Probability Distributions
"""
from os.path import dirname, realpath
from pandas import DataFrame, read_excel
from matplotlib.pyplot import figure, show, xlabel, ylabel, scatter

PATH = dirname(realpath(__file__))


def daily():
    """
    wrapper function
    """
    data = DataFrame(read_excel(f"{PATH}/daily_views_post.xlsx"))
    print(data)
    xaxis = data["Days after release"]
    for i in data.columns[1:]:
        figure(i)
        yaxis = data[i]
        scatter(xaxis, yaxis)
        ylabel(i)
        xlabel("Days after release")


if __name__ == "__main__":
    daily()
    show()
