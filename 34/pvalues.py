"""
How to (properly) include p-values with sklearn
"""
from os.path import dirname
import seaborn as sns
from pandas import read_csv, DataFrame
from scipy.stats import t
import numpy as np
from numpy import array, sqrt, diagonal, dot, squeeze
from numpy.linalg import inv
from sklearn.linear_model import LinearRegression


class LinearRegress(LinearRegression):
    """
    LinearRegression class after sklearn's, but calculate t-statistics
    and p-values for model coefficients (betas).
    """

    # nothing changes in __init__
    def __init__(self, fit_intercept=True, copy_X=True, n_jobs=1):
        super().__init__()
        self.fit_intercept = fit_intercept
        self.copy_X = copy_X
        self.n_jobs = n_jobs
        self.t_statistic = 0
        self.p_value = 0

    def fit(self, X, y, sample_weight=1):
        super().fit(X, y, sample_weight)

        # Calculate SSE (sum of squared errors)
        # and SE (standard error)
        sse = np.sum((self.predict(X) - y) ** 2, axis=0) / float(
            X.shape[0] - X.shape[1]
        )
        s_error = array([sqrt(diagonal(sse * inv(dot(X.T, X))))])

        # compute the t-statistic for each feature
        self.t_statistic = self.coef_ / s_error
        # find the p-value for each feature
        self.p_value = squeeze(
            2 * (1 - t.cdf(np.abs(self.t_statistic), y.shape[0] - X.shape[1]))
        )
        return self


def wrapper():
    """
    wrapper function which description will not change
    """
    sns.set()
    path = dirname(__file__)
    data = DataFrame(read_csv(f"{path}\\multiple_linear_regression.csv"))
    print(data.head())
    print(data.describe())

    x_data = data[["SAT", "Rand 1,2,3"]]
    y_data = data["GPA"]
    reg_with_pvalues = LinearRegress()
    reg_with_pvalues.fit(x_data, y_data)
    print(reg_with_pvalues.p_value)
    reg_summary = DataFrame([["SAT"], ["Rand 1,2,3"]], columns=["Features"])
    reg_summary["Coefficients"] = reg_with_pvalues.coef_
    reg_summary["p-values"] = reg_with_pvalues.p_value.round(3)
    print(reg_summary)


if __name__ == "__main__":
    wrapper()
