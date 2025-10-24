<<<<<<< HEAD
"""
Purpose: Django project-level URL routing (routes to app URLs).
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("roads.urls")),
]
=======
"""
Purpose: Django project-level URL routing (routes to app URLs).
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("roads.urls")),
]
>>>>>>> 2f55220dae0bb14c7c90517c68fd70ac27d114b2
