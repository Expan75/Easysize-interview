from rest_framework import viewsets, permissions
from .models import Prediction
from .serializers import PredictionSerializer
from django.http import JsonResponse


# User CRUD
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint for serving predictions. Does require login auth.
    """

    queryset = Prediction.objects.all().order_by("-created")
    serializer_class = PredictionSerializer
    permission_classes = [permissions.IsAuthenticated]
