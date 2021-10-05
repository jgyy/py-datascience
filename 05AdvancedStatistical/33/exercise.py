"""
Multiple Linear Regression - Exercise
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
    data = DataFrame(read_csv(f"{path}\\real_estate_price_size_year.csv"))
    print(data.head())
    print(data.describe())

    y_data = data["price"]
    x1_data = data[["size", "year"]]
    x_data = add_constant(x1_data.values)
    result = OLS(y_data, x_data).fit()
    print(result.summary())


if __name__ == "__main__":
    wrapper()
