import streamlit as st
import pandas as pd

st.title("📊 Medi-AI Dashboard")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Patients", "1250")
col2.metric("Predictions", "980")
col3.metric("AI Chats", "540")
col4.metric("Accuracy", "96%")

st.divider()

st.subheader("Monthly Patients")

data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Patients": [120, 180, 150, 220, 260, 300]
})

st.line_chart(data.set_index("Month"))

st.subheader("Recent Activity")

st.table(pd.DataFrame({
    "Patient": ["Rahul", "Priya", "Anil"],
    "Status": ["Healthy", "Diabetes", "Heart Risk"]
}))