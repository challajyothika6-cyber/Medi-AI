import import streamlit as st

st.set_page_config(
    page_title="Medi-AI",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 Medi-AI")
st.subheader("AI Powered Healthcare Assistant")

st.write("""
Welcome to Medi-AI.

Features:
- Disease Prediction
- Symptom Checker
- Medical Dashboard
- Patient Reports
- AI Health Assistant
""")

st.image("https://images.unsplash.com/photo-1576091160399-112ba8d25d1d", use_container_width=True)