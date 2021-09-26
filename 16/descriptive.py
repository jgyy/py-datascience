"""
Practical Example: Descriptive Statistics
"""
from os.path import dirname, realpath
from json import dumps
from pandas import DataFrame, read_excel
from numpy import arange, where
from matplotlib.ticker import PercentFormatter
from matplotlib.pyplot import (
    figure,
    show,
    hist,
    xlabel,
    ylabel,
    grid,
    scatter,
    subplots,
)

PATH = dirname(realpath(__file__))


def descriptive():
    """
    wrapper function
    """
    data = DataFrame(
        read_excel(
            io=f"{PATH}/descriptive_statistics_exercise.xlsx",
            sheet_name="365RE",
        )
    )
    product = DataFrame(
        data.iloc[4:999, 1:10].values, columns=data.iloc[3, 1:10]
    ).dropna(how="all")
    customer = DataFrame(
        data.iloc[4:999, 11:27].values, columns=data.iloc[3, 11:27]
    ).dropna(how="all")

    price = product.loc[:, "Price"]
    figure("Task 2")
    hist(price, bins=int(len(price) / 2))
    xlabel("Price")
    ylabel("Frequency")
    grid(True)

    bins = len(arange(min(price), max(price), 100000))
    figure("Task 3")
    yaxis, xaxis, _ = hist(price, bins=bins)
    xlabel("Price")
    ylabel("Frequency")
    grid(True)

    maxy = where(yaxis == yaxis.max())[0][0]
    print(
        "Task 4: The histograms point to similar insights",
        "- most of the properties' prices are concentrated in the interval",
        f"(${round(xaxis[maxy], 2)} to ${round(xaxis[maxy + 1], 2)})",
    )

    area = product.loc[:, "Area (ft.)"]
    figure("Task 5")
    scatter(area, price)
    xlabel("Area (ft.)")
    ylabel("Price")
    grid(True)

    country = customer.loc[:, "Country"].value_counts().reset_index()
    country.columns = ["Country", "Frequency"]
    frequency = DataFrame(country)
    frequency["Relative frequency"] = [
        round(100 * i / sum(frequency["Frequency"]), 1) for i in frequency["Frequency"]
    ]
    frequency["Cumulative frequency"] = [
        sum(frequency["Relative frequency"][: i + 1])
        for i in range(len(frequency["Country"]))
    ]
    print("Task 6:\n", frequency)

    _, axe = subplots()
    axe.bar(frequency["Country"], frequency["Frequency"], color="C0")
    axe.title.set_text("Task 7")
    ax2 = axe.twinx()
    ax2.plot(
        frequency["Country"],
        frequency["Cumulative frequency"],
        color="C1",
        marker="D",
        ms=7,
    )
    ax2.yaxis.set_major_formatter(PercentFormatter())
    axe.tick_params(axis="y", colors="C0")
    ax2.tick_params(axis="y", colors="C1")

    calc = {
        "Mean": round(price.mean(), 2),
        "Median": round(price.median(), 2),
        "Mode": round(price.mode()[0], 2),
        "Skew": round(price.skew(), 2),
        "Variance": round(price.var(), 2),
        "St. dev.": round(price.std(), 2),
        "Covariance": product.loc[:, ["Price", "Area (ft.)"]]
        .astype(float)
        .cov()
        .iloc[0, 1],
        "Correlation": product.loc[:, ["Price", "Area (ft.)"]]
        .astype(float)
        .corr()
        .iloc[0, 1]
    }
    print("Task 8 & 10:", dumps(calc, indent=2))
    print(
        "Task 9: We will only comment on the skew, as it is a bit tougher.",
        "The skew is right (positive). This means that most properties are",
        "relatively cheap with a tiny portion that is more expensive.",
    )


if __name__ == "__main__":
    datatypes = [
        {
            "Variable": "Cust ID",
            "Type of data": "Categorical",
            "Level of measurement": "Nominal",
            "Comment": "This variable has the same properties as ID.",
        },
        {
            "Variable": "Mortgage",
            "Type of data": "Categorical",
            "Level of measurement": "Nominal",
            "Comment": "This is a Binary variable. Like a Yes/No question or Gender.",
        },
        {
            "Variable": "Year of sale",
            "Type of data": "Numerical, discrete",
            "Level of measurement": "Interval",
            "Comment": "Year is a numerical variable. It is always discrete. "
            + "The level of measurement is questionable, but we would treat it as interval, "
            + "as the 0 year would be the time when the Big Bang happened. "
            + "The current BC-AD calendar was arbitrary chosen "
            + "(similarly to degrees Celsius and Fahrenheit).",
        },
    ]
    print("Task 1:", dumps(datatypes, indent=2))
    descriptive()
    show()
