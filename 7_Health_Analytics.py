import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(
    page_title="Health Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

conn = sqlite3.connect("hospital.db", check_same_thread=False)

st.title("📊 Health Analytics Dashboard")
st.caption("Medi-AI Healthcare Data Analytics")

st.markdown("---")

# Sample hospital data
patients = pd.DataFrame({
    "Month": [
        "Jan","Feb","Mar","Apr",
        "May","Jun","Jul","Aug"
    ],
    "Patients": [
        45,60,75,90,
        110,130,150,170
    ]
})

disease = pd.DataFrame({
    "Disease": [
        "Fever",
        "Diabetes",
        "Heart Disease",
        "Cold",
        "Cancer"
    ],
    "Patients": [
        45,
        30,
        20,
        55,
        10
    ]
})

appointments = pd.DataFrame({
    "Department": [
        "Cardiology",
        "General",
        "Dermatology",
        "Neurology"
    ],
    "Appointments": [
        40,
        80,
        35,
        25
    ]
})


# Top Metrics

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "👨 Total Patients",
        "340",
        "+25"
    )

with col2:
    st.metric(
        "🩺 Appointments",
        "180",
        "+15"
    )

with col3:
    st.metric(
        "💊 Medicines",
        "120",
        "+10"
    )

with col4:
    st.metric(
        "🤖 AI Consultations",
        "95",
        "+20"
    )


st.markdown("---")


# Patient Growth

st.subheader("📈 Patient Growth")

st.line_chart(
    patients.set_index("Month")
)


st.markdown("---")


# Disease Analysis

col1, col2 = st.columns(2)


with col1:

    st.subheader("🦠 Disease Distribution")

    st.bar_chart(
        disease.set_index("Disease")
    )


with col2:

    st.subheader("🏥 Department Appointments")

    st.bar_chart(
        appointments.set_index("Department")
    )


st.markdown("---")


# Patient Records

st.subheader("👥 Recent Patient Data")


patient_data = pd.DataFrame({

    "Patient":[
        "Rahul",
        "Anjali",
        "Kiran",
        "Priya",
        "Arjun"
    ],

    "Age":[
        35,
        28,
        50,
        40,
        32
    ],

    "Disease":[
        "Fever",
        "Diabetes",
        "Heart Disease",
        "Cold",
        "Fever"
    ],

    "Status":[
        "Recovered",
        "Treatment",
        "Treatment",
        "Recovered",
        "Pending"
    ]

})


st.dataframe(
    patient_data,
    use_container_width=True
)


st.markdown("---")


# Download Report

csv = patient_data.to_csv(
    index=False
).encode("utf-8")


st.download_button(
    "⬇ Download Health Analytics Report",
    csv,
    "health_report.csv",
    "text/csv"
)


st.markdown("---")

st.success(
    "✅ Analytics Dashboard Updated Successfully"
)


st.caption(
    "© 2026 Medi-AI Healthcare Platform | Developed by Jyothika"
)