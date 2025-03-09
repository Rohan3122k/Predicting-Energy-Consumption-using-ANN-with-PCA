# Predicting Energy Consumption using ANN with PCA
Deployed via GitHub & Streamlit

## 1. Introduction
Energy consumption forecasting plays a crucial role in grid management, ensuring stability and efficient power distribution. This project leverages Artificial Neural Networks (ANNs) combined with Principal Component Analysis (PCA) to enhance predictive accuracy while reducing computational complexity.

## 2. Dataset Overview
Source: https://gridwatch.co.uk/
- Features: 26 energy-related variables including frequency, coal, nuclear, ccgt, wind, pumped, hydro, and solar generation metrics.
- Target Variable: demand (energy consumption in MW)
- Preprocessing:
 - Removed unnecessary columns (id, timestamp).
 - Filled missing values using the median.
 - Applied Standardization (Z-score scaling) to normalize data.
  
## 3. Feature Reduction using PCA
- To improve model efficiency, PCA was applied to retain 95% variance, reducing dimensionality from 26 to 17 components.
- The top 5 PCA components captured 30% of total variance.
- Implication: No single feature dominates variance, suggesting a complex multi-factor dependency in energy consumption.

## 4. ANN Model Architecture
- Input Layer: 17 neurons (PCA-transformed features).
- Hidden Layers:
 - 128 neurons (ReLU activation).
 - 64 neurons (ReLU activation).
 - 32 neurons (ReLU activation).
- Output Layer: 1 neuron (Linear activation for regression).
- Optimizer: Adam
- Loss Function: Mean Squared Error (MSE)
- Evaluation Metric: Mean Absolute Error (MAE)

## 5. Model Training & Results
- Training: 100 epochs, batch size = 32
- Final Test MAE: 523.71 MW
- Validation Performance:
- Loss reduced significantly from 397M to 524K across 100 epochs.
- MAE improved from 16022 to 523 MW, indicating strong convergence.
- Performance Metrics
- R² Score: 0.9815 (98.15% variance explained)
- MAPE: 4611.3% (Indicating outlier sensitivity)
- MdAPE: 1.38% (Highly accurate predictions)
### Insights from Evaluation
- Scatter Plot (Actual vs Predicted Demand) showed strong linearity, validating model accuracy.
- Residual Analysis: Errors were normally distributed, with no severe bias observed.
- Time-Series Forecasting: Future energy demand predictions (30 time steps) aligned well with historical trends.

## 6. Model Deployment
- Deployment Pipeline:
 - GitHub Repository: Version-controlled project with Jupyter/Colab integration.
 - Streamlit Web App: Interactive interface for real-time energy demand forecasting.
 - Model Export: ANN saved as energy_demand_model.h5.
 - PCA-transformed feature scaler stored as scaler.pkl for inference.

## 7. Hyperparameter Optimization
- Learning rate tuning showed:
 - 0.001 → MAE: 363.59
 - 0.0005 → MAE: 342.21
 - 0.0001 → MAE: 296.42 (Best performing).

## 8. Conclusion & Future Work
- Key Takeaways:
✔ ANN with PCA successfully predicts energy consumption with 98% accuracy.
✔ PCA enhances efficiency by reducing feature dimensionality without losing significant information.
✔ Deployment via GitHub & Streamlit ensures accessibility and scalability.
