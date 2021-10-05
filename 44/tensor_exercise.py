"""
Minimal example with TensorFlow 2.0 exercise
"""
from os.path import dirname
from numpy import column_stack, savez, load, squeeze
from numpy.random import uniform
from tensorflow import random_uniform_initializer
from tensorflow.keras import Sequential, optimizers, layers
from matplotlib.pyplot import figure, plot, xlabel, ylabel, show


def wrapper():
    """
    Wrapper function with static descriptions
    """
    path = dirname(__file__)
    observations = 100000
    xsize = uniform(low=-10, high=10, size=(observations, 1))
    zsize = uniform(-10, 10, (observations, 1))
    generated_inputs = column_stack((xsize, zsize))
    noise = uniform(-1, 1, (observations, 1))
    generated_targets = 2 * xsize - 3 * zsize + 5 + noise

    savez(f"{path}\\tf_intro", inputs=generated_inputs, targets=generated_targets)
    training_data = load(f"{path}\\tf_intro.npz")
    output_size = 1
    model = Sequential(
        [
            layers.Dense(
                output_size,
                kernel_initializer=random_uniform_initializer(minval=-0.1, maxval=0.1),
                bias_initializer=random_uniform_initializer(minval=-0.1, maxval=0.1),
            )
        ]
    )
    custom_optimizer = optimizers.SGD(learning_rate=0.02)
    model.compile(optimizer=custom_optimizer, loss="mean_squared_error")
    model.fit(training_data["inputs"], training_data["targets"], epochs=100, verbose=2)

    print(model.layers[0].get_weights())
    weights = model.layers[0].get_weights()[0]
    print(weights)
    bias = model.layers[0].get_weights()[1]
    print(bias)
    print(model.predict_on_batch(training_data["inputs"]).round(1))
    print(training_data["targets"].round(1))

    figure()
    plot(
        squeeze(model.predict_on_batch(training_data["inputs"])),
        squeeze(training_data["targets"]),
    )
    xlabel("outputs")
    ylabel("targets")


if __name__ == "__main__":
    wrapper()
    show()
