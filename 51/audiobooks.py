"""
Audiobooks business case
"""
from os.path import dirname
from numpy import loadtxt, delete, arange, savez, load
from numpy.random import shuffle
from sklearn.preprocessing import scale
from tensorflow.keras import Sequential, layers, callbacks

PATH = dirname(__file__) + "\\"


def wrapper1():
    """
    wrapper function with no additional descriptions
    """
    raw_csv_data = loadtxt(f"{PATH}audiobooks_data.csv", delimiter=",")
    unscaled_inputs_all = raw_csv_data[:, 1:-1]
    targets_all = raw_csv_data[:, -1]
    num_one_targets = int(sum(targets_all))
    zero_targets_counter = 0
    indices_to_remove = []

    for i in range(targets_all.shape[0]):
        if targets_all[i] == 0:
            zero_targets_counter += 1
            if zero_targets_counter > num_one_targets:
                indices_to_remove.append(i)
    unscaled_inputs_equal_priors = delete(
        unscaled_inputs_all, indices_to_remove, axis=0
    )

    targets_equal_priors = delete(targets_all, indices_to_remove, axis=0)
    scaled_inputs = scale(unscaled_inputs_equal_priors)
    shuffled_indices = arange(scaled_inputs.shape[0])
    shuffle(shuffled_indices)
    shuffled_inputs = scaled_inputs[shuffled_indices]
    shuffled_targets = targets_equal_priors[shuffled_indices]

    train_validate_test(shuffled_inputs, shuffled_targets)


def train_validate_test(shuffled_inputs, shuffled_targets):
    """
    train, validate, test and save audiobook data
    """
    samples_count = shuffled_inputs.shape[0]
    train_samples_count = int(0.8 * samples_count)
    validation_samples_count = int(0.1 * samples_count)
    test_samples_count = samples_count - train_samples_count - validation_samples_count
    train_inputs = shuffled_inputs[:train_samples_count]
    train_targets = shuffled_targets[:train_samples_count]
    validation_inputs = shuffled_inputs[
        train_samples_count : train_samples_count + validation_samples_count
    ]
    validation_targets = shuffled_targets[
        train_samples_count : train_samples_count + validation_samples_count
    ]
    test_inputs = shuffled_inputs[train_samples_count + validation_samples_count :]
    test_targets = shuffled_targets[train_samples_count + validation_samples_count :]

    print(
        sum(train_targets),
        train_samples_count,
        sum(train_targets) / train_samples_count,
    )
    print(
        sum(validation_targets),
        validation_samples_count,
        sum(validation_targets) / validation_samples_count,
    )
    print(sum(test_targets), test_samples_count, sum(test_targets) / test_samples_count)
    savez(f"{PATH}audiobooks_data_train", inputs=train_inputs, targets=train_targets)
    savez(
        f"{PATH}audiobooks_data_validation",
        inputs=validation_inputs,
        targets=validation_targets,
    )
    savez(f"{PATH}audiobooks_data_test", inputs=test_inputs, targets=test_targets)

    load_data()


def load_data():
    """
    train, validate, test and save audiobook data
    """
    npz = load(f"{PATH}audiobooks_data_train.npz")
    train_inputs = npz["inputs"].astype(float)
    train_targets = npz["targets"].astype(int)
    npz = load(f"{PATH}audiobooks_data_validation.npz")
    validation_inputs, validation_targets = npz["inputs"].astype(float), npz[
        "targets"
    ].astype(int)
    npz = load(f"{PATH}audiobooks_data_test.npz")
    test_inputs, test_targets = npz["inputs"].astype(float), npz["targets"].astype(int)

    output_size = 2
    hidden_layer_size = 50
    model = Sequential(
        [
            layers.Dense(hidden_layer_size, activation="relu"),
            layers.Dense(hidden_layer_size, activation="relu"),
            layers.Dense(output_size, activation="softmax"),
        ]
    )
    model.compile(
        optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]
    )
    batch_size = 100
    max_epochs = 100
    early_stopping = callbacks.EarlyStopping(patience=2)
    model.fit(
        train_inputs,
        train_targets,
        batch_size=batch_size,
        epochs=max_epochs,
        callbacks=[early_stopping],
        validation_data=(validation_inputs, validation_targets),
    )

    test_loss, test_accuracy = model.evaluate(test_inputs, test_targets)
    print(
        f"\nTest loss: {round(test_loss, 2)}.",
        f"Test accuracy: {round(test_accuracy * 100.0, 2)}%",
    )


if __name__ == "__main__":
    wrapper1()
