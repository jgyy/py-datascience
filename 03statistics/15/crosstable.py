"""
Cross Tables and Scatter Plots Exercise
"""
from os.path import dirname, realpath
from numpy import arange
from pandas import DataFrame, read_excel
from matplotlib.pyplot import show, subplots

PATH = dirname(realpath(__file__))


def crosstable():
    """
    wrapper function
    """
    cross = DataFrame(
        read_excel(
            io=f"{PATH}/cross_table_scatter_plot.xlsx",
            sheet_name="Cross table",
        )
    )
    cross_data = DataFrame(cross.iloc[17:23, 1:4].values, columns=cross.iloc[16, 1:4])
    print(cross_data)
    sca = DataFrame(
        read_excel(
            io=f"{PATH}/cross_table_scatter_plot.xlsx",
            sheet_name="Scatter plot",
        )
    )
    sca_data = DataFrame(sca.iloc[11:115, 2:5].values, columns=sca.iloc[10, 2:5])
    print(sca_data)

    labels, employed, unemployed = (cross_data.iloc[:, i] for i in range(3))
    xaxis = arange(len(labels))
    width = 0.35
    _, axis = subplots()
    rects1 = axis.bar(xaxis - width / 2, employed, width, label=cross_data.columns[1])
    rects2 = axis.bar(xaxis + width / 2, unemployed, width, label=cross_data.columns[2])
    axis.set_ylabel("Percentage %")
    axis.set_title("Employment by age group")
    axis.set_xticks(xaxis)
    axis.set_xticklabels(labels)
    axis.legend()
    axis.bar_label(rects1, padding=3)
    axis.bar_label(rects2, padding=3)

    aapl, googl, bac = (sca_data.iloc[:, i] for i in range(3))
    _, axis1 = subplots()
    axis1.scatter(aapl, googl)
    axis1.set_title("aapl, googl")
    _, axis2 = subplots()
    axis2.scatter(bac, googl)
    axis2.set_title("bac, googl")
    _, axis3 = subplots()
    axis3.scatter(aapl, bac)
    axis3.set_title("aapl, bac")


if __name__ == "__main__":
    crosstable()
    show()
