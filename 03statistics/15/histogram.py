"""
Histogram Exercise
"""
from os.path import dirname, realpath
from numpy import arange
from pandas import DataFrame, read_excel
from matplotlib.pyplot import figure, show

PATH = dirname(realpath(__file__))


def histogram():
    """
    wrapper function
    """
    data = DataFrame(
        read_excel(
            io=f"{PATH}/histogram_exercise.xlsx",
            sheet_name="The histogram",
        )
    )
    dataset = data.iloc[9:29, 1]
    print(dataset)
    desire_inv = 10
    inv_width = (max(dataset) - min(dataset)) / desire_inv

    col = [data.iloc[13, 3 + i] for i in range(4)]
    start = arange(min(dataset), max(dataset), inv_width)
    end = list(start[1:]) + [max(dataset)]
    absolute = dataset.value_counts(
        bins=list(start) + [max(dataset)], sort=False
    ).tolist()
    relative = [a / len(dataset) for a in absolute]
    table = DataFrame({col[0]: start, col[1]: end, col[2]: absolute, col[3]: relative})
    print(table)

    fig1 = figure().add_axes([0.1, 0.1, 0.85, 0.85])
    fig1.hist(dataset)


if __name__ == "__main__":
    histogram()
    show()
