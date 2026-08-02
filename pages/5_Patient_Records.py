import streamlit as st
import sqlite3
import pandas as pd

conn = sqlite3.connect("patients.db", check_same_thread=False)
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

st.set_page_config(page_title="Patient Records", page_icon="👤")
st.title("👤 Patient Records")

name = st.text_input("Patient Name")
age = st.number_input("Age", min_value=1, max_value=120, value=25)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
disease = st.text_input("Disease")

if st.button("Add Patient"):
    if name == "" or disease == "":
        st.warning("Please fill all fields.")
    else:
        cursor.execute(
            "INSERT INTO patients(name, age, gender, disease) VALUES (?, ?, ?, ?)",
            (name, age, gender, disease)
        )
        conn.commit()
        st.success("✅ Patient Added Successfully")

st.subheader("📋 Patient List")

df = pd.read_sql_query("SELECT * FROM patients", conn)

if len(df) > 0:
    st.dataframe(df, use_container_width=True)

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Patient Records (CSV)",
        data=csv,
        file_name="patients.csv",
        mime="text/csv"
    )
else:
    st.info("No patient records available.")

st.subheader("🗑 Delete Patient")

delete_id = st.number_input("Enter Patient ID", min_value=1, step=1)

if st.button("Delete Patient"):
    cursor.execute("DELETE FROM patients WHERE id=?", (delete_id,))
    conn.commit()
    st.success("✅ Patient Deleted Successfully")
    st.rerun()