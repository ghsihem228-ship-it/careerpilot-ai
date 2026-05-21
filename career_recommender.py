def recommend_careers(found_keywords):

    careers = []

    skills = [skill.lower() for skill in found_keywords]

    if "python" in skills or "data analysis" in skills:
        careers.append("Data Analyst")

    if "machine learning" in skills or "python" in skills:
        careers.append("Machine Learning Engineer")

    if "react" in skills or "javascript" in skills:
        careers.append("Frontend Developer")

    if "python" in skills and "communication" in skills:
        careers.append("AI Trainer")

    if "excel" in skills or "sql" in skills:
        careers.append("Business Intelligence Analyst")

    if len(careers) == 0:
        careers.append("General Technology Career")

    return list(set(careers))
