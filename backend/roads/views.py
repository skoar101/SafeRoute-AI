"""
Purpose: Handles all business logic, APIs, and page rendering.
"""
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import BlockedRoad
from django.conf import settings
import requests
from django.views.decorators.csrf import csrf_exempt

def vehicle_can_pass(vehicle_type, water_level_cm):
    limits = {"pedestrian": 20, "bicycle": 30, "car": 50, "bus": 80, "truck": 200}
    return water_level_cm < limits.get(vehicle_type, 20)

def index(request):
    helplines = [
        {"label": "Police Emergency", "number": "100"},
        {"label": "Ambulance", "number": "108"},
        {"label": "Municipal Flood Helpline", "number": "01666-234567"},
        {"label": "National Highway Helpline", "number": "1033"},
        {"label": "District Disaster Office, Sirsa", "number": "01666-220200"},
    ]
    return render(request, "roads/index.html", {
        "helplines": helplines,
        "city_center": [29.5334, 75.0177],
    })

def blocked_roads(request):
    vehicle_type = request.GET.get("vehicle", "car")
    blockages = []
    for br in BlockedRoad.objects.all():
        can_pass = True
        if br.reason == "waterlogging":
            can_pass = vehicle_can_pass(vehicle_type, br.water_level_cm)
        if not can_pass or vehicle_type in br.affected_vehicles:
            blockages.append(br.geojson)
    return JsonResponse({"type": "FeatureCollection", "features": blockages})

@csrf_exempt
def report_blockage(request):
    if request.method == "POST":
        data = request.POST
        BlockedRoad.objects.create(
            name=data.get("name"),
            geojson=data.get("geojson"),
            reason=data.get("reason"),
            water_level_cm=int(data.get("water_level_cm", 0)),
            affected_vehicles=data.getlist("affected_vehicles"),
            reporter=data.get("reporter", "Anonymous"),
            image=request.FILES.get("image"),
        )
        return redirect("blocked_list")
    return render(request, "roads/report.html")

def blocked_list(request):
    blocked_roads = BlockedRoad.objects.order_by("-timestamp")
    return render(request, "roads/blocked_list.html", {"blocked_roads": blocked_roads})

def weather(request):
    city = request.GET.get("city", "Sirsa")
    key = settings.OPENWEATHER_API_KEY
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={key}&units=metric"
    resp = requests.get(url)
    return JsonResponse(resp.json())

def flood_news(request):
    api_key = settings.NEWSAPI_KEY
    query = "flood blocked road Sirsa Haryana"
    url = f"https://newsapi.org/v2/everything?q={query}&language=en&sortBy=publishedAt&apiKey={api_key}"
    resp = requests.get(url)
    news = resp.json().get("articles", [])[:10]
    return JsonResponse({"articles": news})

def route_suggestion(request):
    origin = request.GET.get("origin")
    destination = request.GET.get("destination")
    vehicle_type = request.GET.get("vehicle", "car")
    ors_key = settings.ORS_API_KEY
    url = "https://api.openrouteservice.org/v2/directions/driving-car"
    headers = {"Authorization": ors_key}
    body = {
        "coordinates": [origin, destination],
    }
    resp = requests.post(url, json=body, headers=headers)
    return JsonResponse(resp.json())