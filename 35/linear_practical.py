"""
Practical example
"""
from warnings import filterwarnings
from os.path import dirname
import seaborn as sns
from seaborn import histplot
from numpy import log, exp, absolute
from pandas import DataFrame, read_csv, get_dummies, options, set_option
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from matplotlib.pyplot import (
    show,
    figure,
    subplots,
    scatter,
    xlabel,
    ylabel,
    xlim,
    ylim,
    title,
)


def wrapper1():
    """
    wrapper function which description will not change
    """
    filterwarnings("ignore", category=RuntimeWarning)
    sns.set()
    path = dirname(__file__)
    raw_data = DataFrame(read_csv(f"{path}\\real_life_example.csv"))
    print(raw_data.head())
    print(raw_data.describe(include="all"))
    data = raw_data.drop(["Model"], axis=1)
    data.describe(include="all")
    print(data.isnull().sum())
    data_no_mv = data.dropna(axis=0)
    print(data_no_mv.describe(include="all"))

    figure('data_no_mv["Price"]')
    histplot(data_no_mv["Price"], kde=True)

    q_data = data_no_mv["Price"].quantile(0.99)
    data_1 = data_no_mv[data_no_mv["Price"] < q_data]
    print(data_1.describe(include="all"))
    figure('data_1["Price"]')
    histplot(data_1["Price"], kde=True)
    figure('data_no_mv["Mileage"]')
    histplot(data_no_mv["Mileage"], kde=True)

    q_data2 = data_1["Mileage"].quantile(0.99)
    data_2 = data_1[data_1["Mileage"] < q_data2]
    figure('data_2["Mileage"]')
    histplot(data_2["Mileage"], kde=True)
    figure('data_no_mv["EngineV"]')
    histplot(data_no_mv["EngineV"], kde=True)

    data_3 = data_2[data_2["EngineV"] < 6.5]
    figure('data_3["EngineV"]')
    histplot(data_3["EngineV"], kde=True)
    figure('data_no_mv["Year"]')
    histplot(data_no_mv["Year"], kde=True)

    q_data3 = data_3["Year"].quantile(0.01)
    data_4 = data_3[data_3["Year"] > q_data3]
    figure('data_4["Year"]')
    histplot(data_4["Year"], kde=True)
    data_cleaned = data_4.reset_index(drop=True)
    print(data_cleaned.describe(include="all"))
    print(data_cleaned["Brand"].unique())

    wrapper2(data_cleaned)


def wrapper2(data_clean):
    """
    part 2 of wrapper function
    """
    _, (ax1, ax2, ax3) = subplots(1, 3, sharey=True, figsize=(15, 3))
    ax1.scatter(data_clean["Year"], data_clean["Price"])
    ax1.set_title("Price and Year")
    ax2.scatter(data_clean["EngineV"], data_clean["Price"])
    ax2.set_title("Price and EngineV")
    ax3.scatter(data_clean["Mileage"], data_clean["Price"])
    ax3.set_title("Price and Mileage")

    figure('data_clean["Price"]')
    histplot(data_clean["Price"], kde=True)
    log_price = log(data_clean["Price"])
    data_clean["log_price"] = log_price
    print(data_clean)

    _, (ax1, ax2, ax3) = subplots(1, 3, sharey=True, figsize=(15, 3))
    ax1.scatter(data_clean["Year"], data_clean["log_price"])
    ax1.set_title("Log Price and Year")
    ax2.scatter(data_clean["EngineV"], data_clean["log_price"])
    ax2.set_title("Log Price and EngineV")
    ax3.scatter(data_clean["Mileage"], data_clean["log_price"])
    ax3.set_title("Log Price and Mileage")

    data_clean = data_clean.drop(["Price"], axis=1)
    print(data_clean.columns.values)
    variables = data_clean[["Mileage", "Year", "EngineV"]]
    vif = DataFrame()
    vif["VIF"] = [
        variance_inflation_factor(variables.values, i)
        for i in range(variables.shape[1])
    ]
    vif["Features"] = variables.columns
    print(vif)
    data_no_multicollinearity = data_clean.drop(["Year"], axis=1)
    print(data_no_multicollinearity)

    data_with_dummies = get_dummies(data_no_multicollinearity, drop_first=True)
    print(data_with_dummies.head())
    print(data_with_dummies.columns.values)
    cols = [
        "log_price",
        "Mileage",
        "EngineV",
        "Brand_BMW",
        "Brand_Mercedes-Benz",
        "Brand_Mitsubishi",
        "Brand_Renault",
        "Brand_Toyota",
        "Brand_Volkswagen",
        "Body_hatch",
        "Body_other",
        "Body_sedan",
        "Body_vagon",
        "Body_van",
        "Engine Type_Gas",
        "Engine Type_Other",
        "Engine Type_Petrol",
        "Registration_yes",
    ]
    data_preprocessed = data_with_dummies[cols]
    print(data_preprocessed.head())

    exercise(data_preprocessed, data_no_multicollinearity)


