import os
import logging
import joblib
import string
import numpy as np
import pandas as pd
import warnings
from django.db import models
from api.settings import MODEL_DIR


# Get already set up logger
logger = logging.getLogger(__name__)

# setup vars for use in categorical input (django is a bit picky with representation)
categories = tuple(list(string.ascii_lowercase))
choices = zip(categories, categories)

# load model (local fs for now, TODO: should DEF be cached!!!)
model_path = os.path.join(MODEL_DIR, "model.joblib")
with warnings.catch_warnings():
    warnings.filterwarnings("ignore")
    with open(model_path, "rb") as f:
        model = joblib.load(f)


class Prediction(models.Model):
    """Basic predicton class for working with predictions past, present and future"""

    # Util and Meta information
    created = models.DateTimeField(auto_now_add=True)

    # Inputs fed in prediction
    numerical_input1 = models.FloatField()
    numerical_input2 = models.FloatField()
    categorical_input = models.CharField(max_length=1, choices=choices)

    # Model prediction result (based on pipelined inputs)
    output = models.FloatField(editable=False)

    # Utility class to allow ordering
    class Meta:
        ordering = ["created"]

    def generate_output(self):
        """
        Method for pipelining input data into a prediction output.

        If successful: returns and sets the predicted real number based on the inputs.
        else: returns AssertionError
        """
        # logging
        logger.debug(
            f"generate_output() was called /w inputs: {self.numerical_input1}, {self.numerical_input2}, {self.categorical_input}"
        )

        # collect the raw numerical inputs and throw assertion error if input is wrong (empty or shape mismatch)
        raw_filled_inputs = [
            given_input
            for given_input in [
                self.numerical_input1,
                self.numerical_input2,
                self.categorical_input,
            ]
            if given_input != None
        ]
        if len(raw_filled_inputs) != 3:
            raise AssertionError(
                f"Incorrect number of non-null inputs were fed to prediction pipeline. was {len(raw_filled_inputs)}, should be 3."
            )

        # pipe input data through onehot encoder (do not change numerical raw input)
        onehot_encoded = [
            1.0 if ch == raw_filled_inputs[2] else 0.0
            for ch in list(string.ascii_lowercase)
        ]
        # fuse with untouched inputs
        features = np.array(
            raw_filled_inputs[:2] + onehot_encoded, dtype=np.float64
        ).reshape(1, -1)

        # get and save prediction as float
        prediction = model.predict(features)
        self.output = prediction[0]

    # Now override native save method to run generate output automatically
    def save(self, *args, **kwargs):
        """
        Overrites native save method to generate prediction output before model save;
        defaults to generating zero as prediction if pipeline is broken or incorrectly fed.
        """

        logger.debug(f"save() was called on prediction instance.")

        try:
            self.generate_output()
            logger.debug(f"Output was generated succesfully")
        except AssertionError:
            self.output = 0
            logger.debug(f"Output was not generated successfully, defaulting to 0")

        super().save(*args, **kwargs)  # Call the "real" save() method.
