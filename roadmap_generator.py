def generate_learning_roadmap(career_goal):

    career_goal = career_goal.lower()

    roadmaps = {
        "data analyst": [
            "Learn Excel fundamentals",
            "Learn SQL for data querying",
            "Study statistics and probability",
            "Learn Python basics",
            "Practice Pandas and NumPy",
            "Create data visualization projects",
            "Build dashboards using Power BI or Streamlit",
            "Create a portfolio with real datasets"
        ],

        "ai trainer": [
            "Learn prompt engineering basics",
            "Understand AI model evaluation",
            "Practice annotation and data labeling",
            "Study NLP fundamentals",
            "Learn how to evaluate model responses",
            "Build AI evaluation projects",
            "Improve technical writing skills",
            "Create an AI training portfolio"
        ],

        "machine learning engineer": [
            "Master Python programming",
            "Study linear algebra and statistics",
            "Learn NumPy, Pandas, and Scikit-learn",
            "Understand supervised and unsupervised learning",
            "Practice model training and evaluation",
            "Learn deep learning basics",
            "Build end-to-end ML projects",
            "Deploy ML applications"
        ],

        "frontend developer": [
            "Learn HTML, CSS, and JavaScript",
            "Understand React fundamentals",
            "Practice components and props",
            "Learn React Hooks",
            "Build responsive web applications",
            "Use APIs in React projects",
            "Deploy projects using Vercel or Netlify",
            "Create a frontend portfolio"
        ]
    }

    if career_goal in roadmaps:
        return roadmaps[career_goal]

    return [
        "Define your target role clearly",
        "Learn the core technical skills required",
        "Build small projects",
        "Create a professional portfolio",
        "Improve communication and problem-solving skills",
        "Apply to internships or entry-level roles"
    ]
