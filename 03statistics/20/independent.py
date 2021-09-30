"""
Test for the mean. Independent Samples (Part 2). Exercise
"""
from os.path import dirname, realpath
from json import dumps
from pandas import DataFrame, read_excel

PATH = dirname(realpath(__file__))


def independent():
    """
    wrapper function
    """
    dat = DataFrame(
        read_excel(
            io=f"{PATH}/independent_samples_exercise.xlsx",
            sheet_name="Data",
        )
    )
    data = DataFrame(
        dat.iloc[8:11, 2:4].values, columns=dat.iloc[7, 2:4], index=dat.iloc[8:11, 1]
    )
    data.index.name = None
    data.columns.name = None
    print(data)

    values = {
        "Sample Variances Monday": data.loc["Std. deviation", "Monday"] ** 2,
        "Sample Variances Saturday": data.loc["Std. deviation", "Saturday"] ** 2,
        "p-value": 0.16,
    }
    values["Pooled Variance"] = round(
        (
            (data.loc["Sample size", "Monday"] - 1) * values["Sample Variances Monday"]
            + (data.loc["Sample size", "Saturday"] - 1)
            * values["Sample Variances Saturday"]
        )
        / (data.loc["Sample size", "Monday"] + data.loc["Sample size", "Saturday"] - 2),
        2,
    )
    values["T-score"] = round(
        (data.loc["Mean", "Monday"] - data.loc["Mean", "Saturday"])
        / (
            values["Pooled Variance"] / data.loc["Sample size", "Monday"]
            + values["Pooled Variance"] / data.loc["Sample size", "Saturday"]
        )
        ** 0.5,
        2,
    )
    print(dumps(values, indent=2))


if __name__ == "__main__":
    independent()
