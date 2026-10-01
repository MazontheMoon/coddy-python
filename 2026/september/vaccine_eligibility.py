def vaccine_eligibility(age, has_allergies, previous_reactions):
    if age < 12:
        return "Not eligible for the vaccine. Patient is under 12 years old."
    else:
        if has_allergies or previous_reactions:
            return "Eligible for the vaccine, but should consult with a doctor first due to medical history."
        else:
            return "Eligible for the vaccine. Can proceed with vaccination."
