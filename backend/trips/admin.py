from django.contrib import admin
from .models import TravelPlan

@admin.register(TravelPlan)
class TravelPlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'location_name', 'start_date', 'end_date')
    search_fields = ('title', 'location_name')