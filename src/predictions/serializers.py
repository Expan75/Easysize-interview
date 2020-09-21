from .models import Prediction
from rest_framework import serializers

# Prediction Model Serializer
class PredictionSerializer(serializers.HyperlinkedModelSerializer):
    """
    Implements the Prediction model serializer. Serializes inputs and outputs,
    only allows prediction output on outbound request.
    """

    class Meta:
        model = Prediction
        fields = ["numerical_input1", "numerical_input2", "categorical_input", "output"]
        read_only_fields = ["created"]
