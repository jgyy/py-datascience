"""
A Simple Example of Clustering
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
    data = DataFrame(read_csv(f"{PATH}\\country_clusters.csv"))
    print(data)

    figure()
    scatter(data["Longitude"], data["Latitude"])
    xlim(-180, 180)
    ylim(-90, 90)
    x_data = data.iloc[:, 1:3]
    print(x_data)

    kmeans = KMeans(3)
    kmeans.fit(x_data)
    identified_clusters = kmeans.fit_predict(x_data)
    print(identified_clusters)
    data_with_clusters = data.copy()
    data_with_clusters["Cluster"] = identified_clusters
    print(data_with_clusters)
    figure()
    scatter(
        data_with_clusters["Longitude"],
        data_with_clusters["Latitude"],
        c=data_with_clusters["Cluster"],
        cmap="rainbow",
    )
    xlim(-180, 180)
    ylim(-90, 90)


if __name__ == "__main__":
    wrapper1()
    show()
