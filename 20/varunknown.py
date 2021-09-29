"""
Test for the Mean. Population Variance Unknown Exercise
"""
from os.path import dirname, realpath
from json import dumps
from pandas import DataFrame, read_excel

PATH = dirname(realpath(__file__))


def variance_unknown():
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

    dat = DataFrame(
        read_excel(
            io=f"{PATH}/population_variance_unknown_exercise.xlsx",
            sheet_name="Open rate dataset",
        )
    )
    data = DataFrame(dat.iloc[11:21, 1].values, columns=[dat.iloc[10, 1]])
    data.index.name = None
    data.columns.name = None

    tdata5 = {"df": len(data) - 1, "α": round(0.05 / 2, 3)}
    tdata1 = {"df": len(data) - 1, "α": round(0.01 / 2, 3)}

    print(data)
    values = {
        "Sample mean": round(data.mean().values[0] * 100, 2),
        "Sample standard dev": round(data.std().values[0] * 100, 2),
        "Standard error": round(data.std().values[0] * 100 / len(data) ** 0.5, 2),
        "Sample size": len(data),
        "Null hypothesis value": 40,
        "T-score": round(
            (data.mean().values[0] - 0.4)
            / (data.std().values[0] / len(data) ** 0.5),
            2,
        ),
        "t 9, 5% significance": round(ttable.loc[tdata5["df"], tdata5["α"]], 2),
        "t 9, 1% significance": round(ttable.loc[tdata1["df"], tdata1["α"]], 2),
        "p-value": 0.608,
    }
    print(dumps(values, indent=2))
    print(
        "Task 1.3: The p-value of this test is 0.608. 0.608 > 0.05 and 0.01,",
        "therefore, we cannot reject the null hypothesis.",
    )


if __name__ == "__main__":
    variance_unknown()
