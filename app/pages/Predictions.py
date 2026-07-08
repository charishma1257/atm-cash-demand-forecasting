import streamlit as st
import pandas as pd

st.title("📊 Predictions")

df=pd.read_csv("../data/predictions.csv")

st.dataframe(df,use_container_width=True)

st.download_button(
    "Download CSV",
    df.to_csv(index=False),
    "predictions.csv",
    "text/csv"
)