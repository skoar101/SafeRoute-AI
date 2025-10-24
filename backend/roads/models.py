 HEAD
"""
Purpose: Database schema for blocked roads, including attributes for reporting.
"""
from django.db import models

VEHICLE_TYPES = (
    ("pedestrian", "Pedestrian"),
    ("bicycle", "Bicycle"),
    ("car", "Car"),
    ("bus", "Bus"),
    ("truck", "Truck"),
)

BLOCKAGE_TYPES = (
    ("waterlogging", "Waterlogging"),
    ("construction", "Construction"),
)

class BlockedRoad(models.Model):
    name = models.CharField(max_length=128)
    geojson = models.JSONField()  # GeoJSON Feature for blocked segment
    reason = models.CharField(choices=BLOCKAGE_TYPES, max_length=32)
    water_level_cm = models.IntegerField(default=0)
    affected_vehicles = models.JSONField()
    reporter = models.CharField(max_length=64)
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="blockages/", null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.reason})"

"""
Purpose: Database schema for blocked roads, including attributes for reporting.
"""
from django.db import models

VEHICLE_TYPES = (
    ("pedestrian", "Pedestrian"),
    ("bicycle", "Bicycle"),
    ("car", "Car"),
    ("bus", "Bus"),
    ("truck", "Truck"),
)

BLOCKAGE_TYPES = (
    ("waterlogging", "Waterlogging"),
    ("construction", "Construction"),
)

class BlockedRoad(models.Model):
    name = models.CharField(max_length=128)
    geojson = models.JSONField()  # GeoJSON Feature for blocked segment
    reason = models.CharField(choices=BLOCKAGE_TYPES, max_length=32)
    water_level_cm = models.IntegerField(default=0)
    affected_vehicles = models.JSONField()
    reporter = models.CharField(max_length=64)
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="blockages/", null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.reason})"
    
 2f55220dae0bb14c7c90517c68fd70ac27d114b2
