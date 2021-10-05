"""
Calculating the Accuracy of the Model
"""
from warnings import filterwarnings
from os.path import dirname
import seaborn as sns
from scipy import stats
from statsmodels.api import add_constant, Logit
from pandas import DataFrame, read_csv
from numpy import array, histogram2d
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
    estimators = ["interest_rate", "march", "credit", "previous", "duration"]
    x1_estimate = data[estimators]
    y_data = data["y"]
    x_estimate = add_constant(x1_estimate.values)
    reg_logit = Logit(y_data, x_estimate)
    results_logit = reg_logit.fit()
    print(results_logit.summary2())

    def confusion_matrix(data, actual_values, model):
        pred_values = model.predict(data)
        bins = array([0, 0.5, 1])
        confuse_m = histogram2d(actual_values, pred_values, bins=bins)[0]
        accuracy = (confuse_m[0, 0] + confuse_m[1, 1]) / confuse_m.sum()
        return confuse_m, accuracy

    print(confusion_matrix(x_estimate, y_data, results_logit))


if __name__ == "__main__":
    wrapper1()
    show()
