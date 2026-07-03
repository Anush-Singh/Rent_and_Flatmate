def calculate_score(listing, tenant):
    score = 0
    explanation = []

    if listing.location == tenant.preferred_location:
        score += 50
        explanation.append("Preferred location matched")

    if tenant.budget_min <= listing.rent <= tenant.budget_max:
        score += 50
        explanation.append("Budget matched")

    return score, explanation