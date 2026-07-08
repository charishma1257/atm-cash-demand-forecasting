import streamlit as st

st.title("🗺️ ATM Locations")

with open("../atm_map.html","r",encoding="utf-8") as f:

    html=f.read()

st.components.v1.html(html,height=700)