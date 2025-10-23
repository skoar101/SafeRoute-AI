# streamlit_app/app.py

import streamlit as st
import sys
import os

# Add backend folder to path to import your backend code
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../backend/roads')))

# Import functions from your backend (adjust if needed)
try:
    import models  # from backend/roads/models.py
except ImportError:
    st.warning("Backend models not found. Make sure the path is correct.")

# ---- Streamlit UI ----

st.set_page_config(page_title="Safe Route AI Dashboard", layout="wide")
st.title("Safe Route AI Dashboard")
st.write("Welcome to the SafeRoute AI interactive app!")

# Example: Input from user
route_name = st.text_input("Enter a route name:")

if st.button("Check Route"):
    # Example function call from models.py
    try:
        # Replace 'check_route' with an actual function in models.py
        result = models.check_route(route_name)  
        st.success(f"Route info: {result}")
    except Exception as e:
        st.error(f"Error calling backend function: {e}")

# Example: Display static info
st.subheader("Demo Information")
st.write("You can add graphs, maps, or tables here based on your backend data.")
