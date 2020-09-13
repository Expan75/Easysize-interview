import string
from django.db import models


class Prediction(models.Model):
    """Basic predicton class for working with predictions past, present and future"""

    # all valid categories of categorical input
    valid_categories = list(string.ascii_lowercase)

    # Util and Meta information
    created = models.DateTimeField(auto_now_add=True)

    # Inputs fed in prediction
    numerical_input1 = models.FloatField()
    numerical_input2 = models.FloatField()
    categorical_input = models.CharField(max_length=1, choices=valid_categories)

    # Results and performance
    output = models.FloatField()

    class Meta:
        ordering = ["created"]