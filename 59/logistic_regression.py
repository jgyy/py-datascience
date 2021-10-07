"""
Creating a logistic regression to predict absenteeism
"""
from os.path import dirname
from pandas import DataFrame, read_csv
from numpy import where, shape, transpose, exp
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


def wrapper():
    """
    wrapper function
    """
    path = dirname(__file__) + "\\"
    data_preprocessed = DataFrame(read_csv(f"{path}absenteeism_preprocessed.csv"))
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
    print(model_outputs.shape[0])
    print(sum((model_outputs == y_train)) / model_outputs.shape[0])
    print(reg.intercept_)
    print(reg.coef_)
    print(unscaled_inputs.columns.values)

    feature_name = unscaled_inputs.columns.values
    summary_table = DataFrame(columns=["Feature name"], data=feature_name)
    summary_table["Coefficient"] = transpose(reg.coef_)
    print(summary_table)
    summary_table["Odds_ratio"] = exp(summary_table.Coefficient)
    print(summary_table)
    print(summary_table.sort_values("Odds_ratio", ascending=False))


if __name__ == "__main__":
    wrapper()
