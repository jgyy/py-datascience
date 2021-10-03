"""
Testing The Model Exercise
"""
from warnings import filterwarnings
from os.path import dirname
import seaborn as sns
from scipy import stats
from statsmodels.api import add_constant, Logit
from pandas import DataFrame, read_csv
from numpy import array, histogram2d
from matplotlib.pyplot import figure, scatter, xlabel, ylabel, show

PATH = dirname(__file__)


def wrapper1():
    """
    wrapper function which description will not change
    """
    filterwarnings("ignore", category=RuntimeWarning)
    sns.set()
    stats.chisqprob = stats.chi2.sf
    raw_data = DataFrame(read_csv(f"{PATH}\\bank_data.csv"))
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
    estimators = ["interest_rate", "credit", "march", "previous", "duration"]
    x1_all = data[estimators]
    y_data = data["y"]
    x_all = add_constant(x1_all.values)
    reg_logit = Logit(y_data, x_all)
    results_logit = reg_logit.fit()
    results_logit.summary2()
    print(confusion_matrix(x_all, y_data, results_logit))

    wrapper2(estimators, x_all, y_data, results_logit)


def wrapper2(estimators, x_all, y_data, results_logit):
    """
    wrapper function part 2
    """
    raw_data2 = DataFrame(read_csv(f"{PATH}\\bank_data_testing.csv"))
    data_test = raw_data2.copy()
    data_test = data_test.drop(["Unnamed: 0"], axis=1)
    data_test["y"] = data_test["y"].map({"yes": 1, "no": 0})
    print(data_test)
    y_test = data_test["y"]
    x1_test = data_test[estimators]
    x_test = add_constant(x1_test.values)
    print(confusion_matrix(x_test, y_test, results_logit))
    print(confusion_matrix(x_all, y_data, results_logit))


def confusion_matrix(data, actual_values, model):
    """
    data: data frame or array
        data is a data frame formatted in the same way as your input data
        e.g. const, var1, var2, etc. Order is very important!
    actual_values: data frame or array
        These are the actual values from the test_data
        In the case of a logistic regression, it should be a single column with 0s and 1s
    model: a LogitResults object
        this is the variable where you have the fitted model
        e.g. results_log in this course
    """
    pred_values = model.predict(data)
    bins = array([0, 0.5, 1])
    cmatrix = histogram2d(actual_values, pred_values, bins=bins)[0]
    accuracy = (cmatrix[0, 0] + cmatrix[1, 1]) / cmatrix.sum()
    return cmatrix, accuracy


if __name__ == "__main__":
    wrapper1()
    show()
