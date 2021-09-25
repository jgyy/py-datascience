"""
Numerical Variables
"""
from os.path import dirname, realpath
from numpy import arange
from pandas import DataFrame, read_excel

PATH = dirname(realpath(__file__))


def numerical():
    """
    wrapper function
    """
    data = DataFrame(
        read_excel(
            io=f"{PATH}/numerical_variables.xlsx",
            sheet_name="Frequency distribution table",
        )
    )
    dataset = data.iloc[16:36, 1]
    desire_inv = 6
    inv_width = (max(dataset) - min(dataset)) / desire_inv
    col = [data.iloc[20, 8 + i] for i in range(4)]
    start = arange(min(dataset), max(dataset), inv_width)
    end = list(start[1:]) + [max(dataset)]
    absolute = dataset.value_counts(
        bins=list(start) + [max(dataset)], sort=False
    ).tolist()
    relative = [a / len(dataset) for a in absolute]
    table = DataFrame({col[0]: start, col[1]: end, col[2]: absolute, col[3]: relative})
    print(table)


if __name__ == "__main__":
    numerical()
