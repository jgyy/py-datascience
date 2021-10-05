"""
Feature selection through Standardization
"""
from warnings import filterwarnings
from os.path import dirname
import seaborn as sns
from pandas import read_csv, DataFrame
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression


def wrapper():
    """
    wrapper function which description will not change
    """
    sns.set()
    filterwarnings("ignore", category=UserWarning)
    path = dirname(__file__)
    data = DataFrame(read_csv(f"{path}\\multiple_linear_regression.csv"))
    print(data.head())
    print(data.describe())

    x_data = data[["SAT", "Rand 1,2,3"]]
    y_data = data["GPA"]
    scaler = StandardScaler()
    scaler.fit(x_data)
    x_scaled = scaler.transform(x_data)
    print(x_scaled)

    reg = LinearRegression()
    reg.fit(x_scaled, y_data)
    print(reg.coef_)
    print(reg.intercept_)
    reg_summary = DataFrame([["Bias"], ["SAT"], ["Rand 1,2,3"]], columns=["Features"])
    reg_summary["Weights"] = reg.intercept_, reg.coef_[0], reg.coef_[1]
    print(reg_summary)

    new_data = DataFrame(data=[[1700, 2], [1800, 1]], columns=["SAT", "Rand 1,2,3"])
    print(new_data)
    print(reg.predict(new_data))
    new_data_scaled = scaler.transform(new_data)
    print(new_data_scaled)
    print(reg.predict(new_data_scaled))
    reg_simple = LinearRegression()
    x_simple_matrix = x_scaled[:, 0].reshape(-1, 1)
    reg_simple.fit(x_simple_matrix, y_data)
    reg_simple.predict(new_data_scaled[:, 0].reshape(-1, 1))


if __name__ == "__main__":
    wrapper()
