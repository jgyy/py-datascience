"""
Accuracy
"""
from warnings import filterwarnings
from os.path import dirname
import seaborn as sns
from scipy import stats
from statsmodels.api import add_constant, Logit
from pandas import DataFrame, read_csv
from numpy import set_printoptions, array


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
    data = raw_data
    data["Admitted"] = data["Admitted"].map({"Yes": 1, "No": 0})
    data["Gender"] = data["Gender"].map({"Female": 1, "Male": 0})
    print(data)

    y_data = data["Admitted"]
    x1_data = data[["SAT", "Gender"]]
    x_data = add_constant(x1_data)
    reg_log = Logit(y_data, x_data)
    results_log = reg_log.fit()
    print(results_log.summary())
    set_printoptions(formatter={"float": lambda x: f"{round(x, 2)}"})
    print(results_log.predict())
    print(array(data["Admitted"]))
    print(results_log.pred_table())
    cm_df = DataFrame(results_log.pred_table())
    cm_df.columns = ["Predicted 0", "Predicted 1"]
    cm_df = cm_df.rename(index={0: "Actual 0", 1: "Actual 1"})
    print(cm_df)
    confuse_matrix = array(cm_df)
    accuracy_train = (
        confuse_matrix[0, 0] + confuse_matrix[1, 1]
    ) / confuse_matrix.sum()
    print(accuracy_train)


if __name__ == "__main__":
    wrapper1()
