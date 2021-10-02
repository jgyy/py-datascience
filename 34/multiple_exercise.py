"""
Multiple Linear Regression with sklearn - Exercise
"""
from warnings import filterwarnings
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
    filterwarnings("ignore", category=UserWarning)
    path = dirname(__file__)
    data = DataFrame(read_csv(f"{path}\\real_estate_price_size_year.csv"))
    print(data.head())
    print(data.describe())

    x_data = data[["size", "year"]]
    y_data = data["price"]
    reg = LinearRegression()
    reg.fit(x_data, y_data)
    print(reg.intercept_)
    print(reg.coef_)
    print(reg.score(x_data, y_data))

    def adj_r2(xda, yda):
        r_square = reg.score(xda, yda)
        num = xda.shape[0]
        predict = xda.shape[1]
        adjusted_r2 = 1 - (1 - r_square) * (num - 1) / (num - predict - 1)
        return adjusted_r2

    print(adj_r2(x_data, y_data))
    print(reg.predict([[750, 2009]]))
    p_values = f_regression(x_data, y_data)[1]
    print(p_values)
    print(p_values.round(3))
    reg_summary = DataFrame(data=x_data.columns.values, columns=["Features"])
    reg_summary["Coefficients"] = reg.coef_
    reg_summary["p-values"] = p_values.round(3)
    print(reg_summary)


if __name__ == "__main__":
    wrapper()
