"""
Simple Linear Regression. Minimal example
"""
from numpy import column_stack, dot
from numpy.random import uniform
from matplotlib.pyplot import figure, show, plot, xlabel, ylabel


def wrapper():
    """
    weapper function which descriptions will not change
    """
    xsize = uniform(low=-10, high=10, size=(1000, 1))
    zsize = uniform(-10, 10, (1000, 1))
    inputs = column_stack((xsize, zsize))
    print(inputs.shape)
    noise = uniform(-1, 1, (1000, 1))
    targets = 2 * xsize - 3 * zsize + 5 + noise
    print(targets.shape)

    targets = targets.reshape(1000)
    fig = figure()
    axis = fig.add_subplot(111, projection="3d")
    axis.plot(xsize.flatten(), zsize.flatten(), targets)
    axis.set_xlabel("xs")
    axis.set_ylabel("zs")
    axis.set_zlabel("Targets")
    axis.view_init(azim=100)
    targets = targets.reshape(1000, 1)

    weights = uniform(low=-0.1, high=0.1, size=(2, 1))
    biases = uniform(low=-0.1, high=0.1, size=1)
    print(weights)
    print(biases)

    learning_rate = 0.02
    for _ in range(100):
        outputs = dot(inputs, weights) + biases
        deltas = outputs - targets
        loss = sum(deltas ** 2) / 2 / 1000
        print(loss)
        deltas_scaled = deltas / 1000
        weights = weights - learning_rate * dot(inputs.T, deltas_scaled)
        biases = biases - learning_rate * sum(deltas_scaled)

    print(weights, biases)
    figure()
    plot(outputs, targets)
    xlabel("outputs")
    ylabel("targets")


if __name__ == "__main__":
    wrapper()
    show()
