def estimate_salary(job_title):
    job_title = job_title.lower()

    salaries = {
        "data analyst": {
            "Algeria": "500 - 1200 USD / month",
            "Canada": "4500 - 7000 CAD / month",
            "USA": "5000 - 8500 USD / month"
        },
        "ai trainer": {
            "Algeria": "400 - 1000 USD / month",
            "Canada": "3500 - 6000 CAD / month",
            "USA": "4000 - 7500 USD / month"
        },
        "machine learning engineer": {
            "Algeria": "700 - 1500 USD / month",
            "Canada": "6000 - 9500 CAD / month",
            "USA": "7000 - 12000 USD / month"
        },
        "frontend developer": {
            "Algeria": "500 - 1300 USD / month",
            "Canada": "4500 - 7500 CAD / month",
            "USA": "5000 - 9000 USD / month"
        }
    }

    return salaries.get(
        job_title,
        {
            "Algeria": "Varies by experience",
            "Canada": "Varies by experience",
            "USA": "Varies by experience"
        }
    )
