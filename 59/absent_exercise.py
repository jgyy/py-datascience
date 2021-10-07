"""
Creating a logistic regression to predict absenteeism
"""
from os.path import dirname
from pandas import DataFrame, read_csv, concat
from numpy import where, shape, mean, var, transpose, exp
from pickle import dump
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

PATH = dirname(__file__) + "\\"


class CustomScaler(BaseEstimator, TransformerMixin):
    """
    init or what information we need to declare a CustomScaler object
    and what is calculated/declared as we do
    """

    def __init__(self, columns, copy=True, with_mean=True, with_std=True):
        self.scaler = StandardScaler(copy=copy, with_mean=with_mean, with_std=with_std)
        self.columns = columns
        self.mean_ = None
        self.var_ = None

    def fit(self, xdata, ydata=None):
        """
        the fit method, which, again based on StandardScale
        """
        self.scaler.fit(xdata[self.columns], ydata)
        self.mean_ = mean(xdata[self.columns])
        self.var_ = var(xdata[self.columns])
        return self

    def transform(self, xdata):
        """
        the transform method which does the actual scaling
        """
        init_col_order = xdata.columns
        x_scaled = DataFrame(
            self.scaler.transform(xdata[self.columns]), columns=self.columns
        )
        x_not_scaled = xdata.loc[:, ~xdata.columns.isin(self.columns)]
        return concat([x_not_scaled, x_scaled], axis=1)[init_col_order]


def wrapper1():
    """
    wrapper function
    """
    data_preprocessed = DataFrame(read_csv(f"{PATH}absenteeism_preprocessed.csv"))
    print(data_preprocessed.head())
    print(data_preprocessed["Absenteeism Time in Hours"].median())

    targets = where(
        data_preprocessed["Absenteeism Time in Hours"]
        > data_preprocessed["Absenteeism Time in Hours"].median(),
        1,
        0,
    )
    print(targets)
    data_preprocessed["Excessive Absenteeism"] = targets
    print(data_preprocessed.head())
    print(sum(targets) / shape(targets)[0])

    data_with_targets = data_preprocessed.drop(["Absenteeism Time in Hours"], axis=1)
    print(data_with_targets is data_preprocessed)
    print(data_with_targets.head())
    print(data_with_targets.shape)
    print(data_with_targets.iloc[:, :14])
    print(data_with_targets.iloc[:, :-1])

    unscaled_inputs = data_with_targets.iloc[:, :-1]
    absenteeism_scaler = StandardScaler()
    print(unscaled_inputs.columns.values)
    columns_to_omit = ["Reason_1", "Reason_2", "Reason_3", "Reason_4", "Education"]
    columns_to_scale = [
        x for x in unscaled_inputs.columns.values if x not in columns_to_omit
    ]
    absenteeism_scaler = CustomScaler(columns_to_scale)
    absenteeism_scaler.fit(unscaled_inputs)
    scaled_inputs = absenteeism_scaler.transform(unscaled_inputs)
    print(scaled_inputs)
    print(scaled_inputs.shape)

    train_test_split(scaled_inputs, targets)
    x_train, x_test, y_train, y_test = train_test_split(
        scaled_inputs, targets, test_size=0.2, random_state=20
    )
    print(x_train.shape, y_train.shape)
    print(x_test.shape, y_test.shape)
    reg = LogisticRegression()
    reg.fit(x_train, y_train)
    reg.score(x_train, y_train)

    model_outputs = reg.predict(x_train)
    print(model_outputs)
    print(y_train)
    print(model_outputs == y_train)
    print(sum((model_outputs == y_train)))
    print(sum((model_outputs == y_train)) / model_outputs.shape[0])
    print(reg.intercept_)
    print(reg.coef_)
    print(unscaled_inputs.columns.values)

    wrapper2(reg, unscaled_inputs, x_test, y_test, absenteeism_scaler)


def wrapper2(reg, unscaled_inputs, x_test, y_test, absenteeism_scaler):
    """
    wrapper function part 2
    """
    feature_name = unscaled_inputs.columns.values
    summary_table = DataFrame(columns=["Feature name"], data=feature_name)
    summary_table["Coefficient"] = transpose(reg.coef_)
    print(summary_table)
    summary_table.index = summary_table.index + 1
    summary_table.loc[0] = ["Intercept", reg.intercept_[0]]
    summary_table = summary_table.sort_index()
    print(summary_table)
    summary_table["Odds_ratio"] = exp(summary_table.Coefficient)
    print(summary_table)
    print(summary_table.sort_values("Odds_ratio", ascending=False))

    print(reg.score(x_test, y_test))
    predicted_proba = reg.predict_proba(x_test)
    print(predicted_proba)
    print(predicted_proba.shape)
    print(predicted_proba[:, 1])
    with open(f"{PATH}model", "wb") as file:
        dump(reg, file)
    with open(f"{PATH}scaler", "wb") as file:
        dump(absenteeism_scaler, file)


if __name__ == "__main__":
    wrapper1()
