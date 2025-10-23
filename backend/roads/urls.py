"""
Purpose: Django app-level URL routing (routes to views).
"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("blocked-roads/", views.blocked_roads, name="blocked_roads"),
    path("report/", views.report_blockage, name="report"),
    path("route/", views.route_suggestion, name="route_suggestion"),
    path("weather/", views.weather, name="weather"),
    path("news/", views.flood_news, name="flood_news"),
    path("blocked-list/", views.blocked_list, name="blocked_list"),
]