def exercise(data_preprocess, no_multicollinearity):
    """
    Dummies and VIF
    """
    variables = data_preprocess
    vif = DataFrame()
    vif["VIF"] = [
        variance_inflation_factor(variables.values, i)
        for i in range(variables.shape[1])
    ]
    vif["features"] = variables.columns
    print(vif)

    variables = data_preprocess.drop(["log_price"], axis=1)
    vif = DataFrame()
    vif["VIF"] = [
        variance_inflation_factor(variables.values, i)
        for i in range(variables.shape[1])
    ]
    vif["features"] = variables.columns
    print(vif)

    data_with_dummies_new = get_dummies(no_multicollinearity)
    print(data_with_dummies_new.head())
    variables = data_with_dummies_new.drop(["log_price"], axis=1)
    vif = DataFrame()
    vif["VIF"] = [
        variance_inflation_factor(variables.values, i)
        for i in range(variables.shape[1])
    ]
    vif["features"] = variables.columns
    print(vif)

    wrapper3(data_preprocess)


def wrapper3(data_preprocessed):
    """
    part 3 of wrapper function
    """
    targets = data_preprocessed["log_price"]
    inputs = data_preprocessed.drop(["log_price"], axis=1)
    scaler = StandardScaler()
    scaler.fit(inputs)
    inputs_scaled = scaler.transform(inputs)
    x_train, x_test, y_train, y_test = train_test_split(
        inputs_scaled, targets, test_size=0.2, random_state=365
    )
    regression = LinearRegression()
    regression.fit(x_train, y_train)
    y_hat = regression.predict(x_train)

    figure("y_train, y_hat")
    scatter(y_train, y_hat)
    xlabel("Targets (y_train)", size=18)
    ylabel("Predictions (y_hat)", size=18)
    xlim(6, 13)
    ylim(6, 13)

    figure("y_train - y_hat")
    histplot(y_train - y_hat, kde=True)
    title("Residuals PDF", size=18)
    print(regression.score(x_train, y_train))
    print(regression.intercept_)
    print(regression.coef_)
    reg_summary = DataFrame(inputs.columns.values, columns=["Features"])
    reg_summary["Weights"] = regression.coef_
    print(reg_summary)

    wrapper4(regression, (x_test, y_test))


def wrapper4(reg, tts):
    """
    part 4 of wrapper function
    """
    x_test, y_test = tts
    y_hat_test = reg.predict(x_test)
    figure("y_test, y_hat_test")
    scatter(y_test, y_hat_test, alpha=0.2)
    xlabel("Targets (y_test)", size=18)
    ylabel("Predictions (y_hat_test)", size=18)
    xlim(6, 13)
    ylim(6, 13)

    df_pf = DataFrame(exp(y_hat_test), columns=["Prediction"])
    print(df_pf.head())
    df_pf["Target"] = exp(y_test)
    print(df_pf)
    y_test = y_test.reset_index(drop=True)
    print(y_test.head())
    df_pf["Target"] = exp(y_test)
    print(df_pf)
    df_pf["Residual"] = df_pf["Target"] - df_pf["Prediction"]
    df_pf["Difference%"] = absolute(df_pf["Residual"] / df_pf["Target"] * 100)
    print(df_pf)
    print(df_pf.describe())

    options.display.max_rows = 999
    set_option("display.float_format", lambda x: str(round(x, 2)))
    print(df_pf.sort_values(by=["Difference%"]))


if __name__ == "__main__":
    wrapper1()
    show()
