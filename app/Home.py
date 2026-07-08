import streamlit as st

st.set_page_config(
    page_title="ATM Dashboard",
    page_icon="🏧",
    layout="wide"
)

st.title("🏧 ATM Cash Demand Forecasting")
st.subheader("AI Powered Banking Dashboard")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.page_link(
        "pages/ATM_Map.py",
        label=" ATM Locations",
        icon="🗺️"
    )

    st.page_link(
        "pages/Refill_ATMs.py",
        label=" Refill Required",
        icon="🚚"
    )

with col2:
    st.page_link(
        "pages/Predictions.py",
        label=" Predictions",
        icon="📊"
    )

    st.page_link(
        "pages/Analytics.py",
        label="Analytics",
        icon="📈"
    )

st.page_link(
    "pages/About.py",
    label="About Project",
    icon="ℹ️"
)