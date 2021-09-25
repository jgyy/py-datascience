"""
Categorical Variables
"""
from os.path import dirname, realpath
from pandas import DataFrame, read_excel
from matplotlib.pyplot import figure, show, subplots
from matplotlib.ticker import PercentFormatter

PATH = dirname(realpath(__file__))


def categorical():
    """
    wrapper function
    """
    data = DataFrame(
        read_excel(
            io=f"{PATH}/categorical_variables.xlsx",
            sheet_name="Frequency distribution table",
        )
    )
    data = data.iloc[12:15, 1:3]
    data.columns = ["city", "frequency"]
    xaxis = data["city"]
    yaxis = data["frequency"]
    cumpercentage = []
    value = 0
    total = sum(yaxis)
    for i in yaxis:
        value += i
        cumpercentage.append(round((value * 100) / total))
    data["cumpercentage"] = cumpercentage
    print(data)

    fig1 = figure().add_axes([0.1, 0.1, 0.85, 0.85])
    fig1.bar(xaxis, yaxis)
    fig2 = figure().add_axes([0, 0, 1, 1])
    fig2.pie(yaxis, labels=xaxis, autopct="%1.0f%%")

    _, axe = subplots()
    axe.bar(xaxis, yaxis, color="C0")
    ax2 = axe.twinx()
    ax2.plot(xaxis, data["cumpercentage"], color="C1", marker="D", ms=7)
    ax2.yaxis.set_major_formatter(PercentFormatter())
    ax2.tick_params(axis="y", colors="C0")
    ax2.tick_params(axis="y", colors="C1")


if __name__ == "__main__":
    categorical()
    show()
