from rest_framework import generics
from .models import TravelPlan
from .serializers import TravelPlanSerializer

class TravelPlanList(generics.ListCreateAPIView):
    queryset = TravelPlan.objects.all()
    serializer_class = TravelPlanSerializer