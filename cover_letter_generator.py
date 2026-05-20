def generate_cover_letter(resume_text, job_description):
    resume_text = resume_text.lower()
    job_description = job_description.lower()

    if "data" in job_description:
        role = "Data Analyst"
    elif "ai" in job_description or "trainer" in job_description:
        role = "AI Trainer"
    elif "react" in job_description or "frontend" in job_description:
        role = "Frontend Developer"
    else:
        role = "the position"

    cover_letter = f"""
Dear Hiring Manager,

I am excited to apply for {role}. My background in mathematics, data analysis,
and AI-related projects has helped me build strong analytical and problem-solving skills.

Through my projects, I have worked with Python, data analysis, machine learning concepts,
and interactive applications. I am motivated to apply these skills to support your team
and contribute to high-quality results.

I am especially interested in this opportunity because it matches my interest in technology,
AI, data, and continuous learning.

Thank you for considering my application. I would be happy to discuss how my skills
and projects can contribute to your organization.

Sincerely,
Sihem Gherissi
"""

    return cover_letter