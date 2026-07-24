import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("❌ Groq API Key not found. Please check your .env file.")
    st.stop()

# Create Groq client
client = Groq(api_key=api_key)

# Streamlit Page Configuration
st.set_page_config(
    page_title="AI Emergency Health Triage",
    page_icon="🏥",
    layout="centered"
)

# Title
st.title("🏥 AI Emergency Health Triage")
st.markdown("### Enter your symptoms below")

# User Input
symptoms = st.text_area(
    "Symptoms",
    placeholder="Example: I have fever, headache and cough"
)

# Analyze Button
if st.button("🔍 Analyze Symptoms"):

    if symptoms.strip() == "":
        st.warning("⚠️ Please enter your symptoms.")

    else:

        prompt = f"""
You are an AI Emergency Health Assistant.

Analyze the following symptoms carefully.

Symptoms:
{symptoms}

Respond ONLY in this format.

🚨 Urgency Level:
(Low / Medium / High)

🩺 Possible Condition:
(2 or 3 possible conditions)

💊 First Aid:
• Point 1
• Point 2
• Point 3

🏥 Recommendation:

🚑 Emergency Alert:
If symptoms include chest pain, severe breathing difficulty, heavy bleeding, unconsciousness, seizures, stroke symptoms, severe allergic reaction, or other life-threatening emergencies, advise the user to immediately call the local emergency number or visit the nearest hospital.

⚠️ Medical Disclaimer:
This is an AI-generated suggestion only and is NOT a medical diagnosis.

Use simple English.
Limit the response to about 150 words.
"""

        try:

            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            answer = response.choices[0].message.content

            st.success("✅ Analysis Completed")

            st.subheader("🩺 AI Medical Report")

            st.markdown(answer)

            st.info("💧 Stay hydrated, take adequate rest, and monitor your symptoms.")

            st.warning(
                "⚠️ This AI tool provides informational guidance only. "
                "It does NOT replace professional medical advice, diagnosis, or treatment. "
                "Always consult a qualified healthcare professional."
            )

        except Exception as e:
            st.error(f"❌ Error: {e}")

# Footer
st.markdown("---")
st.caption("Developed using ❤️ Python, Streamlit & Groq AI")