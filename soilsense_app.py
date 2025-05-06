import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("soil_model.pkl")

# Title
st.title("🌱 Soil Sense AI - Soil Nature Prediction")

# Input fields
water_ph = st.slider("Water pH", 5.0, 9.0, 6.5)
soil_moisture = st.slider("Soil Moisture (%)", 0, 100, 40)
soil_temp = st.slider("Soil Temperature (°C)", 0, 50, 25)
ambient_temp = st.slider("Ambient Temperature (°C)", 0, 50, 30)
humidity = st.slider("Humidity (%)", 0, 100, 50)
rain_forecast = st.selectbox("Rain Forecast", [0, 1], format_func=lambda x: "No Rain" if x == 0 else "Rain Expected")

# Predict
if st.button("Predict Soil Nature"):
    input_data = np.array([[water_ph, soil_moisture, soil_temp, ambient_temp, humidity, rain_forecast]])
    result = model.predict(input_data)
    st.success(f"🌍 Predicted Soil Nature: **{result[0]}**")
