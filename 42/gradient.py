"""
Gradient descent. Function example.
"""
from pandas import DataFrame


def wrapper():
    """
    Searching for the minimum of 5x^2+3x-4
    Update rule: xi+1 = xi - η * f ' (xi)
    """
    dicts = {
        "xi": [4],
        "f' (xi)": [],
        "Learning rate η (eta)": 0.001,
    }
    fxi = lambda x: 10 * x + 3
    xi_ = lambda x, y, z: x - y * z
    dicts["f' (xi)"].append(fxi(dicts["xi"][-1]))
    for _ in range(99999999):
        dicts["xi"].append(
            xi_(dicts["xi"][-1], dicts["Learning rate η (eta)"], dicts["f' (xi)"][-1])
        )
        dicts["f' (xi)"].append(fxi(dicts["xi"][-1]))
        if (
            dicts["xi"][-1] == dicts["xi"][-2]
            or dicts["f' (xi)"][-1] == dicts["f' (xi)"][-2]
        ):
            break
    data = DataFrame(dicts)
    print(data)


if __name__ == "__main__":
    wrapper()
