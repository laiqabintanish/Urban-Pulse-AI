import streamlit as st
import joblib
import numpy as np

st.title("🌡️ Urban Heat Island (UHI) Micro-Climate Exposure Index")
st.write("Calculate hyper-local pedestrian heat risk based on urban density and green cover.")

ambient = st.slider("Base Ambient Temperature (°C)", 30.0, 45.0, 38.0)
building = st.slider("Building Density (%)", 10.0, 100.0, 80.0)
green = st.slider("Green Canopy Cover (%)", 0.0, 60.0, 10.0)
albedo = st.slider("Surface Albedo (Reflectivity)", 0.1, 0.6, 0.2)
humidity = st.slider("Relative Humidity (%)", 30.0, 90.0, 55.0)

if st.button("Calculate Micro-Climate Risk"):
    model = joblib.load('uhi_model.pkl')
    features = np.array([[ambient, building, green, albedo, humidity]])
    prediction = model.predict(features)[0]
    
    st.success(f"Estimated Pedestrian-Level Heat Index: **{prediction:.2f}°C**")
    if prediction > 42:
        st.error("🚨 Severe Heat Trap Risk! Avoid outdoor exposure.")
    elif prediction > 38:
        st.warning("⚠️ Moderate Heat Caution. Stay hydrated.")
    else:
        st.success("🟢 Safe Zone.")
