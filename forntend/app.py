import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="AI Interview Simulator", page_icon="🤖")

st.title("🤖 AI Interview Simulator")

# -------------------------------
# Session State Setup
# -------------------------------
if "question" not in st.session_state:
    st.session_state.question = None

if "evaluation" not in st.session_state:
    st.session_state.evaluation = None

# -------------------------------
# Sidebar Controls
# -------------------------------
st.sidebar.header("Interview Settings")

role = st.sidebar.text_input("Role", "ML Engineer")
difficulty = st.sidebar.selectbox("Difficulty", ["easy", "medium", "hard"])

# -------------------------------
# Generate Question Button
# -------------------------------
if st.sidebar.button("Generate New Question"):
    try:
        response = requests.get(
            f"{BACKEND_URL}/question/{role}",
            params={"difficulty": difficulty}
        )

        if response.status_code == 200:
            st.session_state.question = response.json()["question"]
            st.session_state.evaluation = None
        else:
            st.error("Failed to generate question. Check backend.")

    except Exception as e:
        st.error(f"Backend not reachable: {e}")

# -------------------------------
# Display Question
# -------------------------------
if st.session_state.question:
    st.subheader("📌 Interview Question")
    st.write(st.session_state.question)

    answer = st.text_area("✍️ Your Answer", height=200)

    if st.button("Submit Answer"):
        if answer.strip() == "":
            st.warning("Please enter your answer.")
        else:
            try:
                response = requests.post(
                    f"{BACKEND_URL}/evaluate",
                    json={
                        "question": st.session_state.question,
                        "answer": answer
                    }
                )

                if response.status_code == 200:
                    st.session_state.evaluation = response.json()["evaluation"]
                else:
                    st.error("Evaluation failed.")

            except Exception as e:
                st.error(f"Backend not reachable: {e}")

# -------------------------------
# Show Evaluation
# -------------------------------
if st.session_state.evaluation:
    st.subheader("📊 Evaluation")
    st.write(st.session_state.evaluation)
