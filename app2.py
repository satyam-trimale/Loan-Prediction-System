import streamlit as st
import joblib
import pandas as pd

# Load the model with error handling
try:
    model = joblib.load('loan_approval_pipeline.pkl')
except FileNotFoundError:
    st.error("Model file not found. Please ensure 'loan_approval_pipeline.pkl' is in the correct location.")
    st.stop()
except Exception as e:
    st.error(f"An error occurred while loading the model: {e}")
    st.stop()

# App title
st.title('Loan Approval Prediction')

# Input fields organized in collapsible sections
with st.expander("Applicant Details"):
    gender = st.selectbox('Gender', ['Male', 'Female'], index=1)
    married = st.selectbox('Married', ['Yes', 'No'], index=1)
    dependents = st.selectbox('Dependents', ['0', '1', '2', '3+'], index=0)
    education = st.selectbox('Education', ['Graduate', 'Not Graduate'], index=0)
    self_employed = st.selectbox('Self Employed', ['Yes', 'No'], index=1)

with st.expander("Income Details"):
    applicant_income = st.slider(
        'Applicant Income (INR)', 0, 100000, 30000, 500,
        help='Enter your monthly income in Indian Rupees.'
    )
    coapplicant_income = st.slider(
        'Coapplicant Income (INR)', 0, 50000, 1500, 500,
        help="Enter your coapplicant's monthly income in Indian Rupees (if applicable)."
    )

with st.expander("Loan Details"):
    loan_amount = st.slider(
        'Loan Amount (in thousands of INR)', 10, 500, 120, 10,
        help='Enter the desired loan amount in thousands of Indian Rupees.'
    )
    loan_amount_term_options = [12, 24, 36, 60, 120, 180, 240, 360]
    loan_amount_term = st.selectbox(
        'Loan Amount Term (months)', loan_amount_term_options,
        help='Select the desired loan term in months.'
    )
    credit_history = st.selectbox('Credit History', ['Yes', 'No'], index=1)

with st.expander("Property Details"):
    property_area = st.selectbox('Property Area', ['Rural', 'Semiurban', 'Urban'], index=2)

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

# Predictions and display
if st.button('Predict Loan Eligibility'):
    try:
        prediction = model.predict(input_data)
        if prediction == 1:
            st.success("🎉 Eligible for Loan")
            st.write("✔ Factors contributing to approval: Good credit history, sufficient income.")
        else:
            st.error("❌ Not Eligible for Loan")
            st.write("✘ Possible reasons for rejection: Low income, poor credit history, or other factors.")
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")

# Reset Button
if st.button('Reset'):
    for key in st.session_state.keys():
        del st.session_state[key]
    st.experimental_rerun()

# Optional: Visual Insights
st.write("Income Distribution:")
chart_data = pd.DataFrame({'Applicant Income': [applicant_income], 'Coapplicant Income': [coapplicant_income]})
st.bar_chart(chart_data)
