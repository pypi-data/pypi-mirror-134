from sklearn.pipeline import Pipeline
from sklearn.dummy import DummyClassifier
from $package_name.processing import preprocessors as pp
from $package_name.config import config

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