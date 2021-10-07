"""
Absenteeism Exercise
"""
import io
from os.path import dirname
from pickle import load, loads
from numpy import array, mean, var
from pandas import DataFrame, concat, read_csv, get_dummies, to_datetime
from sklearn.preprocessing import StandardScaler
from sklearn.base import BaseEstimator, TransformerMixin


class CustomScaler(BaseEstimator, TransformerMixin):
    """
    the custom scaler class
    """

    def __init__(self, columns, copy=True, with_mean=True, with_std=True):
        self.scaler = StandardScaler(copy=copy, with_mean=with_mean, with_std=with_std)
        self.columns = columns
        self.mean_ = None
        self.var_ = None

    def fit(self, xdata, ydata=None):
        """
        fit method
        """
        self.scaler.fit(xdata[self.columns], ydata)
        self.mean_ = array(mean(xdata[self.columns]))
        self.var_ = array(var(xdata[self.columns]))
        return self

    def transform(self, xdata):
        """
        transform method
        """
        init_col_order = xdata.columns
        x_scaled = DataFrame(
            self.scaler.transform(xdata[self.columns]), columns=self.columns
        )
        x_not_scaled = xdata.loc[:, ~xdata.columns.isin(self.columns)]
        return concat([x_not_scaled, x_scaled], axis=1)[init_col_order]


class AbsenteeismModel:
    """
    create the special class to predict new data
    """

    def __init__(self, model_file, scaler_file):
        with open(model_file, "rb") as model, open(scaler_file, "rb") as scaler:
            self.reg = load(model)
            self.scaler = load(scaler)
            self.data = None
            self.df_with_predictions = DataFrame([])
            self.preprocessed_data = DataFrame([])

    def load_and_clean_data(self, data_file):
        """
        take a data file (*.csv) and preprocess it
        """
        dataf = DataFrame(read_csv(data_file, delimiter=","))
        self.df_with_predictions = dataf.copy()
        dataf = dataf.drop(["ID"], axis=1)
        dataf["Absenteeism Time in Hours"] = "NaN"
        reason_columns = get_dummies(dataf["Reason for Absence"], drop_first=True)
        reason_type_1 = reason_columns.loc[:, 1:14].max(axis=1)
        reason_type_2 = reason_columns.loc[:, 15:17].max(axis=1)
        reason_type_3 = reason_columns.loc[:, 18:21].max(axis=1)
        reason_type_4 = reason_columns.loc[:, 22:].max(axis=1)
        dataf = dataf.drop(["Reason for Absence"], axis=1)

        dataf = concat(
            [dataf, reason_type_1, reason_type_2, reason_type_3, reason_type_4], axis=1
        )
        column_names = [
            "Date",
            "Transportation Expense",
            "Distance to Work",
            "Age",
            "Daily Work Load Average",
            "Body Mass Index",
            "Education",
            "Children",
            "Pet",
            "Absenteeism Time in Hours",
            "Reason_1",
            "Reason_2",
            "Reason_3",
            "Reason_4",
        ]
        dataf.columns = column_names
        column_names_reordered = [
            "Reason_1",
            "Reason_2",
            "Reason_3",
            "Reason_4",
            "Date",
            "Transportation Expense",
            "Distance to Work",
            "Age",
            "Daily Work Load Average",
            "Body Mass Index",
            "Education",
            "Children",
            "Pet",
            "Absenteeism Time in Hours",
        ]

        dataf = dataf[column_names_reordered]
        dataf["Date"] = to_datetime(dataf["Date"], format="%d/%m/%Y")
        list_months = [dataf["Date"][i].month for i in range(dataf.shape[0])]
        dataf["Month Value"] = list_months
        dataf["Day of the Week"] = dataf["Date"].apply(lambda x: x.weekday())
        dataf = dataf.drop(["Date"], axis=1)

        column_names_upd = [
            "Reason_1",
            "Reason_2",
            "Reason_3",
            "Reason_4",
            "Month Value",
            "Day of the Week",
            "Transportation Expense",
            "Distance to Work",
            "Age",
            "Daily Work Load Average",
            "Body Mass Index",
            "Education",
            "Children",
            "Pet",
            "Absenteeism Time in Hours",
        ]
        dataf = dataf[column_names_upd]
        dataf["Education"] = dataf["Education"].map({1: 0, 2: 1, 3: 1, 4: 1})
        dataf = dataf.fillna(value=0)
        dataf = dataf.drop(["Absenteeism Time in Hours"], axis=1)
        dataf = dataf.drop(
            ["Day of the Week", "Daily Work Load Average", "Distance to Work"], axis=1
        )
        self.preprocessed_data = dataf.copy()
        self.data = self.scaler.transform(dataf)

    def predicted_probability(self):
        """
        function which outputs the probability of a data point to be 1
        """
        if self.data is not None:
            pred = self.reg.predict_proba(self.data)[:, 1]
            return pred
        return None

    def predicted_output_category(self):
        """
        function which outputs 0 or 1 based on our model
        """
        if self.data is not None:
            pred_outputs = self.reg.predict(self.data)
            return pred_outputs
        return None

    def predicted_outputs(self):
        """
        predict the outputs and the probabilities and
        add columns with these values at the end of the new data
        """
        if self.data is not None:
            self.preprocessed_data["Probability"] = self.reg.predict_proba(self.data)[
                :, 1
            ]
            self.preprocessed_data["Prediction"] = self.reg.predict(self.data)
            return self.preprocessed_data
        return None


def wrapper():
    """
    wrapper function
    """
    path = dirname(__file__) + "\\"
    print(read_csv(f"{path}absenteeism_new_data.csv"))
    model = AbsenteeismModel(f"{path}model", f"{path}scaler")
    model.load_and_clean_data(f"{path}absenteeism_new_data.csv")
    print(model.predicted_outputs())


if __name__ == "__main__":
    wrapper()
