<<<<<<< HEAD
"""
Purpose: Django admin configuration for BlockedRoad model.
"""
from django.contrib import admin
from .models import BlockedRoad

@admin.register(BlockedRoad)
class BlockedRoadAdmin(admin.ModelAdmin):
    list_display = ("name", "reason", "water_level_cm", "timestamp")
    search_fields = ("name", "reason", "reporter")
=======
"""
Purpose: Django admin configuration for BlockedRoad model.
"""
from django.contrib import admin
from .models import BlockedRoad

@admin.register(BlockedRoad)
class BlockedRoadAdmin(admin.ModelAdmin):
    list_display = ("name", "reason", "water_level_cm", "timestamp")
    search_fields = ("name", "reason", "reporter")
>>>>>>> 2f55220dae0bb14c7c90517c68fd70ac27d114b2
