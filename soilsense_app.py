import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load("soil_model.pkl")  # Make sure this file is in the same directory

# App title
st.title("🌾 SoilSense AI - Smart Soil Nature Predictor")

st.markdown("Predict soil nature based on environmental factors and crop type.")

# Input fields
soil_moisture = st.number_input("🌱 Soil Moisture (%)", min_value=0.0, max_value=100.0, value=40.0)
soil_temperature = st.number_input("🌡️ Soil Temperature (°C)", min_value=0.0, max_value=60.0, value=25.0)
water_ph = st.number_input("💧 Water pH", min_value=3.0, max_value=10.0, value=6.5)
ambient_temp_avg = st.number_input("🌡️ 5-day Avg Ambient Temperature (°C)", min_value=0.0, max_value=60.0, value=30.0)
humidity_avg = st.number_input("💧 5-day Avg Humidity (%)", min_value=0.0, max_value=100.0, value=50.0)
rainfall_forecast = st.number_input("🌧️ Rainfall Forecast for next 5 days (mm)", min_value=0.0, max_value=500.0, value=50.0)
sunlight_days = st.slider("☀️ Sunny Days in next 5 days", 0, 5, 3)

crop_type = st.selectbox(
    "🌿 Crop Type",
    options=["leafy", "root", "fruiting"]
)

# Map crop type to numeric value (if model needs it)
crop_type_map = {"leafy": 0, "root": 1, "fruiting": 2}
crop_type_val = crop_type_map[crop_type]

# Predict button
if st.button("🔍 Predict Soil Nature"):
    input_data = np.array([[soil_moisture, soil_temperature, water_ph,
                            ambient_temp_avg, humidity_avg,
                            rainfall_forecast, sunlight_days, crop_type_val]])

    prediction = model.predict(input_data)
    st.success(f"🧪 Predicted Soil Nature: **{prediction[0]}**")
