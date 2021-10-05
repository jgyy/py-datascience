"""
Basics of logistic regression
"""
from warnings import filterwarnings
from os.path import dirname
import seaborn as sns
from scipy import stats
from statsmodels.api import add_constant, Logit
from pandas import DataFrame, read_csv
from numpy import array, exp, sort, ones
from matplotlib.pyplot import show, figure, plot, scatter


def wrapper1():
    """
    wrapper function which description will not change
    """
    filterwarnings("ignore", category=RuntimeWarning)
    sns.set()
    stats.chisqprob = stats.chi2.sf
    path = dirname(__file__)
    raw_data = DataFrame(read_csv(f"{path}\\admittance.csv"))
    print(raw_data)
    data = raw_data.copy()
    data["Admitted"] = data["Admitted"].map({"Yes": 1, "No": 0})
    print(data)

    y_data = data["Admitted"]
    x1_data = data["SAT"]
    x_data = add_constant(list(x1_data))
    reg_log = Logit(y_data, x_data)
    results_log = reg_log.fit()
    print(results_log.summary())
    const = ones(168)
    print(const)
    reg_null = Logit(y_data, const)
    results_null = reg_null.fit()
    print(results_null.summary())

    reg_log = Logit(y_data, x_data)
    results_log = reg_log.fit()
    func = lambda x, b0, b1: array(exp(b0 + x * b1) / (1 + exp(b0 + x * b1)))
    f_sorted = sort(func(x1_data, results_log.params[0], results_log.params[1]))
    x_sorted = sort(array(x1_data))
    figure(figsize=(20, 20))
    scatter(x1_data, y_data, color="C0")
    plot(x_sorted, f_sorted, color="red")


if __name__ == "__main__":
    wrapper1()
    show()
