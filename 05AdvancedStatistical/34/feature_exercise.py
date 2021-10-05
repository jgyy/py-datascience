"""
Feature scaling with sklearn - Exercise
"""
from warnings import filterwarnings
from os.path import dirname
import seaborn as sns
from pandas import read_csv, DataFrame
from sklearn.preprocessing import StandardScaler
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
    scaler = StandardScaler()
    scaler.fit(x_data)
    x_scaled = scaler.transform(x_data)
    reg = LinearRegression()
    reg.fit(x_scaled, y_data)
    print(reg.intercept_)
    print(reg.coef_)
    print(reg.score(x_scaled, y_data))

    def adj_r2(xda, yda):
        rsquare = reg.score(xda, yda)
        num = xda.shape[0]
        predict = xda.shape[1]
        adjusted_r2 = 1 - (1 - rsquare) * (num - 1) / (num - predict - 1)
        return adjusted_r2

    print(adj_r2(x_scaled, y_data))
    new_data = [[750, 2009]]
    new_data_scaled = scaler.transform(new_data)
    reg.predict(new_data_scaled)
    p_values = f_regression(x_data, y_data)[1]
    print(p_values)
    print(p_values.round(3))
    reg_summary = DataFrame(data=x_data.columns.values, columns=["Features"])
    reg_summary["Coefficients"] = reg.coef_
    reg_summary["p-values"] = p_values.round(3)
    print(reg_summary)


if __name__ == "__main__":
    wrapper()
