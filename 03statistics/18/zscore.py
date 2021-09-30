"""
Confidence Intervals; Population Variance Known; Z-score; Exercise
"""
from os.path import dirname, realpath
from json import dumps
from math import sqrt
from pandas import DataFrame, read_excel

PATH = dirname(realpath(__file__))


def zscore():
    """
    wrapper function
    """
    table = DataFrame(read_excel(io=f"{PATH}/z_table.xlsx", sheet_name="z-table"))
    ztable = DataFrame(
        table.iloc[5:36, 2:12].values,
        columns=table.iloc[4, 2:12],
        index=table.iloc[5:36, 1],
    )
    ztable.columns.name = "z"
    ztable.index.name = None
    data = DataFrame(
        read_excel(io=f"{PATH}/population_variance_known.xlsx", sheet_name="CI")
    )
    dataset = DataFrame(data.iloc[10:40, 1].values, columns=[data.iloc[9, 1]])

    zdata = {"aci": 0.95, "bci": 0, "zscore": 0}
    for i in range(len(ztable.index)):
        for j in range(len(ztable.columns)):
            if abs(round(zdata["bci"] - zdata["aci"], 4)) >= abs(
                round(ztable.iloc[i, j] - zdata["aci"], 4)
            ):
                zdata["bci"] = ztable.iloc[i, j]
                zdata["zscore"] = round(i * 0.1 + j * 0.01, 2)
    datainfo = {
        "Sample mean": round(dataset.mean().values[0], 0),
        "Population std": 15000,
        "Standard error": round(15000 / sqrt(len(dataset)), 0),
        "z-score": zdata["zscore"],
        "Z": 90,
        "CI low": round(
            dataset.mean().values[0] - (15000 * zdata["zscore"] / sqrt(len(dataset))), 0
        ),
        "CI high": round(
            dataset.mean().values[0] + (15000 * zdata["zscore"] / sqrt(len(dataset))), 0
        ),
    }
    print(dumps(datainfo, indent=2))


if __name__ == "__main__":
    zscore()
