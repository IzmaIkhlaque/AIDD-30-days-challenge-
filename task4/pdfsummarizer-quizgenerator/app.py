import streamlit as st
import os
import tempfile
from agent import Agent

# --- Page Configuration ---
st.set_page_config(
    page_title="Study Notes Summarizer & Quiz Generator",
    page_icon="🧠",
    layout="wide",
)

# --- CSS for Styling ---
st.markdown("""
<style>
    .stApp {
        background-color: #000;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 12px;
        padding: 10px 24px;
        border: none;
        transition: background-color 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .card {
        background-color: #0D0D0D;
        border-radius: 12px;
        padding: 25px;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .stExpander {
        background-color: #0D0D0D;
        border-radius: 12px;
        border: 1px solid #e6e6e6;
    }
</style>
""", unsafe_allow_html=True)


# --- Session State Initialization ---
if "agent" not in st.session_state:
    try:
        st.session_state.agent = Agent(model="gpt-4o-mini")
    except ValueError as e:
        st.error(f"Initialization Error: {e}. Please ensure your OPENAI_API_KEY is set in a .env file.")
        st.session_state.agent = None
if "summary" not in st.session_state:
    st.session_state.summary = ""
if "quiz" not in st.session_state:
    st.session_state.quiz = {}
if "pdf_text" not in st.session_state:
    st.session_state.pdf_text = ""
if "pdf_ref" not in st.session_state:
    st.session_state.pdf_ref = None


# --- UI Components ---
st.title("📝 Study Notes Summarizer & Quiz Generator")
st.markdown("Upload your PDF study notes, and let AI help you revise faster and test your knowledge!")

if st.session_state.agent:
    uploaded_file = st.file_uploader("Upload your PDF file here", type=["pdf"])

    if uploaded_file is not None:
        # To prevent re-processing, check if it's a new file
        if st.session_state.pdf_ref != uploaded_file.name + str(uploaded_file.size):
            st.session_state.pdf_ref = uploaded_file.name + str(uploaded_file.size)
            st.session_state.summary = ""
            st.session_state.quiz = {}
            st.session_state.pdf_text = ""

            with st.spinner("Analyzing your document... please wait."):
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmpfile:
                    tmpfile.write(uploaded_file.getvalue())
                    st.session_state.pdf_text = st.session_state.agent.extract_text_from_pdf(tmpfile.name)
                os.remove(tmpfile.name)
            
            if not st.session_state.pdf_text:
                st.error("Could not extract text from the PDF. The file might be empty, scanned, or corrupted.")
            else:
                st.success("PDF processed successfully! You can now generate a summary or a quiz.")

        if st.session_state.pdf_text:
            col1, col2 = st.columns(2)
            with col1:
                if st.button("✨ Generate Summary", use_container_width=True):
                    with st.spinner("Crafting your summary..."):
                        st.session_state.summary = st.session_state.agent.generate_summary(st.session_state.pdf_text)
                    st.success("Summary generated!")
            
            with col2:
                if st.button("❓ Create Quiz", use_container_width=True):
                    with st.spinner("Building your quiz..."):
                        st.session_state.quiz = st.session_state.agent.generate_quiz(st.session_state.pdf_text)
                    st.success("Quiz created!")

    # --- Display Area for Summary and Quiz ---
    if st.session_state.summary:
        st.markdown("---")
        st.subheader("✍️ Your Summary")
        st.markdown(f'<div class="card">{st.session_state.summary}</div>', unsafe_allow_html=True)
    
    if st.session_state.quiz:
        st.markdown("---")
        st.subheader("🧠 Test Your Knowledge")
        
        quiz_data = st.session_state.quiz
        
        # --- Multiple Choice Questions ---
        if quiz_data.get("multiple_choice"):
            st.markdown("#### Multiple Choice Questions")
            for i, mcq in enumerate(quiz_data["multiple_choice"]):
                with st.expander(f"**Question {i+1}:** {mcq['question']}"):
                    options = mcq["options"]
                    correct_answer_key = mcq["correct_answer"]
                    
                    # Create a form for each question to handle selections independently
                    with st.form(key=f"mcq_form_{i}"):
                        user_answer = st.radio("Choose your answer:", list(options.values()), key=f"mcq_{i}")
                        submitted = st.form_submit_button("Check Answer")

                        if submitted:
                            if user_answer == options[correct_answer_key]:
                                st.success(f"Correct! 🎉")
                            else:
                                st.error(f"Not quite. The correct answer was: **{options[correct_answer_key]}**")
                            
                            st.info(f"**Explanation:** {mcq['explanation']}")
        
        # --- Short Answer Questions ---
        if quiz_data.get("short_answer"):
            st.markdown("#### Short Answer Questions")
            for i, saq in enumerate(quiz_data["short_answer"]):
                 with st.expander(f"**Question {i+1}:** {saq['question']}"):
                    st.info(f"**Ideal Answer:** {saq['ideal_answer']}")
else:
    st.warning("Agent could not be initialized. Please check your API key setup.")
