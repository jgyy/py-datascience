"""
A Practical Example of Probability Distributions
"""
from os.path import dirname, realpath
from pandas import DataFrame, read_csv
from matplotlib.pyplot import figure, show, hist, xlabel, ylabel

PATH = dirname(realpath(__file__))


def fifa():
    """
    wrapper function
    """
    data = DataFrame(read_csv(f"{PATH}/fifa19_post.csv"))
    for i in data.columns:
        try:
            col = data[i].apply(float)
            print(col)
            figure(i)
            hist(col)
            ylabel("Count")
            xlabel("Data")
        except ValueError as err:
            print(err)


if __name__ == "__main__":
    fifa()
    show()
