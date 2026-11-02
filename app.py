import streamlit as st

st.set_page_config(page_title="AI Quiz Workshop", page_icon="🎓")
st.title("AI-Powered Quiz and Feedback")
st.write("Welcome! This is Module 1: the web interface.")
role = st.selectbox("Choose your role", ["Student", "Teacher"])
if role == "Student":
    st.subheader("Create your quiz")
    lo = st.text_input("Learning Outcome (LO)", "LO1")
    chapter = st.text_input("Chapter", "Introduction")
    topic = st.text_input("Topic", "Basics")
    count = st.number_input("Number of questions", min_value=1, max_value=20, value=5)
    if st.button("Create quiz"):
        st.info(f"Next module: generate {count} questions for {lo} / {chapter} / {topic}.")
else:
    st.subheader("Teacher dashboard")
    st.info("Next modules: upload content and review student attempts.")
