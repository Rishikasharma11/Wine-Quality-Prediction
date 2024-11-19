import streamlit as st
import numpy as np
import pickle

# Loading the trained pipeline
model_path = "wine-quality-prediction.pkl"  
with open(model_path, "rb") as file:
    pipeline = pickle.load(file)

# Streamlit App
st.title("Wine Quality Prediction System")
st.write("Predict the quality of wine based on key chemical properties.")

# Input fields for wine features
fixed_acidity = st.number_input("Fixed Acidity", min_value=0.0, max_value=20.0, step=0.1)
volatile_acidity = st.number_input("Volatile Acidity", min_value=0.0, max_value=2.0, step=0.01)
citric_acid = st.number_input("Citric Acid", min_value=0.0, max_value=2.0, step=0.01)
residual_sugar = st.number_input("Residual Sugar", min_value=0.0, max_value=50.0, step=0.1)
chlorides = st.number_input("Chlorides", min_value=0.0, max_value=1.0, step=0.001)
free_sulfur_dioxide = st.number_input("Free Sulfur Dioxide", min_value=0.0, max_value=100.0, step=1.0)
total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide", min_value=0.0, max_value=400.0, step=1.0)
density = st.number_input("Density", min_value=0.0, max_value=2.0, step=0.001)
pH = st.number_input("pH", min_value=0.0, max_value=14.0, step=0.01)
sulphates = st.number_input("Sulphates", min_value=0.0, max_value=2.0, step=0.01)
alcohol = st.number_input("Alcohol", min_value=0.0, max_value=20.0, step=0.1)

# Predict Button
if st.button("Predict"):
    # Prepare the input data
    input_data = np.array([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides,
                            free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]])
    
    # Prediction using the pipeline
    prediction = pipeline.predict(input_data)[0]

    # Display result
    if prediction == 1:
        st.success("The wine is of good quality!")
    else:
        st.error("The wine is not of good quality.")
