import hydra
from hydra.utils import instantiate
from omegaconf import DictConfig
from tensorflow.keras.models import Model


@hydra.main(config_path="../configs/", config_name="params.yaml")
def main(config: DictConfig):

    classifier = instantiate(config.test_)

    clas = Model(
        inputs=classifier.input,
        outputs=classifier.output,
        name="classifier",
    )

    clas.summary()


if __name__ == "__main__":
    main()
