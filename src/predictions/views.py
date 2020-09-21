from rest_framework import viewsets, permissions
from django.http import JsonResponse
from .serializers import PredictionSerializer
from .models import Prediction

# realtime prediction with asyncronhous save using worker
def generatePrediction(request):
    return


# Predictions CRUD
class PredictionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for serving historical predictions. Does require login auth.
    """

    queryset = Prediction.objects.all().order_by("-created")
    serializer_class = PredictionSerializer
    permission_classes = [permissions.IsAuthenticated]