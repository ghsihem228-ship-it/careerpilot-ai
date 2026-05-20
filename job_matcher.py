def match_resume_to_job(resume_text, job_description):
    resume_text = resume_text.lower()
    job_description = job_description.lower()

    job_words = set(job_description.split())
    resume_words = set(resume_text.split())

    matched_words = job_words.intersection(resume_words)
    missing_words = job_words.difference(resume_words)

    important_missing = [
        word for word in missing_words
        if len(word) > 4
    ]

    if len(job_words) == 0:
        match_score = 0
    else:
        match_score = round((len(matched_words) / len(job_words)) * 100, 2)

    return match_score, list(matched_words), important_missing[:20]