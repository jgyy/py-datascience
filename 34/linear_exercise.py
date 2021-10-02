"""
Simple linear regression - Exercise
"""
from os.path import dirname
import seaborn as sns
from pandas import read_csv, DataFrame
from sklearn.linear_model import LinearRegression
from matplotlib.pyplot import scatter, xlabel, ylabel, show, figure


def wrapper():
    """
    wrapper function which description will not change
    """
    sns.set()
    path = dirname(__file__)
    data = DataFrame(read_csv(f"{path}\\real_estate_price_size.csv"))
    print(data.head())
    print(data.describe())

    x_data = data["size"]
    y_data = data["price"]
    figure()
    scatter(x_data, y_data)
    xlabel("Size", fontsize=20)
    ylabel("Price", fontsize=20)

    x_matrix = x_data.values.reshape(-1, 1)
    reg = LinearRegression()
    reg.fit(x_matrix, y_data)
    print(reg.score(x_matrix, y_data))
    print(reg.intercept_)
    print(reg.coef_)
    print(reg.predict([[750]]))


if __name__ == "__main__":
    wrapper()
    show()
