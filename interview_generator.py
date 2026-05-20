def generate_interview_questions(job_title):

    job_title = job_title.lower()

    questions_db = {
        "ai trainer": [
            "What is prompt engineering?",
            "How do you evaluate AI model responses?",
            "Explain supervised learning.",
            "How would you improve model accuracy?",
            "Describe a difficult annotation task you handled."
        ],

        "data analyst": [
            "What is data cleaning?",
            "Explain the difference between mean and median.",
            "How do you use Excel or Python for analysis?",
            "What is SQL used for?",
            "Describe a data project you worked on."
        ],

        "python developer": [
            "What is OOP in Python?",
            "Explain lists vs tuples.",
            "What are decorators?",
            "How do APIs work?",
            "Describe a Python project you built."
        ],

        "machine learning engineer": [
            "What is overfitting?",
            "Explain supervised vs unsupervised learning.",
            "What is cross-validation?",
            "What is feature engineering?",
            "How would you improve model performance?"
        ]
    }

    if job_title in questions_db:
        return questions_db[job_title]

    return [
        "Tell me about yourself.",
        "Why do you want this job?",
        "What are your strengths and weaknesses?",
        "Describe a challenge you solved.",
        "Where do you see yourself in 5 years?"
    ]
