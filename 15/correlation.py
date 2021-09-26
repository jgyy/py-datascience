"""
Correlation Exercise
"""
from os.path import dirname, realpath
from json import dumps
from numpy import corrcoef
from pandas import DataFrame, read_excel, Series
from matplotlib.pyplot import subplots, show

PATH = dirname(realpath(__file__))


def correlation():
    """
    covariance = sum of (x-x̅)*(y-ȳ) / sample size
    """
    data = DataFrame(
        read_excel(
            io=f"{PATH}/correlation_exercise.xlsx",
            sheet_name="Correlation",
        )
    )
    col = data.iloc[8, 2:4]
    cov_data = DataFrame(data.iloc[9:14, 2:4].values, columns=col)

    write = cov_data.iloc[:, 0]
    read = cov_data.iloc[:, 1]
    cov_data["(x-x̅)*(y-ȳ)"] = [
        (write[i] - write.mean()) * (read[i] - read.mean()) for i in range(len(write))
    ]
    print(cov_data)
    cov_dict = {
        "Mean Writing": write.mean().round(0),
        "Mean Reading": read.mean().round(0),
        "Sum": sum(cov_data["(x-x̅)*(y-ȳ)"]),
        "Sample size": len(write),
        "Cov. Sample": sum(cov_data["(x-x̅)*(y-ȳ)"]) / (len(write) - 1),
        "Correlation coefficient": round(
            Series(list(write)).corr(Series(list(read))), 2
        ),
    }
    print(dumps(cov_dict, indent=2))

    _, (ax1, ax2) = subplots(1, 2, figsize=(10, 5))
    ax1.scatter(write, read)
    ax1.set_xlabel("Writing")
    ax1.set_ylabel("Reading")
    ax2.scatter(read, write)
    ax2.set_xlabel("Reading")
    ax2.set_ylabel("Writing")


if __name__ == "__main__":
    correlation()
    show()
