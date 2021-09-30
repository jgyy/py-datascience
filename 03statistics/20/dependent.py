"""
Test for the Mean. Dependent Samples Exercise
"""
from os.path import dirname, realpath
from json import dumps
from pandas import DataFrame, read_excel

PATH = dirname(realpath(__file__))


def dependent():
    """
    wrapper function
    """
    dat = DataFrame(
        read_excel(
            io=f"{PATH}/dependent_samples_exercise.xlsx",
            sheet_name="Weight-loss data, kg",
        )
    )
    data = DataFrame(dat.iloc[15:25, 1:4].values, columns=dat.iloc[14, 1:4])
    data.index.name = None
    data.columns.name = None
    print(data)

    difference = data["Difference (A - B, kg)"]
    values = {
        "Sample mean": round(difference.mean(), 2),
        "Standard deviation": round(difference.std(), 2),
        "Standard error": round(difference.std() / len(difference) ** 0.5, 2),
        "T-score": round(
            difference.mean() / (difference.std() / len(difference) ** 0.5), 2
        ),
        "p-value": 0.038,
        "Sample size": len(difference),
    }
    print(dumps(values, indent=2))
    task_dict = {
        "p-value": [0.038, 0.038, 0.038],
        "significance": [0.01, 0.05, 0.10],
        "Decision": ["Accept", "Reject", "Reject"],
        "Comment": [
            "At 1% significance we accept the null hypothesis. "
            + "The data shows that the program is not working.",
            "At 5% significance, we reject the null hypothesis. "
            + "Therefore, the program is successful.",
            "At 10% significance, there is enoug statistical "
            + "evidence that the program is working.",
        ],
    }
    task5 = DataFrame(task_dict)
    print(task5)


if __name__ == "__main__":
    dependent()
