import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load the model
model = joblib.load('loan_approval_pipeline.pkl')

# App title
st.title('Loan Approval Prediction')

# Input fields with improvements and descriptions
gender = st.selectbox('Gender', ['Male', 'Female'], index=1)  # Default: Male
married = st.selectbox('Married', ['Yes', 'No'], index=1)  # Default: Yes
dependents = st.selectbox('Dependents', ['0', '1', '2', '3+'], index=0)  # Default: 0
education = st.selectbox('Education', ['Graduate', 'Not Graduate'], index=0)  # Default: Graduate
self_employed = st.selectbox('Self Employed', ['Yes', 'No'], index=1)  # Default: Yes

# Applicant Income (with slider, currency, description, and default value)
applicant_income = st.slider(
    'Applicant Income (INR)',
    min_value=0,
    max_value=100000,
    step=500,
    value=30000,  # Default value
    help='Enter your monthly income in Indian Rupees.'
)

# Coapplicant Income (with slider, currency, description, and default value)
coapplicant_income = st.slider(
    'Coapplicant Income (INR)',
    min_value=0,
    max_value=50000,
    step=500,
    value=1500,  # Default value
    help='Enter your coapplicant\'s monthly income in Indian Rupees (if applicable).'
)

# Loan Amount (with slider, currency, range, and description)
loan_amount = st.slider(
    'Loan Amount (in thousands of INR)',
    min_value=10,
    max_value=500,
    step=10,
    value=120,
    help='Enter the desired loan amount in thousands of Indian Rupees.'
)

# Loan Amount Term (with dropdown, custom option, and description)
loan_amount_term_options = [12, 24, 36, 60, 120, 180, 240, 360]  # Common loan terms
loan_amount_term = st.selectbox(
    'Loan Amount Term (months)',
    loan_amount_term_options,
    help='Select the desired loan term in months.'
)

# Credit History
credit_history = st.selectbox('Credit History', ['Yes', 'No'], index=1)  # Default: Yes

# Property Area
property_area = st.selectbox('Property Area', ['Rural', 'Semiurban', 'Urban'], index=2)  # Default: Urban

# Preprocess input data
input_data = pd.DataFrame({
    'Gender': [1 if gender == 'Male' else 0],
    'Married': [1 if married == 'Yes' else 0],
    'Dependents': [4 if dependents == '3+' else int(dependents)],
    'Education': [1 if education == 'Graduate' else 0],
    'Self_Employed': [1 if self_employed == 'Yes' else 0],
    'ApplicantIncome': [applicant_income],
    'CoapplicantIncome': [coapplicant_income],
    'LoanAmount': [loan_amount],
    'Loan_Amount_Term': [loan_amount_term],
    'Credit_History': [1 if credit_history == 'Yes' else 0],
    'Property_Area': [0 if property_area == 'Rural' else 1 if property_area == 'Semiurban' else 2]
})

# Make predictions
if st.button('Predict Loan Eligibility'):
    try:
        prediction = model.predict(input_data)
        if prediction == 1:
            st.success("Eligible for Loan")
        else:
            st.error("Not Eligible for Loan")
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")