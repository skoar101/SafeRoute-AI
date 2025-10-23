"""
Purpose: Django admin configuration for BlockedRoad model.
"""
from django.contrib import admin
from .models import BlockedRoad

@admin.register(BlockedRoad)
class BlockedRoadAdmin(admin.ModelAdmin):
    list_display = ("name", "reason", "water_level_cm", "timestamp")
    search_fields = ("name", "reason", "reporter")