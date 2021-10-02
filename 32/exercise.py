"""
Simple linear regression - Exercise
"""
from os.path import dirname
import seaborn as sns
from pandas import read_csv, DataFrame
from statsmodels.api import add_constant, OLS
from matplotlib.pyplot import scatter, xlabel, ylabel, show, plot, figure


def wrapper():
    """
    wrapper function which description will not change
    """
    sns.set()
    path = dirname(__file__)
    data = DataFrame(read_csv(f"{path}\\real_estate_price_size.csv"))
    print(data)
    print(data.describe())

    y_data = data["price"]
    x1_data = data["size"]
    figure()
    scatter(x1_data, y_data)
    xlabel("Size", fontsize=20)
    ylabel("Price", fontsize=20)

    x_data = add_constant(x1_data)
    results = OLS(y_data, x_data).fit()
    print(results.summary())
    figure()
    scatter(x1_data, y_data)
    yhat = x1_data * 223.1787 + 101900
    plot(x1_data, yhat, lw=4, c="orange", label="regression line")
    xlabel("Size", fontsize=20)
    ylabel("Price", fontsize=20)


if __name__ == "__main__":
    wrapper()
    show()
