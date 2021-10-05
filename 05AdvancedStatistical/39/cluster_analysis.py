"""
Cluster analysis
"""
from warnings import filterwarnings
from os.path import dirname
import seaborn as sns
from seaborn import clustermap
from scipy import stats
from pandas import DataFrame, read_csv
from matplotlib.pyplot import show

PATH = dirname(__file__)


def wrapper1():
    """
    wrapper function which description will not change
    """
    filterwarnings("ignore", category=RuntimeWarning)
    sns.set()
    stats.chisqprob = stats.chi2.sf
    data = DataFrame(read_csv(f"{PATH}\\country_clusters_standardized.csv"))
    x_scaled = data.copy()
    x_scaled = x_scaled.drop(["Language"], axis=1)
    x_scaled = x_scaled.set_index("Country")
    print(x_scaled)

    clustermap(x_scaled, cmap="mako")


if __name__ == "__main__":
    wrapper1()
    show()
