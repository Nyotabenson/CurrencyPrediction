import streamlit as st
import pandas as pd
import math
import joblib
from datetime import datetime
from sklearn.preprocessing import LabelEncoder

st.title("CURRENCY PREDICTIONS")

date_entry = None
date_entry = date_entry or datetime.now()

# Extraction of data from date input
def extract_date_features(date_entry):
    try:

        if isinstance(date_entry, str):
            date_entry = pd.to_datetime(date_entry)
    
        # Calculate the week of the month
        first_day_of_month = date_entry.replace(day=1)
        week_of_month = math.ceil((date_entry.day + first_day_of_month.weekday()) / 7)

        # Extract features
        features = {
            "year": date_entry.year,
            "Month": date_entry.month,
            "Quarter": (date_entry.month - 1) // 3 + 1,
            "Week-of-year": date_entry.isocalendar()[1],
            "Day-of-year": date_entry.timetuple().tm_yday,
            "Week-of-month": week_of_month,
            "Day-of-week": date_entry.weekday(),  # 0=Monday, 6=Sunday
        }

        return features
    except:
        st.write("Please input a valid data")







# Inputs
options = ['Yes', 'No']

date = st.date_input("Select a date:", None)
df = pd.DataFrame([extract_date_features(date)])

# Add more columns through input features
df['election-year'] = st.selectbox("Kenya election year?", options)
df['US_election'] = st.selectbox("United State of America election year?", options)
df['Interest-rate'] = float(st.number_input(" US Interest rate"))

try:

    # Rearrange the features
    df = df[["Interest-rate","Month","Quarter","Week-of-year","Week-of-month","Day-of-week","Day-of-year","election-year","US_election"]]


    
    label_encoder = LabelEncoder()
    df['election-year'] = df['election-year'].replace('Yes', 1)
    df['election-year'] = df['election-year'].replace('No', 0)
    df['US_election'] = df['US_election'].replace('Yes', 1)
    df['US_election'] = df['US_election'].replace('No', 0)
    st.dataframe(df)

    # Model
    model = joblib.load("rf_model1.pkl")

    pred = model.predict(df)

    st.write("Currency Prediction is:" , pred)
except:
    st.error("To view the Currency Price, please input data!!")    