import streamlit as st

st.set_page_config(
    page_title="AI Health Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Health Assistant")
st.write("Enter your symptoms below and get basic health guidance.")

question = st.text_input("Describe your health problem")

if st.button("Ask AI"):

    text = question.lower().strip()

    if text == "":
        st.warning("⚠️ Please enter your symptoms.")

    elif "fever" in text:
        st.success("""
### Possible Advice
✅ You may have a viral fever.

Recommendations:
- Drink plenty of water.
- Take proper rest.
- Monitor your temperature.
- Consult a doctor if fever continues.
""")

    elif "headache" in text:
        st.success("""
### Possible Advice
✅ You may have a headache.

Recommendations:
- Take proper rest.
- Drink enough water.
- Avoid stress.
- Consult a doctor if pain is severe.
""")

    elif "cough" in text:
        st.success("""
### Possible Advice
✅ It may be a common cold.

Recommendations:
- Drink warm water.
- Avoid cold foods.
- Take proper rest.
- Consult a doctor if cough lasts several days.
""")

    elif "heart" in text or "chest pain" in text:
        st.error("""
### Emergency Warning

Chest or heart pain can be serious.

Please seek immediate medical attention or visit the nearest hospital.
""")

    elif "stomach" in text:
        st.success("""
### Possible Advice

You may have a stomach problem.

Recommendations:
- Eat light food.
- Drink enough water.
- Avoid spicy food.
- Consult a doctor if pain continues.
""")

    elif "diabetes" in text or "sugar" in text:
        st.info("""
### Diabetes Advice

- Check your blood sugar regularly.
- Eat a balanced diet.
- Exercise regularly.
- Follow your doctor's advice.
""")

    elif "bp" in text or "blood pressure" in text:
        st.info("""
### Blood Pressure Advice

- Reduce salt intake.
- Exercise regularly.
- Check BP frequently.
- Take medicines as prescribed.
""")

    else:
        st.info("""
No matching symptom found.

Please consult a healthcare professional for an accurate diagnosis.
""")

st.divider()

st.subheader("💡 Health Tips")

st.write("✅ Drink 2–3 litres of water daily.")
st.write("✅ Sleep 7–8 hours every night.")
st.write("✅ Exercise at least 30 minutes daily.")
st.write("✅ Eat fresh fruits and vegetables.")
st.write("✅ Avoid smoking and alcohol.")