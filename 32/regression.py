"""
Simple linear regression
"""
from os.path import dirname
from pandas import read_csv, DataFrame
from statsmodels.api import add_constant, OLS
from matplotlib.pyplot import scatter, xlabel, ylabel, show, plot, figure


def wrapper():
    """
    wrapper function which description will not change
    """
    path = dirname(__file__) + "\\"
    data = DataFrame(read_csv(f"{path}simple_linear_regression.csv"))
    print(data)
    print(data.describe())

    y_data = data["GPA"]
    x1_data = data["SAT"]
    figure()
    scatter(x1_data, y_data)
    xlabel("SAT", fontsize=20)
    ylabel("GPA", fontsize=20)

    x_data = add_constant(list(x1_data))
    results = OLS(y_data, x_data).fit()
    print(results.summary())
    figure()
    scatter(x1_data, y_data)
    yhat = 0.0017 * x1_data + 0.275
    plot(x1_data, yhat, lw=4, c="orange", label="regression line")
    xlabel("SAT", fontsize=20)
    ylabel("GPA", fontsize=20)


if __name__ == "__main__":
    wrapper()
    show()
