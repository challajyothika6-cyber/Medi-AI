import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="Patient Records", page_icon="👤")

conn = sqlite3.connect("hospital.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS patients(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    gender TEXT,
    disease TEXT
)
""")
conn.commit()

st.title("👤 Patient Records")

st.subheader("Add Patient")

name = st.text_input("Patient Name")
age = st.number_input("Age", 1, 120)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
disease = st.text_input("Disease")

if st.button("Add Patient"):
    if name and disease:
        cursor.execute(
            "INSERT INTO patients(name,age,gender,disease) VALUES(?,?,?,?)",
            (name, age, gender, disease)
        )
        conn.commit()
        st.success("Patient Added Successfully!")
    else:
        st.warning("Please fill all fields.")

st.markdown("---")

st.subheader("All Patients")

df = pd.read_sql_query("SELECT * FROM patients", conn)

if not df.empty:
    st.dataframe(df, use_container_width=True)
else:
    st.info("No patient records found.")

st.markdown("---")

st.subheader("Delete Patient")

patient_id = st.number_input("Patient ID", 1, step=1)

if st.button("Delete"):
    cursor.execute("DELETE FROM patients WHERE id=?", (patient_id,))
    conn.commit()
    st.success("Patient Deleted Successfully!")