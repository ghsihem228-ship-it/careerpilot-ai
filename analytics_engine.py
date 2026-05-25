def calculate_career_readiness(score, found_keywords):

    readiness = score

    bonus = len(found_keywords) * 2

    readiness += bonus

    if readiness > 100:
        readiness = 100

    return readiness
