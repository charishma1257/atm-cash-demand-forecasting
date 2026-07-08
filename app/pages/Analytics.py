import streamlit as st
import pandas as pd

st.title("📈 Analytics")

df=pd.read_csv("../data/predictions.csv")

left,right=st.columns(2)

with left:

    st.subheader("Withdrawal Trend")

    st.area_chart(
        df["Predicted Withdrawal"]
    )

with right:

    st.subheader("Top 5 ATM")

    top=df.sort_values(
        "Predicted Withdrawal",
        ascending=False
    ).head()

    st.table(top)