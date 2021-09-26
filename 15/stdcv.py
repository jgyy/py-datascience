"""
Standard Deviation and Coefficient of Variation Exercise
"""
from os.path import dirname, realpath
from json import dumps
from pandas import DataFrame, read_excel

PATH = dirname(realpath(__file__))


def standard_deviation():
    """
    Coefficient of Variance = Standard Deviation / Mean
    """
    data = DataFrame(
        read_excel(
            io=f"{PATH}/standard_deviation_coefficient_of_variation.xlsx",
            sheet_name="Std and cv",
        )
    )
    col = [data.iloc[11, 1], data.iloc[11, 4]]
    std_data = DataFrame(
        {col[0]: data.iloc[12:23, 1].values, col[1]: data.iloc[12:23, 4].values}
    )
    print(std_data)
    usa = std_data.iloc[:, 0]
    denmark = std_data.iloc[:, 1]
    std_dict = {
        "Mean US": usa.mean().round(2),
        "Variance US": usa.var().round(2),
        "Standard deviation US": usa.std().round(2),
        "Coefficient of var. US": round(usa.std() / usa.mean(), 2),
        "Median US": usa.median().round(2),
        "Mean Denmark": denmark.mean().round(2),
        "Variance Denmark": denmark.var().round(2),
        "Standard deviation Denmark": denmark.std().round(2),
        "Coefficient of var. Denmark": round(denmark.std() / denmark.mean(), 2),
        "Median Denmark": denmark.median().round(2),
    }
    print(dumps(std_dict, indent=2))


if __name__ == "__main__":
    standard_deviation()
