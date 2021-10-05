"""
Deep Neural Network for MNIST Classification
"""
from tensorflow import cast, int64, float32
from tensorflow.keras import Sequential, layers
from tensorflow_datasets import load


def wrapper():
    """
    Wrapper function with no new descriptions
    """
    mnist_dataset, mnist_info = load(name="mnist", with_info=True, as_supervised=True)
    mnist_train, mnist_test = mnist_dataset["train"], mnist_dataset["test"]
    num_validation_samples = 0.1 * mnist_info.splits["train"].num_examples
    num_validation_samples = cast(num_validation_samples, int64)
    num_test_samples = mnist_info.splits["test"].num_examples
    num_test_samples = cast(num_test_samples, int64)
    scale = lambda i, l: (cast(i, float32) / 255, l)
    scaled_train_and_validation_data = mnist_train.map(scale)
    test_data = mnist_test.map(scale)
    buffer_size = 10000
    shuffled_train_and_validation_data = scaled_train_and_validation_data.shuffle(
        buffer_size
    )

    validation_data = shuffled_train_and_validation_data.take(num_validation_samples)
    train_data = shuffled_train_and_validation_data.skip(num_validation_samples)
    batch_size = 100
    train_data = train_data.batch(batch_size)
    validation_data = validation_data.batch(num_validation_samples)
    test_data = test_data.batch(num_test_samples)

    models(train_data, test_data, validation_data)


def models(train_data, test_data, validation_data):
    """
    functions to do modelling
    """
    validation_inputs, validation_targets = next(iter(validation_data))
    output_size = 10
    hidden_layer_size = 50
    model = Sequential(
        [
            layers.Flatten(input_shape=(28, 28, 1)),
            layers.Dense(hidden_layer_size, activation="relu"),
            layers.Dense(hidden_layer_size, activation="relu"),
            layers.Dense(output_size, activation="softmax"),
        ]
    )
    model.compile(
        optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]
    )
    num_epochs = 5
    model.fit(
        train_data,
        epochs=num_epochs,
        validation_data=(validation_inputs, validation_targets),
        verbose=2,
    )
    test_loss, test_accuracy = model.evaluate(test_data)
    print(
        f"Test loss: {round(test_loss, 2)}. Test accuracy: {round(test_accuracy * 100.0, 2)}%"
    )


if __name__ == "__main__":
    wrapper()
