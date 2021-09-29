"""
Test for the Mean. Population Variance Known Exercise
"""
from os.path import dirname, realpath
from json import dumps
from pandas import DataFrame, read_excel

PATH = dirname(realpath(__file__))


def variance_known():
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

    dat = DataFrame(
        read_excel(
            io=f"{PATH}/population_variance_known_exercise.xlsx",
            sheet_name="Data",
        )
    )
    data = DataFrame(dat.iloc[8:38, 1].values, columns=[dat.iloc[7, 1]])
    data.index.name = None
    data.columns.name = None

    # Scan across each cell in the ztable to find the zscore closest to the percentage
    zdata = {"aci": 1 - (0.1 / 2), "bci": 0, "zscore": 0}
    for i in range(len(ztable.index)):
        for j in range(len(ztable.columns)):
            if abs(round(zdata["bci"] - zdata["aci"], 4)) >= abs(
                round(ztable.iloc[i, j] - zdata["aci"], 4)
            ):
                zdata["bci"] = ztable.iloc[i, j]
                zdata["zscore"] = round(i * 0.1 + j * 0.01, 2)

    print(data)
    values = {
        "Sample mean": round(data.mean().values[0], 0),
        "Population std": 15000,
        "Standard error": round(15000 / len(data) ** 0.5, 0),
        "Sample size": len(data),
        "H0 (Glassdoor data)": 113000,
        "Z-score": round(
            (data.mean().values[0] - 113000) / (15000 / len(data) ** 0.5), 2
        ),
        "z0.05": zdata["zscore"],
    }
    print(dumps(values, indent=2))
    print(
        f"Task 1: {abs(values['Z-score'])} > {values['z0.05']},",
        "therefore, we reject the null hypothesis.",
        "There was no need for the test as we have already rejected it lower significance levels.",
        "You could simply say that you would reject the null hypothesis.",
    )


if __name__ == "__main__":
    variance_known()
