import streamlit as st
from prediction_page import show_prediction_page
from data_explore_page import show_data_explore_page



page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

if page == "Predict":
    show_prediction_page()
else:
    show_data_explore_page()

