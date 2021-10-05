"""
Multiple linear regression
"""
from os.path import dirname
import seaborn as sns
from pandas import read_csv, DataFrame
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import f_regression


def wrapper():
    """
    wrapper function which description will not change
    """
    sns.set()
    path = dirname(__file__)
    data = DataFrame(read_csv(f"{path}\\multiple_linear_regression.csv"))
    print(data.head())
    print(data.describe())

    x_data = data[["SAT", "Rand 1,2,3"]]
    y_data = data["GPA"]
    reg = LinearRegression()
    reg.fit(x_data, y_data)
    print(reg.coef_)
    print(reg.intercept_)
    print(reg.score(x_data, y_data))
    print(x_data.shape)
    r_square = reg.score(x_data, y_data)
    num, predict = x_data.shape
    adjusted_r2 = 1 - (1 - r_square) * (num - 1) / (num - predict - 1)
    print(adjusted_r2)

    p_values = f_regression(x_data, y_data)[1]
    print(p_values)
    print(p_values.round(3))
    reg_summary = DataFrame(data=x_data.columns.values, columns=["Features"])
    print(reg_summary)
    reg_summary["Coefficients"] = reg.coef_
    reg_summary["p-values"] = p_values.round(3)
    print(reg_summary)


if __name__ == "__main__":
    wrapper()
