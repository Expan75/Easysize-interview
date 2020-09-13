from .models import Prediction
from rest_framework import serializers

# Prediction Model Serializer
class PredictionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prediction
        fields = [
            "created",
            "numerical_input1",
            "numerical_input2",
            "categorical_input",
            "output",
        ]