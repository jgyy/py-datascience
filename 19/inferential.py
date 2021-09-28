"""
Practical Example: Inferential Statistics Exercise
"""
from os.path import dirname, realpath
from pandas import DataFrame, read_excel

PATH = dirname(realpath(__file__))


def inferential():
    """
    Inferential statistics. Confidence intervals
    """
    table = DataFrame(read_excel(io=f"{PATH}/t_table.xlsx", sheet_name="t-table"))
    ttable = DataFrame(
        table.iloc[5:41, 2:7].values,
        columns=table.iloc[4, 2:7],
        index=table.iloc[5:41, 1],
    )
    ttable.index.name = None
    ttable.columns.name = "d.f. / α"

    bundy = DataFrame(
        read_excel(
            io=f"{PATH}/confidence_intervals_exercise.xlsx",
            sheet_name="Al Bundy",
        )
    )
    aibundy = DataFrame(bundy.iloc[3:, 1:15].values, columns=bundy.iloc[2, 1:15])
    aibundy.index.name = None
    aibundy.columns.name = None
    sizes = DataFrame(
        read_excel(
            io=f"{PATH}/confidence_intervals_exercise.xlsx",
            sheet_name="Shoe size conversion table",
        )
    )
    men = DataFrame(sizes.iloc[4:21, 1:6].values, columns=sizes.iloc[3, 1:6].values)
    men.columns.name = "Male"
    women = DataFrame(sizes.iloc[4:21, 9:14].values, columns=sizes.iloc[3, 9:14].values)
    women.columns.name = "Female"

    usa15 = confidence(aibundy, [2015], men, "United States", aibundy["Country"])
    usa16 = confidence(aibundy, [2016], men, "United States", aibundy["Country"])
    usa_num = 24
    t23 = round(ttable.loc[usa_num - 1, round((1 - 0.95) / 2, 3)], 2)
    print(f"United States: n = {usa_num}, t95%,23 = {t23}")
    usa_res = {
        "Mean": [
            round((usa15.iloc[i, :].mean() + usa16.iloc[i, :].mean()) / 2, 2)
            for i in range(len(men.index))
        ],
        "Standard error": [
            round(
                (usa15.iloc[i, :].std() + usa16.iloc[i, :].std()) / 2 / usa_num ** 0.5,
                2,
            )
            for i in range(len(men.index))
        ],
    }
    usa_res["Margin of error"] = [round(i * t23, 2) for i in usa_res["Standard error"]]
    usa_res["CI low"] = [
        i - j for i, j in zip(usa_res["Mean"], usa_res["Margin of error"])
    ]
    usa_res["CI high"] = [
        i + j for i, j in zip(usa_res["Mean"], usa_res["Margin of error"])
    ]
    usa_res["math round"] = [round(i, 0) for i in usa_res["CI high"]]
    usa_res["lesson"] = [4, 3, 3, 5, 8, 13, 23, 36, 26, 21, 12, 8, 6, 2, 4, 1, 0]
    usa_res["Difference"] = [
        i - j for i, j in zip(usa_res["lesson"], usa_res["math round"])
    ]
    usa_result = DataFrame(usa_res, columns=usa_res.keys(), index=men["US"])
    usa_result.columns.name = "US"
    usa_result.index.name = None
    print(usa_result)

    ger1 = confidence(aibundy, [2014, 2015, 2016], women, "GER1", aibundy["Shop"])
    ger2 = confidence(aibundy, [2014, 2015, 2016], women, "GER2", aibundy["Shop"])
    ger_num = 12
    t22 = round(ttable.loc[ger_num * 2 - 2, round((1 - 0.9) / 2, 2)], 2)
    print(f"GER1/2 n = {ger_num}, t90%,22 = {t22}")
    ger_res = {
        "GER1 Mean": [
            round(ger1.iloc[i, :].mean(), 2) for i in range(len(women.index))
        ],
        "GER2 Mean": [
            round(ger2.iloc[i, :].mean(), 2) for i in range(len(women.index))
        ],
        "GER1 Sample variance": [
            round(ger1.iloc[i, :].var(), 2) for i in range(len(women.index))
        ],
        "GER2 Sample variance": [
            round(ger2.iloc[i, :].var(), 2) for i in range(len(women.index))
        ],
    }
    ger_res["Pooled variance"] = [
        round(((ger_num - 1) * i + (ger_num - 1) * j) / (ger_num + ger_num - 2), 2)
        for i, j in zip(
            ger_res["GER1 Sample variance"], ger_res["GER2 Sample variance"]
        )
    ]
    ger_res["Margin of error"] = [
        round(t22 * (i / ger_num + i / ger_num) ** 0.5, 2)
        for i in ger_res["Pooled variance"]
    ]
    ger_res["CI low"] = [
        i - j - k
        for i, j, k in zip(
            ger_res["GER1 Mean"], ger_res["GER2 Mean"], ger_res["Margin of error"]
        )
    ]
    ger_res["CI high"] = [
        i - j + k
        for i, j, k in zip(
            ger_res["GER1 Mean"], ger_res["GER2 Mean"], ger_res["Margin of error"]
        )
    ]
    ger_result = DataFrame(ger_res, columns=ger_res.keys(), index=women["US"])
    ger_result.columns.name = "US"
    ger_result.index.name = None
    print(ger_result)


def confidence(data, year, gender, country, condition):
    """
    Task 1: Calculate the confidence intervals for men shoes sales in the USA,
    this time based on a bigger sample - 2015-2016.
    """
    countries = (
        data[
            (data["Year"].isin(year))
            & (data["Gender"] == gender.columns.name)
            & (condition == country)
        ]
        .loc[:, ["Size (US)", "Month"]]
        .astype(float)
    )
    country_data = [
        [
            countries[(countries["Month"] == j) & (countries["Size (US)"] == i)]
            .count()
            .values[0]
            for j in range(1, 13)
        ]
        for i in gender["US"]
    ]
    country_data = DataFrame(
        country_data, columns=list(range(1, 13)), index=gender["US"]
    )
    country_data.columns.name = "US"
    country_data.index.name = None
    print(f"{country}, {year}\n", country_data)
    return country_data


if __name__ == "__main__":
    inferential()
