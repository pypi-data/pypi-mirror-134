from sklearn.pipeline import Pipeline
from sklearn.dummy import DummyClassifier
from recoform.processing import preprocessors as pp
from recoform.config import config

pipe = Pipeline(
    [
        (
            "first_step",
            pp.CategoricalImputer(variables=config.VARIABLES),
        ),
        (
            "last_step",
            DummyClassifier(strategy="most_frequent")
        )
    ]
)