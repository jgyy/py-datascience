"""
Basics of cluster analysis
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

    data_mapped = data.copy()
    data_mapped["Language"] = data_mapped["Language"].map(
        {"English": 0, "French": 1, "German": 2}
    )
    print(data_mapped)
    x_data = data_mapped.iloc[:, 1:4]
    print(x_data)
    kmeans = KMeans(2)
    kmeans.fit(x_data)

    identified_clusters = kmeans.fit_predict(x_data)
    print(identified_clusters)
    data_with_clusters = data_mapped.copy()
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
