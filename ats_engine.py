def analyze_resume(text):
    score = 0

    keywords = [
        "python",
        "sql",
        "machine learning",
        "data analysis",
        "excel",
        "communication",
        "teamwork",
        "react",
        "javascript",
        "problem solving",
    ]

    found_keywords = []

    text_lower = text.lower()

    for keyword in keywords:
        if keyword in text_lower:
            score += 10
            found_keywords.append(keyword)

    if score >= 80:
        level = "Excellent"
    elif score >= 60:
        level = "Good"
    elif score >= 40:
        level = "Average"
    else:
        level = "Weak"

    feedback = []

    if "python" not in text_lower:
        feedback.append("Add Python skills")

    if "sql" not in text_lower:
        feedback.append("Add SQL skills")

    if "communication" not in text_lower:
        feedback.append("Mention communication skills")

    if "teamwork" not in text_lower:
        feedback.append("Mention teamwork experience")

    return score, level, found_keywords, feedback