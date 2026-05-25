import streamlit as st
import pandas as pd

from analytics_engine import calculate_career_readiness
from resume_parser import extract_text_from_pdf
from roadmap_generator import generate_learning_roadmap
from salary_estimator import estimate_salary
from career_recommender import recommend_careers
from interview_generator import generate_interview_questions
from ats_engine import analyze_resume
from job_matcher import match_resume_to_job
from cover_letter_generator import generate_cover_letter

st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide"
)

# ==========================
# Custom UI Theme
# ==========================

st.markdown("""
<style>
.stApp {
    background-color: #0f172a;
    color: #ffffff;
}

h1, h2, h3 {
    color: #38bdf8;
}

[data-testid="stMetric"] {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 16px;
    border: 1px solid #334155;
}

.stTextInput input,
.stTextArea textarea {
    background-color: #1e293b;
    color: white;
    border-radius: 10px;
    border: 1px solid #38bdf8;
}

.stButton button {
    background-color: #38bdf8;
    color: #0f172a;
    font-weight: bold;
    border-radius: 10px;
    border: none;
    padding: 10px 20px;
}

.stButton button:hover {
    background-color: #0ea5e9;
    color: white;
}

[data-testid="stFileUploader"] {
    background-color: #1e293b;
    padding: 15px;
    border-radius: 12px;
}

[data-testid="stExpander"] {
    background-color: #1e293b;
    border-radius: 12px;
}

hr {
    border-color: #334155;
}
</style>
""", unsafe_allow_html=True)

# ==========================
# Sidebar
# ==========================

st.sidebar.title("🚀 CareerPilot AI")
st.sidebar.markdown("### Navigation")
st.sidebar.info("AI Career Assistant Platform")

st.sidebar.markdown("""
### Features
- 📄 Resume Analyzer
- 🎯 Job Matcher
- 🧠 Career Recommendations
- 🎤 Interview Questions
- 📚 Learning Roadmap
- 💰 Salary Estimator
- 📝 Cover Letter Generator
- 📊 Analytics Dashboard
""")

st.sidebar.success("Portfolio Project by Sihem")

# ==========================
# Header
# ==========================

st.title("🚀 CareerPilot AI")

st.markdown("""
### AI-Powered Career Assistant Platform

Analyze resumes, match jobs, generate cover letters,  
estimate salaries, and build your career roadmap.
""")

# ==========================
# Resume Upload
# ==========================

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description",
    height=180,
    placeholder="Paste the job description here..."
)

# ==========================
# Interview Generator
# ==========================

st.divider()

st.subheader("🎤 Interview Question Generator")

job_title = st.text_input(
    "Enter Job Title",
    placeholder="Example: AI Trainer, Data Analyst"
)

if st.button("Generate Interview Questions"):

    questions = generate_interview_questions(job_title)

    st.subheader("Interview Questions")

    for i, question in enumerate(questions, start=1):
        st.write(f"{i}. {question}")

# ==========================
# Learning Roadmap
# ==========================

st.divider()

st.subheader("📚 Learning Roadmap Generator")

career_goal = st.text_input(
    "Enter Career Goal",
    placeholder="Example: Data Analyst, AI Trainer, Machine Learning Engineer"
)

if st.button("Generate Learning Roadmap"):

    roadmap = generate_learning_roadmap(career_goal)

    st.subheader("Your Learning Roadmap")

    for i, step in enumerate(roadmap, start=1):
        st.write(f"{i}. {step}")

# ==========================
# Salary Estimator
# ==========================

st.divider()

st.subheader("💰 Salary Estimator")

salary_job = st.text_input(
    "Enter Job Title for Salary Estimate",
    placeholder="Example: Data Analyst, AI Trainer"
)

if st.button("Estimate Salary"):

    salary_data = estimate_salary(salary_job)

    st.subheader("Estimated Salary Range")

    for country, salary in salary_data.items():
        st.info(f"{country}: {salary}")

# ==========================
# Resume Analysis
# ==========================

if uploaded_file is not None:

    resume_text = extract_text_from_pdf(uploaded_file)

    score, level, found_keywords, feedback = analyze_resume(
        resume_text
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "ATS Score",
            f"{score}/100"
        )

    with col2:
        st.metric(
            "Resume Level",
            level
        )

    with col3:
        st.metric(
            "Detected Skills",
            len(found_keywords)
        )

    st.progress(score / 100)

    # ==========================
    # Analytics Dashboard
    # ==========================

    st.divider()

    st.subheader("📊 Career Analytics Dashboard")

    career_score = calculate_career_readiness(
        score,
        found_keywords
    )

    st.metric(
        "Career Readiness Score",
        f"{career_score}%"
    )

    st.progress(career_score / 100)

    # ==========================
    # Resume Level
    # ==========================

    if level == "Excellent":
        st.success(f"Level: {level}")

    elif level == "Good":
        st.info(f"Level: {level}")

    elif level == "Average":
        st.warning(f"Level: {level}")

    else:
        st.error(f"Level: {level}")

    # ==========================
    # Skills
    # ==========================

    st.subheader("✅ Detected Skills")

    if found_keywords:
        st.write(", ".join(found_keywords))
    else:
        st.write("No important skills detected.")

    # ==========================
    # Suggestions
    # ==========================

    st.subheader("💡 Improvement Suggestions")

    if feedback:
        for item in feedback:
            st.write(f"- {item}")
    else:
        st.success(
            "Excellent resume. No suggestions."
        )

    # ==========================
    # Skill Analytics
    # ==========================

    st.subheader("📈 Skill Analytics")

    skills_df = pd.DataFrame({
        "Skill": found_keywords,
        "Value": [1] * len(found_keywords)
    })

    if len(found_keywords) > 0:
        st.bar_chart(
            skills_df.set_index("Skill")
        )

    # ==========================
    # Career Recommendations
    # ==========================

    st.divider()

    st.subheader("🧠 Career Recommendations")

    careers = recommend_careers(found_keywords)

    for career in careers:
        st.success(f"✅ {career}")

    # ==========================
    # Job Match
    # ==========================

    if job_description.strip() != "":

        st.divider()

        st.subheader("🎯 Job Description Match")

        match_score, matched_words, missing_words = match_resume_to_job(
            resume_text,
            job_description
        )

        st.metric(
            "Job Match Score",
            f"{match_score}%"
        )

        st.progress(match_score / 100)

        st.subheader("✅ Matched Keywords")

        if matched_words:
            st.write(
                ", ".join(matched_words[:30])
            )
        else:
            st.write(
                "No matching keywords found."
            )

        st.subheader("❌ Missing Keywords")

        if missing_words:
            for word in missing_words:
                st.write(f"- {word}")
        else:
            st.success(
                "No important missing keywords detected."
            )

        # ==========================
        # Cover Letter
        # ==========================

        st.subheader("📝 AI Cover Letter Generator")

        if st.button("Generate Cover Letter"):

            cover_letter = generate_cover_letter(
                resume_text,
                job_description
            )

            st.text_area(
                "Generated Cover Letter",
                cover_letter,
                height=300
            )

    # ==========================
    # Resume Text
    # ==========================

    with st.expander(
        "Extracted Resume Text"
    ):
        st.write(resume_text)
