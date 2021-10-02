"""
Simple linear regression - Exercise
"""
from os.path import dirname
import seaborn as sns
from pandas import read_csv, DataFrame
from statsmodels.api import add_constant, OLS


def wrapper():
    """
    wrapper function which description will not change
    """
    sns.set()
    path = dirname(__file__)
    data = DataFrame(read_csv(f"{path}\\multiple_linear_regression.csv"))
    print(data)
    print(data.describe())

    y_data = data["GPA"]
    x1_data = data[["SAT", "Rand 1,2,3"]]
    x_data = add_constant(x1_data.values)
    result = OLS(y_data, x_data).fit()
    print(result.summary())


if __name__ == "__main__":
    wrapper()
