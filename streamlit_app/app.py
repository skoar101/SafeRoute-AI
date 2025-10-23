import streamlit as st
import requests
import json

# ------------------------------
# Config
# ------------------------------
BACKEND_URL = "http://localhost:8000"  # Or your deployed Django API URL

st.set_page_config(page_title="SafeRouteAI", layout="wide")
st.title("SafeRouteAI - Sirsa Flood & Blocked Road Navigator")

# ------------------------------
# Helplines panel
# ------------------------------
st.header("Emergency & Local Helplines")
helplines = [
    {"label": "Police Emergency", "number": "100"},
    {"label": "Ambulance", "number": "108"},
    {"label": "Municipal Flood Helpline", "number": "01666-234567"},
    {"label": "National Highway Helpline", "number": "1033"},
    {"label": "District Disaster Office, Sirsa", "number": "01666-220200"},
]
for h in helplines:
    st.write(f"**{h['label']}**: {h['number']}")

# ------------------------------
# Vehicle type selector
# ------------------------------
vehicle_type = st.selectbox("Select Vehicle Type", ["pedestrian", "bicycle", "car", "bus", "truck"])

# ------------------------------
# Blocked roads map
# ------------------------------
st.header("Blocked Roads Map")
try:
    response = requests.get(f"{BACKEND_URL}/blocked-roads/?vehicle={vehicle_type}")
    data = response.json()
    st.json(data)  # You can later integrate with st.map or pydeck for a real map
except Exception as e:
    st.error(f"Failed to fetch blocked roads: {e}")

# ------------------------------
# Route suggestion
# ------------------------------
st.header("Route Suggestion")
origin = st.text_input("Origin (lng,lat)")
destination = st.text_input("Destination (lng,lat)")
if st.button("Get Route"):
    if origin and destination:
        try:
            r = requests.get(
                f"{BACKEND_URL}/route/?origin={origin}&destination={destination}&vehicle={vehicle_type}"
            )
            route_data = r.json()
            st.json(route_data)
        except Exception as e:
            st.error(f"Failed to get route: {e}")

# ------------------------------
# Weather info
# ------------------------------
st.header("Weather Info")
city = st.text_input("City", value="Sirsa")
if st.button("Get Weather"):
    try:
        r = requests.get(f"{BACKEND_URL}/weather/?city={city}")
        st.json(r.json())
    except Exception as e:
        st.error(f"Failed to fetch weather: {e}")

# ------------------------------
# Flood news
# ------------------------------
st.header("Latest Flood News")
if st.button("Get News"):
    try:
        r = requests.get(f"{BACKEND_URL}/news/")
        st.json(r.json())
    except Exception as e:
        st.error(f"Failed to fetch news: {e}")
