"""
Confidence Intervals; Population Variance Unknown; T-score; Exercise
"""
from os.path import dirname, realpath
from json import dumps
from math import sqrt
from pandas import DataFrame, read_excel

PATH = dirname(realpath(__file__))


def tscore():
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
        read_excel(io=f"{PATH}/population_variance_unknown.xlsx", sheet_name="Salaries")
    )
    dataset = DataFrame(data.iloc[10:19, 1].values, columns=[data.iloc[9, 1]])
    print(ttable)
    print(dataset)

    zdata = {"df": len(dataset) - 1, "α": 0.005, "tscore": 0}
    datainfo = {
        "Mean": round(dataset.mean().values[0], 0),
        "St. deviation": round(dataset.std().values[0], 0),
        "Standard error": round(dataset.std().values[0] / sqrt(len(dataset)), 0),
        "Task 2": "Population variance is unknown. "
        + "We have a small sample. "
        + "We assume that the population is normally distributed. "
        + "The appropriate statistic to use is the t-statistic.",
        "t-score": round(ttable.loc[zdata["df"], zdata["α"]], 2),
        "T": 99,
        "CI low": round(
            dataset.mean().values[0]
            - (
                dataset.std().values[0]
                * ttable.loc[zdata["df"], zdata["α"]]
                / sqrt(len(dataset))
            ),
            0,
        ),
        "CI high": round(
            dataset.mean().values[0]
            + (
                dataset.std().values[0]
                * ttable.loc[zdata["df"], zdata["α"]]
                / sqrt(len(dataset))
            ),
            0,
        ),
    }
    print(dumps(datainfo, indent=2))


if __name__ == "__main__":
    tscore()
