import streamlit as st
import datetime
import pandas as pd

report = pd.DataFrame()

st.write(datetime.datetime.now())

with st.form("daily_report"):
    name = st.selectbox(label="Name", options=["Jake", "Mark"])
    rig = st.selectbox(label="Rig", options=[1,2,3,4])
    hole_number = st.selectbox(label="Hole Number", options=[1, 2, 3, 4])
    location = st.selectbox(label="Location", options=["Maldives", "Madagascar", "Bahamas"])

    depth = st.slider(label="Depth (m)", min_value=0, max_value=1000)

    submitted = st.form_submit_button()
    if submitted:
        report = pd.DataFrame([[name, rig, hole_number, location, depth]])
        st.write(report)

st.download_button(label="Download Report", data = report.to_csv())





