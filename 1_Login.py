import streamlit as st

st.set_page_config(
    page_title="Medi-AI Login",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Medi-AI Healthcare Platform")
st.subheader("Professional Login System")

st.markdown("---")

username = st.text_input("👤 Username")

password = st.text_input(
    "🔒 Password",
    type="password"
)

remember = st.checkbox("Remember Me")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.button("Login", use_container_width=True):
    if username == "admin" and password == "admin123":
        st.session_state.logged_in = True
        st.success("✅ Login Successful")
        st.balloons()
    else:
        st.error("❌ Invalid Username or Password")

if st.session_state.logged_in:
    st.markdown("---")
    st.success("🎉 Welcome Admin!")
    st.write("You have successfully logged into Medi-AI Healthcare Platform.")
    st.info("Now open Dashboard, Disease Prediction, Health Assistant, Patient Records and PDF Report from the sidebar.")