"""
The Standard Normal Distribution Exercise
"""
from os.path import dirname, realpath
from pandas import DataFrame, read_excel
from matplotlib.pyplot import figure, show, hist, xlabel, ylabel, grid

PATH = dirname(realpath(__file__))


def standard():
    """
    wrapper function
    """
    data = DataFrame(
        read_excel(
            io=f"{PATH}/standard_normal_distribution_exercise.xlsx",
            sheet_name="Standard normal",
        )
    )
    dataset = DataFrame(data.iloc[9:999, 1].values, columns=[data.iloc[8, 1]]).dropna(
        how="all"
    )
    figure("Original dataset")
    hist(dataset)
    xlabel("Data")
    ylabel("Frequency")
    grid(True)
    odmean = round(dataset.mean(), 2).values[0]
    odstd = round(dataset.std(), 2).values[0]
    print(f"Original dataset: mean={odmean}, std={odstd}")

    subtract = DataFrame(dataset.applymap(lambda x: x - odmean)).rename(
        columns={"Original dataset": "Subtract mean"}
    )
    figure("Subtract mean")
    hist(subtract)
    xlabel("Data")
    ylabel("Frequency")
    grid(True)
    submean = round(subtract.mean(), 2).values[0]
    substd = round(subtract.std(), 2).values[0]
    print(f"Subtract mean: mean={submean}, std={substd}")

    standards = DataFrame(subtract.applymap(lambda x: x/substd)).rename(
        columns={"Subtract mean": "Standardized"}
    )
    figure("Standardized")
    hist(standards)
    xlabel("Data")
    ylabel("Frequency")
    grid(True)
    standmean = round(standards.mean(), 2).values[0]
    standstd = round(standards.std(), 2).values[0]
    print(f"Standardized: mean={standmean}, std={standstd}")


if __name__ == "__main__":
    standard()
    show()
