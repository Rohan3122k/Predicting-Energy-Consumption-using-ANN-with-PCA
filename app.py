# -*- coding: utf-8 -*-
"""app

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15GiAKElxTqwd-lcOz1fIMP9_v7JNJhjy
"""

import streamlit as st
import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load the trained model
model = tf.keras.models.load_model("energy_demand_model.h5", custom_objects={"mse": tf.keras.losses.MeanSquaredError()})

# Streamlit UI
st.title(" Energy Demand Predictor")
st.write("Enter values to predict future energy consumption.")

# User Input for Features
0 = st.number_input("Frequency (Hz)", value=50.0)
1 = st.number_input("Coal Generation (MW)", value=1000.0)
2 = st.number_input("Nuclear Generation (MW)", value=5000.0)
3 = st.number_input("CCGT Generation (MW)", value=3000.0)
4 = st.number_input("Wind Generation (MW)", value=2000.0)
5 = st.number_input("Pumped Storage (MW)", value=500.0)
6 = st.number_input("Hydro Generation (MW)", value=600.0)
7 = st.number_input("Biomass Generation (MW)", value=400.0)
8 = st.number_input("Oil Generation (MW)", value=100.0)
9 = st.number_input("Solar Generation (MW)", value=1500.0)
10 = st.number_input("OCGT Generation (MW)", value=50.0)
11 = st.number_input("French ICT (MW)", value=300.0)
12 = st.number_input("Dutch ICT (MW)", value=200.0)
13 = st.number_input("Irish ICT (MW)", value=100.0)
14 = st.number_input("EW ICT (MW)", value=150.0)
15 = st.number_input("Nemo Link (MW)", value=180.0)
16 = st.number_input("Other (MW)", value=250.0)



# Prepare Input Data
input_data = np.array([[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]])

scaler = MinMaxScaler()
input_data = scaler.fit_transform(input_data)

#  Debugging: Print input shapes
print("Expected Model Input Shape:", model.input_shape)  # Shape required by model
print("Actual Input Shape:", input_data.shape)  # Shape being passed to model

# Predict button
if st.button("Predict Energy Demand"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Energy Demand: {prediction[0][0]:.2f} MW")
