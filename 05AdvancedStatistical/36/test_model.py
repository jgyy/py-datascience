"""
Testing the model
"""
from warnings import filterwarnings
from os.path import dirname
import seaborn as sns
from scipy import stats
from statsmodels.api import add_constant, Logit
from pandas import DataFrame, read_csv
from numpy import array, histogram2d, set_printoptions


def wrapper1():
    """
    wrapper function which description will not change
    """
    filterwarnings("ignore", category=RuntimeWarning)
    sns.set()
    stats.chisqprob = stats.chi2.sf
    path = dirname(__file__)
    raw_data = DataFrame(read_csv(f"{path}\\binary_predictors.csv"))
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

    set_printoptions(formatter={"float": lambda x: str(round(x, 2))})
    print(results_log.predict())
    print(array(data["Admitted"]))
    print(results_log.pred_table())
    cm_df = DataFrame(results_log.pred_table())
    cm_df.columns = ["Predicted 0", "Predicted 1"]
    cm_df = cm_df.rename(index={0: "Actual 0", 1: "Actual 1"})
    print(cm_df)
    cmatrix = array(cm_df)
    accuracy_train = (cmatrix[0, 0] + cmatrix[1, 1]) / cmatrix.sum()
    print(accuracy_train)

    test = DataFrame(read_csv(f"{path}\\test_dataset.csv"))
    print(test)
    test["Admitted"] = test["Admitted"].map({"Yes": 1, "No": 0})
    test["Gender"] = test["Gender"].map({"Female": 1, "Male": 0})
    print(test)
    print(x_data)
    test_actual = test["Admitted"]
    test_data = test.drop(["Admitted"], axis=1)
    test_data = add_constant(test_data.values)
    print(test_data)

    cmatrix = confusion_matrix(test_data, test_actual, results_log)
    print(cmatrix)
    cm_df = DataFrame(cmatrix[0])
    cm_df.columns = ["Predicted 0", "Predicted 1"]
    cm_df = cm_df.rename(index={0: "Actual 0", 1: "Actual 1"})
    print(cm_df)
    miss = cmatrix[0][0][1] + cmatrix[0][1][0]
    print("Missclassification rate: " + str(miss / sum(sum(cmatrix[0]))))


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
