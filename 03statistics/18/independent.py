"""
Confidence intervals. Two means. Independent Samples (Part 2). Exercise
"""
from os.path import dirname, realpath
from json import dumps
from math import sqrt
from pandas import DataFrame, read_excel

PATH = dirname(realpath(__file__))


def independent():
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
            io=f"{PATH}/confidence_intervals_two_means_independent_samples.xlsx",
            sheet_name="CI, indep, var unkwn",
        )
    )
    dataset = DataFrame(data.iloc[9:19, 1:3].values, columns=data.iloc[8, 1:3])
    dataset.index.name = None
    dataset.columns.name = None
    nya = dataset.loc[:, "NY apples"]
    laa = dataset.loc[:, "LA apples"].dropna()
    print(dataset)

    tdata = {"df": len(nya) + len(laa) - 1, "α": round((1 - 0.90) / 2, 3)}
    tdata["t"] = ttable.loc[tdata["df"], tdata["α"]]
    datainfo = {
        "Sample mean NY": round(nya.mean(), 2),
        "Sample std NY": round(nya.std(), 2),
        "Sample size NY": len(nya),
        "Sample mean LA": round(laa.mean(), 2),
        "Sample std LA": round(laa.std(), 2),
        "Sample size LA": len(laa),
        "Pooled variance": round(
            (nya.std() ** 2 * (len(nya) - 1) + laa.std() ** 2 * (len(laa) - 1))
            / (len(nya) + len(laa) - 2),
            2,
        ),
        "t-score": round(tdata["t"], 2),
        "T": 90,
    }
    datainfo["Pooled std"] = round(sqrt(datainfo["Pooled variance"]), 2)
    datainfo["CI low"] = round(
        nya.mean()
        - laa.mean()
        - tdata["t"]
        * sqrt(
            datainfo["Pooled variance"] / len(nya)
            + datainfo["Pooled variance"] / len(laa)
        ),
        2,
    )
    datainfo["CI high"] = round(
        nya.mean()
        - laa.mean()
        + tdata["t"]
        * sqrt(
            datainfo["Pooled variance"] / len(nya)
            + datainfo["Pooled variance"] / len(laa)
        ),
        2,
    )

    print(dumps(datainfo, indent=2))
    print("Task 2: A lower confidence results in a narrower interval.")


if __name__ == "__main__":
    independent()
