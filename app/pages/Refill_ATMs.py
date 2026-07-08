import streamlit as st
import pandas as pd

st.title("🚚 Refill Required ATMs")

df=pd.read_csv("../data/predictions.csv")

refill=df[
    df["Predicted Withdrawal"]>4500
]

st.dataframe(refill,use_container_width=True)