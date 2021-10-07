"""
Absenteeism Exercise Preprocessing
"""
from os.path import dirname
from pandas import DataFrame, read_csv, get_dummies, concat


def wrapper():
    """
    wrapper function
    """
    path = dirname(__file__) + "\\"
    raw_csv_data = DataFrame(read_csv(f"{path}absenteeism_data.csv"))
    dataf = raw_csv_data.copy()
    dataf = dataf.drop(["ID"], axis=1)
    reason_columns = get_dummies(dataf["Reason for Absence"])
    reason_columns["check"] = reason_columns.sum(axis=1)
    reason_columns = reason_columns.drop(["check"], axis=1)
    reason_columns = get_dummies(dataf["Reason for Absence"], drop_first=True)
    dataf = dataf.drop(["Reason for Absence"], axis=1)
    reason_type_1 = reason_columns.loc[:, 1:14].max(axis=1)
    reason_type_2 = reason_columns.loc[:, 15:17].max(axis=1)
    reason_type_3 = reason_columns.loc[:, 18:21].max(axis=1)
    reason_type_4 = reason_columns.loc[:, 22:].max(axis=1)

    dataf = concat(
        [dataf, reason_type_1, reason_type_2, reason_type_3, reason_type_4], axis=1
    )
    column_names = [
        "Date",
        "Transportation Expense",
        "Distance to Work",
        "Age",
        "Daily Work Load Average",
        "Body Mass Index",
        "Education",
        "Children",
        "Pets",
        "Absenteeism Time in Hours",
        "Reason_1",
        "Reason_2",
        "Reason_3",
        "Reason_4",
    ]
    dataf.columns = column_names
    column_names_reordered = [
        "Reason_1",
        "Reason_2",
        "Reason_3",
        "Reason_4",
        "Date",
        "Transportation Expense",
        "Distance to Work",
        "Age",
        "Daily Work Load Average",
        "Body Mass Index",
        "Education",
        "Children",
        "Pets",
        "Absenteeism Time in Hours",
    ]
    dataf = dataf[column_names_reordered]
    df_reason_mod = dataf.copy()
    print(df_reason_mod)


if __name__ == "__main__":
    wrapper()
