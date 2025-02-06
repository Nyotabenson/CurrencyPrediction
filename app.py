import streamlit as st
import pandas as pd
import math
import joblib
from datetime import datetime
from sklearn.preprocessing import LabelEncoder
import streamlit.components.v1 as components
import os






GTM_ID = "GTM-P7W3S69H"  # Replace with your GTM ID

GTM_SCRIPT = f"""
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
}})(window,document,'script','dataLayer','{GTM_ID}');</script>
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={GTM_ID}"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
"""

components.html(GTM_SCRIPT, height=0)



# ... Rest of your Streamlit app ...

# st.markdown(f"""
# <!-- Google tag (gtag.js) -->
# <script async src="https://www.googletagmanager.com/gtag/js?id=G-2MNRRM86CQ"></script>
# <script>
#   window.dataLayer = window.dataLayer || [];
#   function gtag(){{dataLayer.push(arguments);}}
#   gtag('js', new Date());
#   gtag('config', 'G-2MNRRM86CQ');
# </script>
# """, unsafe_allow_html=True)

# Inject the Google Analytics script using components.html()
#components.html(GA_SCRIPT, unsafe_allow_html=True)




port = os.environ.get('PORT', 8501)

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

st.markdown("[Check Interest Rate](https://fred.stlouisfed.org/series/DGS1)")

df['Interest-rate'] = float(st.number_input(" US Interest rate"))
if st.button("Predict"):
    if (df['Interest-rate'] == 0).any():
        st.error("Interest Rate is NULL!!")
    else:    
        try:

            # Rearrange the features
            #df = df[["Interest-rate","Month","Quarter","Week-of-year","Week-of-month","Day-of-week","Day-of-year","election-year","US_election"]]
            



            
            label_encoder = LabelEncoder()
            df['election-year'] = df['election-year'].replace('Yes', 1)
            df['election-year'] = df['election-year'].replace('No', 0)
            df['US_election'] = df['US_election'].replace('Yes', 1)
            df['US_election'] = df['US_election'].replace('No', 0)
            df = df[["Interest-rate","Month","Quarter","Week-of-year","Week-of-month","Day-of-week","Day-of-year","election-year","US_election"]]
            #st.dataframe(df)

            # Model
            model = joblib.load("rf_model1.pkl")

            pred = model.predict(df)
            col1, col2 = st.columns(2)
            with col1:
              st.write("Currency Prediction is:" , pred)
            with col2:
              st.markdown("Accuracy:") 
              st.markdown("98.43056322368139%")
        except Exception as e:
            #st.write(" error: ", e)
            st.error("Step 1: Make sure, all data provided is correct,")
            st.error("Step 2: If correct, Contact the Developer!")
                
 
