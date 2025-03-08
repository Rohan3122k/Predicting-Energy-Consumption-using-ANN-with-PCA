# -*- coding: utf-8 -*-
"""app

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15GiAKElxTqwd-lcOz1fIMP9_v7JNJhjy
"""

import streamlit as st
import tensorflow as tf
import numpy as np
import joblib
from sklearn.preprocessing import MinMaxScaler

# Load the trained model and scaler
model = tf.keras.models.load_model("energy_demand_model.h5")
scaler = joblib.load("scaler.pkl")

# Streamlit UI
st.title("Energy Demand Predictor")
st.write("Enter values to predict future energy consumption.")

# User Input for Features (with proper labels from training)
frequency = st.number_input("Frequency (Hz)", value=50.0)
coal_generation = st.number_input("Coal Generation (MW)", value=1000.0)
nuclear_generation = st.number_input("Nuclear Generation (MW)", value=5000.0)
ccgt_generation = st.number_input("CCGT Generation (MW)", value=3000.0)
wind_generation = st.number_input("Wind Generation (MW)", value=2000.0)
pumped_storage = st.number_input("Pumped Storage (MW)", value=500.0)
hydro_generation = st.number_input("Hydro Generation (MW)", value=600.0)
biomass_generation = st.number_input("Biomass Generation (MW)", value=400.0)
oil_generation = st.number_input("Oil Generation (MW)", value=100.0)
solar_generation = st.number_input("Solar Generation (MW)", value=1500.0)
ocgt_generation = st.number_input("OCGT Generation (MW)", value=50.0)
french_ict = st.number_input("French ICT (MW)", value=300.0)
dutch_ict = st.number_input("Dutch ICT (MW)", value=200.0)
irish_ict = st.number_input("Irish ICT (MW)", value=100.0)
ew_ict = st.number_input("EW ICT (MW)", value=150.0)
nemo_link = st.number_input("Nemo Link (MW)", value=180.0)
other_generation = st.number_input("Other Generation (MW)", value=250.0)

# Prepare Input Data (matching the feature names and model input)
input_data = np.array([[frequency, coal_generation, nuclear_generation, ccgt_generation, wind_generation,
                        pumped_storage, hydro_generation, biomass_generation, oil_generation, solar_generation,
                        ocgt_generation, french_ict, dutch_ict, irish_ict, ew_ict, nemo_link, other_generation]])

# Scale the input data using the loaded scaler
input_data_scaled = scaler.transform(input_data)

# Predict Energy Demand when button is pressed
if st.button("Predict Energy Demand"):
    prediction = model.predict(input_data_scaled)
    st.success(f"Predicted Energy Demand: {prediction[0][0]:.2f} MW")
