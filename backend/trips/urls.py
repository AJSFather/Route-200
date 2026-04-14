from django.urls import path
from .views import TravelPlanList

urlpatterns = [
    path('', TravelPlanList.as_view(), name='trip-list'),
]