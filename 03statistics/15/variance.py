"""
Variance Exercise
"""
from os.path import dirname, realpath
from pandas import DataFrame, read_excel

PATH = dirname(realpath(__file__))


def variance():
    """
    wrapper function
    """
    data = DataFrame(
        read_excel(
            io=f"{PATH}/variance_exercise.xlsx",
            sheet_name="Variance",
        )
    )
    data = DataFrame(data.iloc[10:21, 1].values, columns=[data.iloc[9, 1]])
    print(data)
    vari = round(data.var().values[0], 2)
    print(f"Annual Income Variance: $ {vari}")


if __name__ == "__main__":
    variance()
