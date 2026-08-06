import streamlit as st
import pandas as pd

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.error("🔒 Please login first.")
    st.stop()

st.set_page_config(
    page_title="Medi-AI Dashboard",
    page_icon="🏥",
    layout="wide"
)

st.markdown("""
<style>

.main{
    background-color:#F5F7FA;
}

h1{
    color:#1565C0;
}

[data-testid="stMetric"]{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 4px 10px rgba(0,0,0,0.1);
}

div[data-testid="stDataFrame"]{
    background:white;
    border-radius:15px;
    padding:10px;
}

</style>
""", unsafe_allow_html=True)

st.title("🏥 Medi-AI Healthcare Platform")
col1, col2 = st.columns([2,1])

with col1:
    st.info("""
🤖 AI Clinical Assistant

✔ Patient Summary
✔ Disease Prediction
✔ Report Generation
✔ AI Suggestions
""")

with col2:
    st.success("""
📅 Today's Summary

👨 Patients : 25
📅 Appointments : 8
🧪 Reports : 30
""")
col1, col2 = st.columns([4, 1])

with col1:
    st.text_input("", placeholder="🔍 Search patients, appointments, reports...")

with col2:
    st.markdown("""
    👨‍⚕️ **Dr. Mehta**
    
    Cardiologist
    """)
st.caption("AI Powered Hospital Management System")

st.success("👨‍⚕️ Welcome Doctor")

st.write("Manage patients, predict diseases, generate reports and use the AI Health Assistant from one dashboard.")

st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("👨 Total Patients", "25", "+3")

with col2:
    st.metric("🩺 Disease Predictions", "18", "+5")

with col3:
    st.metric("📄 Reports Generated", "30", "+2")

with col4:
    st.metric("🤖 AI Consultations", "15", "+4")

st.markdown("---")

st.subheader("📅 Today's Appointments")

appointments = pd.DataFrame({
    "Patient":["Rahul","Anjali","Kiran","Priya"],
    "Doctor":["Dr. Kumar","Dr. Mehta","Dr. Ravi","Dr. Sneha"],
    "Time":["10:00 AM","11:30 AM","2:00 PM","4:00 PM"],
    "Status":["Confirmed","Pending","Completed","Confirmed"]
})

st.dataframe(appointments, use_container_width=True)

st.markdown("---")

left, right = st.columns(2)

with left:
    st.subheader("📊 Disease Distribution")

    disease = pd.DataFrame({
        "Disease":["Diabetes","Heart Disease","Fever","Cancer"],
        "Patients":[12,8,20,3]
    })

    st.bar_chart(disease.set_index("Disease"))

with right:
    st.subheader("📈 Monthly Patients")

    monthly = pd.DataFrame({
        "Month":["Jan","Feb","Mar","Apr","May","Jun"],
        "Patients":[15,20,22,28,35,40]
    })

    from streamlit_calendar import calendar

st.subheader("📅 Calendar")

calendar_events = [
    {
        "title": "Rahul",
        "start": "2026-08-05",
        "end": "2026-08-05",
        "color": "#4CAF50"
    },
    {
        "title": "Anjali",
        "start": "2026-08-10",
        "end": "2026-08-10",
        "color": "#2196F3"
    }
]

calendar_options = {
    "initialView": "dayGridMonth",
    "height": 500
}

calendar(
    events=calendar_events,
    options=calendar_options,
    key="calendar"
)
st.markdown("### 📋 Today's Schedule")

schedule = [
    ("09:30 AM", "Rahul", "Confirmed"),
    ("11:00 AM", "Anjali", "Pending"),
    ("02:00 PM", "Kiran", "Confirmed"),
    ("04:00 PM", "Priya", "Completed")
]

for time, patient, status in schedule:
    st.write(f"**{time}** — {patient} ({status})")
st.markdown("---")

st.subheader("📝 Recent Activities")

st.success("✅ Rahul's Medical Report Generated")
st.info("🤖 AI Assistant Responded to Patient Query")
st.warning("📅 Appointment Pending Approval")
st.success("🩺 Disease Prediction Completed")

st.markdown("---")

st.subheader("🔔 Notifications")

st.info("📌 3 appointments scheduled today.")
st.info("💊 5 new patient records added.")
st.info("📄 2 reports generated successfully.")

st.markdown("---")
from groq import Groq

client = Groq(api_key="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")

st.subheader("🤖 AI Assistant")

question = st.text_area(
    "🩺 Describe Symptoms",
    placeholder="Example: I have fever and cough..."
)

if st.button("Ask AI"):
    if question:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": question}
            ]
        )

        st.subheader("AI Response")
        st.write(response.choices[0].message.content)
st.caption("© 2026 Medi-AI Healthcare Platform | Developed by Jyothika")