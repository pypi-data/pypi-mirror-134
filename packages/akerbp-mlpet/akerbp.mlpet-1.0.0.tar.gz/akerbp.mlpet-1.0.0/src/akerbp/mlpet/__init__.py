"""
.. include:: ../README.md
"""
import importlib.metadata
from akerbp.mlpet.Datasets.dataset import Dataset
from akerbp.mlpet.Datasets import (
    feature_engineering,
    imputers,
    utilities,
    preprocessors,
)

__version__ = importlib.metadata.version(__name__)

__docformat__ = "restructuredtext"

__all__ = ["Dataset", "feature_engineering", "imputers", "utilities", "preprocessors"]
