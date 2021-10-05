"""
Dummy variables or how to deal with categorical predictors
"""
from os.path import dirname
import seaborn as sns
from pandas import read_csv, DataFrame
from statsmodels.api import add_constant, OLS
from matplotlib.pyplot import figure, scatter, plot, xlabel, ylabel, show


def wrapper():
    """
    wrapper function which description will not change
    """
    sns.set()
    path = dirname(__file__)
    raw_data = DataFrame(read_csv(f"{path}\\dummies.csv"))
    print(raw_data)
    data = raw_data.copy()
    data["Attendance"] = data["Attendance"].map({"Yes": 1, "No": 0})
    print(data)
    print(data.describe())

    y_data = data["GPA"]
    x1_data = data[["SAT", "Attendance"]]
    x_data = add_constant(x1_data.values)
    results = OLS(y_data, x_data).fit()
    print(results.summary())

    figure()
    scatter(data["SAT"], y_data)
    yhat_no = 0.6439 + 0.0014 * data["SAT"]
    yhat_yes = 0.8665 + 0.0014 * data["SAT"]
    plot(data["SAT"], yhat_no, lw=2, c="#006837")
    plot(data["SAT"], yhat_yes, lw=2, c="#a50026")
    xlabel("SAT", fontsize=20)
    ylabel("GPA", fontsize=20)

    figure()
    scatter(data["SAT"], data["GPA"], c=data["Attendance"], cmap="RdYlGn_r")
    yhat_no = 0.6439 + 0.0014 * data["SAT"]
    yhat_yes = 0.8665 + 0.0014 * data["SAT"]
    plot(data["SAT"], yhat_no, lw=2, c="#006837")
    plot(data["SAT"], yhat_yes, lw=2, c="#a50026")
    xlabel("SAT", fontsize=20)
    ylabel("GPA", fontsize=20)

    figure()
    scatter(data["SAT"], data["GPA"], c=data["Attendance"], cmap="RdYlGn_r")
    yhat_no = 0.6439 + 0.0014 * data["SAT"]
    yhat_yes = 0.8665 + 0.0014 * data["SAT"]
    yhat = 0.0017 * data["SAT"] + 0.275
    plot(data["SAT"], yhat_no, lw=2, c="#006837", label="regression line1")
    plot(data["SAT"], yhat_yes, lw=2, c="#a50026", label="regression line2")
    plot(data["SAT"], yhat, lw=3, c="#4C72B0", label="regression line")
    xlabel("SAT", fontsize=20)
    ylabel("GPA", fontsize=20)

    print(x_data)
    new_data = DataFrame({"const": 1, "SAT": [1700, 1670], "Attendance": [0, 1]})
    new_data = new_data[["const", "SAT", "Attendance"]]
    print(new_data)
    new_data.rename(index={0: "Bob", 1: "Alice"})
    predictions = results.predict(new_data)
    print(predictions)
    predictionsdf = DataFrame({"Predictions": predictions})
    joined = new_data.join(predictionsdf)
    joined.rename(index={0: "Bob", 1: "Alice"})


if __name__ == "__main__":
    wrapper()
    show()
