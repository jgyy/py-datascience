"""
How to Choose the Number of Clusters
"""
from warnings import filterwarnings
from os.path import dirname
import seaborn as sns
from scipy import stats
from pandas import DataFrame, read_csv
from sklearn.cluster import KMeans
from matplotlib.pyplot import (
    figure,
    scatter,
    xlim,
    ylim,
    xlabel,
    ylabel,
    show,
    plot,
    title,
)

PATH = dirname(__file__)


def wrapper1():
    """
    wrapper function which description will not change
    """
    filterwarnings("ignore", category=RuntimeWarning)
    sns.set()
    stats.chisqprob = stats.chi2.sf
    data = DataFrame(read_csv(f"{PATH}\\countries_exercise.csv"))
    print(data)

    figure()
    scatter(data["Longitude"], data["Latitude"])
    xlim(-180, 180)
    ylim(-90, 90)
    x_data = data.iloc[:, 1:3]
    kmeans = KMeans(4)
    kmeans.fit(x_data)
    identified_clusters = kmeans.fit_predict(x_data)
    print(identified_clusters)
    data_with_clusters = data.copy()
    data_with_clusters["Cluster"] = identified_clusters
    print(data_with_clusters)

    plotting(data, data_with_clusters)
    print(kmeans.inertia_)
    wcss = []
    cl_num = 11
    for i in range(1, cl_num):
        kmeans = KMeans(i)
        kmeans.fit(x_data)
        wcss_iter = kmeans.inertia_
        wcss.append(wcss_iter)
    print(wcss)

    figure()
    number_clusters = range(1, cl_num)
    plot(number_clusters, wcss)
    title("The Elbow Method")
    xlabel("Number of clusters")
    ylabel("Within-cluster Sum of Squares")

    kmeans = KMeans(2)
    kmeans.fit(x_data)
    identified_clusters = kmeans.fit_predict(x_data)
    data_with_clusters = data.copy()
    data_with_clusters["Cluster"] = identified_clusters
    plotting(data, data_with_clusters)

    kmeans = KMeans(3)
    kmeans.fit(x_data)
    identified_clusters = kmeans.fit_predict(x_data)
    data_with_clusters = data.copy()
    data_with_clusters["Cluster"] = identified_clusters
    plotting(data, data_with_clusters)


def plotting(data, data_with_clusters):
    """
    Refactoring the figure
    """
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
