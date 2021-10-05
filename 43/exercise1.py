"""
Simple Linear Regression. Minimal example
"""
from numpy import column_stack, dot
from numpy.random import uniform
from matplotlib.pyplot import figure, show, plot, xlabel, ylabel


def wrapper1():
    """
    Wrapper function which descriptions will not change
    """
    observations = 10000
    xsize = uniform(low=-10, high=10, size=(observations, 1))
    zsize = uniform(-10, 10, (observations, 1))
    inputs = column_stack((xsize, zsize))
    print(inputs.shape)
    noise = uniform(-1, 1, (observations, 1))
    targets = 2 * xsize - 3 * zsize + 5 + noise
    print(targets.shape)

    targets = targets.reshape(observations)
    fig = figure()
    axis = fig.add_subplot(111, projection="3d")
    axis.plot(xsize.flatten(), zsize.flatten(), targets)
    axis.set_xlabel("xs")
    axis.set_ylabel("zs")
    axis.set_zlabel("Targets")
    axis.view_init(azim=100)
    targets = targets.reshape(observations, 1)

    init_range = 0.1
    weights = uniform(low=-init_range, high=init_range, size=(2, 1))
    biases = uniform(low=-init_range, high=init_range, size=1)
    print(weights)
    print(biases)

    wrapper2(inputs, targets, observations, weights, biases)


def wrapper2(inputs, targets, observations, weights, biases):
    """
    Part 2 of wrapper function to reduce number of variables
    """
    learning_rate = 0.02
    for _ in range(100):
        outputs = dot(inputs, weights) + biases
        deltas = outputs - targets
        loss = sum(deltas ** 2) / 2 / observations
        print(loss)
        deltas_scaled = deltas / observations
        weights = weights - learning_rate * dot(inputs.T, deltas_scaled)
        biases = biases - learning_rate * sum(deltas_scaled)

    print(weights, biases)
    figure()
    print(len(outputs), len(targets))
    plot(outputs, targets)
    xlabel("outputs")
    ylabel("targets")


if __name__ == "__main__":
    wrapper1()
    show()
