import streamlit as st
import sqlite3
import pandas as pd


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.error("🔒 Please login first.")
    st.stop()


from reportlab.platypus import SimpleDocTemplate, Table
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph

st.set_page_config(page_title="PDF Report", page_icon="📄")

st.title("📄 Patient PDF Report")

conn = sqlite3.connect("patients.db")
df = pd.read_sql_query("SELECT * FROM patients", conn)

st.dataframe(df, use_container_width=True)

if st.button("Generate PDF Report"):
    pdf_file = "Patient_Report.pdf"

    doc = SimpleDocTemplate(pdf_file)
    elements = []

    styles = getSampleStyleSheet()
    elements.append(Paragraph("Patient Records Report", styles["Heading1"]))

    data = [df.columns.tolist()] + df.values.tolist()

    table = Table(data)
    table.setStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.grey),
        ("TEXTCOLOR", (0,0), (-1,0), colors.whitesmoke),
        ("GRID", (0,0), (-1,-1), 1, colors.black),
        ("BACKGROUND", (0,1), (-1,-1), colors.beige),
    ])

    elements.append(table)
    doc.build(elements)

    with open(pdf_file, "rb") as file:
        st.download_button(
            "📥 Download PDF",
            file,
            file_name="Patient_Report.pdf",
            mime="application/pdf"
        )

    st.success("✅ PDF Generated Successfully")