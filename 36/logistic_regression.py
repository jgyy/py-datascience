"""
Basics of logistic regression
"""
from warnings import filterwarnings
from os.path import dirname
import seaborn as sns
from statsmodels.api import add_constant, OLS, Logit
from pandas import DataFrame, read_csv
from numpy import array, exp, sort
from matplotlib.pyplot import show, figure, plot, scatter, xlabel, ylabel


def wrapper1():
    """
    wrapper function which description will not change
    """
    filterwarnings("ignore", category=RuntimeWarning)
    sns.set()
    path = dirname(__file__)
    raw_data = DataFrame(read_csv(f"{path}\\admittance.csv"))
    print(raw_data)
    data = raw_data.copy()
    data["Admitted"] = data["Admitted"].map({"Yes": 1, "No": 0})
    print(data)

    y_data = data["Admitted"]
    x1_data = data["SAT"]
    figure()
    scatter(x1_data, y_data, color="C0")
    xlabel("SAT", fontsize=20)
    ylabel("Admitted", fontsize=20)

    x_data = add_constant(list(x1_data))
    reg_lin = OLS(y_data, x_data)
    results_lin = reg_lin.fit()
    figure()
    scatter(x1_data, y_data, color="C0")
    y_hat = x1_data * results_lin.params[1] + results_lin.params[0]
    plot(x1_data, y_hat, lw=2.5, color="C8")
    xlabel("SAT", fontsize=20)
    ylabel("Admitted", fontsize=20)

    reg_log = Logit(y_data, x_data)
    results_log = reg_log.fit()
    func = lambda x, b0, b1: array(exp(b0 + x * b1) / (1 + exp(b0 + x * b1)))
    f_sorted = sort(func(x1_data, results_log.params[0], results_log.params[1]))
    x_sorted = sort(array(x1_data))
    figure()
    scatter(x1_data, y_data, color="C0")
    xlabel("SAT", fontsize=20)
    ylabel("Admitted", fontsize=20)
    plot(x_sorted, f_sorted, color="C8")


if __name__ == "__main__":
    wrapper1()
    show()
