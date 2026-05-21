import streamlit as st
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

st.title("🚀 CareerPilot AI")
st.subheader("AI Career Assistant Platform")

st.write(
    "Upload your resume, analyze your ATS score, and compare it with a job description."
)

uploaded_file = st.file_uploader("Upload Resume PDF", type=["pdf"])

job_description = st.text_area(
    "Paste Job Description",
    height=180,
    placeholder="Paste the job description here..."
)

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

if uploaded_file is not None:
    resume_text = extract_text_from_pdf(uploaded_file)
    score, level, found_keywords, feedback = analyze_resume(resume_text)

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("ATS Score", f"{score}/100")

    with col2:
        st.metric("Resume Level", level)

    with col3:
        st.metric("Detected Skills", len(found_keywords))

    st.progress(score / 100)

    if level == "Excellent":
        st.success(f"Level: {level}")
    elif level == "Good":
        st.info(f"Level: {level}")
    elif level == "Average":
        st.warning(f"Level: {level}")
    else:
        st.error(f"Level: {level}")

    st.subheader("✅ Detected Skills")

    if found_keywords:
        st.write(", ".join(found_keywords))
    else:
        st.write("No important skills detected.")

    st.subheader("💡 Improvement Suggestions")

    if feedback:
        for item in feedback:
            st.write(f"- {item}")
    else:
        st.success("Excellent resume. No suggestions.")

    st.divider()

    st.subheader("🧠 Career Recommendations")

    careers = recommend_careers(found_keywords)

    for career in careers:
        st.success(f"✅ {career}")

    if job_description.strip() != "":
        st.divider()
        st.subheader("🎯 Job Description Match")

        match_score, matched_words, missing_words = match_resume_to_job(
            resume_text,
            job_description
        )

        st.metric("Job Match Score", f"{match_score}%")
        st.progress(match_score / 100)

        st.subheader("✅ Matched Keywords")

        if matched_words:
            st.write(", ".join(matched_words[:30]))
        else:
            st.write("No matching keywords found.")

        st.subheader("❌ Missing Keywords")

        if missing_words:
            for word in missing_words:
                st.write(f"- {word}")
        else:
            st.success("No important missing keywords detected.")

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

    with st.expander("Extracted Resume Text"):
        st.write(resume_text)

