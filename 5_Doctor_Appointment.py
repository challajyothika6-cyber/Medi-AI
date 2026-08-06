import streamlit as st
import sqlite3
import pandas as pd
from datetime import date

st.set_page_config(
    page_title="Doctor Appointment",
    page_icon="🩺",
    layout="wide"
)

conn = sqlite3.connect("hospital.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS appointments(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_name TEXT,
    age INTEGER,
    gender TEXT,
    doctor TEXT,
    appointment_date TEXT,
    appointment_time TEXT,
    problem TEXT
)
""")

conn.commit()

st.title("🩺 Doctor Appointment Booking")

st.subheader("Book Appointment")

name = st.text_input("Patient Name")

age = st.number_input(
    "Age",
    min_value=1,
    max_value=120,
    value=25
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female", "Other"]
)

doctor = st.selectbox(
    "Select Doctor",
    [
        "Dr. Mehta (Cardiologist)",
        "Dr. Kumar (General Physician)",
        "Dr. Sneha (Dermatologist)",
        "Dr. Ravi (Neurologist)"
    ]
)

appointment_date = st.date_input(
    "Appointment Date",
    min_value=date.today()
)

appointment_time = st.selectbox(
    "Appointment Time",
    [
        "09:00 AM",
        "10:00 AM",
        "11:00 AM",
        "12:00 PM",
        "02:00 PM",
        "03:00 PM",
        "04:00 PM",
        "05:00 PM"
    ]
)

problem = st.text_area(
    "Describe Your Health Problem"
)

if st.button("📅 Book Appointment"):

    if name == "" or problem == "":
        st.warning("Please fill all fields.")

    else:

        cursor.execute(
            """
            INSERT INTO appointments
            (
                patient_name,
                age,
                gender,
                doctor,
                appointment_date,
                appointment_time,
                problem
            )
            VALUES
            (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                name,
                age,
                gender,
                doctor,
                str(appointment_date),
                appointment_time,
                problem
            )
        )

        conn.commit()

        st.success("✅ Appointment Booked Successfully!")

st.markdown("---")

st.subheader("📋 Appointment List")

df = pd.read_sql_query(
    "SELECT * FROM appointments",
    conn
)

if len(df) > 0:

    st.dataframe(
        df,
        use_container_width=True
    )

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇ Download Appointment List",
        csv,
        "appointments.csv",
        "text/csv"
    )

else:

    st.info("No appointments available.")

st.markdown("---")

st.subheader("❌ Cancel Appointment")

delete_id = st.number_input(
    "Appointment ID",
    min_value=1,
    step=1
)

if st.button("Delete Appointment"):

    cursor.execute(
        "DELETE FROM appointments WHERE id=?",
        (delete_id,)
    )

    conn.commit()

    st.success("✅ Appointment Deleted Successfully")