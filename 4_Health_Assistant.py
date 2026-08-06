import streamlit as st
from groq import Groq
from streamlit_mic_recorder import mic_recorder
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

st.set_page_config(
    page_title="Medi-AI Health Assistant",
    page_icon="🤖",
    layout="wide"
)

client = Groq(api_key="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")

st.title("🤖 Medi-AI Health Assistant")
st.caption("AI Powered Healthcare Assistant")

st.warning(
    "⚠️ This AI provides general health information only. "
    "Please consult a qualified doctor for diagnosis or treatment."
)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.subheader("🎤 Voice Recorder")

audio = mic_recorder(
    start_prompt="🎤 Start Recording",
    stop_prompt="⏹ Stop Recording",
    key="voice"
)

if audio:
    st.success("✅ Voice recorded successfully!")

question = st.text_area(
    "🩺 Describe your symptoms",
    placeholder="Example: I have fever, cough and headache for 2 days..."
)

col1, col2 = st.columns(2)

with col1:
    ask = st.button("🤖 Ask AI")

with col2:
    clear = st.button("🗑 Clear Chat")

if clear:
    st.session_state.chat_history = []
    st.rerun()

answer = ""

if ask:
    if question.strip() == "":
        st.warning("Please enter your symptoms.")
    else:
        with st.spinner("🤖 AI is analyzing..."):

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a helpful healthcare assistant. "
                            "Provide general health information only. "
                            "Do not diagnose diseases or prescribe medicines. "
                            "Recommend consulting a doctor when appropriate."
                        )
                    },
                    {
                        "role": "user",
                        "content": question
                    }
                ]
            )

            answer = response.choices[0].message.content

            st.session_state.chat_history.append(("🧑 You", question))
            st.session_state.chat_history.append(("🤖 AI", answer))

            st.subheader("🤖 AI Response")
            st.write(answer)


if answer:
    st.subheader("🤖 AI Response")
st.write(answer)

if answer:
    pdf_file = "AI_Health_Report.pdf"

    doc = SimpleDocTemplate(pdf_file)
    styles = getSampleStyleSheet()

    story = [
        Paragraph("Medi-AI Health Report", styles["Title"]),
        Paragraph(f"<b>Symptoms:</b> {question}", styles["BodyText"]),
        Paragraph(f"<b>AI Response:</b> {answer}", styles["BodyText"])
    ]

    doc.build(story)

    with open(pdf_file, "rb") as file:
        st.download_button(
            label="📄 Download AI Report",
            data=file,
            file_name="AI_Health_Report.pdf",
            mime="application/pdf"
        )
st.markdown("---")
st.subheader("💬 Chat History")

if st.session_state.chat_history:
    for sender, message in st.session_state.chat_history:
        if "You" in sender:
            st.info(f"{sender}: {message}")
        else:
            st.success(f"{sender}: {message}")
else:
    st.write("No chat history yet.")

st.markdown("---")
st.caption("© 2026 Medi-AI Healthcare Platform | Developed by Jyothika")