"""
How to Choose the Number of Clusters
"""
from warnings import filterwarnings
from os.path import dirname
import seaborn as sns
from scipy import stats
from pandas import DataFrame, read_csv
from sklearn.cluster import KMeans
from sklearn import preprocessing
from matplotlib.pyplot import figure, scatter, xlabel, ylabel, show, plot, title

PATH = dirname(__file__)


def wrapper1():
    """
    wrapper function which description will not change
    """
    filterwarnings("ignore", category=RuntimeWarning)
    sns.set()
    stats.chisqprob = stats.chi2.sf
    data = DataFrame(read_csv(f"{PATH}\\iris_dataset.csv"))
    print(data)
    figure()
    scatter(data["sepal_length"], data["sepal_width"])
    xlabel("Lenght of sepal")
    ylabel("Width of sepal")

    x_data = data.copy()
    kmeans = KMeans(2)
    kmeans.fit(x_data)
    clusters = data.copy()
    clusters["cluster_pred"] = kmeans.fit_predict(x_data)
    figure()
    scatter(
        clusters["sepal_length"],
        clusters["sepal_width"],
        c=clusters["cluster_pred"],
        cmap="rainbow",
    )

    x_scaled = preprocessing.scale(data)
    print(x_scaled)
    kmeans_scaled = KMeans(2)
    kmeans_scaled.fit(x_scaled)
    clusters_scaled = data.copy()
    clusters_scaled["cluster_pred"] = kmeans_scaled.fit_predict(x_scaled)
    figure()
    scatter(
        clusters_scaled["sepal_length"],
        clusters_scaled["sepal_width"],
        c=clusters_scaled["cluster_pred"],
        cmap="rainbow",
    )

    wcss = []
    cl_num = 10
    for i in range(1, cl_num):
        kmeans = KMeans(i)
        kmeans.fit(x_scaled)
        wcss_iter = kmeans.inertia_
        wcss.append(wcss_iter)
    print(wcss)
    number_clusters = range(1, cl_num)
    figure()
    plot(number_clusters, wcss)
    title("The Elbow Method")
    xlabel("Number of clusters")
    ylabel("Within-cluster Sum of Squares")

    wrapper2(x_scaled, x_data)


def wrapper2(x_scaled, x_data):
    """
    part 2 of wrapper function
    """
    kmeans_2 = KMeans(2)
    kmeans_2.fit(x_scaled)
    clusters_2 = x_data.copy()
    clusters_2["cluster_pred"] = kmeans_2.fit_predict(x_scaled)
    figure()
    scatter(
        clusters_2["sepal_length"],
        clusters_2["sepal_width"],
        c=clusters_2["cluster_pred"],
        cmap="rainbow",
    )

    kmeans_3 = KMeans(3)
    kmeans_3.fit(x_scaled)
    clusters_3 = x_data.copy()
    clusters_3["cluster_pred"] = kmeans_3.fit_predict(x_scaled)
    figure()
    scatter(
        clusters_3["sepal_length"],
        clusters_3["sepal_width"],
        c=clusters_3["cluster_pred"],
        cmap="rainbow",
    )

    kmeans_5 = KMeans(5)
    kmeans_5.fit(x_scaled)
    clusters_5 = x_data.copy()
    clusters_5["cluster_pred"] = kmeans_5.fit_predict(x_scaled)
    figure()
    scatter(
        clusters_5["sepal_length"],
        clusters_5["sepal_width"],
        c=clusters_5["cluster_pred"],
        cmap="rainbow",
    )

    real_data = DataFrame(read_csv(f"{PATH}\\iris_with_answers.csv"))
    print(real_data["species"].unique())
    real_data["species"] = real_data["species"].map(
        {"setosa": 0, "versicolor": 1, "virginica": 2}
    )
    print(real_data.head())

    figure()
    scatter(
        real_data["sepal_length"],
        real_data["sepal_width"],
        c=real_data["species"],
        cmap="rainbow",
    )
    figure()
    scatter(
        real_data["petal_length"],
        real_data["petal_width"],
        c=real_data["species"],
        cmap="rainbow",
    )
    figure()
    scatter(
        clusters_3["sepal_length"],
        clusters_3["sepal_width"],
        c=clusters_3["cluster_pred"],
        cmap="rainbow",
    )
    figure()
    scatter(
        clusters_3["petal_length"],
        clusters_3["petal_width"],
        c=clusters_3["cluster_pred"],
        cmap="rainbow",
    )


if __name__ == "__main__":
    wrapper1()
    show()
