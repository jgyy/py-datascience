"""
Audiobooks business case
"""
from os.path import dirname
from numpy import loadtxt, delete, arange, savez
from numpy.random import shuffle
from sklearn.preprocessing import scale

PATH = dirname(__file__) + "\\"


def wrapper1():
    """
    wrapper function with no additional descriptions
    """
    raw_csv_data = loadtxt(f"{PATH}audiobooks_data.csv", delimiter=",")
    unscaled_inputs_all = raw_csv_data[:, 1:-1]
    targets_all = raw_csv_data[:, -1]

    shuffled_indices = arange(unscaled_inputs_all.shape[0])
    shuffle(shuffled_indices)
    unscaled_inputs_all = unscaled_inputs_all[shuffled_indices]
    targets_all = targets_all[shuffled_indices]
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
    Split the dataset into train, validation, and test
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


if __name__ == "__main__":
    wrapper1()
