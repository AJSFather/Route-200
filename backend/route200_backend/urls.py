from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def test_api(request):
    return JsonResponse({"message": "Route 200: Connection Successful!"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/trips/', include('trips.urls')), 
]