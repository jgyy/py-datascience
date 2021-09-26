"""
Cross Tables and Scatter Plots Exercise
"""
from os.path import dirname, realpath
from pandas import DataFrame, read_excel

PATH = dirname(realpath(__file__))


def meanmedianmode():
    """
    wrapper function
    """
    mmm = DataFrame(
        read_excel(
            io=f"{PATH}/mean_median_and_mode.xlsx",
            sheet_name="Mean, median and mode",
        )
    )
    mmm_data = DataFrame(mmm.iloc[9:20, 1].values, columns=[mmm.iloc[8, 1]])
    mmm_mean = round(mmm_data.mean().iloc[0], 2)
    mmm_median = mmm_data.median().iloc[0]
    mmm_mode = mmm_data.mode().iloc[0, 0]
    print(mmm_data)
    print(f"Annual Income Mean: ${mmm_mean}")
    print(f"Annual Income Median: ${mmm_median}")
    print(f"Annual Income Mode: ${mmm_mode}")


if __name__ == "__main__":
    meanmedianmode()
