"""
Multiple Linear Regression with Dummies - Exercise
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
    raw_data = DataFrame(read_csv(f"{path}\\real_estate_price_size_year_view.csv"))
    print(raw_data.head())
    print(raw_data.describe(include="all"))
    data = raw_data.copy()
    data["view"] = data["view"].map({"Sea view": 1, "No sea view": 0})
    print(data.head())

    y_data = data["price"]
    x1_data = data[["size", "year", "view"]]
    x_data = add_constant(x1_data.values)
    results = OLS(y_data, x_data).fit()
    print(results.summary())


if __name__ == "__main__":
    wrapper()
