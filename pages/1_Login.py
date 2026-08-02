import streamlit as st

st.set_page_config(page_title="Login", page_icon="🔐")

st.title("🔐 Medi-AI Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username == "admin" and password == "admin123":
        st.success("✅ Login Successful")
    else:
        st.error("❌ Invalid Username or Password")