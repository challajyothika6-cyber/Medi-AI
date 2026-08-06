import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(
    page_title="Disease Prediction",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 AI Disease Prediction System")
st.caption("Machine Learning Based Health Prediction")

st.warning(
    "⚠️ This prediction is for educational purposes only. "
    "Consult a doctor for medical decisions."
)


data = {
    "fever": [1,1,0,0,1,0,1,1],
    "cough": [1,1,0,1,0,1,1,1],
    "headache": [1,0,1,0,1,1,0,1],
    "fatigue": [1,1,1,0,0,1,1,1],
    "body_pain": [1,0,1,0,1,0,1,1],
    "disease": [
        "Flu",
        "Viral Infection",
        "Migraine",
        "Cold",
        "Flu",
        "Migraine",
        "Dengue",
        "Viral Infection"
    ]
}


df = pd.DataFrame(data)


X = df.drop("disease", axis=1)
y = df["disease"]


model = RandomForestClassifier()

model.fit(X, y)


st.subheader("📝 Enter Patient Symptoms")


col1, col2 = st.columns(2)


with col1:

    fever = st.radio(
        "🌡 Fever",
        ["Yes","No"]
    )

    cough = st.radio(
        "😷 Cough",
        ["Yes","No"]
    )

    headache = st.radio(
        "🤕 Headache",
        ["Yes","No"]
    )


with col2:

    fatigue = st.radio(
        "😴 Fatigue",
        ["Yes","No"]
    )

    body_pain = st.radio(
        "💪 Body Pain",
        ["Yes","No"]
    )


if st.button("🔍 Predict Disease"):

    input_data = [[
        1 if fever=="Yes" else 0,
        1 if cough=="Yes" else 0,
        1 if headache=="Yes" else 0,
        1 if fatigue=="Yes" else 0,
        1 if body_pain=="Yes" else 0
    ]]


    result = model.predict(input_data)


    st.success(
        f"🩺 Predicted Disease: {result[0]}"
    )


    st.info(
        """
        General Advice:
        - Take proper rest
        - Drink enough water
        - Monitor symptoms
        - Consult a qualified doctor
        """
    )


st.markdown("---")

st.subheader("🤖 Model Details")

st.write(
    """
    Machine Learning Algorithm:
    
    ✅ Random Forest Classifier

    Input Features:
    - Fever
    - Cough
    - Headache
    - Fatigue
    - Body Pain
    """
)


st.caption(
    "© 2026 Medi-AI Healthcare Platform | Developed by Jyothika"
)