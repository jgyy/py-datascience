"""
Train Test Split
"""
from numpy import arange
from sklearn.model_selection import train_test_split


def wrapper():
    """
    wrapper function which description will not change
    """
    a_data = arange(1, 101)
    print(a_data)
    b_data = arange(501, 601)
    print(b_data)
    print(train_test_split(a_data))
    a_train, a_test, b_train, b_test = train_test_split(
        a_data, b_data, test_size=0.2, random_state=365
    )

    print(a_train.shape, a_test.shape)
    print(a_train)
    print(a_test)
    print(b_train.shape, b_test.shape)
    print(b_train)
    print(b_test)


if __name__ == "__main__":
    wrapper()
