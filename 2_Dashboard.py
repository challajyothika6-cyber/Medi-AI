import streamlit as st

st.set_page_config(page_title="Dashboard", page_icon="📊")

st.title("📊 Medi-AI Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Patients", "120")

with col2:
    st.metric("Predictions", "350")

with col3:
    st.metric("Accuracy", "98%")

st.divider()

st.subheader("Welcome")

st.write("""
Welcome to Medi-AI.

This dashboard will help doctors to:
- Predict diseases
- Store patient records
- Generate reports
- Chat with AI Health Assistant
""")