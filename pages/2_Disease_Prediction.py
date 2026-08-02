import streamlit as st

st.set_page_config(page_title="Disease Prediction")

st.title("🩺 Disease Prediction")

age = st.number_input("Age", 1, 100, 25)
fever = st.selectbox("Fever", ["No", "Yes"])
cough = st.selectbox("Cough", ["No", "Yes"])
bp = st.number_input("Blood Pressure", 80, 200, 120)

if st.button("Predict Disease"):
    if fever == "Yes" and cough == "Yes":
        st.error("Prediction: Flu")
    elif bp > 140:
        st.warning("Prediction: High Blood Pressure")
    else:
        st.success("Prediction: Healthy")