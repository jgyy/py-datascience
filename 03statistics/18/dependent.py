"""
Confidence Intervals; Population Variance Unknown; T-score; Exercise
"""
from os.path import dirname, realpath
from json import dumps
from math import sqrt
from pandas import DataFrame, read_excel

PATH = dirname(realpath(__file__))


def dependent():
    """
    wrapper function
    """
    table = DataFrame(read_excel(io=f"{PATH}/t_table.xlsx", sheet_name="t-table"))
    ttable = DataFrame(
        table.iloc[5:41, 2:7].values,
        columns=table.iloc[4, 2:7],
        index=table.iloc[5:41, 1],
    )
    ttable.index.name = None
    ttable.columns.name = "d.f. / α"
    data = DataFrame(
        read_excel(
            io=f"{PATH}/confidence_intervals_two_means_dependent_samples.xlsx",
            sheet_name="Data in kg",
        )
    )
    dataset = DataFrame(data.iloc[13:23, 1:5].values, columns=data.iloc[12, 1:5])
    dataset.index.name = None
    dataset.columns.name = None
    difference = dataset.loc[:, "Difference"]
    print(dataset)

    zdata = {"df": len(difference) - 1, "α": round((1 - 0.95) / 2, 3)}
    datainfo = {
        "Mean": round(difference.mean(), 2),
        "St. deviation": round(difference.std(), 2),
        "t-score": round(ttable.loc[zdata["df"], zdata["α"]], 2),
        "T": 95,
        "CI low": round(
            difference.mean()
            - (
                difference.std()
                * ttable.loc[zdata["df"], zdata["α"]]
                / sqrt(len(difference))
            ),
            2,
        ),
        "CI high": round(
            difference.mean()
            + (
                difference.std()
                * ttable.loc[zdata["df"], zdata["α"]]
                / sqrt(len(difference))
            ),
            2,
        ),
    }

    print(dumps(datainfo, indent=2))
    print(
        "Task 2: Population variance is unknown.",
        "We have a small sample.",
        "We assume that the population is normally distributed",
        "The appropriate statistic to use is the t-statistic.",
    )
    print(
        f"Task 4: You are {datainfo['T']}% confident that you will lose between",
        f"{abs(datainfo['CI low'])} and {abs(datainfo['CI high'])} kg,",
        "given that you follow the program as strict as the sample.",
    )


if __name__ == "__main__":
    dependent()
