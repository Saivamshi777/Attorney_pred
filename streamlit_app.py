import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load the trained model
with open("logistic_regression_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("scaler.pkl", "rb") as file:
    scaler = pickle.load(file)

# Streamlit UI
st.title("Insurance Claim Prediction App")
st.write("Enter the details below to predict claim approval.")

# User Inputs
CLMSEX = st.selectbox("Claimant Sex", [0, 1])  # 0 = Female, 1 = Male
CLMINSUR = st.selectbox("Claimant Insured", [0, 1])  # 0 = No, 1 = Yes
SEATBELT = st.selectbox("Seatbelt Used", [0, 1])  # 0 = No, 1 = Yes
CLMAGE = st.number_input("Claimant Age", min_value=0, max_value=120, step=1)
LOSS = st.number_input("Loss Amount", min_value=0.0, step=0.01)
CLAIM_AMOUNT_REQUESTED = st.number_input("Claim Amount Requested", min_value=0.0, step=0.01)
CLAIM_APPROVAL_STATUS = st.selectbox("Claim Approval Status", [0, 1])  # 0 = Rejected, 1 = Approved
SETTLEMENT_AMOUNT = st.number_input("Settlement Amount", min_value=0.0, step=0.01)
Accident_Severity = st.selectbox('Accident Severity',['Minor','Severe','Moderate'])
Policy_Type       = st.selectbox('Policy Type',['Comprehensive','Third-Party'])
Driving_Record    = st.selectbox('Driving Record',['Minor Offenses','Clean','Major Offenses'])

data = {
    
    'CLMSEX': [CLMSEX],
    'CLMINSUR': [CLMINSUR],
    'SEATBELT': [SEATBELT],
    'CLMAGE': [CLMAGE],
    'LOSS': [LOSS],
    'CLAIM_AMOUNT_REQUESTED': [CLAIM_AMOUNT_REQUESTED],
    'Claim_Approval_Status': [Claim_Approval_Status],
    'SETTLEMENT_AMOUNT': [SETTLEMENT_AMOUNT],
    'Accident_Severity_Moderate': [1 if Accident_Severity = 'Moderate'],
    'Accident_Severity_Severe': [1 if Accident_Severity = 'Severe'],
    'Policy_Type_Third-Party': [1 if Policy_Type = 'Third-Party'],
    'Driving_Record_Major Offenses': [1 if Driving_Record = 'Major Offenses'],
    'Driving_Record_Minor Offenses': [1 if Driving_Record = 'Minor Offenses']
}


# Prepare input data
input_data = pd.Dataframe(data,index = [0])

input_data[["CLMAGE", "LOSS", "Claim_Amount_Requested", "Settlement_Amount"]] = scaler.transform(input_data[["CLMAGE", "LOSS", "Claim_Amount_Requested", "Settlement_Amount"]])


# Predict


if st.button("Show Result"):
    prediction = model.predict_proba(input_data)
    # Code to execute after button click
    if survival_proba[0][1] > 0.5:
        st.write("Survived")
    else:
        st.write("Not Survived")
