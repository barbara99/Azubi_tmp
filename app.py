import streamlit as st
import pandas as pd
import joblib
import os
import requests

# =========================
# Load Model and Artifacts
# =========================

# Load trained model
@st.cache_resource
def download_model():
    url = "https://huggingface.co/BarbaraAsiamah/model_rf/resolve/main/model_rf.pkl"
    model_path = "model_rf.pkl"
    
    if not os.path.exists(model_path):
        response = requests.get(url)
        if response.status_code == 200:
            with open(model_path, "wb") as f:
                f.write(response.content)
        else:
            st.error("Failed to download model from Hugging Face.")
            st.stop()
    
    return joblib.load(model_path)

# Load model
model = download_model()

# Load scaler used during model training
scaler = joblib.load("scaler.pkl")

# Load expected feature names for one-hot encoding
expected_features = joblib.load("feature_names.pkl")

# ======================
# Streamlit App Header
# ======================

st.title("📊 TERM DEPOSIT SUBSCRIPTION PREDICTION")
st.markdown("### Term Deposit Prediction App")

# ======================
# Section: Personal Info
# ======================

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

# ==========================
# Section: Contact Info
# ==========================

contact = st.selectbox("**Contact**: Contact communication of client", ['telephone', 'cellular'])

month = st.selectbox("**Month**: Last contact month of the year", [
    'january', 'february', 'march', 'april', 'may', 'june', 'july',
    'august', 'september', 'october', 'november', 'december'
])

day_of_week = st.selectbox("**Day of Week**: Last contact day of the year", [
    'monday', 'tuesday', 'wednesday', 'thursday', 'friday'
])

duration = st.number_input("**Duration**: Last contact duration of the year, in seconds", min_value=0.0, value=0.0)

# ==========================
# Section: Campaign Details
# ==========================

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

# ==========================
# Prediction Section
# ==========================

if st.button("Predict"):
    st.markdown("#### 🎯 Prediction Result")

    # Build input dictionary from user inputs
    raw_input = {
        "age": age,
        "job": job,
        "marital": marital,
        "education": education,
        "default": default,
        "housing": housing,
        "loan": loan,
        "contact": contact,
        "month": month,
        "day_of_week": day_of_week,
        "duration": duration,
        "campaign": campaign,
        "pdays": pdays,
        "previous": previous,
        "poutcome": poutcome,
        "emp.var.rate": emp_var_rate,
        "cons.price.idx": cons_price_idx,
        "cons.conf.idx": cons_conf_idx,
        "euribor3m": euribor3m,
        "nr.employed": nr_employed,
        "campaign_diff": campaign_diff
    }

    # Convert input dictionary to DataFrame
    input_df = pd.DataFrame([raw_input])

    # One-hot encode categorical variables
    input_df_encoded = pd.get_dummies(input_df)

    # Align encoded input to expected features (fill missing with 0)
    input_df_encoded = input_df_encoded.reindex(columns=expected_features, fill_value=0)

    # Scale numeric features
    scaled_input = scaler.transform(input_df_encoded)

    # Generate prediction and probability
    prediction = model.predict(scaled_input)[0]
    probability = model.predict_proba(scaled_input)[0][1]

    # Display results
    if prediction == 1:
        st.success(f"✅ Yes (Will Subscribe) — Confidence: {probability:.2%}")
    else:
        st.warning(f"❌ No (Will Not Subscribe) — Confidence: {1 - probability:.2%}")
