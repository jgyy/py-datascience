"""
Binary Predictors
"""
from warnings import filterwarnings
from os.path import dirname
import seaborn as sns
from scipy import stats
from statsmodels.api import add_constant, Logit
from pandas import DataFrame, read_csv


def wrapper1():
    """
    wrapper function which description will not change
    """
    filterwarnings("ignore", category=RuntimeWarning)
    sns.set()
    stats.chisqprob = stats.chi2.sf
    path = dirname(__file__)
    raw_data = DataFrame(read_csv(f"{path}\\binary_predictors.csv"))
    print(raw_data)

    data = raw_data.copy()
    data["Admitted"] = data["Admitted"].map({"Yes": 1, "No": 0})
    data["Gender"] = data["Gender"].map({"Female": 1, "Male": 0})
    print(data)
    y_data = data["Admitted"]
    x1_data = data[["SAT", "Gender"]]
    x_data = add_constant(x1_data.values)
    reg_log = Logit(y_data, x_data)
    results_log = reg_log.fit()
    print(results_log.summary())


if __name__ == "__main__":
    wrapper1()
