"""
Practical Example: Hypothesis Testing Exercise
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
            io=f"{PATH}/hypothesis_testing_section.xlsx",
            sheet_name="Dataset",
        )
    )
    data = DataFrame(dat.iloc[3:177, 1:11].values, columns=dat.iloc[2, 1:11])
    data.index.name = None
    data.columns.name = None
    print(data)

    white = data[data["Ethnicity"] == "White"]
    nonwhite = data[data["Ethnicity"] != "White"]
    values = {
        "White n": len(white),
        "NonWhite n": len(nonwhite),
        "White Mean": round(white["Salary"].mean(), 2),
        "NonWhite Mean": round(nonwhite["Salary"].mean(), 2),
        "White Population variance": round(white["Salary"].var(), 2),
        "NonWhite Population variance": round(nonwhite["Salary"].var(), 2),
        "Pooled variance": round(
            (
                (len(white) - 1) * white["Salary"].var()
                + (len(nonwhite) - 1) * nonwhite["Salary"].var()
            )
            / (len(white) + len(nonwhite) - 2),
            2,
        ),
        "p-value": 0.51,
    }
    values["T-score"] = round(
        (nonwhite["Salary"].mean() - white["Salary"].mean())
        / (
            values["Pooled variance"] / len(white)
            + values["Pooled variance"] / len(nonwhite)
        )
        ** 0.5,
        2,
    )
    print(dumps(values, indent=2))


if __name__ == "__main__":
    independent()
