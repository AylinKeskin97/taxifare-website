import streamlit as st
import requests
import geopandas as gpd
import pandas as pd

# Title and introduction
st.title("TaxiFareModel")
st.subheader("Select the parameters of the ride")

# Instruction text
st.markdown("""
1. Please provide the following details:
    - Date and Time
    - Pickup Longitude
    - Pickup Latitude
    - Dropoff Longitude
    - Dropoff Latitude
    - Passenger Count
""")

# Form for input parameters
query = None
with st.form('Ride Parameters'):
    date_time = st.text_input("Date and Time", '2013-07-06 17:18:00')
    pickup_long = st.text_input('Pickup Longitude', '-73.950655')
    pickup_lat = st.text_input('Pickup Latitude', '40.783282')
    drop_long = st.text_input('Dropoff Longitude', '-73.984365')
    drop_lat = st.text_input('Dropoff Latitude', '40.769802')
    pass_count = st.text_input('Passenger Count', '1')

    # Submit button
    submitted = st.form_submit_button("Submit")
    if submitted:
        query = {
            'pickup_datetime': date_time,
            'pickup_longitude': float(pickup_long),
            'pickup_latitude': float(pickup_lat),
            'dropoff_longitude': float(drop_long),
            'dropoff_latitude': float(drop_lat),
            'passenger_count': int(pass_count)
        }

# New York City map coordinates for display
nyc_map_data = pd.DataFrame({
    'lat': [float(pickup_lat), float(drop_lat)],
    'lon': [float(pickup_long), float(drop_long)]
})

# Display map of New York City
st.map(nyc_map_data)

# API URL
url = 'https://taxifare.lewagon.ai/predict'

# Warning about the API URL
st.warning('You might want to use your own API for the prediction, not the one provided by Le Wagon.')

# Display estimated fare
st.header("Your estimated fare is:")
if query is not None:
    response = requests.get(url=url, params=query).json()["fare"]
    st.write(f"${response:.2f}")
