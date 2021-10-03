"""
A Simple Example of Clustering Exercise
"""
from warnings import filterwarnings
from os.path import dirname
import seaborn as sns
from scipy import stats
from pandas import DataFrame, read_csv
from sklearn.cluster import KMeans
from matplotlib.pyplot import figure, scatter, xlim, ylim, show

PATH = dirname(__file__)


def wrapper1():
    """
    wrapper function which description will not change
    """
    filterwarnings("ignore", category=RuntimeWarning)
    sns.set()
    stats.chisqprob = stats.chi2.sf
    raw_data = DataFrame(read_csv(f"{PATH}\\countries_exercise.csv"))
    print(raw_data)
    data = raw_data.copy()

    figure()
    scatter(data["Longitude"], data["Latitude"])
    xlim(-180, 180)
    ylim(-90, 90)
    x_data = data.iloc[:, 1:3]
    print(x_data)

    kmeans = KMeans(7)
    kmeans.fit(x_data)
    identified_clusters = kmeans.fit_predict(x_data)
    print(identified_clusters)
    data_with_clusters = data.copy()
    data_with_clusters["Cluster"] = identified_clusters
    print(data_with_clusters)
    figure()
    scatter(
        data["Longitude"],
        data["Latitude"],
        c=data_with_clusters["Cluster"],
        cmap="rainbow",
    )
    xlim(-180, 180)
    ylim(-90, 90)


if __name__ == "__main__":
    wrapper1()
    show()
