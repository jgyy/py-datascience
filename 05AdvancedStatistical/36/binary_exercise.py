"""
Binary Predictors in a Logistic Regression
"""
from warnings import filterwarnings
from os.path import dirname
import seaborn as sns
from scipy import stats
from statsmodels.api import add_constant, Logit
from pandas import DataFrame, read_csv
from matplotlib.pyplot import figure, scatter, xlabel, ylabel, show


def wrapper1():
    """
    wrapper function which description will not change
    """
    filterwarnings("ignore", category=RuntimeWarning)
    sns.set()
    stats.chisqprob = stats.chi2.sf
    path = dirname(__file__)
    raw_data = DataFrame(read_csv(f"{path}\\bank_data.csv"))
    print(raw_data)

    data = raw_data.copy()
    data = data.drop(["Unnamed: 0"], axis=1)
    data["y"] = data["y"].map({"yes": 1, "no": 0})
    print(data)
    print(data.describe())
    y_data = data["y"]
    x1_data = data["duration"]
    x_data = add_constant(x1_data.values)
    reg_log = Logit(y_data, x_data)
    results_log = reg_log.fit()
    print(results_log.summary())
    figure()
    scatter(x1_data, y_data, color="C0")
    xlabel("Duration", fontsize=20)
    ylabel("Subscription", fontsize=20)


if __name__ == "__main__":
    wrapper1()
    show()
