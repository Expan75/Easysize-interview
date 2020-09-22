import warnings
import os
import logging
import joblib
import string
import numpy as np
import pandas as pd

# pipeline specific dependencies
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# import and unpickle model (local fs for now)
model_path = "/Users/Erik/Dev/Easysize/notebooks/model.joblib"

with warnings.catch_warnings():
    warnings.filterwarnings("ignore")
    with open(model_path, "rb") as f:
        model = joblib.load(f)

# inspecting pipeline attributes
print(model)

# sample data /w with onehot encoding
categories = [ch for ch in string.ascii_lowercase]
data = [2.2, 3.9, "c"]
features = np.array(
    data[:2] + [0 if category != data[2] else 1 for category in categories]
).reshape(1, -1)
print("printing features:")
print(features)


prediction = model.predict(features)
print("prediction: %s" % prediction[0])
