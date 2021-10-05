from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Model, Sequential


def main():

    classifier = Sequential(
        [
            Dense(32, input_shape=(12,), name="Dense1"),
            Dense(32, name="Dense2"),
        ]
    )

    clas = Model(
        inputs=classifier.input,
        outputs=classifier.output,
        name="classifier",
    )

    clas.summary()


if __name__ == "__main__":
    main()
