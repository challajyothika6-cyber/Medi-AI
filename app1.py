import os
from dotenv import load_dotenv
import streamlit as st
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(
    page_title="MediCro AI",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 MediCro AI")
st.subheader("AI Emergency Health Triage Assistant")

st.warning(
    "This tool is for educational purposes only and is not a substitute for professional medical advice."
)

name = st.text_input("Patient Name")

age = st.number_input(
    "Age",
    min_value=1,
    max_value=120,
    value=20
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female", "Other"]
)

symptoms = st.text_area(
    "Describe your symptoms",
    height=180
)

if st.button("Analyze Symptoms"):

    if symptoms.strip() == "":
        st.error("Please enter symptoms.")

    else:

        prompt = f"""
You are an expert emergency medical assistant.

Patient:
Name: {name}
Age: {age}
Gender: {gender}

Symptoms:
{symptoms}

Respond in the following format:

🔴 Urgency Level

🩺 Possible Conditions

💊 First Aid

🏥 Recommendation

⚠️ Emergency Warning Signs

Mention clearly this is NOT a medical diagnosis.
"""

        with st.spinner("Analyzing..."):

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            answer = response.choices[0].message.content

        st.success("Analysis Complete")

        st.markdown(answer)

st.divider()

st.subheader("Emergency Numbers")

c1, c2, c3 = st.columns(3)

with c1:
    st.error("🚑 Ambulance\n\n108")

with c2:
    st.warning("👮 Police\n\n100")

with c3:
    st.info("🔥 Fire\n\n101")

st.divider()

st.caption("Developed using Streamlit + Groq AI")