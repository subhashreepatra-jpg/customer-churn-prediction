import streamlit as st
import joblib
import pandas as pd

model = joblib.load("customer_churn_model.pkl")
gender_encoder = joblib.load("gender_encoder.pkl")
geography_encoder = joblib.load("geography_encoder.pkl")

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="🏦",
    layout="centered"
)

st.title("🏦 Customer Churn Prediction")
st.write("Predict whether a banking customer is likely to stay or churn.")

st.subheader("Enter Customer Details")

credit_score = st.number_input("Credit Score", min_value=300, max_value=900, value=650)

geography = st.selectbox("Geography", ["France", "Germany", "Spain"])

gender = st.selectbox("Gender", ["Male", "Female"])

age = st.number_input("Age", min_value=18, max_value=100, value=35)

tenure = st.number_input("Tenure", min_value=0, max_value=10, value=5)

balance = st.number_input("Balance", min_value=0.0, value=50000.0)

num_products = st.number_input(
    "Number of Products", min_value=1, max_value=4, value=1
)

has_cr_card = st.selectbox("Has Credit Card?", ["Yes", "No"])

active_member = st.selectbox("Is Active Member?", ["Yes", "No"])

estimated_salary = st.number_input(
    "Estimated Salary", min_value=0.0, value=50000.0
)

if st.button("Predict Churn"):

    geography_encoded = geography_encoder.transform([geography])[0]
    gender_encoded = gender_encoder.transform([gender])[0]

    has_cr_card_value = 1 if has_cr_card == "Yes" else 0
    active_member_value = 1 if active_member == "Yes" else 0

    input_data = pd.DataFrame([{
        "year": 2026,
        "CreditScore": credit_score,
        "Geography": geography_encoded,
        "Gender": gender_encoded,
        "Age": age,
        "Tenure": tenure,
        "Balance": balance,
        "NumOfProducts": num_products,
        "HasCrCard": has_cr_card_value,
        "IsActiveMember": active_member_value,
        "EstimatedSalary": estimated_salary
    }])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("🔴 Customer is likely to churn.")
    else:
        st.success("🟢 Customer is likely to stay.")
