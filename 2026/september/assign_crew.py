def assign_crew(building_description, unit_number):
    if "adobe" in building_description.lower():
        crew_type = "Specialized"
    else:
        crew_type = "Standard"
    
    return f"Unit {unit_number}: {crew_type} crew assigned"