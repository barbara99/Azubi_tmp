import streamlit as st
import pandas as pd
import joblib

# Load model artifacts
model = joblib.load("model_rf.pkl")
scaler = joblib.load("scaler.pkl")
expected_features = joblib.load("feature_names.pkl")

st.title("📊 TERM DEPOSIT SUBSCRIPTION PREDICTION")
st.markdown("### Term Deposit Prediction App")

# === Personal Info ===
age = st.number_input("**Age**: Age of client", min_value=17.0, max_value=98.0, value=30.0)

job = st.selectbox("**Job**: Type of Job", [
    'housemaid', 'services', 'admin.', 'blue-collar', 'technician', 'retired',
    'management', 'unemployed', 'self-employed', 'entrepreneur', 'student', 'unknown'
])

marital = st.selectbox("**Marital**: Marital status of client", [
    'married', 'single', 'divorced', 'unknown'
])

education = st.selectbox("**Education**: Education level of client", [
    'lower basic', 'mid basic', 'upper basic', 'high school', 'university degree',
    'professional course', 'illiterate', 'unknown'
])

default = st.selectbox("**Credit Default**: Has client defaulted on credit?", ['no', 'yes', 'unknown'])
housing = st.selectbox("**Housing**: Does Client have a house loan?", ['no', 'yes', 'unknown'])
loan = st.selectbox("**Personal Loan**: Does the client have a personal loan", ['no', 'yes', 'unknown'])

# === Contact Info ===
contact = st.selectbox("**Contact**: Contact communication of client", ['telephone', 'cellular'])
month = st.selectbox("**Month**: Last contact month of the year", [
    'january', 'february', 'march', 'april', 'may', 'june', 'july',
    'august', 'september', 'october', 'november', 'december'
])
day_of_week = st.selectbox("**Day of Week**: Last contact day of the year", [
    'monday', 'tuesday', 'wednesday', 'thursday', 'friday'
])
duration = st.number_input("**Duration**: Last contact duration of the year, in seconds", min_value=0.0, value=0.0)

# === Campaign Info ===
previous = st.number_input("**Previous**: Number of contacts before this campaign", min_value=0.0, value=0.0)
poutcome = st.selectbox("**Previous Outcome**: Outcome of the previous campaign", [
    'nonexistent', 'failure', 'success'
])
emp_var_rate = st.number_input("**Employment Variation Rate**: Client employment variation rate", value=0.0)
cons_price_idx = st.number_input("**Consumer Price Index**: Current CPI", value=0.0)
cons_conf_idx = st.number_input("**Consumer Confidence Index**: Current CCI", value=0.0)
euribor3m = st.number_input("**Euro Interbank Offered Rate**: Current 3-month EURIBOR", value=0.0)
nr_employed = st.number_input("**Number of Employees**: Number of bank employees", value=0.0)
pdays = st.number_input("**Pdays**: Days since client was last contacted", value=0.0)
campaign = st.number_input("**Campaign**: Number of contacts during this campaign", value=0.0)
campaign_diff = st.number_input("**Campaign Difference**", value=0.0)

# === Prepare Input ===
# Placeholder - You’ll still need to encode these into the model's feature format
if st.button("Predict"):
    st.markdown("#### 🎯 Prediction Result")
    
    # Build input_dict based on your model features and one-hot encoding
    # For now, just display success message (you will insert model code here)
    st.success("✅ Yes (Will Subscribe)")  # Replace with actual prediction output
