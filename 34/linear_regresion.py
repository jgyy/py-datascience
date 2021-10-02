"""
Simple linear regression
"""
from os.path import dirname
import seaborn as sns
from pandas import read_csv, DataFrame
from sklearn.linear_model import LinearRegression
from matplotlib.pyplot import scatter, figure, plot, xlabel, ylabel, show


def wrapper():
    """
    wrapper function which description will not change
    """
    sns.set()
    path = dirname(__file__)
    data = DataFrame(read_csv(f"{path}\\simple_linear_regression.csv"))
    print(data.head())

    x_data = data["SAT"]
    y_data = data["GPA"]
    print(x_data.shape)
    print(y_data.shape)
    x_matrix = x_data.values.reshape(-1, 1)
    print(x_matrix.shape)
    reg = LinearRegression()
    reg.fit(x_matrix, y_data)
    print(reg.score(x_matrix, y_data))
    print(reg.coef_)
    print(reg.intercept_)
    print(reg.predict([[1740]]))

    new_data = DataFrame(data=[1740, 1760], columns=["SAT"])
    print(new_data)
    print(reg.predict(new_data.values))
    new_data["Predicted_GPA"] = reg.predict(new_data.values)
    print(new_data)

    figure()
    scatter(x_data, y_data)
    yhat = reg.coef_ * x_matrix + reg.intercept_
    plot(x_data, yhat, lw=4, c="orange", label="regression line")
    xlabel("SAT", fontsize=20)
    ylabel("GPA", fontsize=20)


if __name__ == "__main__":
    wrapper()
    show()
