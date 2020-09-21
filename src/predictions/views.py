from rest_framework import viewsets, permissions
from django.http import JsonResponse
from .serializers import PredictionSerializer
from .models import Prediction


# Predictions CRUD
class PredictionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for serving historical predictions. Does require login auth & permissions.
    """

    queryset = Prediction.objects.all().order_by("-created")
    serializer_class = PredictionSerializer
    permission_classes = [permissions.IsAuthenticated]